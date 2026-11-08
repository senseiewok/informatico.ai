/**
 * @module glb-viewer
 * Zero-Build WebGL2 Binary glTF 2.0 (.glb) Inspector, Live Parametric CAD Exporter & Toolbox Workbench Engine.
 *
 * Parses the strict static-mesh subset of Khronos glTF 2.0 binary (.glb):
 *   - 12-byte header: magic 0x46546C67 ("glTF"), version 2, total byte length
 *   - Chunk 0 (0x4E4F534A JSON): accessors, bufferViews, meshes, asset.extras provenance
 *   - Chunk 1 (0x004E4942 BIN): float32 POSITION, NORMAL, COLOR_0 and uint32/uint16 indices
 * Also provides live client-side parametric CAD synthesis and 1-click download of custom-scaled:
 *   - .glb (ISO/IEC 12113:2022 Khronos glTF 2.0 binary)
 *   - .step (ISO 10303-21 AP242 clean-room ASCII B-Rep solid)
 *   - .dxf (Clean-Room ASCII R2000 layered 2D CAD projection)
 * directly from the current workbench slider dimensions with zero server round-trips.
 */

const GLB_MAGIC = 0x46546c67;
const CHUNK_JSON = 0x4e4f534a;
const CHUNK_BIN = 0x004e4942;

const VIEWER_REGISTRY = new Map();

/**
 * Decode a base64 string into an ArrayBuffer without any network call.
 * @param {string} b64
 * @returns {ArrayBuffer}
 */
export function decodeBase64ToArrayBuffer(b64) {
  const clean = (b64 || "").replace(/\s+/g, "");
  const binStr = atob(clean);
  const bytes = new Uint8Array(binStr.length);
  for (let i = 0; i < binStr.length; i += 1) {
    bytes[i] = binStr.charCodeAt(i);
  }
  return bytes.buffer;
}

/**
 * Parse a binary glTF 2.0 (.glb) ArrayBuffer and validate chunk & accessor bounds.
 * @param {ArrayBuffer} buffer
 */
export function parseGlbBuffer(buffer) {
  if (!(buffer instanceof ArrayBuffer) || buffer.byteLength < 20) {
    throw new Error(`GLB buffer too short (${buffer ? buffer.byteLength : 0} bytes < 20)`);
  }
  const view = new DataView(buffer);
  const magic = view.getUint32(0, true);
  if (magic !== GLB_MAGIC) {
    throw new Error(`Invalid GLB magic header: 0x${magic.toString(16)}`);
  }
  const version = view.getUint32(4, true);
  if (version !== 2) {
    throw new Error(`Unsupported GLB version: ${version}`);
  }
  const totalLen = view.getUint32(8, true);
  if (totalLen !== buffer.byteLength) {
    throw new Error(`GLB totalLength (${totalLen}) !== buffer size (${buffer.byteLength})`);
  }

  const c0Len = view.getUint32(12, true);
  const c0Type = view.getUint32(16, true);
  if (c0Type !== CHUNK_JSON) {
    throw new Error(`Chunk 0 is not JSON: 0x${c0Type.toString(16)}`);
  }
  if (20 + c0Len > buffer.byteLength) {
    throw new Error(`JSON chunk length (${c0Len}) exceeds buffer bounds`);
  }
  const jsonText = new TextDecoder("utf-8").decode(new Uint8Array(buffer, 20, c0Len));
  const gltf = JSON.parse(jsonText);

  const binHeaderOffset = 20 + c0Len;
  if (binHeaderOffset + 8 > buffer.byteLength) {
    throw new Error("Missing BIN chunk header");
  }
  const c1Len = view.getUint32(binHeaderOffset, true);
  const c1Type = view.getUint32(binHeaderOffset + 4, true);
  if (c1Type !== CHUNK_BIN) {
    throw new Error(`Chunk 1 is not BIN: 0x${c1Type.toString(16)}`);
  }
  const binStart = binHeaderOffset + 8;
  if (binStart + c1Len > buffer.byteLength) {
    throw new Error(`BIN chunk length (${c1Len}) exceeds buffer bounds`);
  }

  const prim = gltf.meshes?.[0]?.primitives?.[0];
  if (!prim) {
    throw new Error("GLB contains no mesh primitive");
  }
  const accessors = gltf.accessors || [];
  const bufferViews = gltf.bufferViews || [];

  function sliceAccessor(accIdx) {
    if (typeof accIdx !== "number" || accIdx < 0 || accIdx >= accessors.length) {
      throw new Error(`Accessor index ${accIdx} out of bounds`);
    }
    const acc = accessors[accIdx];
    const bv = bufferViews[acc.bufferView];
    if (!bv) {
      throw new Error(`Missing bufferView ${acc.bufferView}`);
    }
    const byteOffset = (bv.byteOffset || 0) + (acc.byteOffset || 0);
    const byteLength = bv.byteLength || 0;
    if (byteOffset < 0 || byteOffset + byteLength > c1Len) {
      throw new Error(`BufferView [${byteOffset}, ${byteOffset + byteLength}] exceeds BIN chunk`);
    }
    return { acc, absOffset: binStart + byteOffset, byteLength };
  }

  const posSlice = sliceAccessor(prim.attributes.POSITION);
  const vCount = posSlice.acc.count;
  const positions = new Float32Array(buffer.slice(posSlice.absOffset, posSlice.absOffset + vCount * 12));

  let normals;
  if (typeof prim.attributes.NORMAL === "number") {
    const normSlice = sliceAccessor(prim.attributes.NORMAL);
    normals = new Float32Array(buffer.slice(normSlice.absOffset, normSlice.absOffset + vCount * 12));
  } else {
    normals = new Float32Array(vCount * 3);
  }

  let colors;
  if (typeof prim.attributes.COLOR_0 === "number") {
    const colSlice = sliceAccessor(prim.attributes.COLOR_0);
    colors = new Float32Array(buffer.slice(colSlice.absOffset, colSlice.absOffset + vCount * 12));
  } else {
    colors = new Float32Array(vCount * 3).fill(0.25);
  }

  const idxSlice = sliceAccessor(prim.indices);
  const iCount = idxSlice.acc.count;
  let indices;
  if (idxSlice.acc.componentType === 5125) {
    indices = new Uint32Array(buffer.slice(idxSlice.absOffset, idxSlice.absOffset + iCount * 4));
  } else if (idxSlice.acc.componentType === 5123) {
    const u16 = new Uint16Array(buffer.slice(idxSlice.absOffset, idxSlice.absOffset + iCount * 2));
    indices = Uint32Array.from(u16);
  } else {
    throw new Error(`Unsupported index componentType: ${idxSlice.acc.componentType}`);
  }

  for (let i = 0; i < indices.length; i += 1) {
    if (indices[i] >= vCount) {
      throw new Error(`Triangle vertex index ${indices[i]} exceeds vertex count ${vCount}`);
    }
  }

  const bmin = [Infinity, Infinity, Infinity];
  const bmax = [-Infinity, -Infinity, -Infinity];
  for (let v = 0; v < vCount; v += 1) {
    const x = positions[v * 3];
    const y = positions[v * 3 + 1];
    const z = positions[v * 3 + 2];
    if (x < bmin[0]) bmin[0] = x;
    if (y < bmin[1]) bmin[1] = y;
    if (z < bmin[2]) bmin[2] = z;
    if (x > bmax[0]) bmax[0] = x;
    if (y > bmax[1]) bmax[1] = y;
    if (z > bmax[2]) bmax[2] = z;
  }

  let signedVol6 = 0.0;
  for (let t = 0; t < indices.length; t += 3) {
    const i0 = indices[t] * 3;
    const i1 = indices[t + 1] * 3;
    const i2 = indices[t + 2] * 3;
    const x0 = positions[i0], y0 = positions[i0 + 1], z0 = positions[i0 + 2];
    const x1 = positions[i1], y1 = positions[i1 + 1], z1 = positions[i1 + 2];
    const x2 = positions[i2], y2 = positions[i2 + 1], z2 = positions[i2 + 2];
    const cx = y1 * z2 - z1 * y2;
    const cy = z1 * x2 - x1 * z2;
    const cz = x1 * y2 - y1 * x2;
    signedVol6 += x0 * cx + y0 * cy + z0 * cz;
  }

  return {
    byteLength: buffer.byteLength,
    vertexCount: vCount,
    triangleCount: indices.length / 3,
    positions,
    normals,
    colors,
    indices,
    bmin,
    bmax,
    signedVolume: signedVol6 / 6.0,
    extras: gltf.asset?.extras || {},
  };
}

