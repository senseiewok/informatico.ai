// CC.02 · La Sagrada Família: motion pause, catenary backdrop, coupled 2D-to-3D WebGL2 stereotomy atelier,
// live .GLB / .DXF CAD export, counter-rotating star column explorer, 18-tower post-tension decompression bench,
// east-west solar light & Eyring acoustics, and plaster-shard workshop drawer.
// Strict CSP: DOM APIs only, CSS classes only, no dynamic code generation; static under prefers-reduced-motion.

import { encodeCustomGlbBuffer } from "./glb-viewer.mjs";

const SVG_NS = "http://www.w3.org/2000/svg";
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

function isEs() {
  return (document.documentElement.lang || "").toLowerCase().startsWith("es");
}

function L(en, es) {
  return isEs() ? es : en;
}

function store(key, value) {
  try {
    if (value === undefined) return window.localStorage.getItem(key);
    window.localStorage.setItem(key, value);
  } catch (_e) { /* private browsing */ }
  return null;
}

function isFrozenTime() {
  const params = new URLSearchParams(window.location.search);
  const t = params.get("t");
  if (t === null || t === "") return null;
  const parsed = Number.parseFloat(t);
  return Number.isFinite(parsed) ? parsed : null;
}

function isMotionStopped() {
  return reduceMotion.matches || document.documentElement.classList.contains("sf-paused");
}

// ---------------------------------------------------------------- motion pause (WCAG 2.2.2)
function initPause() {
  const btn = document.querySelector("[data-sf-pause]");
  if (!btn) return;
  const root = document.documentElement;
  const apply = (paused) => {
    root.classList.toggle("sf-paused", paused);
    btn.setAttribute("aria-pressed", String(paused));
    btn.textContent = paused ? btn.dataset.labelResume : btn.dataset.labelPause;
  };
  apply(store("sf-motion") === "paused");
  btn.addEventListener("click", () => {
    const paused = !root.classList.contains("sf-paused");
    apply(paused);
    store("sf-motion", paused ? "paused" : "running");
  });
  document.addEventListener("visibilitychange", () => {
    if (store("sf-motion") !== "paused") {
      root.classList.toggle("sf-paused", document.hidden);
    }
  });
}

// ---------------------------------------------------------------- sticky 8-era rail & backdrop parallax
function initEraRailAndParallax() {
  const chips = new Map();
  document.querySelectorAll(".sf-era-chip").forEach((el) => chips.set(el.dataset.move, el));
  const lanes = new Map();
  document.querySelectorAll(".sf-skyline-lane").forEach((el) => lanes.set(el.dataset.move, el));
  const cards = document.querySelectorAll(".sf-card[data-move]");

  if (cards.length && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.dataset.move;
        chips.forEach((chip) => {
          chip.classList.remove("is-current");
          chip.removeAttribute("aria-current");
        });
        const activeChip = chips.get(id);
        if (activeChip) {
          activeChip.classList.add("is-current");
          activeChip.setAttribute("aria-current", "true");
        }
        lanes.forEach((lane) => lane.classList.remove("is-current"));
        const activeLane = lanes.get(id);
        if (activeLane) activeLane.classList.add("is-current");
      });
    }, { rootMargin: "-38% 0px -52% 0px" });
    cards.forEach((c) => io.observe(c));
  }

  const layers = [...document.querySelectorAll(".sf-catenary-backdrop .sf-layer")];
  if (!layers.length) return;
  let queued = false;
  const paint = () => {
    queued = false;
    if (isMotionStopped()) return;
    const y = window.scrollY;
    layers.forEach((g) => {
      const depth = Number(g.dataset.depth) || 0;
      g.setAttribute("transform", `translate(0 ${(-((y * depth) % 800)).toFixed(1)})`);
    });
  };
  window.addEventListener("scroll", () => {
    if (!queued) {
      queued = true;
      window.requestAnimationFrame(paint);
    }
  }, { passive: true });
  paint();
}

// ---------------------------------------------------------------- exact star-polygon intersection math
function starRadius(psi, n, rIn, ratio) {
  const rOut = rIn * ratio;
  const sector = (2 * Math.PI) / n;
  const half = Math.PI / n;
  const wrapped = ((((psi + half) % sector) + sector) % sector) - half;
  const phi = Math.abs(wrapped);
  const denom = rIn * Math.sin(half) * Math.cos(phi) + (rOut - rIn * Math.cos(half)) * Math.sin(phi);
  return (rOut * rIn * Math.sin(half)) / Math.max(denom, 1e-6);
}

// ---------------------------------------------------------------- watertight 3D stereotomy mesh generators
function pushTri(idxArr, a, b, c) {
  idxArr.push(a, b, c);
}

function orientOutwardTriangles(positions, indices) {
  // Check signed volume; if negative, flip winding on every triangle so signedVolume > 0 for GLB export.
  let vol6 = 0;
  for (let i = 0; i < indices.length; i += 3) {
    const i0 = indices[i] * 3;
    const i1 = indices[i + 1] * 3;
    const i2 = indices[i + 2] * 3;
    const x0 = positions[i0], y0 = positions[i0 + 1], z0 = positions[i0 + 2];
    const x1 = positions[i1], y1 = positions[i1 + 1], z1 = positions[i1 + 2];
    const x2 = positions[i2], y2 = positions[i2 + 1], z2 = positions[i2 + 2];
    vol6 += x0 * (y1 * z2 - z1 * y2) + y0 * (z1 * x2 - x1 * z2) + z0 * (x1 * y2 - y1 * x2);
  }
  if (vol6 < 0) {
    for (let i = 0; i < indices.length; i += 3) {
      const tmp = indices[i + 1];
      indices[i + 1] = indices[i + 2];
      indices[i + 2] = tmp;
    }
  }
}

