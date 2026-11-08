/**
 * @file webgl-observatory.mjs
 * @description Zero-build WebGL2 4-Lens Continuum, Tectonic & Biophysical Surface Observatory
 * for the Informatico.ai 30-Folio Living Monograph Platform.
 *
 * Upgraded per Frontier Council Mandate:
 * 1. 30 Distinct 3D Geometries (`potentialSurface(vec2 xz)` branches for every Pillar 0..4 × Folio 0..5).
 * 2. Folio-differentiated mineral colormaps, grid scales, and camera perspectives.
 * 3. True Y-Up 3D Turntable Spherical Camera + 5-Step Binary Bisection Raymarcher.
 * 4. Folio-Specific Lens 3 (Noether-Kirchhoff 4-Stage Alluvial Ribbon reading the Folio's actual 4 stepper stages)
 *    and Lens 4 (6-Axis Polar Performance Radar reading the Folio's actual 2 sliders + 4 readout metrics).
 */

const VERTEX_SHADER_SRC = `#version 300 es
in vec2 a_position;
out vec2 v_uv;
void main() {
  v_uv = a_position * 0.5 + 0.5;
  gl_Position = vec4(a_position, 0.0, 1.0);
}
`;

const FRAGMENT_SHADER_SRC = `#version 300 es
precision highp float;

in vec2 v_uv;
out vec4 fragColor;

uniform vec2 u_resolution;
uniform float u_time;
uniform vec2 u_rotation;   // x = pitch (elevation radians), y = yaw (azimuth radians)
uniform float u_affinity;  // primary folio slider normalized driver (1..25)
uniform float u_bias;      // secondary folio slider driver (-60..+40)
uniform float u_theme;     // 0.0 = Limestone Paper (light), 1.0 = Blueprint Plate (dark)
uniform float u_pillar;    // 0 = engineering, 1 = architecture, 2 = physics, 3 = math, 4 = cf
uniform float u_folio;     // 0..5 = folio index within pillar (e.g. e01=0 .. e06=5)
uniform float u_mode;      // 0.0 = 3D Turntable Slab, 1.0 = 2D Phase-Space Streamlines
uniform float u_zoom;      // camera radius (default 3.05)

// Evaluate 30 distinct folio-specific 3D surfaces y = f(x, z) over domain (x, z) in [-1.15, 1.15]^2
float potentialSurface(vec2 xz) {
  float aNorm = clamp((u_affinity - 1.0) / 24.0, 0.0, 1.0);
  float bNorm = clamp((u_bias + 60.0) / 100.0, 0.0, 1.0);
  float r = length(xz);
  float r2 = dot(xz, xz);
  float breath = 0.028 * sin(u_time * 1.75);

  if (u_pillar < 0.5) {
    // Pillar I: Civil Engineering & Construction (E.01..E.06)
    if (u_folio < 0.5) {
      // E.01: Darcy-Brinkman Porous Percolation Throat Lattice & Critical Saddle (phi_c = 0.5927)
      float pores = 0.34 * cos(4.2 * xz.x + u_time * 0.8) * cos(4.2 * xz.y) * (0.45 + 0.55 * aNorm);
      float channel = -0.36 * exp(-6.0 * xz.y * xz.y) * smoothstep(0.35, 0.85, aNorm);
      float brinkmanRim = 0.28 * exp(-3.8 * pow(xz.x - 0.25 * (bNorm - 0.5), 2.0)) - 0.16 * r2;
      return pores + channel + brinkmanRim + breath;
    } else if (u_folio < 1.5) {
      // E.02: Herschel-Bulkley 3D Bingham Plug-Core Cylinder + Annular Shear Velocity Dome
      float plugR = mix(0.22, 0.78, 1.0 - aNorm);
      float plateau = smoothstep(plugR + 0.32, plugR, r);
      float shearWave = 0.08 * cos(6.0 * atan(xz.y, xz.x) + u_time * 1.4) * (1.0 - plateau);
      return -0.28 + (0.62 + 0.25 * bNorm) * plateau + shearWave + breath;
    } else if (u_folio < 2.5) {
      // E.03: Sub-Wavelength Coiled Helmholtz Acoustic Metamaterial Ring Resonator
      float spiralAng = atan(xz.y, xz.x);
      float labyrinth = 0.26 * cos(10.0 * r - 2.0 * spiralAng + u_time * 1.1) * exp(-0.55 * r2);
      float helmholtzWell = -0.58 * exp(-9.5 * r2) * (0.45 + 0.55 * aNorm);
      float neckRim = 0.24 * exp(-18.0 * pow(r - 0.48, 2.0)) * (0.5 + 0.5 * bNorm);
      return 0.12 + labyrinth + helmholtzWell + neckRim + breath;
    } else if (u_folio < 3.5) {
      // E.04: Kays-London Cross-Corrugated Chevron Enthalpy Exchanger Plates
      float chevronA = 0.22 * sin(7.5 * (xz.x + 0.8 * xz.y) + u_time * 0.9);
      float chevronB = 0.22 * sin(7.5 * (xz.x - 0.8 * xz.y) - u_time * 0.9);
      float ntuPlane = 0.32 * (aNorm - 0.35) * xz.x - 0.24 * (bNorm - 0.5) * xz.y;
      return 0.06 + (chevronA + chevronB) * (0.55 + 0.45 * aNorm) + ntuPlane;
    } else if (u_folio < 4.5) {
      // E.05: Terzaghi 3D Consolidation Settlement Dish + 4 CFA Pile Bearing Cones
      float dish = -0.38 * exp(-1.6 * r2) * (1.15 - 0.65 * aNorm);
      vec2 pCell = abs(xz) - vec2(0.55);
      float piles = 0.52 * exp(-14.0 * dot(pCell, pCell)) * (0.6 + 0.4 * bNorm);
      float poreIso = 0.12 * cos(4.5 * xz.x + u_time * 1.2) * cos(4.5 * xz.y);
      return dish + piles + poreIso;
    } else if (u_folio < 5.5) {
      // E.06: ASCE 7-22 Lead-Rubber Base Isolator Hysteretic Energy Bowl & Spiral Shear Core
      float bowl = 0.36 * r2 - 0.28;
      float leadCore = 0.44 * exp(-9.0 * r2) * (0.5 + 0.5 * bNorm);
      float hysteresis = 0.14 * sin(3.5 * xz.x + 2.5 * xz.y + u_time * 1.6) * aNorm;
      return bowl + leadCore + hysteresis;
    } else if (u_folio < 6.5) {
      // E.07: Scanlan Long-Span Suspension Bridge Aeroelastic Flutter & Twin-Box Torsional Wave
      float spanCable = 0.38 * xz.x * xz.x - 0.18;
      float flutterTorsion = (0.16 + 0.28 * aNorm) * sin(4.2 * xz.x - u_time * 2.2) * xz.y;
      float twinGap = -0.22 * exp(-18.0 * xz.y * xz.y) * (0.5 + 0.5 * bNorm);
      return spanCable + flutterTorsion + twinGap + breath;
    } else if (u_folio < 7.5) {
      // E.08: EPB-TBM Peck-Mair Gaussian Subsurface Settlement Trough & Cutterhead Cone
      float trough = -(0.28 + 0.38 * aNorm) * exp(-4.2 * xz.x * xz.x / (0.35 + 0.65 * bNorm)) * smoothstep(-0.8, 0.6, xz.y);
      float tbmShield = 0.34 * exp(-9.0 * dot(xz - vec2(0.0, -0.45), xz - vec2(0.0, -0.45)));
      return 0.08 + trough + tbmShield + breath * 0.5;
    } else if (u_folio < 8.5) {
      // E.09: Autogenous Self-Healing Concrete Crack Fissure & Rhombohedral CaCO3 Bridges
      float fissure = -(0.46 - 0.32 * bNorm) * exp(-22.0 * xz.x * xz.x / (0.35 + 0.65 * aNorm));
      float calciteBridges = (0.18 + 0.28 * bNorm) * exp(-18.0 * xz.x * xz.x) * pow(cos(7.5 * xz.y + u_time * 1.2), 2.0);
      float codaWave = 0.06 * cos(12.0 * r - u_time * 2.4);
      return 0.12 + fissure + calciteBridges + codaWave;
    } else {
      // E.10: 3D Concrete Printing (3DCP) Corrugated Layer Stack & Roussel Thixotropic Ridge
      float layerRibs = 0.08 * cos(16.0 * xz.y) * exp(-3.5 * xz.x * xz.x);
      float funicularWall = (0.42 + 0.24 * aNorm) * exp(-6.5 * pow(xz.x - 0.14 * sin(5.0 * xz.y), 2.0));
      float buckleMode = 0.14 * (1.0 - aNorm) * sin(3.5 * xz.y - u_time * 1.8) * xz.x;
      return -0.16 + funicularWall + layerRibs + buckleMode;
    }
  } else if (u_pillar < 1.5) {
    // Pillar II: Architecture (A.01..A.08)
    if (u_folio < 0.5) {
      // A.01: Heyman Biaxial Catenary Masonry Groin Vault & Middle-Third Kern Ribs
      float rise = mix(0.34, 0.74, aNorm);
      float ecc = (bNorm - 0.5) * 0.36;
      float vault = rise * (1.0 - 0.60 * (pow(xz.x - ecc, 2.0) + 0.72 * pow(xz.y, 2.0))) - 0.12;
      float groinRibs = 0.11 * exp(-18.0 * pow(abs(xz.x) - abs(xz.y), 2.0));
      return vault + groinRibs + breath * 0.5;
    } else if (u_folio < 1.5) {
      // A.02: Reciprocal Timber Gridshell (Nexorade 4-Beam Pinwheel Lattice)
      float dome = (0.42 + 0.32 * aNorm) * (1.0 - 0.52 * r2);
      float weave = 0.13 * (sin(11.0 * xz.x + 5.5 * xz.y) + sin(11.0 * xz.y - 5.5 * xz.x)) * 0.5;
      float lapNotch = -0.12 * exp(-16.0 * r2) * (1.0 - bNorm);
      return dome + weave + lapNotch - 0.08;
    } else if (u_folio < 2.5) {
      // A.03: Double-Skin Facade Buoyancy Stack Canyon & Rising Thermal Plume Waves
      float cavityTrough = -0.38 * exp(-8.5 * xz.x * xz.x);
      float outerSkin = 0.36 * exp(-22.0 * pow(abs(xz.x) - 0.62, 2.0));
      float stackPlume = 0.22 * sin(5.5 * xz.y - u_time * 2.1) * exp(-5.0 * xz.x * xz.x) * (0.45 + 0.55 * aNorm);
      float louverfins = 0.07 * cos(14.0 * xz.y) * smoothstep(0.35, 0.75, abs(xz.x));
      return 0.05 + cavityTrough + outerSkin + stackPlume + louverfins + 0.12 * bNorm;
    } else if (u_folio < 3.5) {
      // A.04: Archigram Plug-In Megastructure & British High-Tech Gerberette Exoskeleton Truss
      float spanArch = (0.32 + 0.28 * aNorm) * (1.0 - 0.45 * xz.x * xz.x);
      float gerberetteCantilever = 0.22 * exp(-10.0 * pow(abs(xz.x) - 0.78, 2.0)) * cos(3.0 * xz.y);
      float diagrid = 0.085 * cos(9.0 * (xz.x + xz.y)) * cos(9.0 * (xz.x - xz.y));
      float podPulse = 0.12 * exp(-12.0 * dot(xz - vec2(0.0, 0.45 * (bNorm - 0.5)), xz - vec2(0.0, 0.45 * (bNorm - 0.5)))) * (1.0 + 0.3 * sin(u_time * 2.2));
      return spanArch + gerberetteCantilever + diagrid + podPulse - 0.12;
    } else if (u_folio < 4.5) {
      // A.05: Schroeder Prime-Sequence (p=17) Stepped Acoustic Diffuser & Sabine Vault
      float qrdIdx = floor((xz.x + 1.15) * 4.8);
      float qrdRes = mod(qrdIdx * qrdIdx, 7.0) / 7.0;
      float steppedWells = -0.28 * qrdRes * (0.45 + 0.55 * aNorm);
      float shellArch = 0.38 * (1.0 - 0.48 * xz.y * xz.y);
      float waveFront = 0.09 * cos(8.0 * r - u_time * 1.8) * (0.4 + 0.6 * bNorm);
      return shellArch + steppedWells + waveFront - 0.04;
    } else if (u_folio < 5.5) {
      // A.06: Terraced Subsurface Constructed Wetland Cascade & UV-C Fluence Cone
      float terrace = -0.22 * floor((xz.x + 1.15) * 1.6) + 0.24;
      float reedBeds = 0.08 * sin(9.0 * xz.x) * cos(9.0 * xz.y) * (1.0 - 0.4 * aNorm);
      float uvcCone = 0.52 * exp(-11.0 * dot(xz - vec2(0.45, 0.0), xz - vec2(0.45, 0.0))) * (0.45 + 0.55 * bNorm);
      return terrace + reedBeds + uvcCone + breath;
    } else if (u_folio < 6.5) {
      // A.07: Luis Barragán Chromatic Stucco Planes, Water Pool Reflection & Kubelka-Munk Radiosity
      float pinkWall = (0.34 + 0.24 * aNorm) * smoothstep(-0.25, -0.55, xz.x);
      float yellowCorridor = (0.28 + 0.22 * bNorm) * smoothstep(0.25, 0.55, xz.x);
      float waterPool = -0.18 + 0.06 * sin(9.5 * xz.x + 6.0 * xz.y - u_time * 2.0) * smoothstep(0.45, 0.0, abs(xz.x));
      return pinkWall + yellowCorridor + waterPool;
    } else if (u_folio < 7.5) {
      // A.08: Daytime Radiative Sky-Cooling Photonic Multilayer (8-13 um Window) & PCM Roof
      float windowWell = -0.46 * exp(-6.5 * xz.x * xz.x) * (0.45 + 0.55 * aNorm);
      float braggLayers = 0.14 * cos(12.0 * xz.y + u_time * 1.1) * (0.5 + 0.5 * bNorm);
      float solarRim = 0.32 * (1.0 - exp(-3.5 * r2));
      return 0.08 + windowWell + braggLayers + solarRim;
    } else if (u_folio < 8.5) {
      // A.09: Timoshenko Hygroscopic Beech Bilayer Curvature Petal
      float timoshenkoCurl = (0.24 + 0.42 * aNorm) * (xz.x + 0.85) * (xz.x + 0.85) * 0.28 / (0.55 + 0.45 * bNorm);
      float woodGrain = 0.05 * sin(14.0 * xz.y + 3.0 * xz.x);
      return -0.22 + timoshenkoCurl + woodGrain + breath * 0.4;
    } else {
      // A.10: Miura-Ori Kinetic Origami Tessellation & Auxetic Saddle
      float zigX = abs(fract(xz.x * 2.2) - 0.5) * 2.0;
      float zigY = abs(fract(xz.y * 2.2 + 0.25 * zigX) - 0.5) * 2.0;
      float miuraFacets = (0.22 + 0.26 * (1.0 - aNorm)) * (zigX * 0.65 + zigY * 0.35) - 0.18;
      float auxeticSaddle = 0.18 * (xz.x * xz.x - 0.85 * xz.y * xz.y) * (0.5 + 0.5 * bNorm);
      return miuraFacets + auxeticSaddle;
    }
  } else if (u_pillar < 2.5) {
    // Pillar III: Physics (P.01..P.08)
    if (u_folio < 0.5) {
      // P.01: Keizer Non-Equilibrium Asymmetric Double-Well Landscape Tilted by ATP Affinity
      float wellL = -0.46 * exp(-5.0 * (pow(xz.x + 0.54, 2.0) + 1.4 * xz.y * xz.y));
      float wellR = -0.64 * mix(0.45, 1.15, aNorm) * exp(-5.0 * (pow(xz.x - 0.54, 2.0) + 1.4 * xz.y * xz.y));
      float barrier = 0.44 * exp(-8.5 * xz.x * xz.x - 1.8 * xz.y * xz.y) * (1.1 - 0.55 * aNorm);
      float tilt = -0.16 * (aNorm - 0.45) * xz.x + 0.12 * (bNorm - 0.5) * xz.y;
      return 0.24 + wellL + wellR + barrier + tilt + breath;
    } else if (u_folio < 1.5) {
      // P.02: Kuramoto Metachronal Symplectic Ciliary Travelling Wave Train
      float kPhase = 6.2 * xz.x - 2.8 * xz.y - u_time * 2.4;
      float metachronal = (0.22 + 0.24 * aNorm) * sin(kPhase) * exp(-0.25 * r2);
      float whipHarmonic = 0.11 * cos(2.0 * kPhase + 0.6) * (0.4 + 0.6 * bNorm);
      return 0.04 + metachronal + whipHarmonic;
    } else if (u_folio < 2.5) {
      // P.03: Carreau-Yasuda Entangled Mucin Biopolymer Mesh & Shear-Thinning Furrow
      float meshCage = 0.26 * (cos(6.5 * xz.x) * cos(6.5 * xz.y)) * (1.15 - 0.65 * aNorm);
      float shearTrough = -0.42 * exp(-5.5 * xz.y * xz.y) * (0.35 + 0.65 * bNorm);
      float subdiffTrap = -0.32 * exp(-12.0 * r2) * (1.0 - aNorm);
      return 0.12 + meshCage + shearTrough + subdiffTrap + breath;
    } else if (u_folio < 3.5) {
      // P.04: Donnan-Nernst-Planck Osmotic Brush Terrace vs. Hyperconcentrated Mucus Step
      float brushStep = 0.34 * tanh(-3.8 * (xz.x - 0.25 * (aNorm - 0.5)));
      float donnanRipples = 0.09 * sin(10.0 * xz.y + u_time * 1.5) * smoothstep(-0.2, 0.6, -xz.x);
      float osmoticCrush = -0.28 * (1.0 - bNorm) * smoothstep(-0.1, 0.7, xz.x);
      return 0.08 + brushStep + donnanRipples + osmoticCrush;
    } else if (u_folio < 4.5) {
      // P.05: WKB Quantum Proton-Tunneling Barrier Ridge & Evanescent Wave Packet
      float barrierRidge = (0.68 - 0.34 * aNorm) * exp(-16.0 * xz.x * xz.x);
      float incidentWave = 0.18 * cos(11.0 * xz.x - u_time * 2.5) * smoothstep(0.1, -0.8, xz.x) * exp(-1.5 * xz.y * xz.y);
      float transmittedWave = (0.06 + 0.18 * aNorm * bNorm) * cos(11.0 * xz.x - u_time * 2.5) * smoothstep(-0.1, 0.8, xz.x) * exp(-1.5 * xz.y * xz.y);
      return -0.14 + barrierRidge + incidentWave + transmittedWave;
    } else if (u_folio < 5.5) {
      // P.06: Doi-Edwards Curvilinear Polymer Reptation Tube Canyon & Writhe Chain
      float snakeCenter = 0.46 * sin(2.5 * xz.x + 0.4 * u_time);
      float distToTube = abs(xz.y - snakeCenter);
      float tubeWalls = 0.42 * smoothstep(0.14, 0.48, distToTube) - 0.24;
      float polymerChain = 0.28 * exp(-28.0 * distToTube * distToTube) * (0.55 + 0.45 * cos(9.0 * xz.x - u_time * 2.0)) * (0.5 + 0.5 * aNorm);
      return tubeWalls + polymerChain;
    } else if (u_folio < 6.5) {
      // P.07: Formula 1 Venturi Underfloor Suction Throat, Vortex Edge Seal & Active X/Z-Mode
      float venturiThroat = -(0.42 + 0.32 * (1.0 - aNorm)) * exp(-7.5 * xz.x * xz.x) * exp(-2.2 * xz.y * xz.y);
      float edgeVortex = 0.26 * exp(-16.0 * pow(abs(xz.y) - 0.65, 2.0)) * cos(7.0 * xz.x - u_time * 2.6);
      float diffuserRamp = 0.28 * smoothstep(0.1, 1.0, xz.x) * (0.5 + 0.5 * bNorm);
      return 0.08 + venturiThroat + edgeVortex + diffuserRamp;
    } else if (u_folio < 7.5) {
      // P.08: Bragg Thin-Film Interference Waves (Automotive Pearlescence vs. Barragán Stucco)
      float braggWave = (0.28 + 0.24 * aNorm) * cos(9.0 * r - u_time * 2.2) * exp(-0.45 * r2);
      float stuccoDiffuse = 0.14 * sin(8.0 * xz.x) * sin(8.0 * xz.y) * (1.0 - bNorm);
      return braggWave + stuccoDiffuse;
    } else if (u_folio < 8.5) {
      // P.09: Sir Geoffrey Taylor 49.3-deg Electrohydrodynamic Cone & Monodisperse Jet
      float taylorCone = 0.62 * max(0.0, 0.72 - r * 0.86);
      float apexJet = 0.26 * exp(-28.0 * r2) * (1.0 + 0.35 * cos(14.0 * r - u_time * 3.0));
      float equipotential = -0.14 * sqrt(r + 0.05) * (0.5 + 0.5 * bNorm);
      return -0.12 + taylorCone + apexJet + equipotential;
    } else {
      // P.10: Haldane-Raghu Topological Photonic Berry Curvature & Chiral Edge Mode
      float diracK1 = 0.38 * exp(-9.5 * dot(xz - vec2(-0.42, 0.0), xz - vec2(-0.42, 0.0)));
      float diracK2 = -0.38 * (aNorm > 0.35 ? -1.0 : 1.0) * exp(-9.5 * dot(xz - vec2(0.42, 0.0), xz - vec2(0.42, 0.0)));
      float chiralEdge = 0.28 * exp(-18.0 * pow(xz.y - 0.68, 2.0)) * cos(8.0 * xz.x - u_time * 2.8);
      return diracK1 + diracK2 + chiralEdge;
    }
  } else if (u_pillar < 4.5) {
    // Pillar IV: Formal Mathematics & Complexity (M.01..M.12)
    if (u_folio < 0.5) {
      // M.01: Lean 4 Fermat / Taylor-Wiles 5-Stage Modularity Bridge Reduction
      float chain = 0.22 * cos(5.2 * xz.x) * exp(-2.2 * xz.y * xz.y);
      float unbridgedPeak = 0.62 * exp(-9.0 * (pow(xz.x - 0.35, 2.0) + xz.y * xz.y)) * (1.05 - 0.72 * aNorm);
      float galoisValley = -0.30 * exp(-6.0 * pow(xz.x + 0.42, 2.0)) * (0.4 + 0.6 * bNorm);
      return -0.05 + chain + unbridgedPeak + galoisValley + breath;
    } else if (u_folio < 1.5) {
      // M.02: Riemann XiPrime Critical-Line Zero-Free Canyon (sigma = 1/2) & Gram Cliffs
      float critCanyon = -0.52 * exp(-14.0 * xz.x * xz.x);
      float zeroPockets = -0.24 * pow(cos(6.5 * xz.y + u_time * 0.8), 2.0) * exp(-16.0 * xz.x * xz.x);
      float densityCliffs = 0.48 * (1.0 - exp(-3.5 * xz.x * xz.x)) * (0.55 + 0.45 * aNorm);
      return 0.14 + critCanyon + zeroPockets + densityCliffs;
    } else if (u_folio < 2.5) {
      // M.03: FunSearch Cap-Set F_3^n Combinatorial Lattice Plateaus & Tensor Saddle
      vec2 grid3 = fract((xz + 1.15) * 1.32) - 0.5;
      float capTower = 0.48 * exp(-18.0 * dot(grid3, grid3)) * (0.45 + 0.55 * aNorm);
      float tensorBase = -0.22 * (xz.x * xz.y) * (0.5 + 0.5 * bNorm) - 0.14;
      return tensorBase + capTower + breath * 0.5;
    } else if (u_folio < 3.5) {
      // M.04: Polynomial Freiman-Ruzsa Entropic Gaussian Subgroup Convolution Dome
      float centralBell = 0.64 * exp(-2.4 * r2 / (0.45 + 0.75 * aNorm));
      float cosetRipples = 0.18 * (1.0 - aNorm) * cos(7.5 * xz.x) * cos(7.5 * xz.y);
      return -0.22 + centralBell + cosetRipples + 0.10 * bNorm + breath;
    } else if (u_folio < 4.5) {
      // M.05: AlphaGeometry 2 Neuro-Symbolic Polyhedral Tropical Roof & Intersection Ridge
      float f1 = 0.52 - 0.68 * abs(xz.x - 0.18 * (aNorm - 0.5));
      float f2 = 0.52 - 0.68 * abs(xz.y - 0.18 * (bNorm - 0.5));
      float f3 = 0.44 - 0.52 * abs(xz.x + xz.y);
      float tropRoof = max(max(f1, f2), f3);
      float auxCone = 0.24 * exp(-16.0 * r2) * sin(u_time * 1.8);
      return tropRoof + auxCone - 0.12;
    } else if (u_folio < 5.5) {
      // M.06: Williams Sub-Cubic APSP & (min, +) Tropical Matrix Shortcut Trough
      float diagShortcut = -0.48 * exp(-8.5 * pow(xz.x - xz.y, 2.0)) * (0.45 + 0.55 * aNorm);
      float cubicHills = 0.36 * exp(-4.5 * pow(xz.x + xz.y, 2.0)) + 0.12 * cos(6.0 * xz.x) * sin(6.0 * xz.y);
      return 0.10 + diagShortcut + cubicHills;
    } else if (u_folio < 6.5) {
      // M.07: Formula 1 350 kW Pontryagin Hamiltonian Saddle & Fourier Neural Operator Mode Surface
      float hamiltonian = 0.34 * (xz.x * xz.x - 0.75 * xz.y * xz.y) * (0.5 + 0.5 * aNorm);
      float fnoModes = 0.18 * cos(6.0 * xz.x + u_time * 1.8) * cos(5.0 * xz.y) * (0.4 + 0.6 * bNorm);
      return hamiltonian + fnoModes;
    } else if (u_folio < 7.5) {
      // M.08: Schrödinger Riemannian Color Manifold & MacAdam Metric Ellipsoids
      float schrodingerDome = 0.48 * sqrt(max(0.05, 1.0 - 0.42 * r2)) - 0.22;
      float macadamEllipses = 0.14 * exp(-12.0 * (1.8 * pow(xz.x - 0.25 * (aNorm - 0.5), 2.0) + 0.7 * pow(xz.y - 0.25 * (bNorm - 0.5), 2.0)));
      return schrodingerDome + macadamEllipses + breath * 0.5;
    } else if (u_folio < 8.5) {
      // M.09: Benamou-Brenier Wasserstein-2 Geodesic Optimal Transport Bridge
      float tInterp = clamp(0.5 * (xz.y + 1.0), 0.0, 1.0);
      float meanShift = mix(-0.52, 0.52, tInterp);
      float w2Bridge = 0.56 * exp(-9.0 * pow(xz.x - meanShift, 2.0) / (0.65 + 0.45 * tInterp));
      return -0.20 + w2Bridge + breath * 0.4;
    } else {
      // M.10: Vietoris-Rips Simplicial Filtration & Betti Percolation Saddle
      float vrPeaks = 0.36 * (exp(-12.0 * dot(xz - vec2(-0.45, -0.35), xz - vec2(-0.45, -0.35)))
        + exp(-12.0 * dot(xz - vec2(0.45, -0.35), xz - vec2(0.45, -0.35)))
        + exp(-12.0 * dot(xz - vec2(0.0, 0.48), xz - vec2(0.0, 0.48))));
      float h1CycleHole = -0.44 * exp(-16.0 * r2) * (0.45 + 0.55 * aNorm);
      return -0.06 + vrPeaks + h1CycleHole + breath * 0.4;
    }
  } else {
    // Pillar V: Open-Bounty & Grand-Challenge Prize Crucible (B.01..B.06)
    if (u_folio < 0.5) {
      // B.01: Erdős Sidon B2 Difference Lattice &Erdős-Turán Bowl
      float rulerWaves = 0.28 * cos(6.5 * xz.x) * cos(6.5 * xz.y) * (0.4 + 0.6 * aNorm);
      float turanBowl = 0.34 * r2 - 0.24;
      float collisionSpike = 0.42 * bNorm * exp(-14.0 * dot(xz - vec2(0.25, -0.25), xz - vec2(0.25, -0.25)));
      return turanBowl + rulerWaves + collisionSpike + breath * 0.5;
    } else if (u_folio < 1.5) {
      // B.02: Kitaev Rotated Surface-Code Checkerboard & FeMoCo QPE Well
      float checker = 0.26 * sin(7.5 * xz.x) * sin(7.5 * xz.y) * (0.5 + 0.5 * aNorm);
      float femocoWell = -0.52 * exp(-8.5 * r2) * (1.1 - 0.5 * bNorm);
      float thresholdRidge = 0.30 * bNorm * exp(-12.0 * xz.x * xz.x);
      return 0.08 + checker + femocoWell + thresholdRidge + breath * 0.4;
    } else if (u_folio < 2.5) {
      // B.03: Bendsøe-Sigmund SIMP Funicular Rib Arch & Carbon-Compliance Saddle
      float ribArch = (0.44 + 0.24 * aNorm) * (1.0 - 0.58 * xz.x * xz.x) * exp(-2.5 * xz.y * xz.y);
      float diagRibs = 0.16 * exp(-14.0 * pow(abs(xz.x) - abs(xz.y), 2.0));
      float voidPockets = -0.26 * (1.0 - aNorm) * cos(5.5 * xz.x) * cos(5.5 * xz.y);
      return -0.14 + ribArch + diagRibs + voidPockets + 0.10 * bNorm;
    } else if (u_folio < 3.5) {
      // B.04: Maxwell 3D Airy Stress Dome & 8-13 um Radiative Sky-Cooling Well
      float airyDome = (0.46 + 0.28 * aNorm) * (1.0 - 0.54 * r2);
      float lwirWell = -0.38 * bNorm * exp(-10.0 * r2);
      float polyFacets = 0.08 * cos(8.0 * xz.x) * cos(8.0 * xz.y);
      return -0.10 + airyDome + lwirWell + polyFacets;
    } else if (u_folio < 4.5) {
      // B.05: Viscous Burgers Shock Wavefront & PySR Pareto MDL Cliff
      float shockStep = -0.38 * tanh(4.5 * (xz.x - 0.22 * sin(2.5 * xz.y + u_time)));
      float paretoCliff = 0.26 * exp(-8.0 * pow(xz.y + 0.35, 2.0)) * (0.5 + 0.5 * bNorm);
      float noiseRipples = 0.18 * aNorm * sin(12.0 * xz.x + u_time * 2.0) * cos(12.0 * xz.y);
      return 0.04 + shockStep + paretoCliff + noiseRipples;
    } else {
      // B.06: PhysLean Chiral Hypercharge Balance Saddle & Calabrese-Cardy Entanglement Cone
      float chiralSaddle = 0.32 * (xz.x * xz.x - xz.y * xz.y) * (1.0 + 0.5 * bNorm);
      float cftCone = 0.38 * log(1.0 + 3.5 * r) * (0.4 + 0.6 * aNorm) - 0.24;
      return chiralSaddle + cftCone + breath * 0.4;
    }
  }
}

// Central-difference 3D surface normal for y = potentialSurface(x, z)
vec3 computeSurfaceNormal(vec2 xz) {
  float eps = 0.006;
  float dydx = (potentialSurface(xz + vec2(eps, 0.0)) - potentialSurface(xz - vec2(eps, 0.0))) / (2.0 * eps);
  float dydz = (potentialSurface(xz + vec2(0.0, eps)) - potentialSurface(xz - vec2(0.0, eps))) / (2.0 * eps);
  return normalize(vec3(-dydx, 1.0, -dydz));
}

// Ray-AABB intersection for bounding box [boxMin, boxMax]
vec2 intersectBox(vec3 ro, vec3 rd, vec3 boxMin, vec3 boxMax) {
  vec3 invRd = 1.0 / (rd + vec3(1e-6));
  vec3 t0 = (boxMin - ro) * invRd;
  vec3 t1 = (boxMax - ro) * invRd;
  vec3 tSmaller = min(t0, t1);
  vec3 tBigger = max(t0, t1);
  float tNear = max(max(tSmaller.x, tSmaller.y), tSmaller.z);
  float tFar = min(min(tBigger.x, tBigger.y), tBigger.z);
  return vec2(tNear, tFar);
}

void main() {
  vec2 coord = (gl_FragCoord.xy - 0.5 * u_resolution) / min(u_resolution.x, u_resolution.y);
  vec3 bgStone = mix(vec3(0.93, 0.94, 0.95), vec3(0.043, 0.055, 0.078), u_theme);

  // Folio-differentiated mineral palettes so articles within a pillar have distinct chromatic signatures
  float fShift = fract(u_folio * 0.23 + u_pillar * 0.17);
  vec3 colLowL = mix(vec3(0.09, 0.24, 0.39), vec3(0.16, 0.19, 0.36), smoothstep(0.0, 1.0, sin(u_folio * 1.3) * 0.5 + 0.5));
  vec3 colMidL = mix(vec3(0.11, 0.46, 0.37), vec3(0.14, 0.42, 0.52), fShift);
  vec3 colHighL = mix(vec3(0.80, 0.25, 0.17), vec3(0.76, 0.46, 0.12), fract(u_folio * 0.37));

  vec3 colVerdigris = mix(colMidL, vec3(0.34, 0.90, 0.75), u_theme);
  vec3 colMinium = mix(colHighL, vec3(1.0, 0.54, 0.38), u_theme);
  vec3 colPrussian = mix(colLowL, vec3(0.50, 0.78, 1.0), u_theme);
  vec3 colGold = mix(vec3(0.76, 0.53, 0.12), vec3(0.98, 0.82, 0.36), u_theme);

  // Lens Mode 1: 2D Symplectic Phase-Space Vector Field, Iso-Potential Contours & Advected Streamlines
  if (u_mode > 0.5) {
    vec2 p = coord * 1.55;
    float pot = potentialSurface(p);
    vec3 n = computeSurfaceNormal(p);
    vec2 grad = vec2(-n.x, -n.z);
    vec2 vel = vec2(grad.y, -grad.x) * 0.68 + grad * 0.32;

    float contour = abs(fract(pot * (5.0 + 0.4 * u_folio)) - 0.5);
    float contourLine = smoothstep(0.055, 0.0, contour);

    float streamPhase = fract(dot(p, normalize(vel + vec2(0.001))) * 5.0 - u_time * 0.95);
    float streamPulse = smoothstep(0.20, 0.0, abs(streamPhase - 0.5));

    vec2 cell = fract(p * (5.5 + 0.35 * u_folio)) - 0.5;
    float dotCore = smoothstep(0.13, 0.04, length(cell));

    vec2 eqPos = vec2(0.45 * cos(u_time * 0.9 + u_folio), 0.35 * sin(u_time * 1.2 + u_pillar));
    float eqGlow = smoothstep(0.14, 0.02, length(p - eqPos));

    vec3 baseCol = mix(bgStone, colPrussian, 0.12);
    vec3 fieldCol = mix(colMinium, colVerdigris, clamp(pot * 0.65 + 0.5, 0.0, 1.0));
    vec3 outCol = mix(baseCol, fieldCol, 0.32 + 0.38 * streamPulse);
    outCol = mix(outCol, colPrussian, contourLine * 0.55);
    outCol = mix(outCol, colVerdigris, dotCore * 0.65);
    outCol = mix(outCol, colGold, eqGlow * 0.92);
    fragColor = vec4(outCol, 1.0);
    return;
  }

  // Lens Mode 0: True Y-Up 3D Turntable Spherical Camera + Solid Slab Raymarcher
  float pitch = clamp(u_rotation.x, 0.26, 1.28);
  float yaw = u_rotation.y;
  float camDist = clamp(u_zoom, 2.15, 4.40);

  vec3 target = vec3(0.0, -0.06, 0.0);
  vec3 ro = vec3(
    camDist * cos(pitch) * sin(yaw),
    camDist * sin(pitch),
    camDist * cos(pitch) * cos(yaw)
  );
  vec3 fwd = normalize(target - ro);
  vec3 right = normalize(cross(fwd, vec3(0.0, 1.0, 0.0)));
  vec3 up = cross(right, fwd);
  vec3 rd = normalize(fwd * 1.72 + right * coord.x + up * coord.y);

  float vign = length(coord);
  vec3 color = bgStone * (1.02 - vign * 0.14);

  // Intersect floor reference grid at y = -0.52
  float baseY = -0.52;
  if (rd.y < -0.001) {
    float tFloor = (baseY - ro.y) / rd.y;
    if (tFloor > 0.0) {
      vec3 pFloor = ro + rd * tFloor;
      if (max(abs(pFloor.x), abs(pFloor.z)) < 1.48) {
        vec2 fGrid = abs(fract(pFloor.xz * 3.5) - 0.5);
        float fLine = smoothstep(0.045, 0.0, min(fGrid.x, fGrid.y));
        float edgeFade = 1.0 - smoothstep(1.12, 1.48, max(abs(pFloor.x), abs(pFloor.z)));
        color = mix(color, colPrussian, fLine * 0.22 * edgeFade);
      }
    }
  }

  // Intersect 3D Slab Domain [-1.14, 1.14] x [-0.52, 0.95] x [-1.14, 1.14]
  vec3 boxMin = vec3(-1.14, baseY, -1.14);
  vec3 boxMax = vec3(1.14, 0.95, 1.14);
  vec2 tBox = intersectBox(ro, rd, boxMin, boxMax);

  if (tBox.x < tBox.y && tBox.y > 0.0) {
    float tStart = max(tBox.x, 0.05);
    float tEnd = tBox.y;
    int steps = 60;
    float dt = (tEnd - tStart) / float(steps);

    float tPrev = tStart;
    bool hit = false;
    bool hitSideWall = false;
    float tHit = tStart;

    for (int i = 0; i <= 60; i++) {
      float tCurr = tStart + float(i) * dt;
      vec3 p = ro + rd * tCurr;
      float h = clamp(potentialSurface(p.xz), baseY + 0.04, 0.90);
      if (p.y <= h && p.y >= baseY - 0.02) {
        hit = true;
        if (i == 0) {
          hitSideWall = true;
          tHit = tCurr;
        } else {
          // 5-step binary bisection for razor-sharp surface intersection
          float tA = tPrev;
          float tB = tCurr;
          for (int b = 0; b < 5; b++) {
            float tMid = 0.5 * (tA + tB);
            vec3 pMid = ro + rd * tMid;
            float hMid = clamp(potentialSurface(pMid.xz), baseY + 0.04, 0.90);
            if (pMid.y <= hMid) {
              tB = tMid;
            } else {
              tA = tMid;
            }
          }
          tHit = 0.5 * (tA + tB);
        }
        break;
      }
      tPrev = tCurr;
    }

    if (hit) {
      vec3 pHit = ro + rd * tHit;
      vec3 lightDir = normalize(vec3(0.55, 0.85, 0.45));
      vec3 viewDir = -rd;

      if (hitSideWall) {
        vec3 boxN = vec3(0.0);
        if (abs(pHit.x - boxMin.x) < 0.025) boxN = vec3(-1.0, 0.0, 0.0);
        else if (abs(pHit.x - boxMax.x) < 0.025) boxN = vec3(1.0, 0.0, 0.0);
        else if (abs(pHit.z - boxMin.z) < 0.025) boxN = vec3(0.0, 0.0, -1.0);
        else boxN = vec3(0.0, 0.0, 1.0);

        float sideDiff = 0.45 + 0.45 * max(dot(boxN, lightDir), 0.0);
        float strata = smoothstep(0.06, 0.0, abs(fract((pHit.y - baseY) * 7.0) - 0.5));
        vec3 sideCol = mix(bgStone * 0.78, colPrussian, 0.28 + 0.25 * strata) * sideDiff;
        color = sideCol;
      } else {
        vec3 normal = computeSurfaceNormal(pHit.xz);
        if (dot(normal, viewDir) < 0.0) normal = -normal;

        float diff = max(dot(normal, lightDir), 0.0);
        vec3 halfVec = normalize(lightDir + viewDir);
        float spec = pow(max(dot(normal, halfVec), 0.0), 28.0);
        float fresnel = pow(1.0 - max(dot(normal, viewDir), 0.0), 3.0);

        float hNorm = clamp((pHit.y - baseY) / 1.05, 0.0, 1.0);
        vec3 surfTint = mix(colPrussian, colVerdigris, smoothstep(0.15, 0.65, hNorm));
        surfTint = mix(surfTint, colMinium, smoothstep(0.62, 0.95, hNorm));

        float contour = abs(fract(pHit.y * (5.8 + 0.35 * u_folio)) - 0.5);
        float contourLine = smoothstep(0.045, 0.0, contour);

        float gridScale = 3.8 + 0.45 * mod(u_folio + u_pillar, 4.0);
        vec2 meshGrid = abs(fract(pHit.xz * gridScale) - 0.5);
        float wireLine = smoothstep(0.042, 0.0, min(meshGrid.x, meshGrid.y));

        vec2 orbXZ = vec2(0.52 * cos(u_time * 1.05 + u_folio), 0.52 * sin(u_time * 0.85 + u_pillar));
        float dOrb = length(pHit.xz - orbXZ);
        float orbRing = smoothstep(0.18, 0.13, dOrb) - smoothstep(0.11, 0.06, dOrb);
        float orbCore = smoothstep(0.075, 0.015, dOrb);

        vec3 baseShade = surfTint * (0.34 + 0.68 * diff) + vec3(spec * 0.28) + colVerdigris * (fresnel * 0.22);
        baseShade = mix(baseShade, mix(vec3(0.98), vec3(0.75, 0.92, 1.0), u_theme), contourLine * 0.35);
        baseShade = mix(baseShade, colPrussian, wireLine * 0.28);
        baseShade = mix(baseShade, colGold, clamp(orbRing * 0.75 + orbCore, 0.0, 1.0));

        color = baseShade;
      }
    }
  }

  fragColor = vec4(color, 1.0);
}
`;

function createShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    const info = gl.getShaderInfoLog(shader);
    gl.deleteShader(shader);
    console.warn("[webgl-observatory] Shader compile error:", info);
    return null;
  }
  return shader;
}

function createProgram(gl, vsSrc, fsSrc) {
  const vs = createShader(gl, gl.VERTEX_SHADER, vsSrc);
  const fs = createShader(gl, gl.FRAGMENT_SHADER, fsSrc);
  if (!vs || !fs) return null;
  const program = gl.createProgram();
  gl.attachShader(program, vs);
  gl.attachShader(program, fs);
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    const info = gl.getProgramInfoLog(program);
    gl.deleteProgram(program);
    console.warn("[webgl-observatory] Program link error:", info);
    return null;
  }
  return program;
}

const SVG_NS = "http://www.w3.org/2000/svg";

function svgEl(tag, attrs = {}, text = "") {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    el.setAttribute(k, String(v));
  }
  if (text) el.textContent = text;
  return el;
}

const PILLAR_STAGE_LABELS = {
  engineering: ["1. Surcharge / Head", "2. Pore / Yield Stress", "3. Shear Mobilization", "4. Resilient Pass"],
  architecture: ["1. Applied Load q(x)", "2. Exoskeleton / Thrust", "3. Kern / Gerberette", "4. Adaptable Bay"],
  physics: ["1. ATP Affinity Drive", "2. Allosteric Bridge", "3. Open Conductance", "4. Airway Hydration"],
  math: ["1. Human Conjecture", "2. Galois / Sieve Map", "3. Taylor-Wiles Bridge", "4. Verified QED"],
  cf: ["1. Genetic / Mucus Defect", "2. Allosteric / LNP Delivery", "3. Channel / Editing Rescue", "4. Clinical Clearance"],
  bounties: ["1. Problem / Operator", "2. 4-Stage Proof Spine", "3. Invariant Gate R1-R3", "4. T0/T1 Certified Pass"],
};