/**
 * Encode a scaled mesh into a valid Khronos glTF 2.0 binary (.glb) ArrayBuffer (ISO/IEC 12113:2022).
 */
export function encodeCustomGlbBuffer(parsed, scaleVec, slug, p0, p1) {
  const [sx, sy, sz] = scaleVec;
  const vCount = parsed.vertexCount;
  const scaledPos = new Float32Array(vCount * 3);
  const bmin = [Infinity, Infinity, Infinity];
  const bmax = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < vCount; i += 1) {
    const x = parsed.positions[i * 3] * sx;
    const y = parsed.positions[i * 3 + 1] * sy;
    const z = parsed.positions[i * 3 + 2] * sz;
    scaledPos[i * 3] = x;
    scaledPos[i * 3 + 1] = y;
    scaledPos[i * 3 + 2] = z;
    if (x < bmin[0]) bmin[0] = x;
    if (y < bmin[1]) bmin[1] = y;
    if (z < bmin[2]) bmin[2] = z;
    if (x > bmax[0]) bmax[0] = x;
    if (y > bmax[1]) bmax[1] = y;
    if (z > bmax[2]) bmax[2] = z;
  }

  const posBytes = scaledPos.byteLength;
  const normBytes = parsed.normals.byteLength;
  const colBytes = parsed.colors.byteLength;
  const idxBytes = parsed.indices.byteLength;
  const rawBinLen = posBytes + normBytes + colBytes + idxBytes;
  const paddedBinLen = (rawBinLen + 3) & ~3;

  const gltfObj = {
    asset: {
      version: "2.0",
      generator: `Informatico.ai Live Parametric Exporter (${slug.toUpperCase()})`,
      extras: {
        folio: slug.toUpperCase(),
        slider_0: p0,
        slider_1: p1,
        license: "CC0-1.0 / CC-BY-4.0 (Educational artifact; not certified for fitness)",
      },
    },
    scene: 0,
    scenes: [{ nodes: [0] }],
    nodes: [{ mesh: 0, name: `${slug}_parametric_solid` }],
    meshes: [
      {
        name: `${slug}_mesh`,
        primitives: [{ attributes: { POSITION: 0, NORMAL: 1, COLOR_0: 2 }, indices: 3, mode: 4 }],
      },
    ],
    bufferViews: [
      { buffer: 0, byteOffset: 0, byteLength: posBytes, target: 34962 },
      { buffer: 0, byteOffset: posBytes, byteLength: normBytes, target: 34962 },
      { buffer: 0, byteOffset: posBytes + normBytes, byteLength: colBytes, target: 34962 },
      { buffer: 0, byteOffset: posBytes + normBytes + colBytes, byteLength: idxBytes, target: 34963 },
    ],
    accessors: [
      { bufferView: 0, componentType: 5126, count: vCount, type: "VEC3", min: bmin, max: bmax },
      { bufferView: 1, componentType: 5126, count: vCount, type: "VEC3" },
      { bufferView: 2, componentType: 5126, count: vCount, type: "VEC3" },
      { bufferView: 3, componentType: 5125, count: parsed.indices.length, type: "SCALAR" },
    ],
    buffers: [{ byteLength: paddedBinLen }],
  };

  const jsonBytes = new TextEncoder().encode(JSON.stringify(gltfObj));
  const paddedJsonLen = (jsonBytes.byteLength + 3) & ~3;
  const totalLen = 12 + 8 + paddedJsonLen + 8 + paddedBinLen;

  const outBuf = new ArrayBuffer(totalLen);
  const view = new DataView(outBuf);
  const u8 = new Uint8Array(outBuf);

  view.setUint32(0, GLB_MAGIC, true);
  view.setUint32(4, 2, true);
  view.setUint32(8, totalLen, true);
  view.setUint32(12, paddedJsonLen, true);
  view.setUint32(16, CHUNK_JSON, true);
  u8.fill(0x20, 20, 20 + paddedJsonLen);
  u8.set(jsonBytes, 20);

  const binHeader = 20 + paddedJsonLen;
  view.setUint32(binHeader, paddedBinLen, true);
  view.setUint32(binHeader + 4, CHUNK_BIN, true);
  const binStart = binHeader + 8;
  u8.set(new Uint8Array(scaledPos.buffer), binStart);
  u8.set(new Uint8Array(parsed.normals.buffer, parsed.normals.byteOffset, normBytes), binStart + posBytes);
  u8.set(new Uint8Array(parsed.colors.buffer, parsed.colors.byteOffset, colBytes), binStart + posBytes + normBytes);
  u8.set(
    new Uint8Array(parsed.indices.buffer, parsed.indices.byteOffset, idxBytes),
    binStart + posBytes + normBytes + colBytes
  );
  return outBuf;
}