export function buildStereotomyMesh(kind, params) {
  const n = params.nPoints || 12;
  const tiltRad = params.tiltRad || 0;
  const pos = [];
  const norm = [];
  const col = [];
  const idx = [];
  const lines = [];

  const tierColors = {
    6: [0.76, 0.58, 0.34],   // Montjuic sandstone
    8: [0.58, 0.62, 0.68],   // Grey granite
    10: [0.28, 0.32, 0.38],  // Black basalt
    12: [0.64, 0.25, 0.22],  // Red porphyry
  };
  const baseCol = tierColors[n] || [0.64, 0.25, 0.22];

  const addVert = (x, y, z, nx, ny, nz, rgb) => {
    const vIdx = pos.length / 3;
    const len = Math.hypot(nx, ny, nz) || 1;
    pos.push(x, y, z);
    norm.push(nx / len, ny / len, nz / len);
    col.push(rgb[0], rgb[1], rgb[2]);
    return vIdx;
  };

  if (kind === "column") {
    const H = 2.4;
    const rIn = 0.42;
    const ratio = 1.18;
    const nz = 36;
    const nPhi = 72;
    const ringStart = [];

    const cosT = Math.cos(tiltRad);
    const sinT = Math.sin(tiltRad);
    const rot = (x, y, z) => [x * cosT + y * sinT, -x * sinT + y * cosT, z];

    for (let iz = 0; iz <= nz; iz += 1) {
      const zFrac = iz / nz;
      const yLocal = -H * 0.5 + zFrac * H;
      const theta = (Math.PI / (2 * n)) * zFrac;
      const shade = 0.85 + 0.15 * zFrac;
      const rgb = [baseCol[0] * shade, baseCol[1] * shade, baseCol[2] * shade];
      ringStart.push(pos.length / 3);
      for (let ip = 0; ip < nPhi; ip += 1) {
        const phi = (ip / nPhi) * Math.PI * 2;
        const r = Math.min(starRadius(phi - theta, n, rIn, ratio), starRadius(phi + theta, n, rIn, ratio));
        const xLocal = r * Math.cos(phi);
        const zLocal = r * Math.sin(phi);
        const [wx, wy, wz] = rot(xLocal, yLocal, zLocal);
        const [wnx, wny, wnz] = rot(Math.cos(phi), 0, Math.sin(phi));
        addVert(wx, wy, wz, wnx, wny, wnz, rgb);
      }
    }

    for (let iz = 0; iz < nz; iz += 1) {
      const r0 = ringStart[iz];
      const r1 = ringStart[iz + 1];
      for (let ip = 0; ip < nPhi; ip += 1) {
        const next = (ip + 1) % nPhi;
        pushTri(idx, r0 + ip, r1 + ip, r1 + next);
        pushTri(idx, r0 + ip, r1 + next, r0 + next);
      }
    }

    // Watertight end caps
    const [bx, by, bz] = rot(0, -H * 0.5, 0);
    const [bnx, bny, bnz] = rot(0, -1, 0);
    const botCenter = addVert(bx, by, bz, bnx, bny, bnz, baseCol);
    const botRing = pos.length / 3;
    for (let ip = 0; ip < nPhi; ip += 1) {
      const phi = (ip / nPhi) * Math.PI * 2;
      const r = starRadius(phi, n, rIn, ratio);
      const [wx, wy, wz] = rot(r * Math.cos(phi), -H * 0.5, r * Math.sin(phi));
      addVert(wx, wy, wz, bnx, bny, bnz, baseCol);
    }
    for (let ip = 0; ip < nPhi; ip += 1) {
      pushTri(idx, botCenter, botRing + ip, botRing + ((ip + 1) % nPhi));
    }

    const [tx, ty, tz] = rot(0, H * 0.5, 0);
    const [tnx, tny, tnz] = rot(0, 1, 0);
    const topCenter = addVert(tx, ty, tz, tnx, tny, tnz, baseCol);
    const topRing = pos.length / 3;
    const topTheta = Math.PI / (2 * n);
    for (let ip = 0; ip < nPhi; ip += 1) {
      const phi = (ip / nPhi) * Math.PI * 2;
      const r = Math.min(starRadius(phi - topTheta, n, rIn, ratio), starRadius(phi + topTheta, n, rIn, ratio));
      const [wx, wy, wz] = rot(r * Math.cos(phi), H * 0.5, r * Math.sin(phi));
      addVert(wx, wy, wz, tnx, tny, tnz, baseCol);
    }
    for (let ip = 0; ip < nPhi; ip += 1) {
      pushTri(idx, topCenter, topRing + ((ip + 1) % nPhi), topRing + ip);
    }

    // Helical flute ridge overlay lines (two families wrapping counter-clockwise and clockwise)
    for (let k = 0; k < n; k += 1) {
      const phi0 = (k / n) * Math.PI * 2;
      for (const sgn of [1, -1]) {
        for (let iz = 0; iz < nz; iz += 1) {
          const z0 = iz / nz;
          const z1 = (iz + 1) / nz;
          const a0 = phi0 + sgn * (Math.PI / (2 * n)) * z0;
          const a1 = phi0 + sgn * (Math.PI / (2 * n)) * z1;
          const rr = rIn * ratio * 1.005;
          const pA = rot(rr * Math.cos(a0), -H * 0.5 + z0 * H, rr * Math.sin(a0));
          const pB = rot(rr * Math.cos(a1), -H * 0.5 + z1 * H, rr * Math.sin(a1));
          lines.push(...pA, ...pB);
        }
      }
    }
  } else if (kind === "hyperboloid") {
    const a = 0.68, b = 0.57, c = 0.90, vMax = 1.12;
    const nu = 56, nv = 24;
    const wall = 0.86;
    const outRings = [], inRings = [];
    const rgbOut = [0.84, 0.80, 0.72];
    const rgbIn = [0.66, 0.62, 0.55];

    const pt = (u, v, scale) => {
      const x = scale * a * (Math.cos(u) - v * Math.sin(u));
      const z = scale * b * (Math.sin(u) + v * Math.cos(u));
      const y = c * v;
      return [x, y, z];
    };

    for (let iv = 0; iv <= nv; iv += 1) {
      const v = -vMax + (2 * vMax * iv) / nv;
      outRings.push(pos.length / 3);
      for (let iu = 0; iu < nu; iu += 1) {
        const u = (iu / nu) * Math.PI * 2;
        const [x, y, z] = pt(u, v, 1.0);
        addVert(x, y, z, x / (a * a), -y / (c * c), z / (b * b), rgbOut);
      }
      inRings.push(pos.length / 3);
      for (let iu = 0; iu < nu; iu += 1) {
        const u = (iu / nu) * Math.PI * 2;
        const [x, y, z] = pt(u, v, wall);
        const ax = a * wall, bx = b * wall;
        addVert(x, y, z, -x / (ax * ax), y / (c * c), -z / (bx * bx), rgbIn);
      }
    }

    for (let iv = 0; iv < nv; iv += 1) {
      for (let iu = 0; iu < nu; iu += 1) {
        const next = (iu + 1) % nu;
        pushTri(idx, outRings[iv] + iu, outRings[iv + 1] + iu, outRings[iv + 1] + next);
        pushTri(idx, outRings[iv] + iu, outRings[iv + 1] + next, outRings[iv] + next);
        pushTri(idx, inRings[iv] + iu, inRings[iv + 1] + next, inRings[iv + 1] + iu);
        pushTri(idx, inRings[iv] + iu, inRings[iv] + next, inRings[iv + 1] + next);
      }
    }
    // Bottom & top annular caps
    for (let iu = 0; iu < nu; iu += 1) {
      const next = (iu + 1) % nu;
      pushTri(idx, outRings[0] + iu, outRings[0] + next, inRings[0] + next);
      pushTri(idx, outRings[0] + iu, inRings[0] + next, inRings[0] + iu);
      pushTri(idx, outRings[nv] + iu, inRings[nv] + next, outRings[nv] + next);
      pushTri(idx, outRings[nv] + iu, inRings[nv] + iu, inRings[nv] + next);
    }

    // Two straight-line ruling families
    for (let k = 0; k < 20; k += 1) {
      const u = (k / 20) * Math.PI * 2;
      for (const sgn of [1, -1]) {
        const x0 = 1.006 * a * (Math.cos(u) - sgn * (-vMax) * Math.sin(u));
        const z0 = 1.006 * b * (Math.sin(u) + sgn * (-vMax) * Math.cos(u));
        const x1 = 1.006 * a * (Math.cos(u) - sgn * vMax * Math.sin(u));
        const z1 = 1.006 * b * (Math.sin(u) + sgn * vMax * Math.cos(u));
        lines.push(x0, -c * vMax, z0, x1, c * vMax, z1);
      }
    }
  } else {
    // Saddle Hypar ("hypar") or Sinusoidal Conoid ("conoid") thickened closed slab
    const nx = 28, nz = 28, halfT = 0.08;
    const isConoid = kind === "conoid";
    const evalY = (x, z) => (isConoid ? 0.36 * (1 - Math.abs(z)) + 0.32 * Math.abs(z) * Math.sin(Math.PI * 2 * x) - 0.12 : 0.72 * x * z);
    const evalN = (x, z) => {
      const eps = 1e-3;
      const dydx = (evalY(x + eps, z) - evalY(x - eps, z)) / (2 * eps);
      const dydz = (evalY(x, z + eps) - evalY(x, z - eps)) / (2 * eps);
      const len = Math.hypot(-dydx, 1, -dydz) || 1;
      return [-dydx / len, 1 / len, -dydz / len];
    };
    const rgbTop = isConoid ? [0.78, 0.54, 0.36] : [0.80, 0.78, 0.72];
    const rgbBot = [0.58, 0.56, 0.52];
    const topGrid = [], botGrid = [];
    for (let ix = 0; ix <= nx; ix += 1) {
      const x = -1.0 + (2.0 * ix) / nx;
      topGrid.push([]);
      botGrid.push([]);
      for (let iz = 0; iz <= nz; iz += 1) {
        const z = -1.0 + (2.0 * iz) / nz;
        const y = evalY(x, z);
        const [nnx, nny, nnz] = evalN(x, z);
        topGrid[ix].push(addVert(x, y + halfT, z, nnx, nny, nnz, rgbTop));
        botGrid[ix].push(addVert(x, y - halfT, z, -nnx, -nny, -nnz, rgbBot));
      }
    }
    for (let ix = 0; ix < nx; ix += 1) {
      for (let iz = 0; iz < nz; iz += 1) {
        pushTri(idx, topGrid[ix][iz], topGrid[ix][iz + 1], topGrid[ix + 1][iz + 1]);
        pushTri(idx, topGrid[ix][iz], topGrid[ix + 1][iz + 1], topGrid[ix + 1][iz]);
        pushTri(idx, botGrid[ix][iz], botGrid[ix + 1][iz + 1], botGrid[ix][iz + 1]);
        pushTri(idx, botGrid[ix][iz], botGrid[ix + 1][iz], botGrid[ix + 1][iz + 1]);
      }
    }
    // Side walls
    for (let ix = 0; ix < nx; ix += 1) {
      pushTri(idx, topGrid[ix][0], topGrid[ix + 1][0], botGrid[ix + 1][0]);
      pushTri(idx, topGrid[ix][0], botGrid[ix + 1][0], botGrid[ix][0]);
      pushTri(idx, topGrid[ix][nz], botGrid[ix + 1][nz], topGrid[ix + 1][nz]);
      pushTri(idx, topGrid[ix][nz], botGrid[ix][nz], botGrid[ix + 1][nz]);
    }
    for (let iz = 0; iz < nz; iz += 1) {
      pushTri(idx, topGrid[0][iz], botGrid[0][iz + 1], topGrid[0][iz + 1]);
      pushTri(idx, topGrid[0][iz], botGrid[0][iz], botGrid[0][iz + 1]);
      pushTri(idx, topGrid[nx][iz], topGrid[nx][iz + 1], botGrid[nx][iz + 1]);
      pushTri(idx, topGrid[nx][iz], botGrid[nx][iz + 1], botGrid[nx][iz]);
    }
    // Straight rulings lying on top surface
    for (let k = -4; k <= 4; k += 1) {
      const cVal = k * 0.25;
      if (isConoid) {
        const yC = evalY(cVal, 0) + halfT + 0.008;
        const yP = evalY(cVal, 1) + halfT + 0.008;
        const yM = evalY(cVal, -1) + halfT + 0.008;
        lines.push(cVal, yC, 0, cVal, yP, 1.0);
        lines.push(cVal, yC, 0, cVal, yM, -1.0);
      } else {
        lines.push(cVal, evalY(cVal, -1) + halfT + 0.008, -1, cVal, evalY(cVal, 1) + halfT + 0.008, 1);
        lines.push(-1, evalY(-1, cVal) + halfT + 0.008, cVal, 1, evalY(1, cVal) + halfT + 0.008, cVal);
      }
    }
  }

  orientOutwardTriangles(pos, idx);

  return {
    vertexCount: pos.length / 3,
    triangleCount: idx.length / 3,
    positions: new Float32Array(pos),
    normals: new Float32Array(norm),
    colors: new Float32Array(col),
    indices: new Uint32Array(idx),
    rulingLines: new Float32Array(lines),
  };
}

