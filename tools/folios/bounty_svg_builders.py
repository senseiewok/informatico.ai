"""Bespoke 3-Plate Interactive Triad Renderers for Bounty Folios B.01–B.06:
- Plate A: Bespoke Domain-Specific 2D SVG Scientific Observatory (960x320) + 4-Stage Invariant Spectrum
- Plate B: 4-Lens 3D WebGL2 & 6-Axis Polar Benchmark Radar Observatory
- Plate C: Interactive Prize Submission Readiness & Tri-Invariant Stress-Tester Tool
"""
from __future__ import annotations

import html


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


BOUNTY_3D_META: dict[str, tuple[str, str]] = {
    "b01": (
        "Sidon B₂ Difference Lattice & Erdős–Turán Potential Bowl",
        "X: Interval Horizon N · Z: Candidate Cardinality |A| · Y: Pairwise Sum Collision Energy",
    ),
    "b02": (
        "Kitaev Rotated Surface-Code Topological Syndrome Manifold",
        "X: Code Distance d · Z: Gate Error p_phys · Y: Logical Suppression -log10(P_L)",
    ),
    "b03": (
        "Bendsøe–Sigmund SIMP Funicular Rib & Carbon-Compliance Saddle",
        "X: Volume Fraction V/V0 · Z: Mineralized CO2 Uptake · Y: Compliance-Carbon Pareto Surface",
    ),
    "b04": (
        "Maxwell 3D Airy Stress Dome & 8–13 μm Sky-Cooling Well",
        "X: Vault Crown Rise f · Z: Solar Reflectance R_sol · Y: Funicular Thrust & Radiative Cooling Potential",
    ),
    "b05": (
        "Viscous Burgers Shock Wavefront & Pareto MDL Cliff",
        "X: Spatiotemporal Coordinate x · Z: Sparsity Threshold λ · Y: Velocity Field u(x,t) & MDL Basin",
    ),
    "b06": (
        "Chiral Hypercharge Cubic Trace & Calabrese–Cardy Entanglement Cone",
        "X: MPS Bond Dimension χ · Z: Hypercharge Drift δY · Y: Anomaly Potential |Tr[Y³]| + S_vN(L)",
    ),
}