const PILLAR_RADAR_AXES = {
  engineering: ["Bearing FS", "Permeability κ", "Seismic Damping", "Ductility μ", "Serviceability", "Code Margin"],
  architecture: ["Funicular Kern", "Buckling λ_cr", "Daylight UDI", "Sabine STI", "Shearing Pods", "Tectonic Stiffness"],
  physics: ["ATP Coupling", "Open Prob P_o", "Kramers Rate", "Mucus Mesh ξ", "Ciliary Clearance", "Allosteric ΔΔG"],
  math: ["Axiom Purity", "Lemma Conservation", "Bridge Speedup", "Zero Simplicity", "Word-RAM Bound", "Human+AI Guard"],
  cf: ["Band C / Editing", "Open Prob P_o", "PCL Brush 7 μm", "Mucosal Slip", "NMD / Off-Target", "Registry Equity"],
  bounties: ["Invariant R1", "Invariant R2", "Invariant R3", "T0/T1 Fidelity", "Zero-Sorry Gate", "Benchmark Margin"],
};

function shortLabel(raw, maxLen = 22) {
  const cleaned = String(raw || "")
    .replace(/^\d+\s*\(/, "")
    .replace(/\)$/, "")
    .split("(")[0]
    .trim();
  return cleaned.length > maxLen ? `${cleaned.slice(0, maxLen - 1)}…` : cleaned;
}