// ---------------------------------------------------------------- pure-ASCII clean-room R2000 .DXF CAD export
function buildDxfString(mesh, kind, nPoints, tiltDeg) {
  const out = [
    "0", "SECTION", "2", "HEADER",
    "9", "$INSUNITS", "70", "6",
    "0", "ENDSEC",
    "0", "SECTION", "2", "TABLES",
    "0", "TABLE", "2", "LAYER", "70", "2",
    "0", "LAYER", "2", "RULINGS", "70", "0", "62", "1", "6", "CONTINUOUS",
    "0", "LAYER", "2", "SECTION", "70", "0", "62", "5", "6", "CONTINUOUS",
    "0", "ENDTAB", "0", "ENDSEC",
    "0", "SECTION", "2", "ENTITIES",
  ];
  const rLines = mesh.rulingLines;
  for (let i = 0; i + 5 < rLines.length; i += 6) {
    out.push(
      "0", "LINE", "8", "RULINGS",
      "10", rLines[i].toFixed(5), "20", rLines[i + 2].toFixed(5), "30", rLines[i + 1].toFixed(5),
      "11", rLines[i + 3].toFixed(5), "21", rLines[i + 5].toFixed(5), "31", rLines[i + 4].toFixed(5)
    );
  }
  const tris = mesh.indices;
  const maxFaces = Math.min(tris.length, 1800 * 3);
  for (let i = 0; i + 2 < maxFaces; i += 3) {
    const a = tris[i] * 3, b = tris[i + 1] * 3, c = tris[i + 2] * 3;
    const p = mesh.positions;
    out.push(
      "0", "3DFACE", "8", "SECTION",
      "10", p[a].toFixed(5), "20", p[a + 2].toFixed(5), "30", p[a + 1].toFixed(5),
      "11", p[b].toFixed(5), "21", p[b + 2].toFixed(5), "31", p[b + 1].toFixed(5),
      "12", p[c].toFixed(5), "22", p[c + 2].toFixed(5), "32", p[c + 1].toFixed(5),
      "13", p[c].toFixed(5), "23", p[c + 2].toFixed(5), "33", p[c + 1].toFixed(5)
    );
  }
  out.push("0", "ENDSEC", "0", "EOF", "");
  void kind; void nPoints; void tiltDeg;
  return out.join("\n");
}

function triggerDownload(blob, filename) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", filename);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// ---------------------------------------------------------------- WebGL2 #version 300 es stereotomy renderer
const VS_MESH = `#version 300 es
in vec3 a_pos;
in vec3 a_norm;
in vec3 a_col;
uniform mat4 u_mvp;
uniform mat3 u_nmat;
out vec3 v_norm;
out vec3 v_col;
out vec3 v_pos;
void main() {
  vec4 clip = u_mvp * vec4(a_pos, 1.0);
  gl_Position = clip;
  v_norm = normalize(u_nmat * a_norm);
  v_col = a_col;
  v_pos = a_pos;
}`;

const FS_MESH = `#version 300 es
precision highp float;
in vec3 v_norm;
in vec3 v_col;
in vec3 v_pos;
out vec4 fragColor;
void main() {
  vec3 N = normalize(v_norm);
  vec3 L1 = normalize(vec3(0.62, 0.84, 0.55));
  vec3 L2 = normalize(vec3(-0.70, 0.28, -0.52));
  vec3 V = vec3(0.0, 0.0, 1.0);
  float diff1 = max(dot(N, L1), 0.0);
  float diff2 = max(dot(N, L2), 0.0) * 0.34;
  float wrap = max(0.0, (dot(N, L1) + 0.35) / 1.35) * 0.22;
  vec3 H = normalize(L1 + V);
  float spec = pow(max(dot(N, H), 0.0), 36.0) * 0.24;
  float rim = pow(1.0 - max(abs(dot(N, V)), 0.0), 3.0) * 0.22;
  vec3 color = v_col * (0.24 + 0.72 * diff1 + diff2 + wrap) + vec3(0.95, 0.90, 0.80) * spec + vec3(0.45, 0.72, 0.95) * rim;
  fragColor = vec4(color, 1.0);
}`;

const VS_LINE = `#version 300 es
in vec3 a_pos;
uniform mat4 u_mvp;
void main() {
  gl_Position = u_mvp * vec4(a_pos, 1.0);
}`;

const FS_LINE = `#version 300 es
precision highp float;
uniform vec4 u_lineColor;
out vec4 fragColor;
void main() {
  fragColor = u_lineColor;
}`;

function mat4Perspective(fovRad, aspect, near, far) {
  const f = 1.0 / Math.tan(fovRad * 0.5);
  const nf = 1.0 / (near - far);
  return new Float32Array([
    f / aspect, 0, 0, 0,
    0, f, 0, 0,
    0, 0, (far + near) * nf, -1,
    0, 0, 2 * far * near * nf, 0,
  ]);
}

function mat4Mul(a, b) {
  const o = new Float32Array(16);
  for (let c = 0; c < 4; c += 1) {
    for (let r = 0; r < 4; r += 1) {
      o[c * 4 + r] = a[r] * b[c * 4] + a[4 + r] * b[c * 4 + 1] + a[8 + r] * b[c * 4 + 2] + a[12 + r] * b[c * 4 + 3];
    }
  }
  return o;
}

function mat4ModelView(yaw, pitch, dist) {
  const cy = Math.cos(yaw), sy = Math.sin(yaw);
  const cp = Math.cos(pitch), sp = Math.sin(pitch);
  const mv = new Float32Array([
    cy, sy * sp, -sy * cp, 0,
    0, cp, sp, 0,
    sy, -cy * sp, cy * cp, 0,
    0, 0, -dist, 1,
  ]);
  const nmat = new Float32Array([
    mv[0], mv[1], mv[2],
    mv[4], mv[5], mv[6],
    mv[8], mv[9], mv[10],
  ]);
  return { mv, nmat };
}

function compileProgram(gl, vsSrc, fsSrc) {
  const compile = (type, src) => {
    const sh = gl.createShader(type);
    gl.shaderSource(sh, src);
    gl.compileShader(sh);
    if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) {
      const log = gl.getShaderInfoLog(sh);
      gl.deleteShader(sh);
      throw new Error(log || "Shader compile error");
    }
    return sh;
  };
  const vs = compile(gl.VERTEX_SHADER, vsSrc);
  const fs = compile(gl.FRAGMENT_SHADER, fsSrc);
  const prog = gl.createProgram();
  gl.attachShader(prog, vs);
  gl.attachShader(prog, fs);
  gl.linkProgram(prog);
  gl.deleteShader(vs);
  gl.deleteShader(fs);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
    const log = gl.getProgramInfoLog(prog);
    gl.deleteProgram(prog);
    throw new Error(log || "Program link error");
  }
  return prog;
}