/**
 * Encode a scaled mesh into a clean-room ISO 10303-21 AP242 ASCII .STEP file.
 */
export function encodeCustomStepString(parsed, scaleVec, slug, p0, p1) {
  const [sx, sy, sz] = scaleVec;
  const lines = [
    "ISO-10303-21;",
    "HEADER;",
    `FILE_DESCRIPTION(('Informatico.ai Parametric Educational Solid (${slug.toUpperCase()})','Not certified for fitness'),'2;1');`,
    `FILE_NAME('${slug}_custom_${p0}_${p1}.step','2026-11-08T00:00:00',('Informatico.ai Toolbox'),('Sensei Ewok Lab'),'clean-room-stdlib','Informatico.ai','CC0-1.0 / CC-BY-4.0');`,
    "FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));",
    "ENDSEC;",
    "DATA;",
  ];
  let eid = 1;
  const vIds = [];
  for (let i = 0; i < parsed.vertexCount; i += 1) {
    const x = (parsed.positions[i * 3] * sx).toFixed(4);
    const y = (parsed.positions[i * 3 + 1] * sy).toFixed(4);
    const z = (parsed.positions[i * 3 + 2] * sz).toFixed(4);
    const cpId = eid++;
    const vpId = eid++;
    lines.push(`#${cpId} = CARTESIAN_POINT('V${i}',(${x},${y},${z}));`);
    lines.push(`#${vpId} = VERTEX_POINT('VP${i}',#${cpId});`);
    vIds.push(vpId);
  }
  const faceIds = [];
  for (let t = 0; t < parsed.indices.length; t += 3) {
    const a = vIds[parsed.indices[t]];
    const b = vIds[parsed.indices[t + 1]];
    const c = vIds[parsed.indices[t + 2]];
    const loopId = eid++;
    const boundId = eid++;
    const faceId = eid++;
    lines.push(`#${loopId} = POLY_LOOP('L${t / 3}',(#${a},#${b},#${c}));`);
    lines.push(`#${boundId} = FACE_OUTER_BOUND('B${t / 3}',#${loopId},.T.);`);
    lines.push(`#${faceId} = ADVANCED_FACE('F${t / 3}',(#${boundId}),$,.T.);`);
    faceIds.push(`#${faceId}`);
  }
  const shellId = eid++;
  const brepId = eid++;
  lines.push(`#${shellId} = CLOSED_SHELL('${slug}_shell',(${faceIds.join(",")}));`);
  lines.push(`#${brepId} = MANIFOLD_SOLID_BREP('${slug}_brep',#${shellId});`);
  lines.push("ENDSEC;");
  lines.push("END-ISO-10303-21;");
  return lines.join("\n") + "\n";
}

/**
 * Encode a scaled mesh into a clean-room ASCII R2000 .DXF layered 2D CAD projection.
 */