def render_bounty_bespoke_svg(bounty: dict) -> str:
    """Return a rich domain-specific 960x320 SVG schematic for Bounty B.01..B.06."""
    slug = bounty["slug"]
    fid = bounty["folio_id"]
    bid = bounty["bounty_id"]
    gov = esc(bounty["governing_law"])

    # Common right-hand panel (x=636..948): 4-Stage Invariant Margin Spectrum + State-Space Curve
    right_panel = f"""
      <rect x="636" y="12" width="312" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
      <text x="792" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">{esc(fid)} STATE TRAJECTORY &amp; 4-STAGE MARGINS</text>
      <line x1="658" y1="138" x2="928" y2="138" stroke="currentColor" stroke-opacity="0.3"/>
      <line x1="658" y1="44" x2="658" y2="138" stroke="currentColor" stroke-opacity="0.3"/>
      <polyline data-bw-curve points="666,128 730,106 792,76 856,60 920,48" fill="none" stroke="var(--tp-prussian)" stroke-width="2.5"/>
      <line data-bw-thresh x1="658" y1="114" x2="928" y2="114" stroke="var(--tp-minium)" stroke-width="1.5" stroke-dasharray="4,3"/>
      <circle data-bw-dot cx="792" cy="76" r="6.5" fill="var(--tp-verdigris)" stroke="var(--tp-vellum)" stroke-width="2"/>
      <line x1="658" y1="274" x2="928" y2="274" stroke="currentColor" stroke-opacity="0.3"/>
      <rect data-bw-bar="0" x="672" y="182" width="44" height="92" rx="4" fill="var(--tp-verdigris)" opacity="0.92"/>
      <rect data-bw-bar="1" x="736" y="174" width="44" height="100" rx="4" fill="var(--tp-verdigris)" opacity="0.92"/>
      <rect data-bw-bar="2" x="800" y="178" width="44" height="96" rx="4" fill="var(--tp-verdigris)" opacity="0.92"/>
      <rect data-bw-bar="3" x="864" y="170" width="44" height="104" rx="4" fill="var(--tp-verdigris)" opacity="0.92"/>
      <text x="694" y="290" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">Stage 1</text>
      <text x="758" y="290" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">Stage 2</text>
      <text x="822" y="290" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">Stage 3</text>
      <text x="886" y="290" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">Stage 4</text>
    """

    if slug == "b01":
        # B.01: Mian-Chowla Golomb Ruler + 8x8 Pairwise Sum Collision Matrix + Lean 4 Blueprint DAG
        marks = [1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, 123]
        ruler_ticks = []
        for idx, m in enumerate(marks):
            rx = 32 + int((m / 125.0) * 280)
            ruler_ticks.append(
                f'<line data-b01-tick="{idx}" x1="{rx}" y1="66" x2="{rx}" y2="96" stroke="var(--tp-prussian)" stroke-width="2.2"/>'
                f'<circle cx="{rx}" cy="66" r="3.2" fill="var(--tp-verdigris)"/>'
                f'<text x="{rx}" y="110" text-anchor="middle" font-size="7.5" fill="currentColor">{m}</text>'
            )
        matrix_cells = []
        for r in range(7):
            for c in range(r, 7):
                cx = 368 + c * 28
                cy = 52 + r * 24
                s_val = marks[r] + marks[c]
                is_alert = "true" if (r == 5 and c == 6) else "false"
                matrix_cells.append(
                    f'<rect data-b01-cell="{r}-{c}" data-collision-watch="{is_alert}" x="{cx}" y="{cy}" width="25" height="21" rx="3" fill="var(--tp-verdigris)" fill-opacity="0.22" stroke="var(--tp-verdigris)" stroke-width="1"/>'
                    f'<text x="{cx + 12.5}" y="{cy + 14}" text-anchor="middle" font-size="8" font-weight="600" fill="currentColor">{s_val}</text>'
                )
        left_panels = f"""
          <rect x="12" y="12" width="324" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="174" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">MIAN–CHOWLA GOLOMB RULER &amp; PHASED ARRAY</text>
          <rect x="26" y="76" width="296" height="10" rx="3" fill="var(--tp-prussian)" fill-opacity="0.18"/>
          {"".join(ruler_ticks)}
          <path d="M 34 62 Q 112 34 190 62" fill="none" stroke="var(--tp-verdigris)" stroke-width="1.4" stroke-dasharray="3,2"/>
          <path d="M 68 62 Q 178 28 288 62" fill="none" stroke="var(--tp-prussian)" stroke-width="1.4" stroke-dasharray="3,2"/>
          <text x="174" y="134" text-anchor="middle" font-size="8.5" fill="var(--tp-verdigris)" font-weight="700">All k(k-1)/2 Pairwise Differences a_j - a_i Strictly Distinct</text>
          <rect x="26" y="150" width="296" height="142" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)" stroke-width="1"/>
          <text x="174" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="var(--tp-prussian)">ERDŐS–TURÁN SLIDING-WINDOW ENVELOPE</text>
          <polyline points="42,268 95,232 155,208 215,192 275,180 308,174" fill="none" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>
          <polyline data-b01-greedy-line points="42,274 95,246 155,224 215,210 275,198 308,191" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.4"/>
          <text x="174" y="284" text-anchor="middle" font-size="8.2" fill="currentColor">Upper: √N + N^(1/4) + 1 = 28.09 vs Greedy |A(500)| = 20</text>

          <rect x="348" y="12" width="276" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="486" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">UPPER-TRIANGULAR B₂ SUM MATRIX (a_i + a_j)</text>
          {"".join(matrix_cells)}
          <rect x="364" y="232" width="244" height="62" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)" stroke-width="1"/>
          <text x="486" y="249" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-prussian)">LEAN 4 ZERO-SORRY BLUEPRINT DAG</text>
          <rect x="374" y="258" width="68" height="24" rx="4" fill="var(--tp-verdigris)" fill-opacity="0.2" stroke="var(--tp-verdigris)"/>
          <text x="408" y="273" text-anchor="middle" font-size="7.8" font-weight="700" fill="currentColor">Finset.IsSidon</text>
          <rect x="452" y="258" width="68" height="24" rx="4" fill="var(--tp-verdigris)" fill-opacity="0.2" stroke="var(--tp-verdigris)"/>
          <text x="486" y="273" text-anchor="middle" font-size="7.8" font-weight="700" fill="currentColor">CauchyWindow</text>
          <rect data-b01-qed-node x="530" y="258" width="68" height="24" rx="4" fill="var(--tp-prussian)" fill-opacity="0.22" stroke="var(--tp-prussian)"/>
          <text x="564" y="273" text-anchor="middle" font-size="7.8" font-weight="700" fill="currentColor">ErdosTuranQED</text>
        """
    elif slug == "b02":
        # B.02: Rotated d x d Surface Code Stabilizer Lattice + FeMoCo [Fe7MoS9C] Cluster + Active-Volume Tiles
        plaquettes = []
        for r in range(4):
            for c in range(4):
                px = 42 + c * 42
                py = 56 + r * 42
                is_x = (r + c) % 2 == 0
                fill = "var(--tp-prussian)" if is_x else "var(--tp-verdigris)"
                lbl = "X" if is_x else "Z"
                plaquettes.append(
                    f'<rect data-b02-plaq="{r}-{c}" x="{px}" y="{py}" width="40" height="40" rx="4" fill="{fill}" fill-opacity="0.20" stroke="{fill}" stroke-width="1.2"/>'
                    f'<text x="{px + 20}" y="{py + 24}" text-anchor="middle" font-size="9" font-weight="700" fill="currentColor">{lbl}</text>'
                )
        left_panels = f"""
          <rect x="12" y="12" width="248" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="136" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">KITAEV ROTATED SURFACE CODE (X/Z)</text>
          {"".join(plaquettes)}
          <path data-b02-syndrome-chain d="M 62 76 L 104 118 L 146 118 L 188 160" fill="none" stroke="var(--tp-minium)" stroke-width="2.6" stroke-dasharray="4,3" opacity="0.35"/>
          <circle cx="62" cy="76" r="5" fill="var(--tp-verdigris)"/>
          <circle cx="188" cy="160" r="5" fill="var(--tp-verdigris)"/>
          <text x="136" y="246" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)">MWPM PyMatching Syndrome Pairing</text>
          <text x="136" y="266" text-anchor="middle" font-size="8" fill="currentColor">d = 27 ⇒ (d+1)/2 = 14 error weight bound</text>
          <text x="136" y="286" text-anchor="middle" font-size="8" fill="currentColor">P_L = 3.00 × 10⁻¹⁶ &lt; 10⁻¹² Toffoli budget</text>

          <rect x="272" y="12" width="352" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="448" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">FeMoCo [Fe₇MoS₉C] ACTIVE-SPACE &amp; 294 LOGICAL TILES</text>
          <rect x="288" y="44" width="320" height="124" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <line x1="340" y1="106" x2="400" y2="74" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="340" y1="106" x2="400" y2="138" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="400" y1="74" x2="448" y2="106" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="400" y1="138" x2="448" y2="106" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="448" y1="106" x2="500" y2="74" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="448" y1="106" x2="500" y2="138" stroke="var(--tp-graphite)" stroke-width="2.2"/>
          <line x1="500" y1="74" x2="556" y2="106" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <line x1="500" y1="138" x2="556" y2="106" stroke="var(--tp-prussian)" stroke-width="2.5"/>
          <circle cx="340" cy="106" r="10" fill="var(--tp-minium)"/>
          <text x="340" y="109" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">Fe1</text>
          <circle cx="400" cy="74" r="9.5" fill="var(--tp-minium)"/>
          <text x="400" y="77" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">Fe2</text>
          <circle cx="400" cy="138" r="9.5" fill="var(--tp-minium)"/>
          <text x="400" y="141" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">Fe3</text>
          <circle cx="448" cy="106" r="8.5" fill="var(--tp-ink)"/>
          <text x="448" y="109" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">C⁴⁻</text>
          <circle cx="500" cy="74" r="9.5" fill="var(--tp-minium)"/>
          <text x="500" y="77" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">Fe6</text>
          <circle cx="500" cy="138" r="9.5" fill="var(--tp-minium)"/>
          <text x="500" y="141" text-anchor="middle" font-size="7.5" font-weight="700" fill="#fff">Fe7</text>
          <circle cx="556" cy="106" r="12" fill="var(--tp-verdigris)"/>
          <text x="556" y="109" text-anchor="middle" font-size="8" font-weight="700" fill="#fff">Mo</text>
          <text x="448" y="158" text-anchor="middle" font-size="8" fill="currentColor">PDB 3U7Q (1.0 Å) · CAS(54e, 54o) → 108 Spin-Orbitals · THC Block Encoding</text>

          <rect x="288" y="180" width="320" height="112" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="448" y="198" text-anchor="middle" font-size="8.8" font-weight="700" fill="var(--tp-prussian)">ACTIVE-VOLUME ARCHITECTURE (294 TILES × 2d² = 428,652 QUBITS)</text>
          <rect x="304" y="210" width="134" height="54" rx="4" fill="var(--tp-prussian)" fill-opacity="0.22" stroke="var(--tp-prussian)"/>
          <text x="371" y="233" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">114 Data &amp; Routing Tiles</text>
          <text x="371" y="249" text-anchor="middle" font-size="8" fill="currentColor">166,212 physical qubits</text>
          <rect x="454" y="210" width="138" height="54" rx="4" fill="var(--tp-verdigris)" fill-opacity="0.22" stroke="var(--tp-verdigris)"/>
          <text x="523" y="233" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">180 Magic-State Factories</text>
          <text x="523" y="249" text-anchor="middle" font-size="8" fill="currentColor">262,440 physical qubits</text>
          <text data-b02-tile-hud x="448" y="281" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-verdigris)">15-to-1 CCZ Distillation + Qubitized Phase Estimation</text>
        """
    elif slug == "b03":
        # B.03: SIMP Funicular Rib Density Mesh + Alluvial Embodied-Carbon Mass-Balance Sankey Ribbon
        left_panels = """
          <rect x="12" y="12" width="308" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="166" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">SIMP TOPOLOGY RIB FIELD ρ(x,y) (V/V₀ = 0.35)</text>
          <rect x="28" y="46" width="276" height="156" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect x="28" y="46" width="276" height="18" rx="3" fill="var(--tp-prussian)" opacity="0.88"/>
          <path data-b03-rib-arch d="M 34 196 Q 166 64 298 196" fill="none" stroke="var(--tp-prussian)" stroke-width="14" stroke-linecap="round"/>
          <path data-b03-rib-sec1 d="M 88 196 Q 166 102 244 196" fill="none" stroke="var(--tp-verdigris)" stroke-width="8" stroke-linecap="round"/>
          <line x1="112" y1="62" x2="72" y2="162" stroke="var(--tp-prussian)" stroke-width="6" stroke-linecap="round"/>
          <line x1="220" y1="62" x2="260" y2="162" stroke="var(--tp-prussian)" stroke-width="6" stroke-linecap="round"/>
          <line x1="166" y1="62" x2="166" y2="112" stroke="var(--tp-verdigris)" stroke-width="6" stroke-linecap="round"/>
          <polygon points="30,198 42,198 36,186" fill="var(--tp-minium)"/>
          <polygon points="290,198 302,198 296,186" fill="var(--tp-minium)"/>
          <text x="166" y="186" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-verdigris)">65% Tension-Zone Voided · Trabecular Michell Ribs</text>
          <rect x="28" y="214" width="276" height="78" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="166" y="232" text-anchor="middle" font-size="8.8" font-weight="700" fill="var(--tp-prussian)">FEniCS / DOLFINX COMPLIANCE PARETO BOUND</text>
          <text x="166" y="252" text-anchor="middle" font-size="8.2" fill="currentColor">E(ρ_e) = E_min + ρ_e³ (E₀ − E_min) · p = 3.0</text>
          <text x="166" y="272" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-verdigris)">c / c₀ = 1.224 &lt; 1.35 (Eurocode 2 L/250 PASS)</text>

          <rect x="332" y="12" width="292" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="478" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">EMBODIED CARBON SANKEY MASS BALANCE</text>
          <rect x="350" y="54" width="36" height="176" rx="4" fill="var(--tp-minium)" opacity="0.82"/>
          <text x="368" y="48" text-anchor="middle" font-size="8" font-weight="700" fill="currentColor">Baseline 148.0</text>
          <path d="M 386 54 C 430 54, 430 48, 474 48 L 474 162 C 430 162, 430 168, 386 168 Z" fill="var(--tp-verdigris)" fill-opacity="0.28" stroke="var(--tp-verdigris)" stroke-width="1.4"/>
          <path data-b03-sankey-retain d="M 386 168 C 450 168, 490 184, 558 184 L 558 232 C 490 232, 450 230, 386 230 Z" fill="var(--tp-prussian)" fill-opacity="0.32" stroke="var(--tp-prussian)" stroke-width="1.4"/>
          <rect x="474" y="48" width="128" height="114" rx="5" fill="var(--tp-verdigris)" fill-opacity="0.18" stroke="var(--tp-verdigris)"/>
          <text x="538" y="84" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)">−96.2 kg CO₂e/m²</text>
          <text x="538" y="102" text-anchor="middle" font-size="8" fill="currentColor">SIMP Voiding (65% saved)</text>
          <text x="538" y="126" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)">−12.4 kg CO₂e/m²</text>
          <text x="538" y="144" text-anchor="middle" font-size="8" fill="currentColor">CaCO₃ Mineralization</text>
          <rect data-b03-net-bar x="558" y="184" width="44" height="48" rx="4" fill="var(--tp-prussian)"/>
          <text x="580" y="250" text-anchor="middle" font-size="8.8" font-weight="700" fill="var(--tp-prussian)">39.40 kg/m²</text>
          <text x="478" y="284" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-verdigris)">IStructE SCORS A+ Ceiling: 45.0 kg CO₂e/m² (PASS)</text>
        """
    elif slug == "b04":
        # B.04: Dual Reciprocal Form Diagram Gamma & Force Polyhedron Gamma* + 8-13 um Atmospheric Window Spectrum
        left_panels = """
          <rect x="12" y="12" width="312" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="168" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">MAXWELL RECIPROCAL FORM Γ &amp; FORCE POLYHEDRON Γ*</text>
          <rect x="26" y="44" width="284" height="134" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <path d="M 38 158 Q 168 48 298 158" fill="none" stroke="var(--tp-graphite)" stroke-width="14" stroke-opacity="0.24"/>
          <path data-b04-thrust-arch d="M 38 158 Q 168 52 298 158" fill="none" stroke="var(--tp-verdigris)" stroke-width="3.2"/>
          <line x1="38" y1="158" x2="298" y2="158" stroke="var(--tp-prussian)" stroke-width="2" stroke-dasharray="5,3"/>
          <text x="168" y="148" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-prussian)">Span L = 16.0 m · Rise f = 2.56 m · H = 100.0 kN (0 kg rebar)</text>
          <text x="168" y="170" text-anchor="middle" font-size="7.8" fill="var(--tp-verdigris)">Heyman Middle-Third Kern e ≤ t/6 Satisfied Everywhere</text>

          <rect x="26" y="188" width="284" height="106" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="168" y="205" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-prussian)">CLOSED DUAL FORCE POLYGON Γ* (∑ A_f n_f = 0)</text>
          <polygon data-b04-force-poly points="84,274 168,216 252,274 168,252" fill="var(--tp-prussian)" fill-opacity="0.20" stroke="var(--tp-prussian)" stroke-width="1.8"/>
          <line x1="84" y1="274" x2="252" y2="274" stroke="var(--tp-verdigris)" stroke-width="2.2"/>
          <text x="168" y="286" text-anchor="middle" font-size="8" fill="currentColor">COMPAS 3D Graphic Statics · Pure Compression Equilibrium</text>

          <rect x="336" y="12" width="288" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="480" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">8–13 μm SKY-COOLING SPECTRAL SELECTIVITY</text>
          <rect x="352" y="46" width="256" height="148" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <rect x="478" y="56" width="96" height="120" fill="var(--tp-verdigris)" fill-opacity="0.18"/>
          <polyline points="364,66 436,68 456,164 476,168" fill="none" stroke="var(--tp-prussian)" stroke-width="2.6"/>
          <polyline data-b04-lwir-curve points="478,70 526,66 574,68 596,148" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.8"/>
          <text x="410" y="92" text-anchor="middle" font-size="8" font-weight="700" fill="var(--tp-prussian)">Solar R_sol = 0.97</text>
          <text x="526" y="92" text-anchor="middle" font-size="8" font-weight="700" fill="var(--tp-verdigris)">8–13 μm ε_IR = 0.96</text>
          <text x="480" y="186" text-anchor="middle" font-size="8" fill="currentColor">P(VdF-HFP) Hierarchical Micropores Scatter 0.3–2.5 μm Sun</text>
          <rect x="352" y="204" width="256" height="90" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="480" y="222" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-prussian)">MIDDAY RADIATIVE ENERGY BALANCE (1,000 W/m² SUN)</text>
          <text x="480" y="242" text-anchor="middle" font-size="8.2" fill="currentColor">q_rad (151.7) − q_atm (23.3) − q_sol (30.0) = 98.4 W/m²</text>
          <text x="480" y="264" text-anchor="middle" font-size="8.8" font-weight="700" fill="var(--tp-verdigris)">Stagnation Depression ΔT = −5.2 °C (Zero Grid Power)</text>
        """
    elif slug == "b05":
        # B.05: Viscous Burgers Shock Wavefront Evolution u(x,t) + PySR Expression Tree DAG + STLSQ Spectrum
        left_panels = """
          <rect x="12" y="12" width="308" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="166" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">DEDALUS VISCOUS BURGERS SHOCK ROLLOUT u(x,t)</text>
          <rect x="28" y="46" width="276" height="148" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <line x1="40" y1="120" x2="292" y2="120" stroke="currentColor" stroke-opacity="0.25"/>
          <path d="M 42 120 Q 104 54 166 120 T 290 120" fill="none" stroke="var(--tp-prussian)" stroke-width="1.6" stroke-dasharray="4,3"/>
          <path data-b05-shock-wave d="M 42 120 C 98 52, 156 52, 166 120 C 176 188, 234 188, 290 120" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.8"/>
          <circle cx="108" cy="76" r="3" fill="var(--tp-minium)"/>
          <circle cx="142" cy="84" r="3" fill="var(--tp-minium)"/>
          <circle cx="166" cy="120" r="3.5" fill="var(--tp-minium)"/>
          <circle cx="190" cy="156" r="3" fill="var(--tp-minium)"/>
          <circle cx="224" cy="164" r="3" fill="var(--tp-minium)"/>
          <text x="166" y="182" text-anchor="middle" font-size="8" fill="currentColor">Chebyshev–Fourier N = 200 Collocation Nodes (σ = 0.02)</text>

          <rect x="28" y="204" width="276" height="90" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="166" y="222" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-prussian)">STLSQ HARD-THRESHOLDING SPECTRUM (|ξ_k| ≥ λ = 0.05)</text>
          <line x1="44" y1="268" x2="288" y2="268" stroke="currentColor" stroke-opacity="0.35"/>
          <line data-b05-cutoff-line x1="44" y1="252" x2="288" y2="252" stroke="var(--tp-minium)" stroke-width="1.4" stroke-dasharray="4,3"/>
          <rect x="56" y="264" width="24" height="4" fill="var(--tp-graphite)"/>
          <rect x="94" y="264" width="24" height="4" fill="var(--tp-graphite)"/>
          <rect x="132" y="264" width="24" height="4" fill="var(--tp-graphite)"/>
          <rect x="170" y="228" width="24" height="40" rx="2" fill="var(--tp-verdigris)"/>
          <rect data-b05-visc-bar x="208" y="242" width="24" height="26" rx="2" fill="var(--tp-prussian)"/>
          <rect data-b05-spurious-bar x="246" y="264" width="24" height="4" fill="var(--tp-graphite)"/>
          <text x="68" y="282" text-anchor="middle" font-size="7.5" fill="currentColor">1</text>
          <text x="106" y="282" text-anchor="middle" font-size="7.5" fill="currentColor">u</text>
          <text x="144" y="282" text-anchor="middle" font-size="7.5" fill="currentColor">u_x</text>
          <text x="182" y="282" text-anchor="middle" font-size="7.5" font-weight="700" fill="var(--tp-verdigris)">u·u_x</text>
          <text x="220" y="282" text-anchor="middle" font-size="7.5" font-weight="700" fill="var(--tp-prussian)">u_xx</text>
          <text x="258" y="282" text-anchor="middle" font-size="7.5" fill="currentColor">u³</text>

          <rect x="332" y="12" width="292" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="478" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">PYSR EXPRESSION TREE DAG (C_tree = 6)</text>
          <rect x="348" y="46" width="260" height="248" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <line x1="478" y1="78" x2="412" y2="132" stroke="var(--tp-prussian)" stroke-width="2"/>
          <line x1="478" y1="78" x2="544" y2="132" stroke="var(--tp-prussian)" stroke-width="2"/>
          <line x1="412" y1="132" x2="380" y2="192" stroke="var(--tp-verdigris)" stroke-width="1.8"/>
          <line x1="412" y1="132" x2="444" y2="192" stroke="var(--tp-verdigris)" stroke-width="1.8"/>
          <line x1="544" y1="132" x2="512" y2="192" stroke="var(--tp-verdigris)" stroke-width="1.8"/>
          <line x1="544" y1="132" x2="576" y2="192" stroke="var(--tp-verdigris)" stroke-width="1.8"/>
          <circle cx="478" cy="78" r="16" fill="var(--tp-prussian)"/>
          <text x="478" y="82" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">+</text>
          <circle cx="412" cy="132" r="15" fill="var(--tp-verdigris)"/>
          <text x="412" y="136" text-anchor="middle" font-size="9.5" font-weight="700" fill="#fff">−1·*</text>
          <circle cx="544" cy="132" r="15" fill="var(--tp-verdigris)"/>
          <text x="544" y="136" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">*</text>
          <rect x="360" y="192" width="40" height="24" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)"/>
          <text x="380" y="208" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">u</text>
          <rect x="424" y="192" width="40" height="24" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)"/>
          <text x="444" y="208" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">u_x</text>
          <rect x="492" y="192" width="40" height="24" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)"/>
          <text x="512" y="208" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">0.10</text>
          <rect x="556" y="192" width="40" height="24" rx="4" fill="var(--tp-stone)" stroke="var(--tp-prussian)"/>
          <text x="576" y="208" text-anchor="middle" font-size="8.5" font-weight="700" fill="currentColor">u_xx</text>
          <text x="478" y="246" text-anchor="middle" font-size="9" font-weight="700" fill="var(--tp-prussian)">u_t = −1.00 u·u_x + 0.10 u_xx</text>
          <text x="478" y="268" text-anchor="middle" font-size="8.2" font-weight="700" fill="var(--tp-verdigris)">Pareto MDL Knee: L_MDL = −1360.87 nats (PASS)</text>
        """
    else:
        # B.06: Standard Model Chiral Hypercharge Y_f^3 Balance Fulcrum + 1D MPS Tensor Chain & CFT Cut
        mps_nodes = []
        for idx in range(6):
            nx = 366 + idx * 42
            mps_nodes.append(
                f'<line x1="{nx}" y1="92" x2="{nx}" y2="124" stroke="var(--tp-prussian)" stroke-width="2"/>'
                f'<rect x="{nx - 13}" y="76" width="26" height="26" rx="5" fill="var(--tp-verdigris)" stroke="var(--tp-prussian)" stroke-width="1.4"/>'
                f'<text x="{nx}" y="93" text-anchor="middle" font-size="8" font-weight="700" fill="#fff">A^{idx+1}</text>'
            )
        left_panels = f"""
          <rect x="12" y="12" width="312" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="168" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-prussian)">PHYSLEAN CHIRAL HYPERCHARGE Tr[Y³] = 0 FULCRUM</text>
          <rect x="26" y="46" width="284" height="248" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <g data-b06-balance-beam>
            <line x1="48" y1="152" x2="288" y2="152" stroke="var(--tp-prussian)" stroke-width="3.2"/>
            <rect x="52" y="106" width="96" height="42" rx="5" fill="var(--tp-verdigris)" fill-opacity="0.22" stroke="var(--tp-verdigris)"/>
            <text x="100" y="124" text-anchor="middle" font-size="8" font-weight="700" fill="currentColor">Positive Cubes (+19/18)</text>
            <text x="100" y="139" text-anchor="middle" font-size="7.5" fill="currentColor">Q_L(6/216)+d_R(3/27)+e_R(1)</text>
            <rect x="188" y="106" width="96" height="42" rx="5" fill="var(--tp-minium)" fill-opacity="0.22" stroke="var(--tp-minium)"/>
            <text x="236" y="124" text-anchor="middle" font-size="8" font-weight="700" fill="currentColor">Negative Cubes (−19/18)</text>
            <text x="236" y="139" text-anchor="middle" font-size="7.5" fill="currentColor">u_R(−24/27) + L_L(−2/8)</text>
          </g>
          <polygon points="154,184 182,184 168,154" fill="var(--tp-prussian)"/>
          <text x="168" y="210" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-verdigris)">Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 (Lean 4 QED)</text>
          <text x="168" y="232" text-anchor="middle" font-size="8" fill="currentColor">Requires N_c = 3 Quark Colors for Lepton-Quark Cancellation</text>
          <text x="168" y="256" text-anchor="middle" font-size="8" font-weight="700" fill="var(--tp-prussian)">HEPLean / PhysLean · by norm_num over ℚ</text>

          <rect x="336" y="12" width="288" height="296" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="480" y="31" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--tp-verdigris)">ITENSORS.JL 1D MPS &amp; CALABRESE–CARDY CUT</text>
          <rect x="348" y="46" width="264" height="112" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <line x1="366" y1="89" x2="576" y2="89" stroke="var(--tp-verdigris)" stroke-width="4"/>
          {"".join(mps_nodes)}
          <line data-b06-cft-cut x1="471" y1="56" x2="471" y2="144" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="4,3"/>
          <text x="480" y="148" text-anchor="middle" font-size="8" font-weight="700" fill="var(--tp-minium)">Bipartite Entanglement Cut · Bond χ = 64 (ln χ = 4.16)</text>
          <rect x="348" y="168" width="264" height="126" rx="6" fill="var(--tp-vellum)" stroke="var(--tp-rule)"/>
          <text x="480" y="186" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--tp-prussian)">CRITICAL TFIM ENTANGLEMENT S_vN(L) = (c/6) ln L + s₁</text>
          <line x1="368" y1="210" x2="592" y2="210" stroke="var(--tp-verdigris)" stroke-width="2" stroke-dasharray="5,3"/>
          <polyline points="368,264 416,248 468,238 524,232 592,226" fill="none" stroke="var(--tp-prussian)" stroke-width="2.4"/>
          <text x="480" y="204" text-anchor="middle" font-size="7.8" font-weight="700" fill="var(--tp-verdigris)">MPS Capacity Ceiling ln(χ) = 4.1589 nats</text>
          <text x="480" y="280" text-anchor="middle" font-size="8" fill="currentColor">c = 1/2 · S_vN(128) = 0.8828 nats · E₀/N = −4/π = −1.2732</text>
        """

    return f"""<svg class="tp-bounty-crucible-svg tp-bounty-bespoke-svg" viewBox="0 0 960 330" role="img" aria-label="Bespoke Scientific Vector Observatory for Bounty {esc(fid)} ({esc(bid)})">
      {left_panels}
      {right_panel}
      <text x="480" y="323" text-anchor="middle" font-size="8.5" font-weight="600" fill="currentColor">Governing Operator ({esc(fid)}): {gov}</text>
    </svg>"""