// ---------------------------------------------------------------- Coupled 2D Funicular + 3D WebGL2 Atelier
function initCoupledAtelier() {
  const root = document.querySelector("[data-sf-atelier]");
  if (!root) return;

  const svg = root.querySelector(".sf-funicular-svg");
  const catPath = svg.querySelector(".sf-funicular-catenary");
  const parPath = svg.querySelector(".sf-funicular-parabola");
  const butL = svg.querySelector(".sf-funicular-buttress-l");
  const butR = svg.querySelector(".sf-funicular-buttress-r");
  const colL = svg.querySelector(".sf-funicular-column-l");
  const colR = svg.querySelector(".sf-funicular-column-r");
  const loadArrow = svg.querySelector(".sf-funicular-load");
  const funReadout = root.querySelector("[data-sf-fun-readout]");

  const lanternRange = root.querySelector("#sf-lantern-range");
  const lanternVal = root.querySelector("#sf-lantern-val");
  const aRange = root.querySelector("#sf-catenary-a-range");
  const aVal = root.querySelector("#sf-catenary-a-val");
  const invertCheck = root.querySelector("#sf-invert-gravity");
  const buttressCheck = root.querySelector("#sf-show-buttress");

  const modeBtns = [...root.querySelectorAll("[data-sf-surface]")];
  const nBtns = [...root.querySelectorAll("[data-sf-n]")];
  const rulingsCheck = root.querySelector("#sf-show-rulings");
  const exportGlbBtn = root.querySelector('[data-sf-export="glb"]');
  const exportDxfBtn = root.querySelector('[data-sf-export="dxf"]');
  const cadReadout = root.querySelector("[data-sf-cad-readout]");
  const canvasWrap = root.querySelector(".sf-canvas-wrap");
  let canvas = root.querySelector("#sf-webgl-canvas");

  const span = Number(root.dataset.span) || 15.0;
  const wKn = Number(root.dataset.wkn) || 18.0;

  const state = {
    lanternKn: Number(lanternRange.value) || 160,
    aParam: Number(aRange.value) || 6.0,
    inverted: true,
    showButtress: true,
    kind: "column",
    nPoints: 12,
    showRulings: true,
    tiltRad: 0.28,
    tiltDeg: 16.4,
    yaw: 0.52,
    pitch: 0.34,
    dist: 4.1,
    mesh: null,
  };

  // --- Left Stage Funicular solver & SVG sync
  const updateFunicular = () => {
    const L_span = span;
    const a = state.aParam;
    const W = state.lanternKn;
    const H = wKn * a;
    const alpha0 = W > 0 ? Math.asinh(W / (2 * H)) : 0;
    const V = H * Math.sinh(L_span / (2 * a) + alpha0);
    const tiltRad = Math.atan2(H, V);
    const tiltDeg = (tiltRad * 180) / Math.PI;
    state.tiltRad = tiltRad;
    state.tiltDeg = tiltDeg;

    const riseLoaded = a * (Math.cosh(L_span / (2 * a) + alpha0) - Math.cosh(alpha0));
    const riseUnloaded = a * (Math.cosh(L_span / (2 * a)) - 1);
    const kinkDeg = (2 * Math.atan2(0.5 * W, H) * 180) / Math.PI;

    let maxGapM = 0;
    const ptsCat = [];
    const ptsPar = [];
    const baseScreenY = state.inverted ? 248 : 54;
    const dir = state.inverted ? -1 : 1;
    const x0 = 60, wPx = 340;
    const scaleY = 148 / Math.max(riseLoaded, 6.0);

    for (let i = 0; i <= 200; i += 1) {
      const xm = -L_span * 0.5 + (L_span * i) / 200;
      const yc0 = a * (Math.cosh(L_span / (2 * a)) - Math.cosh(Math.abs(xm) / a));
      const yp0 = riseUnloaded * (1 - Math.pow((2 * xm) / L_span, 2));
      maxGapM = Math.max(maxGapM, Math.abs(yc0 - yp0));
    }

    const N = 60;
    for (let i = 0; i <= N; i += 1) {
      const xm = -L_span * 0.5 + (L_span * i) / N;
      const ym = a * (Math.cosh(L_span / (2 * a) + alpha0) - Math.cosh(Math.abs(xm) / a + alpha0));
      const yp0 = riseUnloaded * (1 - Math.pow((2 * xm) / L_span, 2));
      const sx = x0 + ((xm + L_span * 0.5) / L_span) * wPx;
      const syCat = baseScreenY + dir * ym * scaleY;
      const syPar = baseScreenY + dir * yp0 * (148 / Math.max(riseLoaded, 6.0));
      ptsCat.push(`${i === 0 ? "M" : "L"}${sx.toFixed(1)},${syCat.toFixed(1)}`);
      ptsPar.push(`${i === 0 ? "M" : "L"}${sx.toFixed(1)},${syPar.toFixed(1)}`);
    }
    catPath.setAttribute("d", ptsCat.join(" "));
    parPath.setAttribute("d", ptsPar.join(" "));

    // Inclined columns below the springers follow resultant angle tan(theta) = H / V
    const dxCol = Math.sin(tiltRad) * 62;
    const dyCol = Math.cos(tiltRad) * 62;
    if (state.inverted) {
      colL.setAttribute("x1", String(x0));
      colL.setAttribute("y1", String(baseScreenY));
      colL.setAttribute("x2", (x0 - dxCol).toFixed(1));
      colL.setAttribute("y2", (baseScreenY + dyCol).toFixed(1));
      colR.setAttribute("x1", String(x0 + wPx));
      colR.setAttribute("y1", String(baseScreenY));
      colR.setAttribute("x2", (x0 + wPx + dxCol).toFixed(1));
      colR.setAttribute("y2", (baseScreenY + dyCol).toFixed(1));
    } else {
      colL.setAttribute("x1", String(x0));
      colL.setAttribute("y1", String(baseScreenY));
      colL.setAttribute("x2", String(x0));
      colL.setAttribute("y2", String(baseScreenY));
      colR.setAttribute("x1", String(x0 + wPx));
      colR.setAttribute("y1", String(baseScreenY));
      colR.setAttribute("x2", String(x0 + wPx));
      colR.setAttribute("y2", String(baseScreenY));
    }
    const visBut = state.showButtress ? "1" : "0";
    butL.setAttribute("opacity", visBut);
    butR.setAttribute("opacity", visBut);

    const crownY = baseScreenY + dir * riseLoaded * scaleY;
    const arrowLen = Math.max(8, (W / 320) * 34);
    loadArrow.setAttribute("d", `M 230 ${crownY - arrowLen - 6} L 230 ${crownY - 4} M 224 ${crownY - 11} L 230 ${crownY - 3} L 236 ${crownY - 11}`);
    loadArrow.setAttribute("opacity", W > 0 ? "1" : "0");

    lanternVal.textContent = `${W.toFixed(0)} kN`;
    aVal.textContent = `${a.toFixed(1)} m`;
    lanternRange.setAttribute("aria-valuetext", `${W.toFixed(0)} kN`);
    aRange.setAttribute("aria-valuetext", `${a.toFixed(1)} m`);

    funReadout.textContent = L(
      `MODEL thrust H = ${H.toFixed(1)} kN · V = ${V.toFixed(1)} kN · Column tilt from vertical θ = ${tiltDeg.toFixed(2)}° · Crown kink = ${kinkDeg.toFixed(1)}° · Catenary-vs-parabola gap = ${(maxGapM * 1000).toFixed(1)} mm`,
      `MODELO empuje H = ${H.toFixed(1)} kN · V = ${V.toFixed(1)} kN · Inclinación desde vertical θ = ${tiltDeg.toFixed(2)}° · Quiebre en clave = ${kinkDeg.toFixed(1)}° · Brecha catenaria-parábola = ${(maxGapM * 1000).toFixed(1)} mm`
    );
  };

  // --- Right Stage WebGL2 renderer
  let gl = canvas.getContext("webgl2", { antialias: true, preserveDrawingBuffer: true });
  let progMesh = null, progLine = null;
  let meshVao = null, lineVao = null;
  let posBuf = null, normBuf = null, colBuf = null, idxBuf = null, lineBuf = null;
  let rafId = 0, visibleOnScreen = true;
  const frozenSec = isFrozenTime();

  const downgradeTo2D = () => {
    if (gl && canvas.parentElement) {
      const unlocked = canvas.cloneNode(false);
      canvas.replaceWith(unlocked);
      canvas = unlocked;
      gl = null;
    }
    canvas.dataset.rendererMode = "2d-fallback";
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const w = canvas.width || 640, h = canvas.height || 480;
    ctx.fillStyle = "#0e141b";
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = "#8ac8ff";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i < 16; i += 1) {
      const x = w * 0.35 + i * 12;
      ctx.moveTo(x, h * 0.2);
      ctx.lineTo(w * 0.65 - i * 12, h * 0.8);
    }
    ctx.stroke();
  };

  const uploadMeshBuffers = () => {
    state.mesh = buildStereotomyMesh(state.kind, { nPoints: state.nPoints, tiltRad: state.tiltRad });
    if (!gl || !meshVao) return;
    const m = state.mesh;
    gl.bindVertexArray(meshVao);
    gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
    gl.bufferData(gl.ARRAY_BUFFER, m.positions, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, normBuf);
    gl.bufferData(gl.ARRAY_BUFFER, m.normals, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, colBuf);
    gl.bufferData(gl.ARRAY_BUFFER, m.colors, gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, idxBuf);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, m.indices, gl.STATIC_DRAW);

    gl.bindVertexArray(lineVao);
    gl.bindBuffer(gl.ARRAY_BUFFER, lineBuf);
    gl.bufferData(gl.ARRAY_BUFFER, m.rulingLines, gl.STATIC_DRAW);
    gl.bindVertexArray(null);
  };

  const initGL = () => {
    if (!gl) {
      downgradeTo2D();
      return;
    }
    try {
      canvas.dataset.rendererMode = "webgl2";
      progMesh = compileProgram(gl, VS_MESH, FS_MESH);
      progLine = compileProgram(gl, VS_LINE, FS_LINE);

      posBuf = gl.createBuffer();
      normBuf = gl.createBuffer();
      colBuf = gl.createBuffer();
      idxBuf = gl.createBuffer();
      lineBuf = gl.createBuffer();

      meshVao = gl.createVertexArray();
      gl.bindVertexArray(meshVao);
      const aPos = gl.getAttribLocation(progMesh, "a_pos");
      const aNorm = gl.getAttribLocation(progMesh, "a_norm");
      const aCol = gl.getAttribLocation(progMesh, "a_col");
      gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
      gl.enableVertexAttribArray(aPos);
      gl.vertexAttribPointer(aPos, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, normBuf);
      gl.enableVertexAttribArray(aNorm);
      gl.vertexAttribPointer(aNorm, 3, gl.FLOAT, false, 0, 0);
      gl.bindBuffer(gl.ARRAY_BUFFER, colBuf);
      gl.enableVertexAttribArray(aCol);
      gl.vertexAttribPointer(aCol, 3, gl.FLOAT, false, 0, 0);

      lineVao = gl.createVertexArray();
      gl.bindVertexArray(lineVao);
      const lPos = gl.getAttribLocation(progLine, "a_pos");
      gl.bindBuffer(gl.ARRAY_BUFFER, lineBuf);
      gl.enableVertexAttribArray(lPos);
      gl.vertexAttribPointer(lPos, 3, gl.FLOAT, false, 0, 0);
      gl.bindVertexArray(null);

      uploadMeshBuffers();
    } catch (_err) {
      downgradeTo2D();
    }
  };

  const drawFrame = (timeMs = 0) => {
    if (!gl || !progMesh || !state.mesh) {
      if (!gl) downgradeTo2D();
      return;
    }
    const w = canvas.width, h = canvas.height;
    if (!w || !h) return;
    gl.viewport(0, 0, w, h);
    gl.clearColor(0.055, 0.078, 0.106, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    gl.enable(gl.DEPTH_TEST);

    const spin = frozenSec !== null ? frozenSec * 0.25 : (isMotionStopped() ? 0 : timeMs * 0.00022);
    const { mv, nmat } = mat4ModelView(state.yaw + spin, state.pitch, state.dist);
    const proj = mat4Perspective(0.72, w / h, 0.1, 30.0);
    const mvp = mat4Mul(proj, mv);

    gl.useProgram(progMesh);
    gl.uniformMatrix4fv(gl.getUniformLocation(progMesh, "u_mvp"), false, mvp);
    gl.uniformMatrix3fv(gl.getUniformLocation(progMesh, "u_nmat"), false, nmat);
    gl.bindVertexArray(meshVao);
    gl.drawElements(gl.TRIANGLES, state.mesh.indices.length, gl.UNSIGNED_INT, 0);

    if (state.showRulings && state.mesh.rulingLines.length > 0) {
      gl.useProgram(progLine);
      gl.uniformMatrix4fv(gl.getUniformLocation(progLine, "u_mvp"), false, mvp);
      gl.uniform4f(gl.getUniformLocation(progLine, "u_lineColor"), 0.96, 0.72, 0.26, 0.95);
      gl.bindVertexArray(lineVao);
      gl.drawArrays(gl.LINES, 0, state.mesh.rulingLines.length / 3);
    }
    gl.bindVertexArray(null);
  };

  const syncCadReadout = (extraMsg = "") => {
    const m = state.mesh;
    if (!m) return;
    const base = L(
      `3D ${state.kind.toUpperCase()} · ${m.vertexCount} vertices · ${m.triangleCount} triangles · Tilt ${state.tiltDeg.toFixed(1)}°`,
      `3D ${state.kind.toUpperCase()} · ${m.vertexCount} vértices · ${m.triangleCount} triángulos · Inclinación ${state.tiltDeg.toFixed(1)}°`
    );
    cadReadout.textContent = extraMsg ? `${base} · ${extraMsg}` : base;
  };

  const refreshAll = () => {
    updateFunicular();
    uploadMeshBuffers();
    drawFrame(performance.now());
    syncCadReadout();
  };

  // Loop management
  const startLoop = () => {
    window.cancelAnimationFrame(rafId);
    if (frozenSec !== null || !gl) {
      drawFrame(0);
      return;
    }
    const tick = (now) => {
      if (visibleOnScreen && !document.hidden) {
        drawFrame(now);
      }
      if (!isMotionStopped()) {
        rafId = window.requestAnimationFrame(tick);
      }
    };
    rafId = window.requestAnimationFrame(tick);
  };

  // ResizeObserver with DPR <= 2
  const ro = new ResizeObserver((entries) => {
    for (const entry of entries) {
      const { width, height } = entry.contentRect;
      if (!width || !height) continue;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const dw = Math.round(width * dpr);
      const dh = Math.round(height * dpr);
      if (canvas.width !== dw || canvas.height !== dh) {
        canvas.width = dw;
        canvas.height = dh;
        drawFrame(performance.now());
      }
    }
  });
  ro.observe(canvasWrap);

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      visibleOnScreen = entries.some((e) => e.isIntersecting);
    }, { threshold: 0.05 });
    io.observe(canvasWrap);
  }

  // Context loss recovery
  canvasWrap.addEventListener("webglcontextlost", (e) => {
    e.preventDefault();
    window.cancelAnimationFrame(rafId);
  });
  canvasWrap.addEventListener("webglcontextrestored", () => {
    initGL();
    startLoop();
  });

  // Pointer & keyboard camera on stable wrapper/canvas
  let dragId = null, lastX = 0, lastY = 0;
  canvasWrap.addEventListener("pointerdown", (e) => {
    if (e.target !== canvas) return;
    dragId = e.pointerId;
    lastX = e.clientX;
    lastY = e.clientY;
    if (canvas.setPointerCapture) canvas.setPointerCapture(dragId);
  });
  canvasWrap.addEventListener("pointermove", (e) => {
    if (dragId === null || e.pointerId !== dragId) return;
    state.yaw += (e.clientX - lastX) * 0.012;
    state.pitch = Math.max(-1.35, Math.min(1.35, state.pitch + (e.clientY - lastY) * 0.012));
    lastX = e.clientX;
    lastY = e.clientY;
    drawFrame(performance.now());
  });
  const endDrag = () => { dragId = null; };
  canvasWrap.addEventListener("pointerup", endDrag);
  canvasWrap.addEventListener("pointercancel", endDrag);

  canvas.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") { state.yaw -= 0.14; drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key === "ArrowRight") { state.yaw += 0.14; drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key === "ArrowUp") { state.pitch = Math.min(1.35, state.pitch + 0.12); drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key === "ArrowDown") { state.pitch = Math.max(-1.35, state.pitch - 0.12); drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key === "+" || e.key === "=") { state.dist = Math.max(2.2, state.dist - 0.25); drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key === "-") { state.dist = Math.min(7.5, state.dist + 0.25); drawFrame(performance.now()); e.preventDefault(); }
    else if (e.key.toLowerCase() === "r") { state.yaw = 0.52; state.pitch = 0.34; state.dist = 4.1; drawFrame(performance.now()); }
  });

  // UI listeners
  lanternRange.addEventListener("input", () => { state.lanternKn = Number(lanternRange.value); refreshAll(); });
  aRange.addEventListener("input", () => { state.aParam = Number(aRange.value); refreshAll(); });
  invertCheck.addEventListener("change", () => { state.inverted = invertCheck.checked; updateFunicular(); });
  buttressCheck.addEventListener("change", () => { state.showButtress = buttressCheck.checked; updateFunicular(); });
  rulingsCheck.addEventListener("change", () => { state.showRulings = rulingsCheck.checked; drawFrame(performance.now()); });

  modeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      state.kind = btn.dataset.sfSurface;
      modeBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      uploadMeshBuffers();
      drawFrame(performance.now());
      syncCadReadout();
    });
  });

  nBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      state.nPoints = Number(btn.dataset.sfN) || 12;
      nBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      if (state.kind !== "column") {
        state.kind = "column";
        modeBtns.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.sfSurface === "column")));
      }
      uploadMeshBuffers();
      drawFrame(performance.now());
      syncCadReadout();
    });
  });

  exportGlbBtn.addEventListener("click", () => {
    const m = state.mesh || buildStereotomyMesh(state.kind, { nPoints: state.nPoints, tiltRad: state.tiltRad });
    const glbBuf = encodeCustomGlbBuffer(m, [1, 1, 1], `cc02-${state.kind}`, state.lanternKn, state.tiltDeg);
    triggerDownload(new Blob([glbBuf], { type: "model/gltf-binary" }), `sagrada-cc02-${state.kind}.glb`);
    syncCadReadout(L(`Exported .GLB (${glbBuf.byteLength.toLocaleString("en-US")} bytes)`, `Exportado .GLB (${glbBuf.byteLength.toLocaleString("en-US")} bytes)`));
  });

  exportDxfBtn.addEventListener("click", () => {
    const m = state.mesh || buildStereotomyMesh(state.kind, { nPoints: state.nPoints, tiltRad: state.tiltRad });
    const dxfStr = buildDxfString(m, state.kind, state.nPoints, state.tiltDeg);
    triggerDownload(new Blob([dxfStr], { type: "application/dxf" }), `sagrada-cc02-${state.kind}.dxf`);
    syncCadReadout(L(`Exported R2000 .DXF (${dxfStr.length.toLocaleString("en-US")} bytes)`, `Exportado .DXF R2000 (${dxfStr.length.toLocaleString("en-US")} bytes)`));
  });

  window.addEventListener("tp-lang-change", () => { updateFunicular(); syncCadReadout(); });

  initGL();
  refreshAll();
  startLoop();
}