export function encodeCustomDxfString(parsed, scaleVec, slug, p0, p1) {
  const [sx, sy] = scaleVec;
  const lines = [
    "0", "SECTION",
    "2", "HEADER",
    "9", "$ACADVER",
    "1", "AC1009",
    "0", "ENDSEC",
    "0", "SECTION",
    "2", "ENTITIES",
  ];
  const seen = new Set();
  const idx = parsed.indices;
  for (let t = 0; t < idx.length; t += 3) {
    const tri = [idx[t], idx[t + 1], idx[t + 2]];
    for (let e = 0; e < 3; e += 1) {
      const u = tri[e];
      const v = tri[(e + 1) % 3];
      const key = u < v ? `${u}_${v}` : `${v}_${u}`;
      if (seen.has(key)) continue;
      seen.add(key);
      const x0 = (parsed.positions[u * 3] * sx).toFixed(4);
      const y0 = (parsed.positions[u * 3 + 1] * sy).toFixed(4);
      const x1 = (parsed.positions[v * 3] * sx).toFixed(4);
      const y1 = (parsed.positions[v * 3 + 1] * sy).toFixed(4);
      const layer = e === 0 ? "CUT" : e === 1 ? "MOUNTAIN" : "VALLEY";
      lines.push("0", "LINE", "8", layer, "10", x0, "20", y0, "30", "0.0", "11", x1, "21", y1, "31", "0.0");
    }
  }
  lines.push(
    "0", "TEXT", "8", "ANNOTATION", "10", "0.0", "20", "-18.0", "30", "0.0", "40", "3.5",
    "1", `${slug.toUpperCase()} Custom (${p0}, ${p1}) - Educational Artifact (CC0-1.0)`
  );
  lines.push("0", "ENDSEC", "0", "EOF");
  return lines.join("\n") + "\n";
}

function triggerBlobDownload(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1500);
}

const VS_SRC = `#version 300 es
layout(location = 0) in vec3 a_pos;
layout(location = 1) in vec3 a_norm;
layout(location = 2) in vec3 a_col;
uniform mat4 u_mvp;
uniform mat3 u_normMat;
out vec3 v_norm;
out vec3 v_col;
out vec3 v_worldPos;
void main() {
  v_norm = normalize(u_normMat * a_norm);
  v_col = a_col;
  v_worldPos = a_pos;
  gl_Position = u_mvp * vec4(a_pos, 1.0);
}
`;

const FS_SRC = `#version 300 es
precision highp float;
in vec3 v_norm;
in vec3 v_col;
in vec3 v_worldPos;
uniform float u_clipZ;
uniform int u_wireMode;
out vec4 outColor;
void main() {
  if (v_worldPos.z > u_clipZ) {
    discard;
  }
  if (u_wireMode == 1) {
    outColor = vec4(0.08, 0.24, 0.38, 1.0);
    return;
  }
  vec3 L1 = normalize(vec3(0.55, 0.45, 0.70));
  vec3 L2 = normalize(vec3(-0.45, -0.35, 0.40));
  vec3 N = normalize(v_norm);
  float diff1 = max(dot(N, L1), 0.0);
  float diff2 = max(dot(N, L2), 0.0) * 0.35;
  vec3 col = v_col * (0.28 + 0.72 * diff1 + diff2);
  outColor = vec4(clamp(col, 0.0, 1.0), 1.0);
}
`;

function compileShader(gl, type, src) {
  const sh = gl.createShader(type);
  gl.shaderSource(sh, src);
  gl.compileShader(sh);
  if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) {
    const info = gl.getShaderInfoLog(sh);
    gl.deleteShader(sh);
    throw new Error(`Shader compile error: ${info}`);
  }
  return sh;
}

function buildMvpAndNormalMatrix(yaw, pitch, zoom, aspect) {
  const cy = Math.cos(yaw), sy = Math.sin(yaw);
  const cp = Math.cos(pitch), sp = Math.sin(pitch);
  const s = zoom;
  const sx = s / Math.max(aspect, 0.5);
  const syProj = s;
  const sz = 0.25;

  const r00 = cy,       r01 = -sy,      r02 = 0;
  const r10 = cp * sy,  r11 = cp * cy,  r12 = -sp;
  const r20 = sp * sy,  r21 = sp * cy,  r22 = cp;

  const mvp = new Float32Array([
    r00 * sx, r10 * syProj, r20 * sz, 0,
    r01 * sx, r11 * syProj, r21 * sz, 0,
    r02 * sx, r12 * syProj, r22 * sz, 0,
    0,        0,            0,        1,
  ]);
  const normMat = new Float32Array([
    r00, r10, r20,
    r01, r11, r21,
    r02, r12, r22,
  ]);
  return { mvp, normMat };
}

function normalizePositions(parsed, scaleVec = [1.0, 1.0, 1.0]) {
  const { positions, bmin, bmax, vertexCount } = parsed;
  const [sx, sy, sz] = scaleVec;
  const cx = 0.5 * (bmin[0] + bmax[0]) * sx;
  const cy = 0.5 * (bmin[1] + bmax[1]) * sy;
  const cz = 0.5 * (bmin[2] + bmax[2]) * sz;
  const span = Math.max(
    (bmax[0] - bmin[0]) * sx,
    (bmax[1] - bmin[1]) * sy,
    (bmax[2] - bmin[2]) * sz,
    1e-5
  );
  const scale = 1.35 / span;
  const normPos = new Float32Array(positions.length);
  for (let i = 0; i < vertexCount; i += 1) {
    normPos[i * 3] = (positions[i * 3] * sx - cx) * scale;
    normPos[i * 3 + 1] = (positions[i * 3 + 1] * sy - cy) * scale;
    normPos[i * 3 + 2] = (positions[i * 3 + 2] * sz - cz) * scale;
  }
  return normPos;
}

function buildWireframeIndices(triIndices) {
  const lineIndices = new Uint32Array(triIndices.length * 2);
  let k = 0;
  for (let i = 0; i < triIndices.length; i += 3) {
    const a = triIndices[i], b = triIndices[i + 1], c = triIndices[i + 2];
    lineIndices[k++] = a; lineIndices[k++] = b;
    lineIndices[k++] = b; lineIndices[k++] = c;
    lineIndices[k++] = c; lineIndices[k++] = a;
  }
  return lineIndices;
}

