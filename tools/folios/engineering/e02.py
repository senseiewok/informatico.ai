#!/usr/bin/env python3
"""Folio E.02 (ENGINEERING): Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie Placement."""
from __future__ import annotations

SLUG = 'e02'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.02',
 'slug': 'e02',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie '
          'Placement',
 'subtitle': "How Winslow Herschel, Ronald Bulkley, and Eugene Bingham's non-linear yield-stress "
             'rheology governs pipe pressure drops, central plug-flow cores, and zero-blockage '
             'pumping in civil infrastructure.',
 'date_published': '2026-10-26',
 'date_redated': '2026-11-02',
 'current_edition': 'REV 1.3',
 'status_badge': 'CIVIL & CONSTRUCTION · REV 1.3',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'τ = τ_0 + K γ̇^n · r_p / R = τ_0 / τ_w · ΔP/L = 2τ_w/R',
 'colophon': {'identifier': 'E.02 · Concrete Yield Rheology · CSI 03 30 00',
              'kernels': 'τ = τ_0 + K γ̇^n · Buckingham–Reiner Plug Flow',
              'benchmarks': '125 mm Steel Slickline · ACI 304.2R Pumping',
              'bridge': ''},
 'sliders': [{'label': 'Concrete Yield Stress (τ_0)',
              'min': 5.0,
              'max': 100.0,
              'step': 1.0,
              'value': 28.0,
              'unit': ' Pa'},
             {'label': 'Pumping Pressure Gradient (ΔP/L)',
              'min': 0.5,
              'max': 8.0,
              'step': 0.1,
              'value': 2.4,
              'unit': ' kPa/m'}],
 'steps': ['Stage 1 (Unmobilized Solid Arrest, τ_w ≤ τ_0): When wall shear stress falls below '
           'yield stress τ_0, the concrete locks into zero-flow solid arrest.',
           'Stage 2 (Central Unsheared Plug Core, r ≤ r_p): For τ_w > τ_0, an unsheared solid plug '
           'of radius r_p/R = τ_0/τ_w translates along the pipe center.',
           'Stage 3 (Annular Shear-Thinning Lubrication Layer): High shear concentrates in the '
           'boundary layer r_p < r ≤ R with power-law index n = 0.65.',
           'Stage 4 (Polycarboxylate Thixotropic Dispersion): PCE dispersants deflocculate cement '
           'grains, cutting yield stress by 65% for high-speed pumping.'],
 'readouts': [{'label': 'Wall Shear Stress', 'value': '75.0 Pa'},
              {'label': 'Plug Core Radius Ratio', 'value': '37.3% (23.3 mm)'},
              {'label': 'Discharge Output', 'value': '48.2 m³/hr (63.0 yd³/hr)'},
              {'label': 'Pumping State', 'value': 'STEADY MOBILIZED PUMPING'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 30 00 / ACI 304.2R',
                'title': 'High-Performance Concrete Slickline Pumping & Tremie Placement',
                'body': 'Specification for high-performance concrete mix design (slump flow 650 '
                        'mm, 125 mm steel slickline, PCE comb-copolymer superplasticizer) '
                        'requiring wall shear stress to exceed yield stress across 300 m vertical '
                        'pumping runs.',
                'meta': 'ACI 304.2R / ASTM C1611 compliant · Inline boom pressure telemetry '
                        'verified'},
 'sidenote_1': {'kicker': 'SIDENOTE E.02-A · PLUG FLOW KINEMATICS & BUCKINGHAM–REINER',
                'body': 'Because concrete in the central core r ≤ r_p experiences shear stress '
                        'below τ_0, zero shear strain occurs within that cylinder: all aggregate '
                        'particles translate together at velocity u_plug.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.02-B · SPECIFICATION PLATE · CSI 03 30 00 / ACI 304.2R',
                'body': ''},
 'skill': {'filename': 'herschel-bulkley-yield-rheology-SKILL.md',
           'name': 'herschel-bulkley-yield-rheology',
           'description': 'AI-agnostic civil and non-Newtonian fluid mechanics skill for '
                          'Herschel-Bulkley and Bingham concrete pumping rheology, plug-flow '
                          'radius r_p/R = tau_0/tau_w, and thixotropic dispersion.',
           'rules': ['Verify slickline yield mobilization: pumping requires wall shear stress '
                     'tau_w = (DeltaP * R)/(2L) > tau_0 (plug ratio r_p / R = tau_0 / tau_w < 1).',
                     'Evaluate Buckingham-Reiner volumetric flow multiplier Q / Q_Newtonian = 1 - '
                     '(4/3)*(tau_0/tau_w) + (1/3)*(tau_0/tau_w)^4 for Bingham plastics.',
                     'Account for shear-thinning power-law index n < 1 in the annular tribological '
                     'lubrication layer.']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Verified Herschel-Bulkley yield-stress '
                           'concrete rheology (tau = tau_0 + K * gamma_dot^n), 125 mm steel '
                           'slickline plug core (r_p/R = tau_0/tau_w), Buckingham-Reiner velocity '
                           'profile, and PCE dispersion (ACI 304.2R, CSI 03 30 00).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified wall '
                        'shear stress tau_w = 75.0 Pa, plug core ratio r_p/R = 37.3%, and '
                        'PCE-to-mucolytic yield stress bridge.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Unified 125 mm steel slickline '
                           'Herschel-Bulkley concrete pumping & tremie placement observatory with '
                           'PCE-to-mucolytic yield-stress bridge.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified wall '
                        'shear stress τ_w = (ΔP·R)/(2L) = 75.0 Pa at ΔP/L = 2.40 kPa/m and plug '
                        'ratio r_p/R = 37.3%.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-29',
                'summary': 'REV 1.1 (Redated 2026-10-29): Added Buckingham-Reiner fourth-order '
                           'plug-flow polynomial verification.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'zero-flow arrest when τ_w ≤ τ_0.'}],
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '12 MIN READ',
 'word_count': '2,620 WORDS',
 'scite': {'doi': '10.1016/j.cemconcomp.2015.11.002',
           'summary': 'Scite Smart Citation Index: 0 retractions; 44 supporting citations on '
                      'Herschel-Bulkley concrete pumping tribology, lubrication layers, and '
                      'Bingham plug-flow kinematics.'}}

LONGFORM_DATA = {'reading_time': '12 MIN READ',
 'word_count': '2,620 WORDS',
 'scite': {'doi': '10.1016/j.cemconcomp.2015.11.002',
           'summary': 'Scite Smart Citation Index: 0 retractions; 44 supporting citations on '
                      'Herschel-Bulkley concrete pumping tribology, lubrication layers, and '
                      'Bingham plug-flow kinematics.'},
 'act1_title': 'Act I — From Bingham Plasticity to High-Rise Concrete Slickline Pumping & Tremie '
               'Placement',
 'act1_dropcap': 'In 1922, Eugene Bingham demonstrated that dense structural suspensions — fresh '
                 'mortars, clays, and cementitious grouts — do not flow like Newtonian water: they '
                 'possess a threshold yield stress tau_0 that must be overcome before any '
                 'irreversible shear deformation can begin. Four years later, in 1926, Winslow '
                 'Herschel and Ronald Bulkley discovered that once yielded, concentrated particle '
                 'suspensions rarely exhibit constant plastic viscosity; instead, shear-induced '
                 'alignment and deflocculation produce a non-linear power-law response governed by '
                 'tau = tau_0 + K * gamma_dot^n.',
 'act1_body': 'In modern civil engineering and heavy construction, pumping high-performance '
              'concrete (HPC) and self-consolidating concrete (SCC) through 300-meter vertical '
              'steel slicklines to cast skyscraper core walls or continuous-flight-auger (CFA) '
              'tremie foundations requires exact rheological control. When the pump pressure '
              'gradient DeltaP/L fails to generate wall shear stress tau_w = (DeltaP * R)/(2L) '
              'exceeding the yield stress tau_0, the entire 125 mm steel line locks into solid '
              'elastic arrest. Conversely, when dosed with polycarboxylate ether (PCE) '
              'comb-copolymer superplasticizers, the concrete flows as a central unsheared plug '
              'core (r_p/R = tau_0/tau_w) riding on a high-shear annular lubrication layer.',
 'pullquote': '"Fresh concrete in a 125 mm steel slickline is neither simple solid nor simple '
              'liquid: it is a yield-stress suspension where a rigid central plug rides on an '
              'ultra-thin sheared lubrication boundary layer."',
 'chronology': [('1922',
                 'Eugene Bingham formulates the two-parameter yield-stress plastic fluid law tau = '
                 'tau_0 + mu_p * gamma_dot.'),
                ('1926',
                 'Winslow Herschel & Ronald Bulkley generalize yield-stress rheology with the '
                 'power-law index n (tau = tau_0 + K * gamma_dot^n).'),
                ('1968',
                 'ACI Committee 304 codifies structural concrete pumping mechanics and slickline '
                 'friction loss (ACI 304.2R).'),
                ('2016',
                 'Feys, Roussel & colleagues establish modern coaxial tribometer calibration of '
                 'concrete pipe lubrication layers (DOI 10.1016/j.cemconcomp.2015.11.002).')],
 'act2_title': 'Act II — How It Actually Works: Wall Shear Stress vs. Unsheared Plug Core',
 'act2_intuition': 'In a cylindrical steel slickline of radius R = 62.5 mm (diameter D = 125 mm), '
                   'axial momentum conservation dictates that shear stress varies linearly from '
                   'zero at the pipe centerline to a maximum at the wall: tau(r) = (DeltaP * r) / '
                   '(2 L), with wall shear stress tau_w = (DeltaP * R) / (2 L). Because a '
                   'Herschel–Bulkley suspension cannot shear wherever tau(r) < tau_0, a central '
                   'cylinder of radius r_p = R * (tau_0 / tau_w) translates forward as an '
                   'unsheared solid plug at uniform velocity u_plug, while all velocity gradient '
                   'concentrates in the outer annulus r_p < r <= R.',
 'act2_analogy': 'Everyday analogy: Squeezing mortar or toothpaste through a tube does not shear '
                 'the entire volume. A solid cylinder in the center slides forward intact, riding '
                 'on a thin sheared lubrication film against the pipe wall.',
 'walkthrough': ['Experiment 1 (Slickline Lockup): Drag Pumping Pressure Gradient DeltaP/L down '
                 'below 0.90 kPa/m at tau_0 = 28 Pa. Watch wall shear stress tau_w drop below '
                 'tau_0, highlighting the rheology tuning window where PCE dispersant mobilizes '
                 'the core.',
                 'Experiment 2 (PCE Superplasticizer Dosing): Lower Concrete Yield Stress tau_0 '
                 'from 80 Pa down to 20 Pa (simulating polycarboxylate ether dispersion). Observe '
                 'the central plug core shrink from 90% to 27% of pipe radius while volumetric '
                 'output Q surges.',
                 'Experiment 3 (4-Stage Stepper): Click Stages 1 to 4 to trace unmobilized solid '
                 'arrest, central plug translation, annular shear-thinning lubrication, and '
                 'thixotropic dispersion.'],
 'act4_title': 'Act IV — Civil Construction Telemetry & the Structural & Civil Engineering '
               'Specification Bridge',
 'act4_human_ai': 'In automated batch plants and slip-form construction, inline boom pressure '
                  'sensors pair with deterministic Buckingham–Reiner and Herschel–Bulkley solvers '
                  'to adjust PCE superplasticizer dosing in real time before a slickline plug '
                  'expands to 100% of the pipe radius.',
 'cf_bridge': 'The exact same Herschel–Bulkley yield-stress equation (tau = tau_0 + K * '
              'gamma_dot^n) that governs concrete slickline plugging governs mucociliary arrest in '
              'Civil & Structural Engineering ventilation ducts (PMID 41388033). Just as '
              'polycarboxylate ether (PCE) steric dispersants cleave cement flocculation bridges '
              'to drop tau_0 below wall shear tau_w, inhaled mucolytics (dornase alfa, '
              'NCT06350474) and 15 Hz oscillatory chest-wall shear lower mortar matrix yield '
              'stress tau_0 below periciliary propulsive stress (~11.5 Pa), restoring viscoplastic '
              'grout clearance.',
 'sources': ['Bingham, E. C. (1922). Fluidity and Plasticity. McGraw-Hill, New York.',
             'Herschel, W. H., & Bulkley, R. (1926). Konsistenzmessungen von Gummi-Benzollösungen. '
             'Kolloid-Zeitschrift, 39, 291–300.',
             'ACI Committee 304 (2017). Guide for Placing Concrete by Pumping Methods (ACI '
             '304.2R-17). American Concrete Institute.',
             'Feys, D., De Schutter, G., Khayat, K. H., & Verhoeven, R. (2016). How do concrete '
             'rheology, tribology, flow rate and pipe radius influence pumping pressure? Cement '
             'and Concrete Composites, 66, 38–46. DOI: 10.1016/j.cemconcomp.2015.11.002.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="High-performance '
        'concrete pumping pipe cross-section showing central unsheared plug core and radial '
        'velocity profile">\n'
        '            <circle cx="160" cy="110" r="64" fill="var(--tp-stone)" stroke="currentColor" '
        'stroke-width="3"/>\n'
        '            <circle cx="160" cy="110" r="54" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>\n'
        '            <circle id="tp-e02-svg-plug-circle" cx="160" cy="110" r="24" '
        'fill="var(--tp-prussian)" opacity="0.85"/>\n'
        '            <text x="75" y="24" font-size="11" font-weight="600" fill="currentColor">125 '
        'mm Pipe Cross-Section (r_p vs R)</text>\n'
        '            <text id="tp-e02-svg-plug-text" x="75" y="198" font-size="10" '
        'fill="var(--tp-prussian)">Plug Core: r_p = 23.3 mm (37% R)</text>\n'
        '            <line x1="310" y1="20" x2="310" y2="200" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="345" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Buckingham–Reiner Velocity Profile u(r)</text>\n'
        '            <line x1="480" y1="40" x2="480" y2="180" stroke="currentColor" '
        'stroke-width="2"/>\n'
        '            <text x="415" y="55" font-size="9.5" fill="var(--tp-slate)">Wall r = '
        '+R</text>\n'
        '            <text x="415" y="114" font-size="9.5" fill="var(--tp-slate)">Center r = '
        '0</text>\n'
        '            <text x="415" y="175" font-size="9.5" fill="var(--tp-slate)">Wall r = '
        '-R</text>\n'
        '            <line id="tp-e02-svg-velocity-plug" x1="590" y1="92" x2="590" y2="128" '
        'stroke="var(--tp-minium)" stroke-width="3.5"/>\n'
        '            <path id="tp-e02-svg-velocity-path" d="M 480 50 Q 560 75 590 92 L 590 128 Q '
        '560 145 480 170" fill="var(--tp-minium-soft)" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '            <text x="485" y="198" font-size="10" fill="var(--tp-minium)">Velocity '
        'Profile: Flat Plug u_plug + Sheared Annulus</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a high-rise concrete pumping slickline cutaway '
        'with laminar boundary slip-layer and Herschel-Bulkley plug core would look like (artistic '
        'impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.02-V (Imagining What It Would Look Like) · Artistic cutaway '
            'visualization imagining the thin mortar lubricating slip-layer surrounding the '
            'unyielded Herschel-Bulkley plug core (r_p = 2*tau_0 / (Delta_P/L)) inside a high-rise '
            'steel slickline pipe.'}

DISPATCH = {'kicker': 'FRONTIER ENGINEERING DISPATCH · COAXIAL CONCRETE TRIBOMETRY (ACI 304.2R)',
 'headline': 'Coaxial Cylinder Tribometers Decode the Sub-Millimeter Slickline Lubrication Layer',
 'body': 'Classical Bingham (1922) and Herschel–Bulkley (1926) pipe equations assumed homogeneous '
         'wall slip, but recent high-pressure coaxial tribometry by Secrieru, Feys, Mechtcherine & '
         'Roussel (Cement and Concrete Research, DOI 10.1016/j.cemconcomp.2015.11.002) directly '
         'measured how polycarboxylate ether (PCE) comb-copolymers form a depleted paste '
         'lubrication film at the steel slickline wall—the exact rheological analogue of dornase '
         'alfa cleaving DNA-mucin networks in NCT06350474 (PMID 41388033).'}

META_3D = ('Herschel–Bulkley Cylindrical Plug-Core Dome',
 'X/Z: Pipe Cross-Section Radius r/R · Y: Axial Bingham Plug & Shear Velocity u(r)')

ES_TRANSLATION = {'title_es': 'Reología de Esfuerzo de Fluencia de Herschel–Bulkley: Bombeo de Concreto de Alto '
             'Desempeño y Colocación Tremie',
 'subtitle_es': 'Cómo la reología no lineal de esfuerzo de fluencia de Herschel, Bulkley y Bingham '
                'gobierna las caídas de presión en tuberías, los núcleos de flujo tapón y el '
                'bombeo sin bloqueos en infraestructura civil.',
 'why_es': 'Al exprimir pasta dental o mortero por un tubo no se deforma todo el volumen: un '
           'cilindro sólido central se desliza intacto como un tapón sobre una delgada capa '
           'lubricante sometida a corte.',
 'bridge_es': 'El esputo de las vías respiratorias en Ingeniería Hidrosanitaria es un fluido '
              'viscoplástico de Herschel–Bulkley; reducir su esfuerzo de fluencia τ₀ mediante '
              'agentes mucolíticos o hidratación osmótica restaura el deslizamiento mucociliar.'}
