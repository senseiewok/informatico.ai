#!/usr/bin/env python3
"""Folio E.10 (ENGINEERING): 3D Concrete Printing (3DCP) Extrusion Rheology & Buildability: Roussel Thixotropic Structuration, Elastic Buckling vs. Plastic Collapse & Robotic Toolpath Control."""
from __future__ import annotations

SLUG = 'e10'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.10',
 'slug': 'e10',
 'pillar': 'engineering',
 'category_code': 'E',
 'parent_folios': ['E.02', 'A.01'],
 'lineage_mode': 'CONTINUATION · Continues E.02 Herschel–Bulkley Pumping & A.01 Funicular Shell '
                 'Geometry',
 'title': '3D Concrete Printing (3DCP) Extrusion Rheology & Buildability: Roussel Thixotropic '
          'Structuration, Elastic Buckling vs. Plastic Collapse & Robotic Toolpath Control',
 'subtitle': "Continuing Folio E.02's concrete slickline rheology and A.01's funicular shells: how "
             "Nicolas Roussel's thixotropic structuration rate A_thix and Suiker's buckling laws "
             'govern formwork-free robotic construction.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': '3DCP ADDITIVE CIVIL · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'τ_0(t) = τ_{0,0} + A_thix t · H_plast = √3 τ_0(t)/(ρg) (von Mises)',
 'colophon': {'identifier': 'E.10 · 3D Concrete Printing Rheology & Buildability',
              'kernels': 'Roussel Thixotropy A_thix · Suiker Elastic Buckling vs. Plastic Collapse',
              'benchmarks': 'Model, ρ = 2,200 kg/m³ assumed: A_thix = 0.85 Pa/s < ρ g v_build/√3 = '
                            '5.5 Pa/s at v_build = 1.6 m/hr ⇒ base yields at H ≈ 0.04 m',
              'bridge': 'Continues E.02/A.01 · Analogy only: cement flocculation ↔ mucus as '
                        'another thixotropic material'},
 'sliders': [{'label': 'Thixotropic Structuration Rate (A_thix)',
              'min': 0.2,
              'max': 2.0,
              'step': 0.05,
              'value': 0.85,
              'unit': ' Pa/s'},
             {'label': 'Robotic Vertical Build Rate (v_build)',
              'min': 0.6,
              'max': 3.8,
              'step': 0.1,
              'value': 1.6,
              'unit': ' m/hr'}],
 'steps': ['Stage 1 (Nozzle Shear Rejuvenation, Continuing E.02): High shear inside the robotic '
           'printhead breaks colloidal links; this folio takes an illustrative initial yield stress '
           'τ_{0,0} = 420 Pa at deposition.',
           'Stage 2 (Roussel Linear Thixotropic Structuration): At rest, flocculation and early '
           'hydration rebuild static yield stress, modelled as τ_0(t) = τ_{0,0} + A_thix t (A_thix '
           '= 0.85 Pa/s). The linear law is a short-time approximation; over longer times strength '
           'can grow faster than linearly.',
           'Stage 3 (Plastic Yield vs. Suiker Buckling): The bottom layer must resist gravity shear '
           'τ_b = ρ g H / √3 (the von Mises criterion). With ρ = 2,200 kg/m³ (assumed) and '
           'v_build = 1.6 m/hr, gravity shear grows at 5.5 Pa/s against A_thix = 0.85 Pa/s, so '
           'in this model the base yields at H ≈ 0.04 m. Self-weight elastic buckling (Suiker '
           '2018) also limits wall height; it is not computed on this page.',
           'Stage 4 (Corrugated Funicular Toolpath, Continuing A.01): Corrugating the toolpath '
           'raises the wall\'s second moment of area and so its buckling resistance; this folio '
           'does not compute by how much, or how much cement it saves.'],
 'readouts': [{'label': 'Plastic Collapse Height (model, defaults)',
               'value': 'H ≈ 0.04 m (ρ = 2,200 kg/m³ assumed)'},
              {'label': 'Structuration vs. Gravity Shear Rate',
               'value': 'A_thix 0.85 < ρgv/√3 ≈ 5.5 Pa/s'},
              {'label': 'Governing Failure Mode (model)',
               'value': 'PLASTIC YIELD (buckling not computed)'},
              {'label': 'Model Buildability Status',
               'value': 'NOT BUILDABLE AT THESE SETTINGS (model)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 30 00 (filing label)',
                'title': 'Robotic 3D-Printed Structural Concrete Walls with Active Nozzle '
                         'Acceleration (Design Study)',
                'body': 'Design study: formwork-free robotic extrusion of a low-clinker '
                        'limestone-calcined-clay (LC3) mortar with an inline set accelerator, '
                        'inline rheometry and optical layer-width sensing. Not a tested or '
                        'specified system.',
                'meta': 'Rheology: Roussel (2018) DOI 10.1016/j.cemconres.2018.04.005 · Interlayer '
                        'bond f_t ≥ 1.8 MPa is a design assumption'},
 'sidenote_1': {'kicker': 'SIDENOTE E.10-A · CONTINUING FOLIO E.02 FROM PIPE FLOW TO FREE STANDING '
                          'WALL',
                'body': 'While Folio E.02 minimized τ_0 to reduce slickline pumping pressure, a '
                        'printed wall needs the opposite at rest. In the linear model, steady '
                        'printing needs A_thix > ρ g v_build / √3: about 5.5 Pa/s at 1.6 m/hr for '
                        'ρ = 2,200 kg/m³, or a maximum rate of about 0.25 m/hr at A_thix = 0.85 '
                        'Pa/s.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.10-B · COLD-JOINT GUARD (DESIGN ASSUMPTION)',
                'body': 'Layer cycle time t_cycle should stay below the time the surface stays '
                        'workable, here an assumed t_open = 18 min, to limit weak cold joints '
                        'between layers. The 18 min figure is illustrative, not from a standard.'},
 'skill': {'filename': '3dcp-roussel-thixotropy-buildability-SKILL.md',
           'name': '3dcp-roussel-thixotropy-buildability',
           'description': 'AI-agnostic additive civil engineering skill for 3D Concrete Printing '
                          '(3DCP) Roussel thixotropic structuration (tau_0(t) = tau_00 + A_thix * '
                          't), plastic yield collapse, and Suiker elastic wall buckling.',
           'rules': ['Evaluate static yield stress evolution tau_0(t) = tau_00 + A_thix * t and '
                     'require A_thix > (rho * g * v_build) / sqrt(3) to prevent bottom-layer '
                     'plastic collapse.',
                     'Remember that self-weight elastic buckling (Suiker 2018) also limits wall '
                     'height; this folio does not compute it, so its H_crit is the '
                     'plastic-collapse height H_plast only.',
                     'Verify interlayer cycle time t_cycle = L_perim / v_nozzle stays below open '
                     'time t_open to prevent interfacial cold joints.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Grounding pass 2026-11-14): The headline figures H_crit = 2.84 '
                           'm and SF = 1.68 did not follow from the folio\'s own plastic-collapse '
                           'formula and are withdrawn; with ρ = 2,200 kg/m³ the default mix yields '
                           'at about 0.04 m. Removed the "ACI 564R PASS" verdict and the ACI 564R '
                           'citation, unsourced 45%/6.4× savings figures, an invented 1997 opening '
                           'scene and an unrelated catalysis reference; the mucus bridge is now a '
                           'stated analogy. A later review renamed the base shear criterion to von '
                           'Mises (ρgH/√3; a Tresca criterion would give ρgH/2) and removed the '
                           'buckling-height formula, which was not computed and was not '
                           'dimensionally consistent as defined.',
                'opus': 'Review: all DOIs checked against Crossref and the Scite index on '
                        '2026-11-14; plastic-collapse arithmetic recomputed by hand.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V additive civil construction '
                           "monograph continuing Folio E.02 & A.01 via Nicolas Roussel's 3DCP "
                           'thixotropic structuration (DOI 10.1016/j.cemconres.2018.04.005) and '
                           'Suiker elastic buckling laws.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Reviewed '
                        'von Mises base shear rho*g*H/sqrt(3) vs. Roussel A_thix build-up rate and '
                        'Suiker buckling scaling. The word "Verified" is withdrawn in REV '
                        '1.1: the published 2.84 m / SF 1.68 figures did not follow from the '
                        'formula.'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.cemconres.2018.04.005',
           'fetched_on': '2026-11-08',
           'citing_publications': 1283,
           'supporting': 4,
           'mentioning': 532,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Roussel 2018 (DOI 10.1016/j.cemconres.2018.04.005), '
                      'fetched 2026-11-08: 1,283 citing publications (4 supporting, 532 '
                      'mentioning, 0 contrasting) and no retraction notice. These counts describe '
                      'that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['E.02', 'A.01'],
 'lineage_mode': 'CONTINUATION · Continues E.02 Herschel–Bulkley Pumping & A.01 Funicular Shell '
                 'Geometry',
 'scite': {'doi': '10.1016/j.cemconres.2018.04.005',
           'fetched_on': '2026-11-08',
           'citing_publications': 1283,
           'supporting': 4,
           'mentioning': 532,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Roussel 2018 (DOI 10.1016/j.cemconres.2018.04.005), '
                      'fetched 2026-11-08: 1,283 citing publications (4 supporting, 532 '
                      'mentioning, 0 contrasting) and no retraction notice. These counts describe '
                      'that one paper, not this folio.'},
 'act1_title': 'Act I — Continuing Folio E.02 & A.01: When Pumped Concrete Leaves the Pipe Without '
               'Formwork',
 'act1_dropcap': 'At the University of Southern California, Behrokh Khoshnevis developed Contour '
                 'Crafting, a computer-controlled process that extrudes cementitious material layer '
                 'by layer to build walls without conventional formwork; he described it in '
                 'Automation in Construction in 2004 (Khoshnevis 2004). Pumping mortar through '
                 'hoses was long-standing practice, but asking fresh paste to hold its own shape the '
                 'moment it leaves the nozzle raises a rheological puzzle. If the cement is fluid '
                 'enough to flow '
                 'through narrow pumps without jamming, what invisible physical mechanism allowed '
                 'it to stiffen within seconds on the print bed to support the weight of '
                 'subsequent layers?',
 'act1_plain_bridge': 'In plain words, three-dimensional concrete printing is like using an '
                      'industrial hot glue gun the size of a construction crane. In traditional '
                      'construction, building a concrete wall requires building a wooden or steel '
                      'mold first, pouring wet concrete inside, waiting days for it to harden, and '
                      'then tearing the wood away. One recent study puts formwork at about a '
                      'quarter of the cost of a concrete structure on average (Bašková et al. '
                      '2023), and it generates timber waste. Robotic printing eliminates the '
                      'mold entirely by squeezing fresh mortar through a robotic nozzle layer upon '
                      'layer. But this creates a delicate balancing act. Inside the delivery hose, '
                      'the mortar must flow smoothly like toothpaste so the pump does not jam. The '
                      'instant it lands on the wall, it must stiffen like setting clay so it does '
                      'not squash outward or buckle under the weight of fifty layers stacked above '
                      'it. Robotic toolpaths control printing speed and can place material only '
                      'where it is needed, which may save cement in curved walls.',
 'act1_body': 'Traditional cast-in-place concrete construction depends on timber and steel '
              'formwork, a substantial share of structural cost (about a quarter on average in '
              'one recent study, Bašková et al. 2023). In 2018, Nicolas Roussel (Cement and '
              'Concrete Research, DOI 10.1016/j.cemconres.2018.04.005) set out rheological '
              'requirements for printable concretes, and A. S. J. Suiker (International Journal of '
              'Mechanical Sciences, DOI 10.1016/j.ijmecsci.2018.01.010) analysed the mechanical '
              'failure of printed walls by plastic collapse and elastic buckling. Fresh mortar must '
              'maintain low '
              'dynamic yield stress while subjected to high shear inside the pump slickline, yet '
              'undergo rapid reversible thixotropic structuration the moment it exits the '
              'extrusion nozzle. As the robotic printhead deposits successive layers, the growing '
              'wall faces two competing failure modes: plastic collapse of the bottom layer when '
              'self-weight gravity shear exceeds the evolving static yield stress, and global '
              'elastic buckling when slender wall height exceeds the Suiker stability limit. '
              'Linking set-accelerator dosing to vertical print speed is one way engineers try to '
              'stay inside that window.',
 'act1_stakes': 'The real-world stakes of 3D concrete printing extend across urban affordability, '
                'material sustainability, and structural safety. If an operator misjudges the '
                'setting kinetics of a printable mortar, the consequences on the job site are '
                'immediate. Extruding material too quickly causes the fresh bottom layers to yield '
                'under the accumulating weight, bulging outward in a sudden plastic collapse that '
                'ruins the entire component. Conversely, printing too slowly allows the top '
                'surface of the preceding layer to dry and form an inert skin before the next bead '
                'arrives, producing an unbonded cold joint that splits apart under shear loads. '
                'Beyond structural collapse, a larger hope for additive manufacturing is lower '
                'carbon: depositing concrete only where stresses require it could reduce the '
                'cement used, though this folio does not quantify the saving. Getting there needs '
                'close coordination between robot motion and the changing rheology of hydrating '
                'cement.',
 'pullquote': '"Robotic 3D concrete printing lives inside a narrow rheological window: fluid '
              'enough inside the nozzle to extrude without tearing, yet stiffening fast enough on '
              'the bed to carry the layers above it without collapse or buckling."',
 'chronology': [('2004',
                 'Behrokh Khoshnevis describes Contour Crafting, robotic extrusion for automated '
                 'construction, in Automation in Construction (DOI 10.1016/j.autcon.2003.08.012).'),
                ('2012',
                 'Roussel, Ovarlez, Garrault and Brumaud examine the origins of thixotropy in '
                 'fresh cement pastes (DOI 10.1016/j.cemconres.2011.09.004).'),
                ('2018',
                 'Roussel sets out rheological requirements for printable concretes in Cement '
                 'and Concrete Research (DOI 10.1016/j.cemconres.2018.04.005); Suiker analyses '
                 'printed-wall collapse and buckling (DOI 10.1016/j.ijmecsci.2018.01.010).'),
                ('2026',
                 'This folio proposes closed-loop accelerator dosing tied to inline rheometry and '
                 'buckling checks (a design idea, not a deployed system).')],
 'act2_title': 'Act II — How It Actually Works: Roussel Thixotropic Structuration vs. Plastic '
               'Collapse & Elastic Buckling',
 'act2_analogy': 'Everyday analogy: Imagine decorating a tall birthday cake with butter frosting. '
                 'If the frosting is too soft and warm when piped from the bag, the bottom tier '
                 'squashes into a messy bulge under the weight above. If you stack narrow wafer '
                 'cookies too high, the tower stays stiff but suddenly sways and folds sideways. '
                 'Thixotropy is the secret stiffness that allows the frosting to flow easily '
                 'through the nozzle, yet firm up within seconds of landing on the cake.',
 'act2_plain_primer': 'To explore the physical boundaries of 3D concrete printing, our interactive '
                      'simulation provides two primary controls. The first control is the '
                      'Thixotropic Structuration Rate, which dictates how quickly the fresh mortar '
                      'stiffens after leaving the nozzle. At low rates, the material remains soft '
                      'and vulnerable to being crushed by the weight of upper layers. Sliding this '
                      'rate higher accelerates the formation of microscopic chemical bonds, '
                      "rapidly boosting the bottom layer's load capacity. The second control is "
                      'the Robotic Vertical Build Rate, which sets how fast the printer climbs as '
                      'it deposits successive layers. Printing at high vertical speeds tests the '
                      "material's limits: if the gantry stacks fresh layers faster than the bottom "
                      'can gain strength, the wall fails through either plastic crushing or '
                      'elastic buckling. Adjusting both sliders reveals the printable operating '
                      'window where the wall rises steadily and remains upright without forms.',
 'distill_diagram': {'analogy_title': 'Piping Frosting on a Layer Cake',
                     'analogy_sub': 'Material must flow under nozzle pressure yet stand tall when '
                                    'placed',
                     'force_a_title': 'Thixotropic Structuration (A_thix)',
                     'force_a_sub': 'Rate at which resting mortar rebuilds internal static yield '
                                    'stress',
                     'force_b_title': 'Vertical Build Rate (v_build)',
                     'force_b_sub': 'Rate at which accumulating self-weight adds gravity shear to '
                                    'base',
                     'threshold_title': 'Suiker Elastic Buckling vs. Plastic Collapse',
                     'threshold_pass': 'Printable: Bottom layer resists shear while wall avoids '
                                       'buckling',
                     'threshold_fail': 'Failure: Base layer squashes flat or slender wall folds '
                                       'sideways'},
 'act2_intuition': 'In robotic 3D concrete printing, an extrusion nozzle deposits a filament of '
                   'width b at a vertical build rate v_build. At time t following the placement of '
                   'the first layer, accumulated wall height reaches H(t) = v_build t, generating '
                   'a vertical gravity stress at the base sigma_v(t) = rho g H(t) and a '
                   'corresponding von Mises shear stress tau_bottom(t) = rho g v_build t / sqrt(3). '
                   'To prevent bottom-layer plastic collapse, rest-state colloidal flocculation '
                   "must increase static yield stress according to Nicolas Roussel's linear "
                   'thixotropic law tau_0(t) = tau_{0,0} + A_thix t. Plastic stability requires '
                   'A_thix > rho g v_build / sqrt(3). However, satisfying yield capacity does not '
                   'guarantee stability: slender unsupported walls can also fail by self-weight '
                   'elastic buckling, which Suiker (2018) analysed and which also limits height; '
                   'it is not computed on this page. The critical buildable height is the smaller '
                   'of the plastic and buckling limits, and this page computes only the plastic '
                   'one. Worked example (this folio\'s numbers, ρ = 2,200 '
                   'kg/m³ assumed): at v_build = 1.6 m/hr gravity shear grows at 21,582 x 4.44e-4 / '
                   '1.732 = 5.5 Pa/s, far above A_thix = 0.85 Pa/s, so τ_{0,0} = 420 Pa is used up '
                   'after 420 / (5.5 - 0.85) = 90 s and the base yields at H ≈ 0.04 m. Even at the '
                   "slider limits (A_thix = 2.0 Pa/s, v_build = 0.6 m/hr) the model's plastic limit "
                   'is about 0.9 m. Real mixes and the full Roussel and Suiker analyses include '
                   'effects this simple linear model leaves out.',
 'act2_deepening': 'At the nanoscale level, thixotropic structuration arises from reversible '
                   'physical coagulation between cement particles. Inside the delivery hose, high '
                   'shear rates overcome interparticle van der Waals attraction, breaking '
                   'colloidal clusters and aligning hydrate grains to create a low-viscosity '
                   'lubrication layer along the pipe boundary. The instant shear ceases upon '
                   'deposition, colloidal particles re-flocculate within seconds, forming an '
                   'initial physical percolation network that establishes static yield stress '
                   'tau_{0,0}. Over subsequent minutes, early chemical hydration nucleates '
                   'ettringite and calcium-silicate-hydrate (C-S-H) bridges at particle contact '
                   'points, which the model approximates as linear structuration at rate A_thix. '
                   'That linear law describes short times; over longer times later work reports '
                   'faster, roughly exponential strength growth. Toolpath geometry also matters '
                   'for buckling: a corrugated or curved wall has a larger second moment of area '
                   'I than a flat wall of the same material volume, which raises the Suiker '
                   'buckling height. How large the gain is depends on the geometry; this folio '
                   'does not compute it.',
 'walkthrough': ['Experiment 1 (Thixotropic Structuration Rate A_thix): Drag Thixotropic Build-Up '
                 'Rate A_thix from 0.25 Pa/s up to 1.80 Pa/s. Watch bottom-layer yield capacity '
                 'tau_0(t) overtake gravity shear stress rho*g*H/sqrt(3) and lift critical '
                 'buildable height H_crit.',
                 'Experiment 2 (Robotic Vertical Build Velocity v_build): Increase Vertical Print '
                 'Rate v_build from 0.8 m/hr to 3.6 m/hr. Watch gravity shear outpace structuration '
                 'and the plastic-collapse height fall. (In the linear model of this folio, with ρ = '
                 '2,200 kg/m³, no slider setting allows steady unlimited printing.)',
                 'Experiment 3 (From E.02 Pipe Shear to Formwork-Free Shell): Step through Stages '
                 '1 to 4 to trace nozzle shear rejuvenation, colloidal C-S-H flocculation, plastic '
                 'vs. buckling bifurcation, and funicular corrugation stiffening.'],
 'act4_title': 'Act IV — Robotic Additive Construction, Archive Continuity & Upstream Discovery '
               'Threads',
 'act4_human_ai': "By combining Folio E.02's inline pump pressure telemetry with Folio A.01's "
                  "funicular corrugation geometry and Roussel's A_thix structuration model, "
                  'printers could in principle adjust accelerator dosing in real time to print '
                  'ribbed shells with less cement. This is a proposal; the folio does not '
                  'quantify the saving.',
 'act4_deepening': 'One direction for additive construction is closed-loop printing, where '
                   'software coordinates material chemistry and robot motion as the print goes. '
                   'Printheads could carry laser profilers and inline sensors to measure filament '
                   'geometry and stiffness soon after deposition; if a temperature rise sped up '
                   'hydration, a controller could change travel speed or retarder dosing to avoid '
                   'cold joints. Topology optimization could also be combined with funicular '
                   'toolpath planning to design hollow, self-bracing columns that use less material '
                   'than solid walls. These are research directions, not practices this folio '
                   'sources. Key open research questions include long-term durability '
                   'under environmental freeze-thaw cycles, automating the continuous placement of '
                   'high-tensile reinforcement within printed filaments, and establishing '
                   'international structural testing standards for formwork-free additive '
                   'construction. Pairing computational rheology with robotics could make '
                   'lower-carbon, freer architectural forms practical.',
 'cf_bridge': 'Standalone Additive Civil Construction Flagship & Thread Continuation (E.02 -> '
              'E.10): Written for civil, structural, and construction robotics engineers '
              'interested in 3D-printed concrete. A loose analogy, not a shared model: airway '
              'mucus is also a material whose structure breaks down under shear and rebuilds at '
              'rest (Folio E.03). Roussel\'s cement equation is not a model of mucus, and nothing '
              'in this folio is clinical information.',
 'sources': ['Roussel, N. (2018). Rheological requirements for printable concretes. Cement and '
             'Concrete Research, 112, 76–85. DOI: 10.1016/j.cemconres.2018.04.005.',
             'Suiker, A. S. J. (2018). Mechanical performance of wall structures in 3D printing '
             'processes: Theory, design tools and experiments. International Journal of Mechanical '
             'Sciences, 137, 145–170. DOI: 10.1016/j.ijmecsci.2018.01.010.',
             'Roussel, N., Ovarlez, G., Garrault, S., & Brumaud, C. (2012). The origins of '
             'thixotropy of fresh cement pastes. Cement and Concrete Research, 42(1), 148–157. '
             'DOI: 10.1016/j.cemconres.2011.09.004.',
             'Khoshnevis, B. (2004). Automated construction by contour crafting—related robotics '
             'and information technologies. Automation in Construction, 13(1), 5–19. DOI: '
             '10.1016/j.autcon.2003.08.012.',
             'Bašková, R., Tažiková, A., Struková, Z., Kozlovská, M., & Čabala, J. (2023). A '
             'dynamic model for effective and optimal planning of formwork in construction '
             'projects. Buildings, 13(7), 1794. DOI: 10.3390/buildings13071794.',
             'CSI MasterFormat, Section 03 30 00 Cast-in-Place Concrete (used here only as a '
             'filing label; no threshold in this folio comes from a standard).',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="3D Concrete '
        'Printing robotic extrusion layer stack and Roussel thixotropic structuration vs plastic '
        'collapse and elastic buckling diagram">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <g id="tp-e10-wall-stack" transform="translate(185, 188)">\n'
        '              <rect x="-55" y="-22" width="110" height="20" rx="8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <rect x="-52" y="-44" width="104" height="20" rx="8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <rect x="-50" y="-66" width="100" height="20" rx="8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <rect x="-48" y="-88" width="96" height="20" rx="8" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '              <rect x="-46" y="-110" width="92" height="20" rx="8" '
        'fill="var(--tp-verdigris)" fill-opacity="0.35" stroke="var(--tp-verdigris)" '
        'stroke-width="2"/>\n'
        '              <polygon points="-14,-142 14,-142 9,-112 -9,-112" '
        'fill="var(--tp-minium)"/>\n'
        '            </g>\n'
        '            <text x="52" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">3DCP Filament Stack &amp; Active Nozzle</text>\n'
        '            <text id="tp-e10-svg-wall-text" x="52" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Model at defaults: base yields at H ≈ 0.04 m</text>\n'
        '            <line x1="350" y1="24" x2="350" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="368" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Roussel Yield τ_0(t) vs. Gravity Shear &amp; Buckling</text>\n'
        '            <line id="tp-e10-thix-line" x1="380" y1="168" x2="625" y2="54" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <line id="tp-e10-grav-line" x1="380" y1="176" x2="625" y2="96" '
        'stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <path id="tp-e10-buck-curve" d="M 380 176 Q 510 140 625 68" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <circle id="tp-e10-op-dot" cx="515" cy="105" r="6" '
        'fill="var(--tp-verdigris)"/>\n'
        '            <text x="382" y="62" font-size="9.5" fill="var(--tp-verdigris)">Thixotropic '
        'Strength τ_0(t) = τ_{0,0} + A_thix t</text>\n'
        '            <text id="tp-e10-mode-text" x="382" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Needs A_thix &gt; ρgv/√3 ≈ 5.5 Pa/s (model, ρ = 2,200 kg/m³)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a robotic 3D concrete printing nozzle extruding a '
        'corrugated funicular mortar wall with Roussel thixotropic yield-stress contours and laser '
        'buildability telemetry would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.10-V (Imagining What It Would Look Like) · Artistic '
            'additive-construction visualization (continuing Folios E.02 & A.01) imagining a '
            'robotic 3DCP printhead extruding formwork-free corrugated concrete layers governed by '
            'Roussel thixotropic structuration and Suiker buckling stability.'}

DISPATCH = {'kicker': 'FRONTIER ADDITIVE CONSTRUCTION DISPATCH · CONTINUING E.02 & A.01 · 3D CONCRETE '
           'PRINTING',
 'headline': 'Roussel Thixotropic Structuration vs. Self-Weight: A Simple Model of '
             'Formwork-Free 3D Concrete Printing',
 'body': "Picking up from Folio E.02's Herschel–Bulkley slickline pumping and Folio A.01's "
         "funicular shells, this folio uses Nicolas Roussel's printability criterion (Cem. Concr. "
         "Res. DOI 10.1016/j.cemconres.2018.04.005) and Suiker's buckling analysis to show how "
         'yield build-up A_thix must outpace self-weight. At its default values the simple model '
         'predicts early plastic collapse.'}

META_3D = ('Roussel 3DCP Thixotropic Buildability & Buckling Surface',
 'X: Vertical Print Rate v_build · Z: Structuration A_thix · Y: Critical Buildable Height H_crit')

ES_TRANSLATION = {'title_es': 'Reología de Extrusión e Imprimibilidad en Impresión 3D de Concreto (3DCP): '
             'Estructuración Tixotrópica de Roussel, Pandeo Elástico vs. Colapso Plástico y '
             'Control Robótico',
 'subtitle_es': 'Continuando los Folios E.02 y A.01: cómo la tasa de estructuración tixotrópica '
                'A_thix de Nicolas Roussel y las leyes de pandeo de Suiker gobiernan la '
                'construcción robótica sin cimbra.',
 'why_es': 'Al decorar un pastel alto sin molde, si el betún está demasiado blando la base se '
           'aplasta por su propio peso (colapso plástico), y si la pared es muy esbelta se dobla '
           'de lado (pandeo elástico); la tixotropía mide qué tan rápido se endurece al salir de '
           'la boquilla.',
 'plain_es': 'En palabras sencillas, la impresión tridimensional de concreto funciona como una '
             'pistola gigante de silicón montada sobre un brazo robótico. En la construcción '
             'convencional, levantar un muro exige armar moldes de madera o acero, vaciar el '
             'concreto húmedo, esperar varios días a que endurezca y retirar la cimbra, lo cual '
             'genera enormes costos y desperdicio de madera. La impresión robótica elimina la '
             'cimbra por completo depositando cordones de mortero capa por capa. Sin embargo, esto '
             'plantea un reto físico extraordinario: dentro de las mangueras de bombeo, el '
             'material debe fluir suavemente como pasta de dientes para no atascar la máquina; '
             'pero en cuanto sale por la boquilla, debe endurecerse rápidamente como plastilina '
             'firme para soportar el peso de decenas de capas colocadas encima sin aplastarse ni '
             'ladearse. Ajustando la velocidad de impresión y la química del fraguado, los robots '
             'pueden levantar muros curvos y colocar material solo donde hace falta, lo que podría '
             'ahorrar cemento; este folio no cuantifica ese ahorro.',
 'deep_es': 'La viabilidad de la impresión 3D de concreto está gobernada por la competencia entre '
            'dos fenómenos mecánicos: la tasa de estructuración tixotrópica y la velocidad '
            'vertical de acumulación de carga. Conforme el robot deposita capas consecutivas, el '
            'peso propio genera un esfuerzo cortante que tiende a aplastar la base del muro. Si la '
            'tasa tixotrópica A_thix es insuficiente, ocurre un colapso plástico en el cordón '
            'inferior. Por otro lado, si la pared es muy esbelta, el sistema alcanza el límite '
            'crítico de pandeo elástico de Suiker y se dobla lateralmente. Para mantener la '
            'estabilidad hay que operar dentro de una ventana reológica donde la resistencia '
            'crezca más rápido que el esfuerzo cortante sin exceder el tiempo de unión entre '
            'capas. Con los valores de este folio (y una densidad supuesta de 2,200 kg/m³), el '
            'cortante por peso propio crece a 5.5 Pa/s frente a A_thix = 0.85 Pa/s, así que el '
            'modelo predice que la base cede a unos 0.04 m de altura. Este folio propone, sin '
            'haberlo probado, ajustar en tiempo real la dosificación de acelerantes con sensores '
            'en la boquilla.',
 'bridge_es': 'Solo una analogía, no un modelo común: el moco de las vías respiratorias también '
              'es un material cuya estructura se rompe con el cortante y se recupera en reposo '
              '(Folio E.03). La ecuación de Roussel para el cemento no modela el moco y nada en '
              'este folio es información clínica.'}
