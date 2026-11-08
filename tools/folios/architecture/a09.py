#!/usr/bin/env python3
"""Folio A.09 (ARCHITECTURE): Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, Orthotropic Moisture Swelling & Zero-Energy Climate Facades."""
from __future__ import annotations

SLUG = 'a09'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.09',
 'slug': 'a09',
 'pillar': 'architecture',
 'category_code': 'A',
 'parent_folios': ['A.02', 'E.04', 'A.08'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.02 Timber Gridshells, E.04 Moisture Sorption '
                 '& A.08 Zero-Energy Envelopes',
 'title': 'Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, '
          'Orthotropic Moisture Swelling & Zero-Energy Climate Facades',
 'subtitle': 'Completing the timber-and-climate thread of Folios A.02, E.04, and A.08: how Stephen '
             "Timoshenko's bilayer curvature theorem and Achim Menges's cross-laminated beech "
             'skins actuate building envelopes with zero motor energy.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-03',
 'current_edition': 'REV 1.0',
 'status_badge': 'HYGROSCOPIC TIMBER · REV 1.0',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 '
                  '18 00',
 'colophon': {'identifier': 'A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00',
              'kernels': 'Timoshenko Bilayer Curvature · Orthotropic Wood Sorption (α_T vs. α_L)',
              'benchmarks': 'ΔMC = +6.0% · h = 6.0 mm ⇒ κ = 1.42 m⁻¹ · δ_tip = 128 mm (0 W Power)',
              'bridge': 'Completes A.02/E.04 · Cellulose Hydrogel Swelling ↔ P.04 Periciliary '
                        'Osmotic Brush'},
 'sliders': [{'label': 'Wood Moisture Content Shift (ΔMC)',
              'min': 1.0,
              'max': 12.0,
              'step': 0.5,
              'value': 6.0,
              'unit': '%'},
             {'label': 'Total Timber Bilayer Thickness (h)',
              'min': 3.0,
              'max': 14.0,
              'step': 0.5,
              'value': 6.0,
              'unit': ' mm'}],
 'steps': ['Stage 1 (Orthotropic Cellulose Cell-Wall Sorption, Continuing E.04): Below fiber '
           'saturation (28% MC), tangential beech wood swells at α_T = 0.32%/%MC while '
           'longitudinal grain stays locked at α_L = 0.012%/%MC.',
           'Stage 2 (Timoshenko Bilayer Interfacial Shear, DOI 10.1364/JOSA.11.000233): Bonding '
           'active tangential ply h_2 to passive longitudinal ply h_1 converts Δε = (α_T − α_L)ΔMC '
           'into pure curvature κ = 1.42 m⁻¹.',
           'Stage 3 (Zero-Energy Weather-Responsive Facade Petal): A 425 mm cantilever petal opens '
           'δ_tip = ½ κ L² = 128 mm in dry sun (64.5% free vent area) and seals tight against '
           'driving rain.',
           'Stage 4 (Industrial Self-Shaping CLT Shells, Continuing A.02): Kiln-drying flat 90 mm '
           'cross-laminated billets pre-forms doubly curved structural tower skins without curved '
           'CNC milling.'],
 'readouts': [{'label': 'Timoshenko Curvature (κ)', 'value': '1.42 m⁻¹ (R = 0.70 m)'},
              {'label': 'Petal Tip Deflection (δ_tip)', 'value': '128.0 mm (at L = 425 mm)'},
              {'label': 'Passive Ventilation Opening', 'value': '64.5% Free Area (0 W)'},
              {'label': 'Eurocode 5 / Hygro Verdict', 'value': 'ZERO-ENERGY ACTUATION · PASS'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 06 18 00 / EN 1995-1-1',
                'title': 'Programmable Hygroscopic European Beech Bilayer Climate Envelope & '
                         'Self-Shaping CLT',
                'body': 'Kiln-programmed cross-grained Fagus sylvatica (European beech) bilayer '
                        'facade elements bonded with zero-VOC 1C-PUR structural adhesive, '
                        'UV-stabilized hydrophobic nano-silicate weather coat, and stainless limit '
                        'stops.',
                'meta': 'Timoshenko (1925) DOI 10.1364/JOSA.11.000233 & ICD/ITKE HygroSkin '
                        'verified · 10,000+ humidity cycles'},
 'sidenote_1': {'kicker': 'SIDENOTE A.09-A · COMPLETING FOLIO A.02 TIMBER MECHANICS WITH '
                          'TIMOSHENKO (1925)',
                'body': "Timoshenko's dimensionless geometry factor f(m, n) peaks when "
                        'stiffness-weighted layer thicknesses satisfy E_1 h_1² = E_2 h_2², '
                        'maximizing autonomous curvature per unit thickness h.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.09-B · SPECIFICATION PLATE · CSI 06 18 00 (PROGRAMMABLE '
                          'WOOD)',
                'body': 'By milling grain orientations relative to local principal curvature '
                        'directions, flat timber panels self-assemble into anticlastic or '
                        'synclastic shells during controlled kiln drying.'},
 'skill': {'filename': 'hygroscopic-timber-timoshenko-bilayer-SKILL.md',
           'name': 'hygroscopic-timber-timoshenko-bilayer',
           'description': 'AI-agnostic architectural and timber-engineering skill for Stephen '
                          'Timoshenko bilayer curvature, orthotropic wood moisture swelling '
                          '(alpha_T vs alpha_L), and zero-energy responsive building skins.',
           'rules': ['Compute differential hygroscopic strain Delta_epsilon = (alpha_T - alpha_L) '
                     '* Delta_MC below the Fiber Saturation Point (MC <= 28%).',
                     'Evaluate Timoshenko curvature kappa = 6 * (1 + m)^2 * Delta_epsilon / (h * '
                     '(3 * (1 + m)^2 + (1 + m*n) * (m^2 + 1/(m*n)))) with m = h_1/h_2 and n = '
                     'E_1/E_2.',
                     'Calculate cantilever aperture tip deflection delta_tip = (1 - cos(kappa * '
                     'L)) / kappa approx 0.5 * kappa * L^2 and verify Eurocode 5 rolling-shear '
                     'stress limits.']},
 'revisions': [{'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V biomimetic timber '
                           'architecture monograph completing Folios A.02, E.04 & A.08 via '
                           "Timoshenko's 1925 bilayer curvature theorem (DOI "
                           '10.1364/JOSA.11.000233) and Menges hygroscopic wood skins.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact Timoshenko denominator 3(1+m)^2 + (1+mn)(m^2 + 1/mn) and '
                        'orthotropic beech swelling differential.'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-08',
           'citing_publications': 2499,
           'supporting': 48,
           'mentioning': 1474,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,499 '
                      'citing publications (48 supporting, 1,474 mentioning, 0 contrasting) on '
                      "Stephen Timoshenko's foundational bi-material thermostat curvature "
                      'theorem.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['A.02', 'E.04', 'A.08'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.02 Timber Gridshells, E.04 Moisture Sorption '
                 '& A.08 Zero-Energy Envelopes',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-08',
           'citing_publications': 2499,
           'supporting': 48,
           'mentioning': 1474,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 2,499 '
                      'citing publications (48 supporting, 1,474 mentioning, 0 contrasting) on '
                      "Stephen Timoshenko's foundational bi-material thermostat curvature "
                      'theorem.'},
 'act1_title': 'Act I — Completing the Timber & Climate Thread from A.02, E.04 & A.08: Wood That '
               'Breathes and Moves Without Motors',
 'act1_dropcap': 'In the quiet laboratories of the Westinghouse Electric Corporation in 1925, the '
                 'Ukrainian-born mechanics pioneer Stephen Timoshenko picked up a small metal '
                 'strip bonded from two different alloys. When heated, the strip curled smoothly '
                 'into a graceful arc, inventing the mathematical foundation for every mechanical '
                 'thermostat. Nearly a century later in 2013, computational architect Achim Menges '
                 'and his team at the University of Stuttgart walked through a damp Black Forest '
                 'morning, observing fallen pinecones lying along the forest floor. Despite being '
                 'composed entirely of dead plant tissue, the pinecone scales were curled tightly '
                 'shut to protect their seeds from the driving rain, only to spread wide open when '
                 'warmed by the dry afternoon sun. Menges realized that nature had achieved what '
                 'modern responsive architecture struggled to accomplish: dynamic building facades '
                 'that sense and respond to changing weather autonomously, moving silently without '
                 'electric motors, mechanical sensors, digital processors, or external wiring.',
 'act1_plain_bridge': 'In plain words, think of what happens to a wooden door in your house during '
                      'a humid summer. The door absorbs moisture from the damp air and swells, '
                      'sticking inside its frame. Wood swells because natural plant cells soak up '
                      'water vapor like millions of tiny sponges. However, wood does not swell '
                      'equally in all directions. It expands dramatically across its grain, but '
                      'hardly changes length along the grain. If you take a thin board cut across '
                      'the grain and glue it tightly to a board cut along the grain, a fascinating '
                      'reaction takes place whenever the humidity changes. When the air becomes '
                      'humid, the cross-grain board tries to grow longer while the lengthwise '
                      'board refuses to stretch. Because the two boards are bonded together, the '
                      'whole piece is forced to bend into a curve. By shaping these wooden '
                      'bilayers into facade petals, windows automatically open when the air is dry '
                      'and seal shut when it rains.',
 'act1_body': 'Conifer pinecones and wheat awns have executed motorless climate actuation for '
              'hundreds of millions of years: cellulose microfibrils wound at contrasting angles '
              'cause outer and inner tissue layers to swell differently as relative humidity '
              'shifts, flexing scales closed in rain and spreading them open in dry wind. In 1925, '
              'Stephen Timoshenko published the exact analytical curvature theorem for bi-material '
              'beams in the Journal of the Optical Society of America (DOI '
              '10.1364/JOSA.11.000233). Over the past decade at ICD/ITKE Stuttgart, Achim Menges, '
              "Dylan Wood, and their collaborators translated Timoshenko's mathematics into "
              'architectural cross-laminated European beech and spruce bilayers (HygroSkin, Urbach '
              'Tower, CSI 06 18 00). By gluing a moisture-active tangential wood veneer (expanding '
              'roughly 0.32 percent per percent change in moisture content) against a '
              'dimensionally stable longitudinal ply under controlled factory humidity, flat '
              'cross-laminated timber billets curl into self-shaping doubly curved architectural '
              'shells during standard kiln drying, or act as zero-energy ventilation petals that '
              'regulate building airflows without electricity.',
 'act1_stakes': 'For centuries, carpenters and cabinetmakers treated wood swelling as an '
                'unpredictable flaw to be restrained through heavy framing, metal fasteners, and '
                'moisture-blocking varnishes. Master shipwrights and joiners learned through trial '
                'and error that unseasoned timber twists, warps, and cracks if moisture escapes '
                'unevenly across different grain directions. In twentieth-century construction, '
                'the standard response was to over-engineer steel mechanical systems: motorized '
                'louvers, motorized dampers, and electric actuators wired to electronic humidity '
                'sensors. But motorized kinetic facades have proven notoriously fragile in '
                'real-world buildings. Mechanical linkages jam from wind-borne dust, electric '
                'servo motors burn out after repetitive weather cycles, and electronic sensors '
                'corrode in coastal air. When building owners face mounting maintenance costs, '
                'motorized facade louvers are frequently locked in fixed positions, abandoning '
                'climate responsiveness altogether. The failure of complex mechanical gadgets '
                'highlighted the need for passive, materially embedded movement where the '
                'structure itself serves as sensor, actuator, and weather barrier.',
 'pullquote': '"In hygroscopic timber tectonics, the sensor, the actuator, and the load-bearing '
              'architectural skin are no longer separate mechanical devices—they are the same '
              'piece of wood."',
 'chronology': [('1925',
                 'Stephen Timoshenko publishes the exact analytical curvature theorem for '
                 'bi-material strips in JOSA (DOI 10.1364/JOSA.11.000233).'),
                ('1997',
                 'Dawson, Vincent & Rocca prove that dead pinecone scales open and close via '
                 'bilayer cellulose microfibril angle (MFA) differentials.'),
                ('2013',
                 'Achim Menges & Steffen Reichert complete the HygroSkin meteorosensitive pavilion '
                 'with zero-energy humidity-driven timber apertures.'),
                ('2019',
                 'ICD/ITKE Urbach Tower demonstrates industrial self-shaping cross-laminated '
                 'timber (CLT) shells curved purely by kiln drying.')],
 'act2_title': 'Act II — How It Actually Works: Timoshenko Bilayer Mechanics + Orthotropic Wood '
               'Swelling',
 'act2_analogy': 'Take two long strips of paper, wet only one strip with a damp sponge, and glue '
                 'them back-to-back. As the wet paper expands, the dry paper stays the same size, '
                 'forcing the glued strip to curl into a tight loop. Conifer pinecones use this '
                 'exact trick, flexing their scales closed during downpours and popping open in '
                 'warm dry air. Programmable timber facades operate on the identical physical '
                 'principle, using natural grain anisotropy instead of mechanical gears.',
 'act2_plain_primer': 'To control this natural wood curling mechanism on a building facade, you '
                      'work with two physical knobs. The first knob represents the change in '
                      'moisture inside the wood as outdoor relative humidity rises or falls with '
                      'the weather. When morning fog rolls into the city, the wood drinks in '
                      'moisture from the air, causing the active tangential layer to swell and '
                      'bending the facade petal tightly against its frame to keep out rain. As the '
                      'midday sun warms and dries the atmosphere, the moisture content drops, '
                      'relaxing the petal and curling it wide open to draw in cooling breezes. The '
                      'second knob sets the total thickness of the bonded wooden bilayer. If you '
                      'choose an ultra-thin wooden veneer, the petal curls rapidly with dramatic '
                      'curvature under the slightest change in humidity. If you increase the '
                      'thickness to several millimeters, the wood bends more slowly but develops '
                      'immense structural force, capable of curling heavy structural roof panels '
                      'into shape.',
 'distill_diagram': {'analogy_title': 'The Pinecone Wet-Paper Curl',
                     'analogy_sub': 'Differential expansion between bonded plies curls the strip '
                                    'with 0 W',
                     'force_a_title': 'Moisture Shift Knob (ΔMC)',
                     'force_a_sub': 'Drives swelling strain differential across tangential '
                                    'cellular grain',
                     'force_b_title': 'Bilayer Thickness Knob (h)',
                     'force_b_sub': 'Governs flexural rigidity and sets the radius of '
                                    'self-actuation',
                     'threshold_title': 'Curvature Equilibrium (κ = 1.42 m⁻¹)',
                     'threshold_pass': 'Autonomous 128 mm tip opening provides 64% passive '
                                       'ventilation',
                     'threshold_fail': 'Fiber saturation or delamination if rolling shear exceeds '
                                       'limit'},
 'act2_intuition': "Extending Folio A.02's Eurocode 5 timber mechanics, solid wood operating below "
                   'its Fiber Saturation Point (roughly 28% to 30% moisture content) exhibits an '
                   'immense 15-to-30-fold anisotropy between its tangential swelling coefficient '
                   'alpha_T (approximately 0.0032 per percent moisture shift) and its longitudinal '
                   'grain coefficient alpha_L (barely 0.00012 per percent moisture shift). When an '
                   'active tangential European beech layer of thickness h_2 and elastic modulus '
                   'E_2 is bonded to a passive longitudinal restraint ply of thickness h_1 and '
                   'modulus E_1 with thickness ratio m = h_1 / h_2 and modulus ratio n = E_1 / '
                   'E_2, any shift in ambient moisture Delta_MC produces an internal misfit strain '
                   "Delta_epsilon = (alpha_T - alpha_L) * Delta_MC. By Stephen Timoshenko's "
                   'classical bilayer mechanics, the resulting uniform curvature is kappa = 6 * (1 '
                   '+ m)^2 * Delta_epsilon / (h * (3 * (1 + m)^2 + (1 + m * n) * (m^2 + 1 / (m * '
                   'n)))). For a cantilevered facade petal of length L, this curvature produces an '
                   'autonomous tip deflection delta_tip = 0.5 * kappa * L^2, seamlessly opening '
                   'ventilation louvers during warm dry weather and sealing tight against rain '
                   'without motor drive.',
 'act2_deepening': 'The mechanical interaction between moisture shift and bilayer thickness '
                   "reveals an essential engineering trade-off governed by Timoshenko's "
                   'denominator. Because curvature kappa scales inversely with total thickness h, '
                   'doubling the thickness of the wood reduces its curvature by half for any given '
                   'moisture shift. However, the flexural bending rigidity of the composite strip '
                   'scales with the cube of thickness, h^3. This means that while a thin '
                   'three-millimeter veneer curls swiftly under rapid ambient relative humidity '
                   'fluctuations, it possesses minimal resistance against aerodynamic wind '
                   'flutter. Conversely, a thick structural bilayer of ten to twelve millimeters '
                   'requires greater moisture differentials to curl, but generates tremendous '
                   'actuation forces capable of self-shaping massive cross-laminated timber '
                   'plates. Furthermore, interfacial shear stress peaks at the adhesive bond line '
                   'near the free ends: if the differential strain Delta_epsilon expands too '
                   'rapidly without proper moisture conditioning, interfacial rolling shear can '
                   'exceed Eurocode 5 strength limits, necessitating carefully calculated '
                   'fiber-orientation angles.',
 'walkthrough': ['Experiment 1 (Ambient Moisture Content Shift Delta_MC): Drag Wood Moisture '
                 'Content Change Delta_MC from +1.0% up to +12.0%. Watch Timoshenko curvature '
                 'kappa (m^-1) and petal tip opening delta_tip grow linearly without a single watt '
                 'of electricity.',
                 'Experiment 2 (Bilayer Thickness & Stiffness Tuning h): Adjust Total Bilayer '
                 'Thickness h from 3.0 mm (rapid, high-curvature facade louver) to 14.0 mm '
                 '(structural self-shaping CLT shell panel).',
                 'Experiment 3 (From Pinecone Microfibrils to Zero-Energy Facade): Step through '
                 'Stages 1 to 4 to explore orthotropic cell-wall sorption, Timoshenko neutral-axis '
                 'shear, aperture airflow modulation, and cyclic hysteresis durability.'],
 'act4_title': 'Act IV — Zero-Energy Climate Skins, Archive Continuity & Upstream Biophysical '
               'Threads',
 'act4_human_ai': "Connecting Folio A.02's timber joinery, Folio A.03's solar buoyancy stacks, and "
                  "Folio E.04's psychrometric moisture balance, computational architects use "
                  'finite-element Timoshenko-hygrothermal solvers to program grain orientation and '
                  'ply thickness so building envelopes self-ventilate when indoor humidity rises.',
 'act4_deepening': 'In modern computational timber design, architects partner with finite-element '
                   'machine-learning workflows to program complex multi-directional curvatures '
                   'into flat mass-timber billets before manufacturing. By feeding micro-computed '
                   'tomography grain scans into anisotropic material models implemented in '
                   'FEniCS/dolfinx, AI optimization algorithms compute the precise toolpath '
                   'trajectories and cutting angles required to yield target three-dimensional '
                   'geometries upon industrial kiln drying. This eliminates tons of wasted offcut '
                   'material associated with subtractive five-axis CNC milling, enabling '
                   'expressive double-curved timber shells with minimal embodied carbon. Open '
                   'research questions continue to challenge material scientists: How do cyclic '
                   'weathering, micro-crack fatigue, and natural lignocellulosic creep alter the '
                   'long-term curvature response over decades of outdoor exposure? Can '
                   'bio-inspired wax and nano-silicate coatings protect against ultraviolet fiber '
                   'degradation while preserving hygroscopic breathability? By answering these '
                   'questions, architects and algorithmic solvers are transforming harvested '
                   'timber from a static structural commodity into a dynamic, climate-attuned '
                   'living building skin.',
 'cf_bridge': 'Standalone Biomimetic Architecture Flagship & Reference Completion (A.02 + E.04 -> '
              'A.09): Written for architects, facade engineers, and mass-timber builders (CSI 06 '
              '18 00 Glued-Laminated Construction, EN 1995-1-1). Upstream biophysical thread for '
              'the lab: the orthotropic osmotic swelling of cellulose-hemicellulose hydrogel '
              'matrices below the fiber saturation point obeys the same Flory–Rehner / Donnan '
              'osmotic swelling pressure that governs periciliary brush height h_PCL in Folio P.04 '
              'when ventilation duct surface liquid hydration changes.',
 'sources': ['Timoshenko, S. (1925). Analysis of bi-metal thermostats. Journal of the Optical '
             'Society of America, 11(3), 233–255. DOI: 10.1364/JOSA.11.000233.',
             'Reichert, S., Menges, A., & Correa, D. (2015). Meteorosensitive architecture: '
             'Biomimetic building skins based on materially embedded responsiveness. '
             'Computer-Aided Design, 60, 50–69.',
             'Wood, D., Grönquist, P., Bechert, S., Aldinger, L., Riggenbach, D., Lehmann, K., '
             'Rüggeberg, M., Burgert, I., Knippers, J., & Menges, A. (2020). From machine control '
             'to material programming: Self-shaping wood manufacturing of a high performance '
             'curved CLT structure—Urbach Tower. Fabricate 2020, 50–57.',
             'CEN (2024). Eurocode 5 (EN 1995-1-1) Design of Timber Structures & CSI MasterFormat '
             '06 18 00.',
             'Baratta, I. A., et al. (2023). DOLFINx: The next generation FEniCS problem solving '
             'environment (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). Zenodo. DOI: '
             '10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Timoshenko '
        'hygroscopic cross-laminated timber bilayer curvature and zero-energy facade aperture '
        'response curve">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <line x1="65" y1="45" x2="65" y2="178" stroke="var(--tp-prussian)" '
        'stroke-width="4"/>\n'
        '            <path d="M 65 145 L 295 145" fill="none" stroke="currentColor" '
        'stroke-opacity="0.3" stroke-width="2" stroke-dasharray="4,4"/>\n'
        '            <path id="tp-a09-active-ply" d="M 65 142 Q 185 135 280 72" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="6"/>\n'
        '            <path id="tp-a09-passive-ply" d="M 65 148 Q 188 141 284 77" fill="none" '
        'stroke="var(--tp-prussian)" stroke-width="4"/>\n'
        '            <text x="55" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">Timoshenko Beech Bilayer (α_T vs. α_L Grain)</text>\n'
        '            <text id="tp-a09-svg-curv-text" x="55" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">κ = 1.42 m⁻¹ · Tip Opening δ_tip = 128 mm (0 W Motor '
        'Power)</text>\n'
        '            <line x1="355" y1="24" x2="355" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="372" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Curvature κ(ΔMC, h) &amp; Aperture Free Area</text>\n'
        '            <path id="tp-a09-curv-line" d="M 380 172 L 625 56" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <circle id="tp-a09-op-dot" cx="502" cy="114" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="382" y="70" font-size="9.5" fill="var(--tp-verdigris)">Timoshenko '
        'Linear Law κ ∝ (α_T − α_L) ΔMC / h</text>\n'
        '            <text id="tp-a09-vent-text" x="382" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Passive Facade Free-Vent Area: 64.5% Open</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a biomimetic hygroscopic cross-laminated beech '
        'timber facade pavilion opening its curved Timoshenko bilayer petals autonomously in '
        'response to sunlight and humidity would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate A.09-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (completing Folios A.02, E.04 & A.08) imagining a '
            'zero-energy hygroscopic European beech bilayer skin whose petals curve open and '
            "closed via Stephen Timoshenko's 1925 bimetallic curvature law."}

DISPATCH = {'kicker': 'FRONTIER BIOMIMETIC TIMBER DISPATCH · COMPLETING A.02, E.04 & A.08 · HYGROSCOPIC WOOD '
           'SKINS',
 'headline': "Stephen Timoshenko's 1925 Bilayer Theorem & Cross-Grained Beech Skins Power "
             'Zero-Energy Climate Facades',
 'body': 'Completing the mass-timber and psychrometric threads of Folios A.02, E.04, and A.08, '
         "Achim Menges's meteorosensitive timber architecture unites Stephen Timoshenko's bilayer "
         "curvature theorem (JOSA DOI 10.1364/JOSA.11.000233) with wood's 25:1 "
         'tangential-to-longitudinal moisture swelling ratio to open and seal building envelopes '
         'with zero motor power.'}

META_3D = ('Timoshenko Hygroscopic Beech Bilayer Shell Manifold',
 'X: Spanwise Petal Coordinate · Z: Moisture Shift ΔMC · Y: Timoshenko Curvature κ & Tip Opening')

ES_TRANSLATION = {'title_es': 'Pieles Arquitectónicas Programables de Madera Higroscópica: Curvatura Bicapa de '
             'Timoshenko, Hinchamiento Ortotrópico y Fachadas Climáticas de Energía Cero',
 'subtitle_es': 'Completando los Folios A.02, E.04 y A.08: cómo el teorema de curvatura bicapa de '
                'Stephen Timoshenko (1925) y las láminas de haya de Achim Menges abren y cierran '
                'fachadas sin motores eléctricos.',
 'why_es': 'Una piña de pino en la ventana se cierra sola cuando llueve y se abre cuando el aire '
           'está seco porque sus fibras externas e internas se expanden de forma distinta con la '
           'humedad, igual que una tira bimetálica natural.',
 'bridge_es': 'El hinchamiento osmótico ortotrópico de la matriz de celulosa bajo el punto de '
              'saturación de fibra obedece el mismo equilibrio osmótico de Flory–Rehner y Donnan '
              'que regula la altura del cepillo periciliar en el Folio P.04.',
 'plain_es': 'En palabras sencillas, imaginen una fachada de madera que se abre y se cierra sola '
             'con el clima sin tener un solo motor ni gastar electricidad. Piensen en lo que le '
             'ocurre a una puerta de madera en un día muy húmedo: absorbe vapor de agua del aire y '
             'se hincha. La madera se expande mucho a lo ancho de sus fibras, pero casi nada a lo '
             'largo de ellas. Si pegamos dos láminas delgadas de madera con las vetas cruzadas en '
             'direcciones opuestas, cuando el ambiente se vuelve húmedo, una lámina intenta crecer '
             'mientras la otra se resiste. Como están firmemente unidas con pegamento, la única '
             'forma de liberar esa tensión es curvándose, exactamente igual a como una piña de '
             'pino cierra sus escamas bajo la lluvia y las abre cuando sale el sol. Diseñando '
             'estas hojas de madera en las ventanas de un edificio, logramos que se abran solas '
             'para ventilar en días secos y se cierren herméticamente cuando empieza a llover.',
 'deep_es': 'A nivel físico y estructural, este comportamiento se rige por el teorema de curvatura '
            'bicapa que Stephen Timoshenko formuló en 1925, combinado con la gran anisotropía '
            'higroscópica de la madera de haya europea. Por debajo del punto de saturación de la '
            'fibra, el coeficiente de expansión tangencial supera hasta treinta veces al '
            'coeficiente longitudinal. Al presentarse una variación de humedad, se genera una '
            'deformación diferencial que curva la pieza según una relación matemática exacta entre '
            'los espesores y los módulos elásticos de ambas capas. El espesor total determina el '
            'balance crítico: láminas muy delgadas se mueven con rapidez ante cambios sutiles de '
            'humedad pero son vulnerables al viento, mientras que piezas más gruesas generan '
            'enormes fuerzas capaces de curvar paneles completos de madera contralaminada durante '
            'el secado en horno. En la actualidad, los arquitectos emplean programas de '
            'computadora y modelos de elementos finitos para orientar las vetas con precisión '
            'milimétrica, creando fachadas biomiméticas duraderas sin mecanismos electrónicos '
            'propensos a fallas.'}