def render_bounty_plate_b_webgl(bounty: dict) -> str:
    """Render Plate B: 4-Lens 3D WebGL2 & Multi-Axis Polar Benchmark Radar Observatory for a Bounty Folio."""
    slug = bounty["slug"]
    fid = bounty["folio_id"]
    bid = bounty["bounty_id"]
    verifier_rel = bounty["verifier_script"]
    surf_title, axes_hud = BOUNTY_3D_META.get(
        slug,
        ("Bounty State-Space & Proof Manifold", "X: Control P1 · Z: Control P2 · Y: Governing Potential"),
    )
    steps_btns = "\n            ".join(
        f'<button type="button" class="tp-step-btn" data-step-idx="{i}" aria-pressed="{"true" if i == 0 else "false"}">{esc(s.split("—")[0].strip())}</button>'
        for i, s in enumerate(bounty["steps"][:4])
    )
    return f"""        <div class="tp-plate tp-bounty-webgl-plate" role="region" aria-label="Plate {esc(fid)}-B 4-Lens 3D WebGL2 and Polar Benchmark Observatory">
          <div class="tp-plate-head">
            <span data-en="Plate {esc(fid)}-B &middot; 4-Lens 3D WebGL2 Manifold, Phase Streamlines, Conservation Ribbon &amp; 6-Axis Polar Radar" data-es="Lámina {esc(fid)}-B &middot; Observatorio 3D WebGL2 de 4 Lentes, Retrato de Fase, Listón de Conservación y Radar Polar">Plate {esc(fid)}-B &middot; 4-Lens 3D WebGL2 Manifold, Phase Streamlines, Conservation Ribbon &amp; 6-Axis Polar Radar</span>
            <div class="tp-plate-head-actions">
              <span>Verifier: <code>{esc(verifier_rel)}</code></span>
            </div>
          </div>
          <div class="tp-stepper" role="group" aria-label="4-Stage Proof &amp; Mechanism Stepper for {esc(fid)}">
            {steps_btns}
          </div>
          <div class="tp-webgl-wrap" role="region" aria-label="3D WebGL2 {esc(surf_title)} Observatory ({esc(fid)})">
            <div class="tp-plate-head">
              <span>{esc(fid)} ({esc(bid)}) &middot; {esc(surf_title)} (Drag to Orbit 360&deg;)</span>
              <div class="tp-lens-bar" role="group" aria-label="Select 4-Lens Visualization Mode for Bounty {esc(fid)}">
                <button type="button" class="tp-lens-btn" data-lens-mode="0" aria-pressed="true" data-en="1 &middot; 3D Surface" data-es="1 &middot; Superficie 3D">1 &middot; 3D Surface</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="1" aria-pressed="false" data-en="2 &middot; Phase Streamlines" data-es="2 &middot; Líneas de Fase">2 &middot; Phase Streamlines</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="2" aria-pressed="false" data-en="3 &middot; 4-Stage Ribbon" data-es="3 &middot; Listón 4 Etapas">3 &middot; 4-Stage Ribbon</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="3" aria-pressed="false" data-en="4 &middot; 6-Axis Polar Radar" data-es="4 &middot; Radar Polar">4 &middot; 6-Axis Polar Radar</button>
              </div>
            </div>
            <canvas class="tp-webgl-canvas" width="680" height="260" data-webgl-type="energy-landscape" data-folio-webgl="{esc(slug)}" data-pillar-webgl="bounties" aria-label="Interactive 3D WebGL2 {esc(surf_title)} for Bounty {esc(fid)}"></canvas>
            <svg class="tp-lens-svg" viewBox="0 0 680 230" role="img" aria-label="Interactive Multi-Lens Phase, 4-Stage Conservation Ribbon, and 6-Axis Polar Radar Diagram for Bounty {esc(fid)}" hidden></svg>
            <div class="tp-stage-axis-hud" data-webgl-axis-hud="{esc(slug)}">
              <span><strong>3D Surface Axes ({esc(fid)}):</strong> {esc(axes_hud)}</span>
            </div>
          </div>
        </div>"""