// ---------------------------------------------------------------- Counter-Rotating Star Column Hierarchy Explorer
function initColumnHierarchy() {
  const box = document.querySelector("[data-sf-columns]");
  if (!box) return;
  const svg = box.querySelector(".sf-star-svg");
  const polyA = svg.querySelector(".sf-star-ghost-a");
  const polyB = svg.querySelector(".sf-star-ghost-b");
  const polyCap = svg.querySelector(".sf-star-core");
  const zRange = box.querySelector("#sf-col-z-range");
  const zVal = box.querySelector("#sf-col-z-val");
  const tierRadios = [...box.querySelectorAll('input[name="sf-col-tier"]')];
  const readout = box.querySelector("[data-sf-col-readout]");

  const tiers = {
    6:  { stoneEn: "Montjuïc sandstone", stoneEs: "Arenisca de Montjuïc", dIn: 1.05, load: 4200 },
    8:  { stoneEn: "Gray granite",       stoneEs: "Granito gris",         dIn: 1.40, load: 8800 },
    10: { stoneEn: "Black basalt",       stoneEs: "Basalto negro",        dIn: 1.75, load: 16500 },
    12: { stoneEn: "Red porphyry",       stoneEs: "Pórfido rojo",         dIn: 2.10, load: 29000 },
  };

  const render = () => {
    const active = tierRadios.find((r) => r.checked);
    const n = Number(active ? active.value : 12);
    const spec = tiers[n];
    const zFrac = Number(zRange.value) / 100;
    const theta = (Math.PI / (2 * n)) * zFrac;

    const rIn = spec.dIn * 0.5;
    const pxScale = 64 / 1.05;
    const cx = 150, cy = 140;
    const ptsA = [], ptsB = [], ptsC = [];
    let areaGross = 0;
    const S = 180;
    const dphi = (2 * Math.PI) / S;

    for (let i = 0; i < S; i += 1) {
      const phi = i * dphi;
      const ra = starRadius(phi - theta, n, rIn, 1.18);
      const rb = starRadius(phi + theta, n, rIn, 1.18);
      const rc = Math.min(ra, rb);
      areaGross += 0.5 * rc * rc * dphi;
      ptsA.push(`${(cx + ra * pxScale * Math.cos(phi)).toFixed(1)},${(cy + ra * pxScale * Math.sin(phi)).toFixed(1)}`);
      ptsB.push(`${(cx + rb * pxScale * Math.cos(phi)).toFixed(1)},${(cy + rb * pxScale * Math.sin(phi)).toFixed(1)}`);
      ptsC.push(`${(cx + rc * pxScale * Math.cos(phi)).toFixed(1)},${(cy + rc * pxScale * Math.sin(phi)).toFixed(1)}`);
    }

    polyA.setAttribute("points", ptsA.join(" "));
    polyB.setAttribute("points", ptsB.join(" "));
    polyCap.setAttribute("points", ptsC.join(" "));

    const rVoid = rIn * 0.14;
    const areaNet = areaGross - Math.PI * rVoid * rVoid;
    const stressMpa = spec.load / areaNet / 1000;
    const hTotal = 2 * n;
    const hShaft = 10 * spec.dIn;
    const flutes = zFrac <= 0.005 ? n : 2 * n;

    zVal.textContent = zFrac.toFixed(2);
    zRange.setAttribute("aria-valuetext", zFrac.toFixed(2));
    readout.textContent = L(
      `${n}-pt ${spec.stoneEn} · H_total = ${hTotal.toFixed(0)} m · D_in = ${spec.dIn.toFixed(2)} m (H_shaft = ${hShaft.toFixed(1)} m) · Flutes = ${flutes} · A_net = ${areaNet.toFixed(2)} m² · MODEL σ = ${stressMpa.toFixed(2)} MPa`,
      `${n} puntas ${spec.stoneEs} · H_total = ${hTotal.toFixed(0)} m · D_int = ${spec.dIn.toFixed(2)} m (H_fuste = ${hShaft.toFixed(1)} m) · Estrías = ${flutes} · A_neta = ${areaNet.toFixed(2)} m² · MODELO σ = ${stressMpa.toFixed(2)} MPa`
    );
  };

  zRange.addEventListener("input", render);
  tierRadios.forEach((r) => r.addEventListener("change", render));
  window.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- 18-Tower & Post-Tensioned Stone Panel Bench
function initTowersAndPostTension() {
  const box = document.querySelector("[data-sf-towers]");
  if (!box) return;
  const fptRange = box.querySelector("#sf-fpt-range");
  const fptVal = box.querySelector("#sf-fpt-val");
  const windRange = box.querySelector("#sf-wind-range");
  const windVal = box.querySelector("#sf-wind-val");
  const trapPoly = box.querySelector(".sf-stress-trap");
  const readout = box.querySelector("[data-sf-pt-readout]");

  const b = 2.40, t = 0.45, h = 4.80, nDuct = 4, rDuct = 0.030, deadKn = 320.0;
  const aNet = b * t - nDuct * Math.PI * rDuct * rDuct;
  const iNet = (b * t * t * t) / 12 - nDuct * (Math.PI * Math.pow(rDuct, 4) / 4);
  const zNet = iNet / (t / 2);

  const render = () => {
    const fPt = Number(fptRange.value);
    const qWind = Number(windRange.value);
    const mWind = 0.5 * qWind * b * h * h;
    const sigAx = (fPt + deadKn) / aNet / 1000;
    const sigBend = mWind / zNet / 1000;
    const sigMin = sigAx - sigBend;
    const sigMax = sigAx + sigBend;

    // Map stress [-1.5, +3.5] MPa onto trapezoid SVG x in [40, 200] where 0 MPa datum sits at y = 120
    const yZero = 112;
    const scale = 28;
    const yL = yZero - sigMin * scale;
    const yR = yZero - sigMax * scale;
    trapPoly.setAttribute("points", `40,${yZero} 40,${yL.toFixed(1)} 220,${yR.toFixed(1)} 220,${yZero}`);
    trapPoly.classList.toggle("sf-stress-comp", sigMin >= 0);
    trapPoly.classList.toggle("sf-stress-tens", sigMin < 0);

    fptVal.textContent = `${fPt.toFixed(0)} kN`;
    windVal.textContent = `${qWind.toFixed(2)} kPa`;
    fptRange.setAttribute("aria-valuetext", `${fPt.toFixed(0)} kN`);
    windRange.setAttribute("aria-valuetext", `${qWind.toFixed(2)} kPa`);

    const stateStr = sigMin >= 0
      ? L("JOINT IN COMPRESSION", "JUNTA EN COMPRESIÓN")
      : L("WINDWARD DECOMPRESSION (TENSION)", "DESCOMPRESIÓN A BARLOVENTO (TRACCIÓN)");

    readout.textContent = L(
      `MODEL M_wind = ${mWind.toFixed(2)} kN·m · σ_min = ${sigMin.toFixed(2)} MPa · σ_max = ${sigMax.toFixed(2)} MPa · ${stateStr}`,
      `MODELO M_viento = ${mWind.toFixed(2)} kN·m · σ_min = ${sigMin.toFixed(2)} MPa · σ_max = ${sigMax.toFixed(2)} MPa · ${stateStr}`
    );
  };

  fptRange.addEventListener("input", render);
  windRange.addEventListener("input", render);
  window.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- East-West Solar Chromatics & Eyring Acoustics
function initLightAndAcoustics() {
  const box = document.querySelector("[data-sf-light]");
  if (!box) return;
  const hourRange = box.querySelector("#sf-solar-range");
  const hourVal = box.querySelector("#sf-solar-val");
  const rayPoly = box.querySelector(".sf-light-ray");
  const readout = box.querySelector("[data-sf-light-readout]");

  const render = () => {
    const hr = Number(hourRange.value);
    const hh = Math.floor(hr);
    const mm = Math.round((hr - hh) * 60);
    const timeStr = `${String(hh).padStart(2, "0")}:${String(mm).padStart(2, "0")}`;
    hourVal.textContent = timeStr;
    hourRange.setAttribute("aria-valuetext", timeStr);

    rayPoly.classList.remove("sf-ray-dawn", "sf-ray-noon", "sf-ray-dusk");
    if (hr < 10.5) {
      rayPoly.classList.add("sf-ray-dawn");
      rayPoly.setAttribute("points", "40,70 40,115 245,190 190,190");
    } else if (hr <= 14.5) {
      rayPoly.classList.add("sf-ray-noon");
      rayPoly.setAttribute("points", "150,30 210,30 235,190 125,190");
    } else {
      rayPoly.classList.add("sf-ray-dusk");
      rayPoly.setAttribute("points", "320,70 320,115 170,190 115,190");
    }

    // Eyring 1930 illustrative hall volume & stone absorption coefficient alpha = 0.045 (MODEL)
    const vol = 185000, area = 26400, alpha = 0.045;
    const rt60 = (0.161 * vol) / (-area * Math.log(1 - alpha));
    const phaseNote = hr < 10.5
      ? L("East Nativity glass · cool cyan-emerald shafts", "Vitrales oriente del Nacimiento · haces cian-esmeralda")
      : (hr <= 14.5
        ? L("Noon zenith oculi · warm stone star glow", "Mediodía cenital por óculos · resplandor estrellado")
        : L("West Passion glass · deep amber-crimson shafts", "Vitrales poniente de la Pasión · haces ámbar-carmesí"));

    readout.textContent = `${timeStr} · ${phaseNote} · ${L("MODEL Eyring stone RT60", "MODELO RT60 de Eyring en piedra")} ≈ ${rt60.toFixed(1)} s`;
  };

  hourRange.addEventListener("input", render);
  window.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- Plaster-Shard Workshop Drawer (Easter Egg)
function initWorkshopDrawer() {
  const btn = document.querySelector(".sf-drawer-btn");
  const panel = document.getElementById("sf-drawer-panel");
  if (!btn || !panel) return;
  const wrap = btn.closest(".sf-drawer");
  const label = btn.querySelector(".sf-drawer-label");

  const setOpen = (open) => {
    panel.hidden = !open;
    wrap.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", String(open));
    if (label) label.textContent = open ? btn.dataset.labelClose : btn.dataset.labelOpen;
    if (open && !reduceMotion.matches) {
      panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  };

  btn.addEventListener("click", () => setOpen(panel.hidden));
  document.addEventListener("keydown", (e) => {
    if (e.defaultPrevented || document.querySelector("dialog[open]")) return;
    if (!wrap.contains(document.activeElement)) return;
    if (e.key === "Escape" && !panel.hidden) {
      setOpen(false);
      btn.focus();
    }
  });
}

// ---------------------------------------------------------------- Five-Generation Torch Relay (1882-2026+)
function initGenerationsRelay() {
  const root = document.querySelector("[data-sf-relay]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-sf-gen]")];
  const segs = [...root.querySelectorAll("[data-sf-seg]")];
  const cards = [...root.querySelectorAll("[data-sf-relay-card]")];

  const activate = (idx) => {
    btns.forEach((btn) => btn.setAttribute("aria-pressed", String(Number(btn.dataset.sfGen) === idx)));
    segs.forEach((seg) => seg.classList.toggle("is-active", Number(seg.dataset.sfSeg) === idx));
    cards.forEach((card) => { card.hidden = Number(card.dataset.sfRelayCard) !== idx; });
  };

  btns.forEach((btn) => {
    btn.addEventListener("click", () => activate(Number(btn.dataset.sfGen) || 0));
  });
  segs.forEach((seg) => {
    seg.addEventListener("click", () => activate(Number(seg.dataset.sfSeg) || 0));
  });
}

// ---------------------------------------------------------------- 1936 Plaster-Shard Algebraic Recovery Bench
function initShardRecoveryBench() {
  const root = document.querySelector("[data-sf-shard]");
  if (!root) return;
  const range = root.querySelector("#sf-caliper-range");
  const valEl = root.querySelector("#sf-caliper-val");
  const readout = root.querySelector("[data-sf-shard-readout]");
  const polyTrue = root.querySelector(".sf-shard-true");
  const polyFree = root.querySelector(".sf-shard-freeform");
  const polyRuled = root.querySelector(".sf-shard-ruled");
  const polyPiece = root.querySelector(".sf-shard-piece");
  if (!range || !polyRuled) return;

  const aTrue = 1.80;
  const cTrue = 2.40;
  const kTrue = (aTrue / cTrue) * (aTrue / cTrue);
  const z1 = 0.20;
  const z2 = 0.55;
  const zTarget = 3.00;
  const rTrue = (z) => Math.sqrt(aTrue * aTrue + kTrue * z * z);
  const r1 = rTrue(z1);
  const r2 = rTrue(z2);
  const dr1 = (kTrue * z1) / r1;
  const d2r1 = (kTrue * aTrue * aTrue) / (r1 * r1 * r1);
  const rFree = (z) => r1 + dr1 * (z - z1) + 0.5 * d2r1 * (z - z1) * (z - z1);

  const svgX = (r) => (75 + ((r - 1.5) / 1.8) * 215).toFixed(1);
  const svgY = (z) => (220 - (z / zTarget) * 190).toFixed(1);
  const buildPts = (fn, zStart, zEnd, steps) => {
    const pts = [];
    for (let i = 0; i <= steps; i += 1) {
      const z = zStart + (zEnd - zStart) * (i / steps);
      pts.push(`${svgX(fn(z))},${svgY(z)}`);
    }
    return pts.join(" ");
  };

  if (polyTrue) polyTrue.setAttribute("points", buildPts(rTrue, 0, zTarget, 15));
  if (polyFree) polyFree.setAttribute("points", buildPts(rFree, z1, zTarget, 14));
  if (polyPiece) polyPiece.setAttribute("points", buildPts(rTrue, z1, z2, 4));

  const render = () => {
    const epsMm = Number(range.value) || 0;
    const delta = epsMm * 0.001;
    const r1m = r1 + delta;
    const r2m = r2 - delta;
    const kRec = (r2m * r2m - r1m * r1m) / (z2 * z2 - z1 * z1);
    const aRec2 = Math.max(0.01, r1m * r1m - kRec * z1 * z1);
    const aRec = Math.sqrt(aRec2);
    const cRec = aRec / Math.sqrt(Math.max(1e-6, kRec));
    const rRuled = (z) => Math.sqrt(Math.max(0.01, aRec2 + kRec * z * z));
    const ruledErrMm = Math.abs(rRuled(zTarget) - rTrue(zTarget)) * 1000.0;
    const freeErrMm = Math.abs(rFree(zTarget) - rTrue(zTarget)) * 1000.0;

    polyRuled.setAttribute("points", buildPts(rRuled, 0, zTarget, 15));
    const txt = `${epsMm.toFixed(1)} mm`;
    if (valEl) valEl.textContent = txt;
    range.setAttribute("aria-valuetext", txt);
    if (readout) {
      readout.textContent = `${L("MODEL recovered", "MODELO recuperado")} a = ${aRec.toFixed(3)} m · c = ${cRec.toFixed(3)} m · ${L("Ruled rim err", "Error reglado")} = ${ruledErrMm.toFixed(1)} mm vs ${L("Freeform drift", "Deriva libre")} = ${freeErrMm.toFixed(1)} mm`;
    }
  };

  range.addEventListener("input", render);
  window.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- Dual-Scale 1:500 <-> 1:10 Tectonic Loupe
function initTectonicLoupe() {
  const root = document.querySelector("[data-sf-loupe]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-sf-node]")];
  const dots = [...root.querySelectorAll("[data-sf-node-dot]")];
  const views = [...root.querySelectorAll("[data-sf-loupe-view]")];
  const cards = [...root.querySelectorAll("[data-sf-node-card]")];

  const activate = (idx) => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(Number(b.dataset.sfNode) === idx)));
    dots.forEach((d) => d.classList.toggle("is-active", Number(d.dataset.sfNodeDot) === idx));
    views.forEach((v) => {
      const active = Number(v.dataset.sfLoupeView) === idx;
      v.classList.toggle("is-active", active);
      if (active) v.removeAttribute("hidden");
      else v.setAttribute("hidden", "");
    });
    cards.forEach((c) => { c.hidden = Number(c.dataset.sfNodeCard) !== idx; });
  };

  btns.forEach((b) => b.addEventListener("click", () => activate(Number(b.dataset.sfNode) || 0)));
  dots.forEach((d) => d.addEventListener("click", () => activate(Number(d.dataset.sfNodeDot) || 0)));
}