function getFolioDynamicStages(plateRoot, pillarName) {
  if (plateRoot) {
    const btns = Array.from(plateRoot.querySelectorAll(".tp-step-btn"));
    if (btns.length >= 4) {
      return btns.slice(0, 4).map((b, i) => `${i + 1}. ${shortLabel(b.textContent, 19)}`);
    }
  }
  return PILLAR_STAGE_LABELS[pillarName] || PILLAR_STAGE_LABELS.engineering;
}

function getFolioDynamicRadarAxes(plateRoot, pillarName) {
  if (plateRoot) {
    const readouts = Array.from(plateRoot.querySelectorAll(".tp-readout-k")).map((el) => shortLabel(el.textContent, 18));
    const sliders = Array.from(plateRoot.querySelectorAll(".tp-control-group label span:first-child")).map((el) => shortLabel(el.textContent, 18));
    const combined = [...readouts.slice(0, 4), ...sliders.slice(0, 2)].filter(Boolean);
    if (combined.length === 6) return combined;
  }
  return PILLAR_RADAR_AXES[pillarName] || PILLAR_RADAR_AXES.engineering;
}

function getFolioReadoutSummary(plateRoot) {
  if (!plateRoot) return [];
  const boxes = Array.from(plateRoot.querySelectorAll(".tp-readout-box")).slice(0, 4);
  return boxes.map((box) => {
    const k = box.querySelector(".tp-readout-k")?.textContent?.trim() || "";
    const v = box.querySelector(".tp-readout-v")?.textContent?.trim() || "";
    return `${shortLabel(k, 16)}: ${shortLabel(v, 18)}`;
  });
}