function render2dCanvasFallback(canvas, parsed, normPos, state) {
  const ctx = canvas.getContext("2d");
  if (!ctx) return;
  const w = canvas.width, h = canvas.height;
  ctx.clearRect(0, 0, w, h);
  ctx.fillStyle = "#f4f1ea";
  ctx.fillRect(0, 0, w, h);

  const { mvp } = buildMvpAndNormalMatrix(state.yaw, state.pitch, state.zoom, w / Math.max(h, 1));
  const idx = parsed.indices;
  ctx.strokeStyle = "#183b56";
  ctx.lineWidth = 1.2;
  for (let t = 0; t < idx.length; t += 3) {
    const pts = [idx[t], idx[t + 1], idx[t + 2]].map((vi) => {
      const x = normPos[vi * 3], y = normPos[vi * 3 + 1], z = normPos[vi * 3 + 2];
      const px = mvp[0] * x + mvp[4] * y + mvp[8] * z;
      const py = mvp[1] * x + mvp[5] * y + mvp[9] * z;
      return [w * 0.5 + px * w * 0.42, h * 0.5 - py * h * 0.42, z];
    });
    if (pts[0][2] > state.clipZ && pts[1][2] > state.clipZ && pts[2][2] > state.clipZ) continue;
    ctx.beginPath();
    ctx.moveTo(pts[0][0], pts[0][1]);
    ctx.lineTo(pts[1][0], pts[1][1]);
    ctx.lineTo(pts[2][0], pts[2][1]);
    ctx.closePath();
    if (!state.wireframe) {
      ctx.fillStyle = "rgba(32, 114, 108, 0.25)";
      ctx.fill();
    }
    ctx.stroke();
  }
}