// ---------------------------------------------------------------- Alluvial / Sankey Gravity-Flux Conservation Ribbon
function initSankeyRibbon() {
  const root = document.querySelector("[data-sf-sankey]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-sf-loadpath]")];
  const modes = [...root.querySelectorAll("[data-sf-sankey-mode]")];
  const readout = root.querySelector("[data-sf-sankey-readout]");
  let active = "gaudi";

  const sync = () => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.sfLoadpath === active)));
    modes.forEach((m) => {
      const show = m.dataset.sfSankeyMode === active;
      m.classList.toggle("is-active", show);
      if (show) m.removeAttribute("hidden");
      else m.setAttribute("hidden", "");
    });
    if (readout) {
      readout.textContent = active === "gaudi"
        ? L(readout.dataset.gaudiEn, readout.dataset.gaudiEs)
        : L(readout.dataset.gothicEn, readout.dataset.gothicEs);
    }
  };

  btns.forEach((b) => b.addEventListener("click", () => { active = b.dataset.sfLoadpath || "gaudi"; sync(); }));
  window.addEventListener("tp-lang-change", sync);
  sync();
}

// ---------------------------------------------------------------- 6-Axis Polar Structural & Acoustic Radar
function initPolarRadar() {
  const root = document.querySelector("[data-sf-radar]");
  if (!root) return;
  const btns = [...root.querySelectorAll("[data-sf-radar-era]")];
  const poly = root.querySelector(".sf-radar-poly");
  const readout = root.querySelector("[data-sf-radar-readout]");
  if (!poly || btns.length === 0) return;

  const cx = 240;
  const cy = 160;
  const rMax = 94;
  const angles = Array.from({ length: 6 }, (_, i) => -Math.PI / 2 + i * (Math.PI / 3));
  let currentBtn = btns.find((b) => b.getAttribute("aria-pressed") === "true") || btns[btns.length - 1];

  const render = () => {
    btns.forEach((b) => b.setAttribute("aria-pressed", String(b === currentBtn)));
    const scores = (currentBtn.dataset.scores || "98,95,97,94,92,88").split(",").map(Number);
    const pts = scores.map((sc, i) => {
      const r = rMax * (Math.max(0, Math.min(100, sc || 0)) / 100);
      return `${(cx + r * Math.cos(angles[i])).toFixed(1)},${(cy + r * Math.sin(angles[i])).toFixed(1)}`;
    }).join(" ");
    poly.setAttribute("points", pts);
    if (readout) {
      const eraLabel = L(currentBtn.dataset.en, currentBtn.dataset.es);
      const eraNote = L(currentBtn.dataset.noteEn, currentBtn.dataset.noteEs);
      readout.textContent = `${eraLabel} · ${eraNote}`;
    }
  };

  btns.forEach((b) => b.addEventListener("click", () => { currentBtn = b; render(); }));
  window.addEventListener("tp-lang-change", render);
  render();
}