function renderMultiLensSvg(svg, mode, pillarName, affinity, bias, plateRoot = null, folioSlug = "e01") {
  if (!svg) return;
  while (svg.firstChild) svg.removeChild(svg.firstChild);

  const aNorm = Math.max(0.08, Math.min(1.0, (affinity - 1.0) / 24.0));
  const bNorm = Math.max(0.08, Math.min(1.0, (bias + 60.0) / 100.0));
  const folioUpper = String(folioSlug || "e01").toUpperCase();

  svg.appendChild(svgEl("title", {}, mode === 2
    ? `Folio ${folioUpper} Noether-Kirchhoff 4-Stage Alluvial Conservation Ribbon`
    : `Folio ${folioUpper} 6-Axis Polar Structural & Biophysical Performance Radar`));

  if (mode === 2) {
    // Lens 3: Folio-Specific 4-Stage Noether-Kirchhoff Conservation Ribbon
    const stages = getFolioDynamicStages(plateRoot, pillarName);
    const xCoords = [82, 250, 422, 592];
    const ret1 = 1.0;
    const ret2 = Math.max(0.32, Math.min(0.96, 0.52 + 0.42 * aNorm));
    const ret3 = Math.max(0.24, Math.min(0.92, ret2 * (0.66 + 0.30 * bNorm)));
    const ret4 = Math.max(0.18, Math.min(0.90, ret3 * (0.72 + 0.24 * aNorm)));
    const retained = [ret1, ret2, ret3, ret4];
    const baseH = 112;
    const topY = 40;

    for (let i = 0; i < 3; i++) {
      const x0 = xCoords[i] + 18;
      const x1 = xCoords[i + 1] - 18;
      const cx = (x0 + x1) * 0.5;
      const h0 = retained[i] * baseH;
      const h1 = retained[i + 1] * baseH;
      const y0Bot = topY + h0;
      const y1Bot = topY + h1;

      const dMain = `M ${x0} ${topY} C ${cx} ${topY}, ${cx} ${topY}, ${x1} ${topY} L ${x1} ${y1Bot.toFixed(1)} C ${cx} ${y1Bot.toFixed(1)}, ${cx} ${y0Bot.toFixed(1)}, ${x0} ${y0Bot.toFixed(1)} Z`;
      svg.appendChild(svgEl("path", {
        d: dMain,
        fill: "var(--tp-verdigris)",
        "fill-opacity": "0.30",
        stroke: "var(--tp-verdigris)",
        "stroke-width": "1.6",
      }));

      const yMid0 = topY + h0 * 0.5;
      const yMid1 = topY + h1 * 0.5;
      svg.appendChild(svgEl("path", {
        d: `M ${x0} ${yMid0.toFixed(1)} C ${cx} ${yMid0.toFixed(1)}, ${cx} ${yMid1.toFixed(1)}, ${x1} ${yMid1.toFixed(1)}`,
        fill: "none",
        stroke: "var(--tp-verdigris)",
        "stroke-width": "2.2",
        "stroke-dasharray": "6 6",
        class: "tp-svg-flow-line",
      }));

      const leakH = Math.max(4, h0 - h1);
      const leakStartTop = y1Bot;
      const leakStartBot = y0Bot;
      const leakEndTop = 168;
      const leakEndBot = Math.min(196, 168 + leakH + 6);
      const dLeak = `M ${x0} ${leakStartTop.toFixed(1)} C ${cx} ${leakStartTop.toFixed(1)}, ${cx} ${leakEndTop}, ${x1 - 8} ${leakEndTop} L ${x1 - 8} ${leakEndBot.toFixed(1)} C ${cx} ${leakEndBot.toFixed(1)}, ${cx} ${leakStartBot.toFixed(1)}, ${x0} ${leakStartBot.toFixed(1)} Z`;
      svg.appendChild(svgEl("path", {
        d: dLeak,
        fill: "var(--tp-minium)",
        "fill-opacity": "0.22",
        stroke: "var(--tp-minium)",
        "stroke-width": "1.1",
        "stroke-dasharray": "3,2",
      }));
    }

    xCoords.forEach((x, idx) => {
      const h = retained[idx] * baseH;
      svg.appendChild(svgEl("rect", {
        x: x - 16,
        y: topY,
        width: 32,
        height: h.toFixed(1),
        fill: idx === 3 ? "var(--tp-verdigris)" : "var(--tp-prussian)",
        rx: "2",
      }));
      svg.appendChild(svgEl("text", {
        x,
        y: 24,
        "text-anchor": "middle",
        "font-size": "10",
        "font-weight": "700",
        fill: "currentColor",
      }, stages[idx]));
      svg.appendChild(svgEl("text", {
        x,
        y: topY + h + 15,
        "text-anchor": "middle",
        "font-size": "10",
        fill: "var(--tp-prussian)",
      }, `${(retained[idx] * 100).toFixed(1)}% flux`));
    });

    svg.appendChild(svgEl("text", {
      x: 340,
      y: 210,
      "text-anchor": "middle",
      "font-size": "10.5",
      fill: "currentColor",
    }, `Folio ${folioUpper} Conservation: J_in (100%) = J_transmitted (${(ret4 * 100).toFixed(1)}%) + Σ D_dissipated (${((1 - ret4) * 100).toFixed(1)}%)`));
  } else {
    // Lens 4: Folio-Specific 6-Axis Polar Structural & Biophysical Envelope Radar
    const axes = getFolioDynamicRadarAxes(plateRoot, pillarName);
    const liveReadouts = getFolioReadoutSummary(plateRoot);
    const cx = 220;
    const cy = 114;
    const maxR = 76;

    [0.35, 0.68, 1.0].forEach((frac, rIdx) => {
      const pts = [];
      for (let i = 0; i < 6; i++) {
        const ang = -Math.PI / 2 + (i * Math.PI) / 3;
        pts.push(`${(cx + Math.cos(ang) * maxR * frac).toFixed(1)},${(cy + Math.sin(ang) * maxR * frac).toFixed(1)}`);
      }
      svg.appendChild(svgEl("polygon", {
        points: pts.join(" "),
        fill: "none",
        stroke: rIdx === 1 ? "var(--tp-minium)" : "currentColor",
        "stroke-opacity": rIdx === 1 ? "0.55" : "0.22",
        "stroke-dasharray": rIdx === 1 ? "4,3" : "none",
        "stroke-width": rIdx === 1 ? "1.4" : "1",
      }));
    });

    const seed = (parseInt(folioSlug.replace(/\D+/g, ""), 10) || 1) * 0.04;
    const ratios = [
      Math.min(0.98, 0.42 + 0.52 * aNorm + seed * 0.3),
      Math.min(0.98, 0.38 + 0.54 * bNorm),
      Math.min(0.98, 0.46 + 0.46 * (0.65 * aNorm + 0.35 * bNorm)),
      Math.min(0.98, 0.36 + 0.56 * (0.35 * aNorm + 0.65 * bNorm)),
      Math.min(0.98, 0.48 + 0.46 * aNorm),
      Math.min(0.98, 0.40 + 0.52 * Math.sqrt(aNorm * bNorm)),
    ];

    const polyPts = [];
    const vertexCoords = [];
    for (let i = 0; i < 6; i++) {
      const ang = -Math.PI / 2 + (i * Math.PI) / 3;
      const xEdge = cx + Math.cos(ang) * maxR;
      const yEdge = cy + Math.sin(ang) * maxR;
      svg.appendChild(svgEl("line", {
        x1: cx,
        y1: cy,
        x2: xEdge.toFixed(1),
        y2: yEdge.toFixed(1),
        stroke: "currentColor",
        "stroke-opacity": "0.25",
      }));

      const lx = cx + Math.cos(ang) * (maxR + 20);
      const ly = cy + Math.sin(ang) * (maxR + 13) + 3;
      svg.appendChild(svgEl("text", {
        x: lx.toFixed(1),
        y: ly.toFixed(1),
        "text-anchor": Math.abs(Math.cos(ang)) < 0.2 ? "middle" : (Math.cos(ang) > 0 ? "start" : "end"),
        "font-size": "9.5",
        "font-weight": "600",
        fill: "currentColor",
      }, axes[i]));

      const rVal = Math.min(1.0, Math.max(0.22, ratios[i]));
      const vx = cx + Math.cos(ang) * maxR * rVal;
      const vy = cy + Math.sin(ang) * maxR * rVal;
      polyPts.push(`${vx.toFixed(1)},${vy.toFixed(1)}`);
      vertexCoords.push([vx, vy]);
    }

    svg.appendChild(svgEl("polygon", {
      points: polyPts.join(" "),
      fill: "var(--tp-verdigris)",
      "fill-opacity": "0.28",
      stroke: "var(--tp-verdigris)",
      "stroke-width": "2.2",
      class: "tp-svg-morph-target",
    }));

    vertexCoords.forEach(([vx, vy]) => {
      svg.appendChild(svgEl("circle", {
        cx: vx.toFixed(1),
        cy: vy.toFixed(1),
        r: "3.5",
        fill: "var(--tp-prussian)",
      }));
    });

    const avgScore = (ratios.reduce((a, b) => a + b, 0) / ratios.length) * 100;
    svg.appendChild(svgEl("text", {
      x: 410,
      y: 44,
      "font-size": "11",
      "font-weight": "700",
      fill: "var(--tp-prussian)",
    }, `FOLIO ${folioUpper} · 6-AXIS ENVELOPE`));
    svg.appendChild(svgEl("text", {
      x: 410,
      y: 64,
      "font-size": "10",
      fill: "currentColor",
    }, `Composite Score: ${avgScore.toFixed(1)}% vs Benchmark (68%)`));
    axes.forEach((ax, i) => {
      const roLine = liveReadouts[i] ? `${liveReadouts[i]} (${(ratios[i] * 100).toFixed(0)}%)` : `${ax}: ${(ratios[i] * 100).toFixed(0)}%`;
      svg.appendChild(svgEl("text", {
        x: 410,
        y: 88 + i * 18,
        "font-size": "9.8",
        fill: "currentColor",
      }, `· ${roLine}`));
    });
  }
}