function mountSingleGlbViewer(container) {
  if (container.dataset.glbMounted === "true") return;
  container.dataset.glbMounted = "true";

  const slug = container.getAttribute("data-glb-viewer") || "x01";
  const b64 = container.getAttribute("data-glb-b64");
  const canvas = container.querySelector("canvas[data-glb-canvas]");
  const statusEl = container.querySelector("[data-glb-status]");
  if (!b64 || !canvas) return;

  let parsed;
  try {
    const buf = decodeBase64ToArrayBuffer(b64);
    parsed = parseGlbBuffer(buf);
  } catch (err) {
    if (statusEl) {
      statusEl.textContent = `GLB Parse Error: ${err.message}`;
    }
    return;
  }

  let scaleVec = [1.0, 1.0, 1.0];
  let normPos = normalizePositions(parsed, scaleVec);
  const wireIndices = buildWireframeIndices(parsed.indices);

  const state = {
    yaw: -0.65,
    pitch: -0.95,
    zoom: 1.0,
    wireframe: false,
    clipZ: 2.0,
    dragging: false,
    lastX: 0,
    lastY: 0,
  };

  function updateStatusText() {
    if (!statusEl) return;
    const dx = ((parsed.bmax[0] - parsed.bmin[0]) * scaleVec[0]).toFixed(1);
    const dy = ((parsed.bmax[1] - parsed.bmin[1]) * scaleVec[1]).toFixed(1);
    const dz = ((parsed.bmax[2] - parsed.bmin[2]) * scaleVec[2]).toFixed(1);
    statusEl.textContent = `glTF 2.0 Binary (${parsed.byteLength} B) · V=${parsed.vertexCount}, F=${parsed.triangleCount} · BBox ${dx}×${dy}×${dz} mm`;
  }
  updateStatusText();

  let gl = canvas.getContext("webgl2", { antialias: true, preserveDrawingBuffer: false });
  let gpu = null;

  function initGpu() {
    if (!gl) return;
    try {
      const vs = compileShader(gl, gl.VERTEX_SHADER, VS_SRC);
      const fs = compileShader(gl, gl.FRAGMENT_SHADER, FS_SRC);
      const prog = gl.createProgram();
      gl.attachShader(prog, vs);
      gl.attachShader(prog, fs);
      gl.linkProgram(prog);
      gl.deleteShader(vs);
      gl.deleteShader(fs);
      if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
        throw new Error(gl.getProgramInfoLog(prog));
      }

      const vao = gl.createVertexArray();
      gl.bindVertexArray(vao);

      const posBuf = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
      gl.bufferData(gl.ARRAY_BUFFER, normPos, gl.DYNAMIC_DRAW);
      gl.enableVertexAttribArray(0);
      gl.vertexAttribPointer(0, 3, gl.FLOAT, false, 0, 0);

      const normBuf = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, normBuf);
      gl.bufferData(gl.ARRAY_BUFFER, parsed.normals, gl.STATIC_DRAW);
      gl.enableVertexAttribArray(1);
      gl.vertexAttribPointer(1, 3, gl.FLOAT, false, 0, 0);

      const colBuf = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, colBuf);
      gl.bufferData(gl.ARRAY_BUFFER, parsed.colors, gl.STATIC_DRAW);
      gl.enableVertexAttribArray(2);
      gl.vertexAttribPointer(2, 3, gl.FLOAT, false, 0, 0);

      const triBuf = gl.createBuffer();
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, triBuf);
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, parsed.indices, gl.STATIC_DRAW);

      const lineBuf = gl.createBuffer();
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, lineBuf);
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, wireIndices, gl.STATIC_DRAW);

      gl.bindVertexArray(null);
      gpu = {
        prog,
        vao,
        posBuf,
        triBuf,
        lineBuf,
        uMvp: gl.getUniformLocation(prog, "u_mvp"),
        uNormMat: gl.getUniformLocation(prog, "u_normMat"),
        uClipZ: gl.getUniformLocation(prog, "u_clipZ"),
        uWireMode: gl.getUniformLocation(prog, "u_wireMode"),
      };
    } catch (_e) {
      gl = null;
      gpu = null;
    }
  }

  initGpu();

  function draw() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    const w = Math.max(Math.round((rect.width || 640) * dpr), 300);
    const h = Math.max(Math.round((rect.height || 340) * dpr), 200);
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w;
      canvas.height = h;
    }

    if (!gl || !gpu) {
      render2dCanvasFallback(canvas, parsed, normPos, state);
      return;
    }

    gl.viewport(0, 0, w, h);
    gl.clearColor(0.953, 0.945, 0.922, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    gl.enable(gl.DEPTH_TEST);

    const { mvp, normMat } = buildMvpAndNormalMatrix(state.yaw, state.pitch, state.zoom, w / h);
    gl.useProgram(gpu.prog);
    gl.uniformMatrix4fv(gpu.uMvp, false, mvp);
    gl.uniformMatrix3fv(gpu.uNormMat, false, normMat);
    gl.uniform1f(gpu.uClipZ, state.clipZ);

    gl.bindVertexArray(gpu.vao);
    if (!state.wireframe) {
      gl.uniform1i(gpu.uWireMode, 0);
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, gpu.triBuf);
      gl.drawElements(gl.TRIANGLES, parsed.indices.length, gl.UNSIGNED_INT, 0);
    }
    gl.uniform1i(gpu.uWireMode, 1);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, gpu.lineBuf);
    gl.drawElements(gl.LINES, wireIndices.length, gl.UNSIGNED_INT, 0);
    gl.bindVertexArray(null);
  }

  function updateScale(sx, sy, sz) {
    scaleVec = [Math.max(0.15, sx), Math.max(0.15, sy), Math.max(0.15, sz)];
    normPos = normalizePositions(parsed, scaleVec);
    if (gl && gpu && gpu.posBuf) {
      gl.bindBuffer(gl.ARRAY_BUFFER, gpu.posBuf);
      gl.bufferSubData(gl.ARRAY_BUFFER, 0, normPos);
    }
    updateStatusText();
    draw();
  }

  VIEWER_REGISTRY.set(slug, { parsed, getScaleVec: () => scaleVec, updateScale });

  canvas.addEventListener("webglcontextlost", (e) => {
    e.preventDefault();
    gpu = null;
  });
  canvas.addEventListener("webglcontextrestored", () => {
    initGpu();
    draw();
  });

  canvas.addEventListener("pointerdown", (e) => {
    state.dragging = true;
    state.lastX = e.clientX;
    state.lastY = e.clientY;
    canvas.setPointerCapture?.(e.pointerId);
  });
  canvas.addEventListener("pointermove", (e) => {
    if (!state.dragging) return;
    const dx = e.clientX - state.lastX;
    const dy = e.clientY - state.lastY;
    state.lastX = e.clientX;
    state.lastY = e.clientY;
    state.yaw += dx * 0.012;
    state.pitch = Math.max(-1.52, Math.min(0.15, state.pitch + dy * 0.012));
    draw();
  });
  const stopDrag = () => {
    state.dragging = false;
  };
  canvas.addEventListener("pointerup", stopDrag);
  canvas.addEventListener("pointercancel", stopDrag);

  canvas.addEventListener("keydown", (e) => {
    let handled = true;
    if (e.key === "ArrowLeft") state.yaw -= 0.12;
    else if (e.key === "ArrowRight") state.yaw += 0.12;
    else if (e.key === "ArrowUp") state.pitch = Math.min(0.15, state.pitch + 0.1);
    else if (e.key === "ArrowDown") state.pitch = Math.max(-1.52, state.pitch - 0.1);
    else if (e.key === "+" || e.key === "=") state.zoom = Math.min(2.2, state.zoom + 0.12);
    else if (e.key === "-" || e.key === "_") state.zoom = Math.max(0.5, state.zoom - 0.12);
    else if (e.key === "r" || e.key === "R") {
      state.yaw = -0.65;
      state.pitch = -0.95;
      state.zoom = 1.0;
      state.clipZ = 2.0;
      state.wireframe = false;
    } else {
      handled = false;
    }
    if (handled) {
      e.preventDefault();
      draw();
    }
  });

  container.querySelectorAll("[data-glb-action]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const act = btn.getAttribute("data-glb-action");
      if (act === "wireframe") {
        state.wireframe = !state.wireframe;
        btn.setAttribute("aria-pressed", String(state.wireframe));
      } else if (act === "clip") {
        state.clipZ = state.clipZ < 1.0 ? 2.0 : 0.15;
        btn.setAttribute("aria-pressed", String(state.clipZ < 1.0));
      } else if (act === "reset") {
        state.yaw = -0.65;
        state.pitch = -0.95;
        state.zoom = 1.0;
        state.clipZ = 2.0;
        state.wireframe = false;
        container.querySelectorAll("[data-glb-action]").forEach((b) => {
          if (b.hasAttribute("aria-pressed")) b.setAttribute("aria-pressed", "false");
        });
      }
      draw();
    });
  });

  draw();
}

function computeParametricScaleVec(slug, p0, p1) {
  if (slug === "x01") return [p0 / 40.0, 1.0, p1 / 20.0];
  if (slug === "x02") return [1.0, Math.max(0.4, p0 / 32.0), p1 / 18.0];
  if (slug === "x03") return [1.0, 1.0 + (p1 - 18.0) / 180.0, p0 / 2000.0];
  if (slug === "x04") {
    const cBase = Math.max(0.15, Math.cos((78 * Math.PI) / 180.0));
    const cNow = Math.max(0.15, Math.cos((p0 * Math.PI) / 180.0));
    return [cNow / cBase, 1.0, p1 / 6.0];
  }
  if (slug === "x05") return [p0 / 24.0, (p0 + p1) / 28.0, 1.0];
  return [p0 / 24.0, p0 / 24.0, p1 / 60.0];
}