// ---------------------------------------------------------------- Filterable 10-Plate Archive & Native <dialog> Lightbox
function initVisualGalleryAndLightbox() {
  const gallery = document.querySelector("[data-sf-gallery]");
  const dialog = document.getElementById("sf-lightbox");
  if (!gallery) return;

  const filterBtns = [...gallery.querySelectorAll("[data-sf-filter]")];
  const galleryCards = [...gallery.querySelectorAll(".sf-gallery-grid .sf-media-card")];

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const mode = btn.dataset.sfFilter || "all";
      filterBtns.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      galleryCards.forEach((card) => {
        card.hidden = mode !== "all" && card.dataset.sfMediaKind !== mode;
      });
    });
  });

  if (!dialog) return;
  const imgEl = document.getElementById("sf-lightbox-img");
  const badgeEl = document.getElementById("sf-lb-badge");
  const capEl = document.getElementById("sf-lb-cap");
  const prevBtn = dialog.querySelector("[data-sf-lb-prev]");
  const nextBtn = dialog.querySelector("[data-sf-lb-next]");
  const closeBtn = dialog.querySelector("[data-sf-lb-close]");

  const items = [...gallery.querySelectorAll(".sf-gallery-grid .sf-media-card")].map((card) => {
    const btn = card.querySelector("[data-sf-open-media]");
    const thumb = card.querySelector(".sf-media-frame img");
    return {
      id: btn ? btn.dataset.sfOpenMedia : "",
      thumbSrc: (thumb && thumb.getAttribute("src")) || "",
      data: btn ? btn.dataset : {},
    };
  });
  let activeIndex = 0;
  let openerEl = null;

  const showAt = (idx) => {
    if (items.length === 0) return;
    activeIndex = (idx + items.length) % items.length;
    const item = items[activeIndex];
    const d = item.data;
    if (imgEl) {
      imgEl.setAttribute("src", item.thumbSrc || "");
      imgEl.setAttribute("alt", L(d.altEn, d.altEs));
    }
    if (badgeEl) badgeEl.textContent = L(d.badgeEn, d.badgeEs);
    if (capEl) capEl.textContent = L(d.capEn, d.capEs);
  };

  document.querySelectorAll("[data-sf-open-media]").forEach((btn) => {
    btn.addEventListener("click", () => {
      openerEl = btn;
      const idx = items.findIndex((x) => x.id === btn.dataset.sfOpenMedia);
      showAt(idx >= 0 ? idx : 0);
      if (typeof dialog.showModal === "function") dialog.showModal();
    });
  });

  if (prevBtn) prevBtn.addEventListener("click", () => showAt(activeIndex - 1));
  if (nextBtn) nextBtn.addEventListener("click", () => showAt(activeIndex + 1));
  if (closeBtn) closeBtn.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
  });
  dialog.addEventListener("close", () => {
    if (openerEl && typeof openerEl.focus === "function") openerEl.focus();
  });
  document.addEventListener("keydown", (e) => {
    if (!dialog.open) return;
    if (e.key === "ArrowLeft") { showAt(activeIndex - 1); e.preventDefault(); }
    else if (e.key === "ArrowRight") { showAt(activeIndex + 1); e.preventDefault(); }
  });
  window.addEventListener("tp-lang-change", () => { if (dialog.open) showAt(activeIndex); });
}

initPause();
initEraRailAndParallax();
initGenerationsRelay();
initTectonicLoupe();
initCoupledAtelier();
initSankeyRibbon();
initColumnHierarchy();
initShardRecoveryBench();
initTowersAndPostTension();
initLightAndAcoustics();
initPolarRadar();
initVisualGalleryAndLightbox();
initWorkshopDrawer();