export function initPlateWebGL(scope = document) {
  const canvases = scope.querySelectorAll(".tp-webgl-canvas");
  canvases.forEach((canvas) => {
    if (canvas.dataset.webglBound === "true") return;
    canvas.dataset.webglBound = "true";

    const wrap = canvas.closest(".tp-webgl-wrap");
    const plateRoot = canvas.closest(".tp-plate") || scope;
    const lensSvg = wrap ? wrap.querySelector(".tp-lens-svg") : null;
    const lensBtns = wrap ? wrap.querySelectorAll(".tp-lens-btn[data-lens-mode]") : [];
    const pillarAttr = (canvas.getAttribute("data-pillar-webgl") || "engineering").toLowerCase();
    const folioAttr = (canvas.getAttribute("data-folio-webgl") || "e01").toLowerCase();
    const folioNum = Math.max(0, Math.min(9, (parseInt(folioAttr.replace(/\D+/g, ""), 10) || 1) - 1));
    const pillarIndex = pillarAttr === "engineering" ? 0.0
      : pillarAttr === "architecture" ? 1.0
      : pillarAttr === "physics" ? 2.0
      : pillarAttr === "math" ? 3.0
      : pillarAttr === "bounties" ? 5.0
      : 4.0;
    const sliderScope = canvas.closest("#tp-folio-mount") || plateRoot;

    let currentMode = 0; // 0 = 3D Turntable Slab, 1 = Phase Portraits, 2 = Kirchhoff Alluvial, 3 = Polar Radar
    const prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let isSpinPaused = prefersReducedMotion;

    // Folio-differentiated default camera pitch/yaw so each article opens at a tailored 3D perspective
    const DEFAULT_PITCH = 0.52 + (folioNum % 3) * 0.08;
    const DEFAULT_YAW = -0.62 + folioNum * 0.22;
    const DEFAULT_ZOOM = 3.02;
    let rotX = DEFAULT_PITCH;
    let rotY = DEFAULT_YAW;
    let camZoom = DEFAULT_ZOOM;

    const lensBar = wrap ? wrap.querySelector(".tp-lens-bar") : null;
    if (lensBar && !lensBar.querySelector("[data-webgl-spin-toggle]")) {
      const spinBtn = document.createElement("button");
      spinBtn.type = "button";
      spinBtn.className = "tp-lens-btn tp-lens-btn-util";
      spinBtn.setAttribute("data-webgl-spin-toggle", "true");
      spinBtn.setAttribute("aria-pressed", isSpinPaused ? "false" : "true");
      spinBtn.textContent = isSpinPaused ? "▶ Orbit 3D" : "⏸ Pause 3D";
      spinBtn.addEventListener("click", () => {
        isSpinPaused = !isSpinPaused;
        spinBtn.setAttribute("aria-pressed", isSpinPaused ? "false" : "true");
        spinBtn.textContent = isSpinPaused ? "▶ Orbit 3D" : "⏸ Pause 3D";
      });

      const resetBtn = document.createElement("button");
      resetBtn.type = "button";
      resetBtn.className = "tp-lens-btn tp-lens-btn-util";
      resetBtn.setAttribute("data-webgl-reset", "true");
      resetBtn.textContent = "↺ Reset 3D";
      resetBtn.addEventListener("click", () => {
        rotX = DEFAULT_PITCH;
        rotY = DEFAULT_YAW;
        camZoom = DEFAULT_ZOOM;
      });

      lensBar.appendChild(spinBtn);
      lensBar.appendChild(resetBtn);
    }

    function getNormalizedSlider(idx, fallbackVal) {
      const sliders = sliderScope.querySelectorAll('input[type="range"]');
      const sl = sliders[idx];
      if (!sl) return fallbackVal;
      const min = parseFloat(sl.min);
      const max = parseFloat(sl.max);
      const val = parseFloat(sl.value);
      if (Number.isFinite(min) && Number.isFinite(max) && max > min && Number.isFinite(val)) {
        return (val - min) / (max - min);
      }
      return fallbackVal;
    }

    function getAffinity() {
      const n0 = getNormalizedSlider(0, 0.72);
      return 1.0 + n0 * 24.0;
    }

    function getBias() {
      const n1 = getNormalizedSlider(1, 0.65);
      return -60.0 + n1 * 100.0;
    }

    function refreshSvgLensIfActive() {
      if (currentMode >= 2 && lensSvg) {
        renderMultiLensSvg(lensSvg, currentMode, pillarAttr, getAffinity(), getBias(), sliderScope, folioAttr);
      }
    }

    lensBtns.forEach((btn) => {
      if (btn.dataset.bound === "true") return;
      btn.dataset.bound = "true";
      btn.addEventListener("click", () => {
        currentMode = parseInt(btn.getAttribute("data-lens-mode") || "0", 10) || 0;
        lensBtns.forEach((b) => b.setAttribute("aria-pressed", b === btn ? "true" : "false"));
        if (currentMode <= 1) {
          canvas.hidden = false;
          canvas.removeAttribute("hidden");
          canvas.style.display = "block";
          if (lensSvg) {
            lensSvg.hidden = true;
            lensSvg.setAttribute("hidden", "");
            lensSvg.style.display = "none";
          }
        } else {
          canvas.hidden = true;
          canvas.setAttribute("hidden", "");
          canvas.style.display = "none";
          if (lensSvg) {
            lensSvg.hidden = false;
            lensSvg.removeAttribute("hidden");
            lensSvg.style.display = "block";
            renderMultiLensSvg(lensSvg, currentMode, pillarAttr, getAffinity(), getBias(), sliderScope, folioAttr);
            if (!prefersReducedMotion && lensSvg.animate) {
              lensSvg.animate(
                [{ opacity: 0.35, transform: "scale(0.985)" }, { opacity: 1, transform: "scale(1)" }],
                { duration: 240, easing: "cubic-bezier(0.22, 1, 0.36, 1)" }
              );
            }
          }
        }
      });
    });

    sliderScope.querySelectorAll('input[type="range"]').forEach((slider) => {
      slider.addEventListener("input", refreshSvgLensIfActive);
    });

    let gl = canvas.getContext("webgl2", { antialias: true, alpha: false });
    if (!gl) {
      console.warn("[webgl-observatory] WebGL2 not supported, falling back to SVG lens.");
      if (lensSvg) {
        canvas.hidden = true;
        lensSvg.hidden = false;
        currentMode = 2;
        renderMultiLensSvg(lensSvg, 2, pillarAttr, getAffinity(), getBias(), plateRoot, folioAttr);
      }
      return;
    }

    let program = createProgram(gl, VERTEX_SHADER_SRC, FRAGMENT_SHADER_SRC);
    if (!program) return;

    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      new Float32Array([
        -1.0, -1.0,
         1.0, -1.0,
        -1.0,  1.0,
        -1.0,  1.0,
         1.0, -1.0,
         1.0,  1.0,
      ]),
      gl.STATIC_DRAW
    );

    let aPosLoc = gl.getAttribLocation(program, "a_position");
    let uResLoc = gl.getUniformLocation(program, "u_resolution");
    let uTimeLoc = gl.getUniformLocation(program, "u_time");
    let uRotLoc = gl.getUniformLocation(program, "u_rotation");
    let uAffLoc = gl.getUniformLocation(program, "u_affinity");
    let uBiasLoc = gl.getUniformLocation(program, "u_bias");
    let uThemeLoc = gl.getUniformLocation(program, "u_theme");
    let uPillarLoc = gl.getUniformLocation(program, "u_pillar");
    let uFolioLoc = gl.getUniformLocation(program, "u_folio");
    let uModeLoc = gl.getUniformLocation(program, "u_mode");
    let uZoomLoc = gl.getUniformLocation(program, "u_zoom");

    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let isIntersecting = true;
    let animId = null;
    let lastNow = performance.now();
    let simTimeSec = 0.0;

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2.0);
      const displayWidth = Math.round((canvas.clientWidth || 680) * dpr);
      const displayHeight = Math.round((canvas.clientHeight || 280) * dpr);
      if (canvas.width !== displayWidth || canvas.height !== displayHeight) {
        canvas.width = displayWidth;
        canvas.height = displayHeight;
        gl.viewport(0, 0, canvas.width, canvas.height);
      }
    }

    canvas.addEventListener("pointerdown", (e) => {
      isDragging = true;
      startX = e.clientX;
      startY = e.clientY;
      canvas.setPointerCapture(e.pointerId);
    });

    canvas.addEventListener("pointermove", (e) => {
      if (!isDragging) return;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      startX = e.clientX;
      startY = e.clientY;
      rotY -= dx * 0.009;
      rotX = Math.max(0.26, Math.min(1.28, rotX + dy * 0.008));
    });

    canvas.addEventListener("pointerup", (e) => {
      isDragging = false;
      try { canvas.releasePointerCapture(e.pointerId); } catch (_) {}
    });

    canvas.addEventListener("pointercancel", () => {
      isDragging = false;
    });

    if (!canvas.hasAttribute("tabindex")) {
      canvas.setAttribute("tabindex", "0");
    }
    canvas.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        rotY -= 0.12;
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        rotY += 0.12;
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        rotX = Math.max(0.26, Math.min(1.28, rotX - 0.08));
      } else if (e.key === "ArrowDown") {
        e.preventDefault();
        rotX = Math.max(0.26, Math.min(1.28, rotX + 0.08));
      } else if (e.key === "+" || e.key === "=") {
        e.preventDefault();
        camZoom = Math.max(2.15, camZoom - 0.18);
      } else if (e.key === "-" || e.key === "_") {
        e.preventDefault();
        camZoom = Math.min(4.40, camZoom + 0.18);
      }
    });

    function getTheme() {
      const root = document.documentElement;
      return (root.getAttribute("data-theme") === "blueprint" || root.getAttribute("data-theme") === "dark") ? 1.0 : 0.0;
    }

    function render(now) {
      if (!isIntersecting) {
        animId = null;
        return;
      }
      const dt = Math.min(0.05, Math.max(0.0, (now - lastNow) * 0.001));
      lastNow = now;
      if (!isSpinPaused && !isDragging) {
        simTimeSec += dt;
        rotY += dt * 0.22;
      } else if (!prefersReducedMotion) {
        simTimeSec += dt * 0.35;
      }

      if (currentMode <= 1) {
        resize();
        gl.useProgram(program);

        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
        gl.enableVertexAttribArray(aPosLoc);
        gl.vertexAttribPointer(aPosLoc, 2, gl.FLOAT, false, 0, 0);

        gl.uniform2f(uResLoc, canvas.width, canvas.height);
        gl.uniform1f(uTimeLoc, simTimeSec);
        gl.uniform2f(uRotLoc, rotX, rotY);
        gl.uniform1f(uAffLoc, getAffinity());
        gl.uniform1f(uBiasLoc, getBias());
        gl.uniform1f(uThemeLoc, getTheme());
        if (uPillarLoc !== null) gl.uniform1f(uPillarLoc, pillarIndex);
        if (uFolioLoc !== null) gl.uniform1f(uFolioLoc, folioNum);
        if (uModeLoc !== null) gl.uniform1f(uModeLoc, currentMode === 1 ? 1.0 : 0.0);
        if (uZoomLoc !== null) gl.uniform1f(uZoomLoc, camZoom);

        gl.drawArrays(gl.TRIANGLES, 0, 6);
      }

      animId = requestAnimationFrame(render);
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        isIntersecting = entry.isIntersecting;
        if (isIntersecting && !animId) {
          lastNow = performance.now();
          animId = requestAnimationFrame(render);
        }
      });
    }, { threshold: 0.05 });
    observer.observe(canvas);

    canvas.addEventListener("webglcontextlost", (e) => {
      e.preventDefault();
      if (animId) cancelAnimationFrame(animId);
      animId = null;
    });

    canvas.addEventListener("webglcontextrestored", () => {
      program = createProgram(gl, VERTEX_SHADER_SRC, FRAGMENT_SHADER_SRC);
      if (!program) return;
      aPosLoc = gl.getAttribLocation(program, "a_position");
      uResLoc = gl.getUniformLocation(program, "u_resolution");
      uTimeLoc = gl.getUniformLocation(program, "u_time");
      uRotLoc = gl.getUniformLocation(program, "u_rotation");
      uAffLoc = gl.getUniformLocation(program, "u_affinity");
      uBiasLoc = gl.getUniformLocation(program, "u_bias");
      uThemeLoc = gl.getUniformLocation(program, "u_theme");
      uPillarLoc = gl.getUniformLocation(program, "u_pillar");
      uFolioLoc = gl.getUniformLocation(program, "u_folio");
      uModeLoc = gl.getUniformLocation(program, "u_mode");
      uZoomLoc = gl.getUniformLocation(program, "u_zoom");
      if (isIntersecting) {
        lastNow = performance.now();
        animId = requestAnimationFrame(render);
      }
    });

    animId = requestAnimationFrame(render);
  });
}