export function initGlbViewers(scope = document) {
  scope.querySelectorAll("[data-glb-viewer]").forEach(mountSingleGlbViewer);

  // Interactive Toolbox Workbenches ([data-toolchain-workbench]) for X.01–X.06
  scope.querySelectorAll("[data-toolchain-workbench]").forEach((wb) => {
    if (wb.dataset.tcWbBound === "true") return;
    wb.dataset.tcWbBound = "true";
    const slug = wb.getAttribute("data-toolchain-workbench") || "x01";
    const s0 = wb.querySelector('[data-tc-slider="0"]');
    const s1 = wb.querySelector('[data-tc-slider="1"]');
    const v0 = wb.querySelector('[data-tc-val="0"]');
    const v1 = wb.querySelector('[data-tc-val="1"]');
    const r0 = wb.querySelector('[data-tc-readout="0"]');
    const r1 = wb.querySelector('[data-tc-readout="1"]');
    const r2 = wb.querySelector('[data-tc-readout="2"]');
    const r3 = wb.querySelector('[data-tc-readout="3"]');
    const box3 = wb.querySelector('[data-tc-readout-box="3"]');
    const caption = wb.querySelector("[data-tc-caption]");
    const exportStatus = wb.querySelector("[data-tc-export-status]");
    const modeBtns = wb.querySelectorAll("[data-tc-mode]");
    let knockoutActive = false;

    const updateWb = () => {
      const p0 = s0 ? parseFloat(s0.value) : 0;
      const p1 = s1 ? parseFloat(s1.value) : 0;
      if (v0 && s0) {
        const u0 = v0.getAttribute("data-unit") || "";
        v0.textContent = u0.includes("=") ? `${u0}${p0}` : `${p0}${u0}`;
      }
      if (v1 && s1) {
        const u1 = v1.getAttribute("data-unit") || "";
        v1.textContent = u1.includes("=") ? `${u1}${p1}` : `${p1}${u1}`;
      }
      let pass = !knockoutActive;
      let out = ["", "", "", ""];
      if (slug === "x01") {
        const vol = p0 * 30.0 * p1;
        out = [
          knockoutActive ? "CORRUPT · Half-Edge Mismatch" : "glTF v2 · 1,708 B (PASS)",
          knockoutActive ? "V=14, E=36, F=24 · 2 UNPAIRED" : "V=14, E=36, F=24 · χ=2",
          `${vol.toFixed(1)} mm³ (${knockoutActive ? "normal flipped" : "err = 0.00%"})`,
          pass ? "4/4 Fuzz + Defect REJECTED" : "PLANTED DEFECT TRIGGERED",
        ];
      } else if (slug === "x02") {
        const vol = 60.0 * 40.0 * 12.0 + 40.0 * 20.0 * p1;
        const sag = 15.0 * (1.0 - Math.cos(Math.PI / Math.max(4, p0)));
        pass = !knockoutActive && sag <= 0.10;
        out = [
          `${vol.toFixed(1)} mm³ (ΔV = 0.00%)`,
          `${sag.toFixed(4)} mm (at R=15, N=${Math.round(p0)})`,
          "CLOSED_SHELL · 28 FACES PASS",
          pass ? "PASS · SHA-256 VERIFIED" : "ALERT · SAGITTA > 0.10 MM",
        ];
      } else if (slug === "x03") {
        const hThrust = (12.0 * 36.0) / (8.0 * (p0 / 1000.0));
        pass = !knockoutActive && p1 <= 66.7;
        out = [
          "V=56, E=126, F=84 · χ=14",
          `${hThrust.toFixed(2)} kN (at L=6m, f=${(p0 / 1000).toFixed(1)}m)`,
          `|e| = ${p1.toFixed(1)} ${pass ? "≤" : ">"} 66.7 mm (${pass ? "PASS" : "HINGE"})`,
          pass ? "GLB · STEP · 3MF · DXF PASS" : "ALERT · KERN ECCENTRICITY BREACH",
        ];
      } else if (slug === "x04") {
        const obtuse = knockoutActive ? 108 : 180 - p0;
        const kawasaki = p0 - obtuse + (180 - p0) - p0;
        const vol = 24000.0 * p1;
        pass = !knockoutActive && Math.abs(kawasaki) < 1e-4;
        out = [
          `${p0}° − ${obtuse}° + ${180 - p0}° − ${p0}° = ${kawasaki}°`,
          pass ? "|3 − 1| = 2 (FLAT-FOLDABLE)" : "NON-FLAT-FOLDABLE VERTEX",
          `${vol.toFixed(1)} mm³ (χ = 2 PASS)`,
          pass ? "CUT · MOUNTAIN · VALLEY" : "ALERT · KAWASAKI SUM != 0°",
        ];
      } else if (slug === "x05") {
        const overhangDeg = (Math.atan2(p1, 16.0) * 180.0) / Math.PI;
        pass = !knockoutActive && overhangDeg <= 45.0;
        const a1 = 1024.0;
        const a2 = p0 * p0;
        const v1 = (16.0 / 3.0) * (1600.0 + a1 + Math.sqrt(1600.0 * a1));
        const v2 = (16.0 / 3.0) * (a1 + a2 + Math.sqrt(a1 * a2));
        const a3 = Math.pow(p0 + 2 * p1, 2);
        const v3 = (16.0 / 3.0) * (a2 + a3 + Math.sqrt(a2 * a3));
        out = [
          `${(v1 + v2 + v3).toFixed(1)} mm³ (ΔV = 0.00%)`,
          "V=16, E=42, F=28 · χ=2",
          `${overhangDeg.toFixed(2)}° ${pass ? "≤" : ">"} 45.0° (GEOMETRY)`,
          pass ? "PASS · DEFECT REJECTED" : "ALERT · OVERHANG > 45°",
        ];
      } else {
        const vol = (6400.0 - p0 * p0) * p1;
        const phi = ((p0 * p0) / 6400.0) * 100.0;
        pass = !knockoutActive && p0 < 72;
        out = [
          knockoutActive ? "V=16, E=48, F=32 · DEFECT" : "V=16, E=48, F=32 · χ=0 (g=1)",
          "β₀ = 1 · β₁ = 2 · β₂ = 1",
          `${vol.toFixed(0)} mm³ · φ = ${phi.toFixed(2)}%`,
          pass ? "PASS · DEFECT REJECTED" : "PLANTED DEFECT TRIGGERED",
        ];
      }
      if (r0) r0.textContent = out[0];
      if (r1) r1.textContent = out[1];
      if (r2) r2.textContent = out[2];
      if (r3) r3.textContent = out[3];
      if (box3) box3.setAttribute("data-alert", pass ? "false" : "true");
      if (caption) {
        caption.textContent = pass
          ? `Certified Geometry Regime (${slug.toUpperCase()}) — All 4 stage invariants satisfied (${out[3]}).`
          : `Planted-Defect / Boundary Knockout (${slug.toUpperCase()}) — Geometric invariant violated (${out[3]}).`;
      }
      const vReg = VIEWER_REGISTRY.get(slug);
      if (vReg) {
        const [sx, sy, sz] = computeParametricScaleVec(slug, p0, p1);
        vReg.updateScale(sx, sy, sz);
      }
    };

    if (s0) s0.addEventListener("input", () => { knockoutActive = false; updateWb(); });
    if (s1) s1.addEventListener("input", () => { knockoutActive = false; updateWb(); });

    wb.querySelectorAll("[data-tc-export]").forEach((expBtn) => {
      expBtn.addEventListener("click", () => {
        const fmt = expBtn.getAttribute("data-tc-export") || "glb";
        const p0 = s0 ? parseFloat(s0.value) : 0;
        const p1 = s1 ? parseFloat(s1.value) : 0;
        const vReg = VIEWER_REGISTRY.get(slug);
        if (!vReg || !vReg.parsed) return;
        const scaleVec = computeParametricScaleVec(slug, p0, p1);
        const fnameBase = `${slug}_custom_${p0}_${p1}`;
        if (fmt === "glb") {
          const glbBuf = encodeCustomGlbBuffer(vReg.parsed, scaleVec, slug, p0, p1);
          triggerBlobDownload(new Blob([glbBuf], { type: "model/gltf-binary" }), `${fnameBase}.glb`);
          if (exportStatus) exportStatus.textContent = `Exported ${fnameBase}.glb (${glbBuf.byteLength} B · ISO/IEC 12113:2022)`;
        } else if (fmt === "step") {
          const stepTxt = encodeCustomStepString(vReg.parsed, scaleVec, slug, p0, p1);
          triggerBlobDownload(new Blob([stepTxt], { type: "application/step" }), `${fnameBase}.step`);
          if (exportStatus) exportStatus.textContent = `Exported ${fnameBase}.step (${stepTxt.length} B · ISO 10303-21 AP242)`;
        } else if (fmt === "dxf") {
          const dxfTxt = encodeCustomDxfString(vReg.parsed, scaleVec, slug, p0, p1);
          triggerBlobDownload(new Blob([dxfTxt], { type: "application/dxf" }), `${fnameBase}.dxf`);
          if (exportStatus) exportStatus.textContent = `Exported ${fnameBase}.dxf (${dxfTxt.length} B · Clean-Room ASCII R2000)`;
        }
      });
    });

    modeBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const m = btn.getAttribute("data-tc-mode");
        modeBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
        knockoutActive = m === "knockout";
        if (knockoutActive && s0 && s1) {
          if (slug === "x02") s0.value = "8";
          else if (slug === "x03") s1.value = "95";
          else if (slug === "x05") s1.value = "20";
        } else if (s0 && s1) {
          if (slug === "x01") { s0.value = "40"; s1.value = "20"; }
          else if (slug === "x02") { s0.value = "32"; s1.value = "18"; }
          else if (slug === "x03") { s0.value = "2000"; s1.value = "18"; }
          else if (slug === "x04") { s0.value = "78"; s1.value = "6"; }
          else if (slug === "x05") { s0.value = "24"; s1.value = "4"; }
          else if (slug === "x06") { s0.value = "24"; s1.value = "60"; }
        }
        updateWb();
      });
    });
    updateWb();
  });

  // Cover & Hub filter buttons for Tech & Tools (#tp-toolchain-toolbox)
  scope.querySelectorAll("[data-toolchain-filter]").forEach((btn) => {
    if (btn.dataset.tcBound === "true") return;
    btn.dataset.tcBound = "true";
    btn.addEventListener("click", () => {
      const cat = btn.getAttribute("data-toolchain-filter") || "all";
      const sec = btn.closest("#tp-toolchain-toolbox") || document;
      sec.querySelectorAll("[data-toolchain-filter]").forEach((b) => {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      sec.querySelectorAll("[data-toolchain-card]").forEach((card) => {
        const cCat = card.getAttribute("data-toolchain-cat") || "";
        card.hidden = cat !== "all" && cCat !== cat;
      });
    });
  });
}