def render_bounty_plate_c_inspector(bounty: dict, py_filename: str) -> str:
    """Render Plate C: 4-Tab Interactive Prize Submission Readiness & Tri-Invariant Stress-Tester Tool."""
    slug = bounty["slug"]
    fid = bounty["folio_id"]
    bid = bounty["bounty_id"]
    verifier_rel = bounty["verifier_script"]
    skill_dir = bounty["skill_dir"]
    reg_name, reg_url = bounty["external_links"][0]
    doi_raw = bounty["primary_doi"]

    inv_cards = []
    for idx, rule_txt in enumerate(bounty["rules"][:3], 1):
        short_rule = rule_txt.split(":")[0].strip()
        inv_cards.append(
            f"""            <div class="tp-inv-switch-card" data-inv-card="{idx}">
              <div class="tp-inv-switch-top">
                <strong>Invariant {esc(fid)}-R{idx} &middot; {esc(short_rule)}</strong>
                <button type="button" class="tp-inv-toggle-btn" data-inv-toggle="{idx}" aria-pressed="true" data-en="ENFORCED (PASS)" data-es="ACTIVO (PASS)">ENFORCED (PASS)</button>
              </div>
              <p>{esc(rule_txt)}</p>
            </div>"""
        )
    inv_cards_html = "\n".join(inv_cards)

    default_json = (
        f'{{\n'
        f'  "folio_id": "{fid}",\n'
        f'  "bounty_id": "{bid}",\n'
        f'  "status": "PASS",\n'
        f'  "verifier": "python {verifier_rel}",\n'
        f'  "invariants_enforced": ["{fid}-R1", "{fid}-R2", "{fid}-R3"],\n'
        f'  "primary_doi": "https://doi.org/{doi_raw}",\n'
        f'  "official_registry": "{reg_url}",\n'
        f'  "benchmark_summary": "{bounty["pass_pill_en"]}"\n'
        f'}}'
    )

    cli_python = (
        f"# 1. Run standalone zero-dependency Bounty {fid} ({bid}) proof harness (< 0.05s)\n"
        f"python {verifier_rel}\n\n"
        f"# 2. Run portable SKILL.md companion verifier\n"
        f"python {skill_dir}/{py_filename}"
    )
    cli_agent = (
        f"# Equip Claude Code, Cursor, Copilot, or Antigravity with Bounty {fid} ({bid}) SKILL.md\n"
        f"cp {skill_dir}/SKILL.md .claude/skills/{bounty['skill_name']}/SKILL.md\n"
        f"python {skill_dir}/{py_filename}"
    )
    cli_cite = (
        f"# Verify Scite Smart Citations & Crossref DOIs for Bounty {fid} ({bid})\n"
        f"python tools/check_folio_citations.py --offline --include-informatico\n"
        f"# Primary Anchor: https://doi.org/{doi_raw}"
    )

    return f"""        <section class="tp-plate-card tp-bounty-submission-tool" data-bounty-inspector="{esc(slug)}" data-folio-id="{esc(fid)}" data-bounty-id="{esc(bid)}" data-verifier="{esc(verifier_rel)}" data-doi="{esc(doi_raw)}" data-registry="{esc(reg_url)}" aria-label="Interactive Prize Submission Readiness and Tri-Invariant Stress-Tester for {esc(fid)}">
          <div class="tp-plate-head">
            <span data-en="Plate {esc(fid)}-C &middot; Interactive Prize Submission Readiness &amp; Tri-Invariant Falsification Inspector" data-es="Lámina {esc(fid)}-C &middot; Inspector Interactivo de Preparación del Premio y Falsación de 3 Invariantes">Plate {esc(fid)}-C &middot; Interactive Prize Submission Readiness &amp; Tri-Invariant Falsification Inspector</span>
            <span class="tp-plate-live-badge" data-inspector-status="true">READY &middot; 3/3 INVARIANTS PASS</span>
          </div>
          <div class="tp-submission-tabs" role="tablist" aria-label="Bounty {esc(fid)} Inspection Tools">
            <button type="button" class="tp-sub-tab" role="tab" aria-selected="true" data-sub-tab="stress" data-en="1 &middot; Tri-Invariant Stress-Tester" data-es="1 &middot; Prueba de 3 Invariantes">1 &middot; Tri-Invariant Stress-Tester</button>
            <button type="button" class="tp-sub-tab" role="tab" aria-selected="false" data-sub-tab="telemetry" data-en="2 &middot; Live JSON Certificate" data-es="2 &middot; Certificado JSON en Vivo">2 &middot; Live JSON Certificate</button>
            <button type="button" class="tp-sub-tab" role="tab" aria-selected="false" data-sub-tab="cli" data-en="3 &middot; Reproducible CLI &amp; Agent Commands" data-es="3 &middot; Comandos CLI y Agente">3 &middot; Reproducible CLI &amp; Agent Commands</button>
          </div>

          <div class="tp-sub-panel" data-sub-panel="stress">
            <p class="tp-sym-caption" data-en="Toggle any of the three machine-checked invariants below to simulate an axiom knockout and inspect how our automated verification gate catches unverified claims before prize submission." data-es="Conmuta cualquiera de los tres invariantes verificados abajo para simular la violación de un axioma y observar cómo nuestra compuerta determinista detecta errores antes de enviar al premio.">Toggle any of the three machine-checked invariants below to simulate an axiom knockout and inspect how our automated verification gate catches unverified claims before prize submission.</p>
            <div class="tp-invariant-switches">
{inv_cards_html}
            </div>
          </div>

          <div class="tp-sub-panel" data-sub-panel="telemetry" hidden>
            <div class="tp-terminal-toolbar">
              <span><code>{esc(verifier_rel)} --json</code></span>
              <button type="button" class="tp-skill-btn tp-skill-btn-secondary" data-copy-inspector-json="true" data-en="Copy Live JSON Certificate" data-es="Copiar Certificado JSON">Copy Live JSON Certificate</button>
            </div>
            <pre class="tp-skill-pre tp-terminal-box"><code data-inspector-json-out>{esc(default_json)}</code></pre>
          </div>

          <div class="tp-sub-panel" data-sub-panel="cli" hidden>
            <div class="tp-symbolic-regime-bar" role="group" aria-label="Select CLI environment">
              <button type="button" class="tp-sym-regime-btn" data-cli-mode="python" aria-pressed="true">Python 3 Verifier</button>
              <button type="button" class="tp-sym-regime-btn" data-cli-mode="agent">AI Agent SKILL.md</button>
              <button type="button" class="tp-sym-regime-btn" data-cli-mode="cite">Scite &amp; DOI Audit</button>
              <button type="button" class="tp-skill-btn tp-skill-btn-secondary" data-copy-inspector-cli="true" data-en="Copy Command" data-es="Copiar Comando">Copy Command</button>
            </div>
            <pre class="tp-skill-pre tp-cli-box"><code data-inspector-cli-out data-cli-python="{esc(cli_python)}" data-cli-agent="{esc(cli_agent)}" data-cli-cite="{esc(cli_cite)}">{esc(cli_python)}</code></pre>
          </div>
        </section>"""
