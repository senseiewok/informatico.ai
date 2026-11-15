#!/usr/bin/env python3
"""Folio E.09 (ENGINEERING): Autogenous Bacterial & Crystalline Self-Healing Concrete: Lucas–Washburn Capillary Imbibition, Fickian–Michaelis–Menten Calcite Precipitation & Ultrasonic Coda-Wave Digital Twins."""
from __future__ import annotations

SLUG = 'e09'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.09',
 'slug': 'e09',
 'pillar': 'engineering',
 'category_code': 'E',
 'parent_folios': ['E.01', 'E.07'],
 'lineage_mode': 'CONTINUATION · Continues E.01 Capillary Percolation & E.07 Bridge Fatigue SHM',
 'title': 'Autogenous Bacterial & Crystalline Self-Healing Concrete: Lucas–Washburn Capillary '
          'Imbibition, Fickian–Michaelis–Menten Calcite Precipitation & Ultrasonic Coda-Wave '
          'Digital Twins',
 'subtitle': "Continuing Folio E.01's capillary pore physics and E.07's structural sensing: how "
             'Bacillus pseudofirmus spores and crystalline admixtures can seal fine flexural '
             'microcracks via CaCO₃ mineralization, shown here as an illustrative model.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'SELF-HEALING CONCRETE · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'z(t) = √(γ r cos θ · t / 2μ) · ∂C/∂t = D_eff ∇²C − V_max C/(K_m + C) · CSI 03 '
                  '30 00',
 'colophon': {'identifier': 'E.09 · Self-Healing Bio-Concrete · CSI 03 30 00',
              'kernels': 'Lucas–Washburn Imbibition · Michaelis–Menten CaCO₃ · Coda-Wave CWI',
              'benchmarks': 'Model: w_0 = 0.30 mm → w_rem = 0.018 mm (94.0% closure, illustrative) ⇒ '
                            '(0.018/0.30)³ = 2.2 × 10⁻⁴ ⇒ −99.98% parallel-plate flow (w³ law)',
              'bridge': 'Continues E.01/E.07 · Analogy only: Ca²⁺-mediated mineral bridging ↔ Ca²⁺ '
                        'in mucin gels'},
 'sliders': [{'label': 'Initial Flexural Crack Aperture (w_0)',
              'min': 0.1,
              'max': 0.8,
              'step': 0.02,
              'value': 0.3,
              'unit': ' mm'},
             {'label': 'Spore & Crystalline Catalyst Activity (k_heal)',
              'min': 0.4,
              'max': 2.2,
              'step': 0.05,
              'value': 1.2,
              'unit': '×'}],
 'steps': ['Stage 1 (Lucas–Washburn Capillary Imbibition): A flexural microcrack of width w_0 = '
           '0.30 mm, treated as a parallel-plate channel (r = w_0/2), draws moisture to depth z(t) = '
           '√(γ w_0 cos θ · t / 4μ), wetting embedded bacterial spores.',
           'Stage 2 (Spore Germination & Lactate-to-Calcite Conversion): Alkali-resistant bacteria '
           'metabolize calcium lactate, and calcium carbonate precipitates along the crack walls '
           '(the mechanism tested by Jonkers et al. 2010).',
           'Stage 3 (Cubic Parallel-Plate Flow, Q ∝ w³): In this model, narrowing w from 0.30 mm to '
           'an illustrative 0.018 mm (94.0% closure) gives (0.018/0.30)³ = 2.2 × 10⁻⁴, a 99.98% cut '
           'in idealized laminar flow. Real healed cracks are rough and partly filled, so this is an '
           'upper-bound idealization.',
           'Stage 4 (Ultrasonic Coda-Wave Interferometry): Multiply scattered ultrasonic coda waves '
           'are sensitive to very small relative velocity changes Δv/v, so CWI could be used to '
           'track stiffness recovery; the 96.4% recovery index shown in the lab is an illustrative '
           'model value, not a measurement.'],
 'readouts': [{'label': 'Calcite Crack Closure (model, η_seal)',
               'value': '94.0% (w_rem = 0.018 mm, illustrative)'},
              {'label': 'Cubic Flow Reduction (w³ model)', 'value': '−99.98% (idealized)'},
              {'label': 'Stiffness Recovery Index (model)', 'value': '96.4% (illustrative)'},
              {'label': 'Model Healing Status',
               'value': 'SEALED IN MODEL · design target w_0 ≤ 0.45 mm'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 30 00 (filing label)',
                'title': 'Bacterial-Crystalline Self-Healing Marine & Tunnel Structural Concrete '
                         '(Design Study)',
                'body': 'Design study: blended slag-fly-ash concrete with carrier-protected '
                        'alkali-resistant Bacillus spores, a calcium lactate nutrient, and embedded '
                        'piezoelectric transducers for coda-wave monitoring. Not a tested or '
                        'specified product.',
                'meta': 'Mechanism: Jonkers et al. (2010) DOI 10.1016/j.ecoleng.2008.12.036 · '
                        'Healing limit w_0 ≤ 0.45 mm is this folio\'s design assumption'},
 'sidenote_1': {'kicker': 'SIDENOTE E.09-A · CONTINUING FOLIO E.01 CAPILLARY & CUBIC POISEUILLE '
                          'SCALING',
                'body': 'For ideal laminar flow between smooth parallel plates, flow per unit length '
                        'scales as Q ∝ w³, so closing 90% of a crack\'s width would cut that flow by '
                        'a factor of 1,000 (0.1³ = 10⁻³). Real cracks are rough, so treat this as an '
                        'idealization.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.09-B · CODA-WAVE INTERFEROMETRY',
                'body': 'Coda-Wave Interferometry (CWI) uses late-arriving, multiply scattered waves, '
                        'which makes it sensitive to very small relative velocity changes (Snieder '
                        '2006). Here it is proposed, not demonstrated, as a way to monitor healing '
                        'in bridge decks (continuing Folio E.07).'},
 'skill': {'filename': 'self-healing-concrete-washburn-calcite-SKILL.md',
           'name': 'self-healing-concrete-washburn-calcite',
           'description': 'AI-agnostic civil materials engineering skill for Lucas-Washburn '
                          'capillary crack imbibition, Fickian-Michaelis-Menten bacterial CaCO3 '
                          'precipitation, cubic Poiseuille permeability cutoff, and Coda-Wave '
                          'Interferometry.',
           'rules': ['Compute Lucas-Washburn capillary penetration depth z(t) = sqrt((gamma * w_0 '
                     '* cos(theta) / (4 * mu)) * t) for crack aperture w_0.',
                     'Integrate crack-closure kinetics dw/dt = -2 * V_m * V_max * [Ca2+] / (K_m + '
                     '[Ca2+]) and evaluate cubic Poiseuille leakage ratio (w_rem / w_0)^3.',
                     'Treat the healing limit w_0 <= 0.45 mm and any Coda-Wave Interferometry '
                     'recovery target as project design assumptions to be tested, not as values '
                     'taken from a standard.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Grounding pass 2026-11-14): Withdrew the "ACI 224R PASS" verdict '
                           'and other verification language; the healing limit, closure and stiffness '
                           'figures are now labelled as model or design values. Corrected what the '
                           'Jonkers et al. 2010 paper is cited for, replaced an invented opening scene '
                           'and a misattributed Vitruvius/tobermorite claim, fixed a "999 percent" '
                           'arithmetic error, and turned the mucus bridge into a stated analogy.',
                'opus': 'Review: all DOIs checked against Crossref on 2026-11-14; cubic-law '
                        'arithmetic recomputed ((0.018/0.30)^3 = 2.16e-4).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V civil materials monograph '
                           'continuing Folio E.01 & E.07 by uniting Lucas-Washburn capillary '
                           'imbibition, Jonkers bacterial CaCO3 mineralization (DOI '
                           '10.1016/j.ecoleng.2008.12.036), and Coda-Wave Interferometry.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Checked '
                        'cubic Poiseuille leakage reduction (1 - (0.018/0.30)^3) = 99.978% and '
                        'Michaelis-Menten calcite molar volume balance. The word "Verified" is '
                        'withdrawn in REV 1.1: these are model values, not measurements.'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.ecoleng.2008.12.036',
           'fetched_on': '2026-11-08',
           'citing_publications': 1593,
           'supporting': 17,
           'mentioning': 817,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Jonkers et al. 2010 (DOI '
                      '10.1016/j.ecoleng.2008.12.036), fetched 2026-11-08: 1,593 citing '
                      'publications (17 supporting, 817 mentioning, 4 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['E.01', 'E.07'],
 'lineage_mode': 'CONTINUATION · Continues E.01 Capillary Percolation & E.07 Bridge Fatigue SHM',
 'scite': {'doi': '10.1016/j.ecoleng.2008.12.036',
           'fetched_on': '2026-11-08',
           'citing_publications': 1593,
           'supporting': 17,
           'mentioning': 817,
           'contrasting': 4,
           'retracted': False,
           'summary': 'Scite index entry for Jonkers et al. 2010 (DOI '
                      '10.1016/j.ecoleng.2008.12.036), fetched 2026-11-08: 1,593 citing '
                      'publications (17 supporting, 817 mentioning, 4 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': 'Act I — Picking Up the Thread from E.01 & E.07: From Roman Pozzolanic Seawalls to '
               'Living Self-Healing Concrete',
 'act1_dropcap': 'Concrete is strong in compression and weak in tension, so it cracks, and those '
                 'cracks let water and de-icing salts reach the steel inside. Builders have long '
                 'known that some concretes partly seal their own fine cracks: in the first century '
                 'BCE the Roman writer Vitruvius described how volcanic ash from the Bay of Naples '
                 'set hard even under water. In 2010, Hendrik Jonkers and colleagues at Delft '
                 'University of Technology published a study of a different idea: adding '
                 'alkali-resistant, spore-forming bacteria and a nutrient to the mix, so that '
                 'water entering a new crack could wake the spores and let them precipitate '
                 'calcium carbonate in the crack (Jonkers et al. 2010).',
 'act1_plain_bridge': 'In plain words, concrete is the most consumed building material on Earth, '
                      'but it has one major weakness: it cracks easily when stretched. Even the '
                      'strongest highway bridges and tunnel walls develop tiny hairline fissures '
                      'over time. Once a tiny crack opens, rain and road salt seep inside, rusting '
                      'the steel rebar hidden within and eventually causing entire slabs to '
                      'crumble. Repairing these cracks by hand is costly and often means closing '
                      'roads. Self-healing concrete is one research answer. Scientists mix dormant '
                      'limestone-producing bacteria into the concrete along with a nutrient. The '
                      'spores are chosen because they can survive the dry, alkaline stone; how long '
                      'they stay viable is still being studied. When a crack forms, moisture leaks '
                      'in and can wake the bacteria, which consume their nutrient and produce '
                      'calcium carbonate that can partly or fully fill a fine crack before water '
                      'reaches the steel.',
 'act1_body': 'When a tensile microcrack opens in concrete, capillary suction governed by the '
              'Lucas–Washburn law draws moisture inward from the exposed surface. In 2010, Hendrik '
              'M. Jonkers and colleagues at TU Delft (Ecological Engineering, DOI '
              '10.1016/j.ecoleng.2008.12.036) reported on alkali-resistant, spore-forming bacteria '
              'as a self-healing agent for concrete. Later work from the same group placed the '
              'spores and a calcium lactate nutrient inside porous expanded-clay particles and '
              'quantified crack healing (Wiktor & Jonkers 2011). As water enters the fissure, the '
              'spores can germinate and, consuming calcium lactate and dissolved oxygen, '
              'precipitate calcium carbonate along the crack walls. In an idealized smooth '
              'parallel-plate crack, flow follows the cubic Poiseuille law, so reducing crack '
              'width by ninety percent would cut flow a thousand-fold (by 99.9 percent). This '
              'folio also proposes embedded piezoelectric transducers using Ultrasonic Coda-Wave '
              'Interferometry to track stiffness recovery over time; that pairing is a design '
              'idea here, not a demonstrated system.',
 'act1_stakes': 'The economic and ecological stakes of concrete degradation are large. Cement '
                'production is commonly estimated at around eight percent of worldwide carbon '
                'dioxide emissions (an estimate not sourced in this folio), so replacing concrete '
                'early carries a real carbon cost. In marine docks, highway bridge decks, and underground '
                'tunnels, microcracks as narrow as three-tenths of a millimeter provide expressway '
                'conduits for chloride ions. Once chlorides reach embedded steel reinforcement, '
                'protective passivation breaks down, producing expansive rust that spalls the '
                'concrete cover and leads to sudden structural failures. Traditional epoxy '
                'injections and surface sealants require dry weather, hazardous solvents, and '
                'expensive manual labor that cannot access buried foundations or submerged piers. '
                'If a healing material could reliably seal fine cracks after moisture contact, it '
                'could lengthen the service life of exposed structures and reduce repair work; how '
                'much is still an open research question, and this folio does not put a number on '
                'it.',
 'pullquote': '"In bacterial self-healing concrete, a new crack can act as a capillary trigger '
              'that wakes dormant spores to deposit mineral in the gap."',
 'chronology': [('c. 30–15 BCE',
                 'Vitruvius, De Architectura (Book II), describes volcanic ash from the Bay of '
                 'Naples (pozzolana) that sets hard even under water.'),
                ('1918–1921',
                 'Richard Lucas (1918) and Edward W. Washburn (1921) publish the capillary '
                 'imbibition law z(t) = sqrt(gamma r cos(theta) t / (2 mu)).'),
                ('2010',
                 'Hendrik M. Jonkers et al. report alkali-resistant spore-forming bacteria as a '
                 'self-healing agent for concrete (DOI 10.1016/j.ecoleng.2008.12.036).'),
                ('2026',
                 'This folio proposes pairing Ultrasonic Coda-Wave Interferometry (CWI) monitoring '
                 'with bacterial-crystalline admixtures (a design idea, not a deployed system).')],
 'act2_title': 'Act II — How It Actually Works: Lucas–Washburn Capillary Ingress + '
               'Michaelis–Menten Calcite Healing',
 'act2_analogy': 'Everyday analogy: Consider what happens when you get a small paper cut on your '
                 'finger. Blood platelets and fibrin immediately rush to the wound, forming a clot '
                 'that weaves the skin back together from the edges inward. Self-healing '
                 'bio-concrete behaves like living tissue. A hairline fracture acts as a capillary '
                 'straw that sucks in rainwater, waking dormant limestone-making bacteria that '
                 'weave a mineral scar of calcite across the fissure until it is watertight.',
 'act2_plain_primer': 'To examine how biological healing works in practice, our interactive '
                      'laboratory offers two key adjustments. The first control is the Initial '
                      'Flexural Crack Width, which sets the size of the structural crack opened by '
                      'bending loads. In the model, narrow fissures up to about three-tenths of a '
                      'millimeter draw moisture rapidly and largely seal within twenty-eight days '
                      '(an illustrative model behaviour, not a test result). Wider gaps '
                      'require significantly more mineral volume to bridge, testing the physical '
                      'limits of autonomous repair. The second control is the Spore and Catalyst '
                      'Activity, which represents the dosage and metabolic rate of the '
                      'encapsulated healing agents. Increasing this multiplier accelerates '
                      'bacterial calcite production, speeding up how quickly mineral crystals '
                      'bridge the crack gap. By experimenting with these two knobs, you can '
                      'observe the cubic drop in idealized water flow: in the parallel-plate model, '
                      'narrowing a crack by ninety percent cuts flow a thousand-fold. Real cracks '
                      'are rough, so treat the curve as an idealization.',
 'distill_diagram': {'analogy_title': 'Paper Cut Healing on Human Skin',
                     'analogy_sub': 'Moisture wakes dormant bacteria to grow a mineral scar across '
                                    'cracks',
                     'force_a_title': 'Initial Crack Width (w_0)',
                     'force_a_sub': 'Dictates capillary suction depth and total void volume to be '
                                    'sealed',
                     'force_b_title': 'Healing Catalyst Rate (k_heal)',
                     'force_b_sub': 'Drives bacterial calcite precipitation kinetics along crack '
                                    'walls',
                     'threshold_title': 'Model Healing Limit (design assumption w_0 <= 0.45 mm)',
                     'threshold_pass': 'Sealed in model: over 90% calcite closure sharply cuts '
                                       'idealized flow',
                     'threshold_fail': 'Unsealed in model: gap exceeds assumed healing capacity'},
 'act2_intuition': 'A flexural crack of initial aperture w_0 behaves as a parallel-plate capillary '
                   'channel with hydraulic radius r_eff = w_0 / 2. Upon exposure to ambient water, '
                   'surface tension pulls moisture to a penetration depth z(t) = sqrt([gamma w_0 '
                   'cos(theta) / (4 mu)] t) governed by the Lucas–Washburn equation. Once wet, '
                   'encapsulated Bacillus spores metabolize calcium lactate and oxygen, '
                   'precipitating insoluble calcium carbonate via Michaelis–Menten kinetics dw/dt '
                   '= -2 V_m V_max [Ca2+] / (K_m + [Ca2+]), where V_m = 36.9 cm^3/mol is the molar '
                   'volume of calcite. As crystals accumulate along opposing crack faces, the '
                   'effective aperture w narrows toward residual clearance w_rem. Because laminar '
                   'seepage through a fracture scales with the cube of the aperture (the cubic '
                   'Poiseuille law Q = [w^3 delta_P] / [12 mu L]), a ninety-four percent reduction '
                   'in crack width gives (0.06)^3 = 2.2 x 10^-4 of the original flow, a 99.98% cut '
                   'for an ideal smooth crack. The molar-volume closure law and the 94% figure are '
                   "this folio's illustrative model, not fitted to data. Ultrasonic Coda-Wave "
                   'Interferometry (CWI) records small relative velocity shifts delta_v / v in '
                   'multiply scattered waves (Snieder 2006) and could be used to track stiffness '
                   'change across a healed zone; the 55 kHz frequency is a design choice here.',
 'act2_deepening': 'Underneath the macro-scale crack closure lies a coupled multi-scale process of '
                   'chemical diffusion, bacterial viability, and crystallization kinetics. The '
                   'interior of concrete is an extreme environment with a pore solution pH often '
                   'exceeding twelve, which destroys most vegetative bacteria. Alkaliphilic '
                   'Bacillus spores are chosen because spores resist harsh conditions, and research '
                   'formulations add further protection by placing them inside porous expanded-clay '
                   '(Wiktor & Jonkers 2011) or other carriers. When cracking '
                   'ruptures the carriers, capillary action supplies water and atmospheric carbon '
                   'dioxide diffuses inward. The bacteria produce carbonate ions that react with '
                   'dissolved calcium ions, nucleating dense rhombohedral calcite crystals at the '
                   'fissure boundary. Because calcite precipitation requires both dissolved '
                   'calcium and oxygen, healing deep inside a crack can become transport-limited '
                   '(this folio does not give a sourced depth). Some research formulations explore '
                   'other bacterial pathways or crystalline mineral admixtures that react with '
                   'unhydrated cement grains, aiming to improve sealing deeper in the member; this '
                   'folio does not cite or test them.',
 'walkthrough': ['Experiment 1 (Crack Aperture vs. Cubic Leakage Cutoff): Drag Initial Crack Width '
                 'w_0 from 0.15 mm to 0.75 mm. Notice how unhealed Poiseuille water leakage scales '
                 'as w_0^3, and watch how, in the model, calcite precipitation closes narrower '
                 'cracks (< 0.45 mm, a design assumption) to >92% closure within 28 days.',
                 'Experiment 2 (Bacterial & Crystalline Catalyst Dosage): Increase Spore & Mineral '
                 'Precursor Activity k_heal from 0.40x to 2.20x. Watch the model calcite front '
                 'bridge the fissure and the illustrative stiffness-recovery index rise toward its '
                 'upper value.',
                 'Experiment 3 (From Capillary Wetting to CWI Digital Twin): Step through Stages 1 '
                 'to 4 to inspect Lucas–Washburn wetting, spore germination, rhombohedral calcite '
                 'bridging, and proposed Coda-Wave Interferometry monitoring.'],
 'act4_title': 'Act IV — Infrastructure Longevity, Archive Lineage & Upstream Biophysical Threads',
 'act4_human_ai': "By uniting Folio E.01's capillary pore physics and Folio E.07's PINN structural "
                  'sensing with ultrasonic coda-wave monitoring, engineers could one day check '
                  'crack closure inside submerged tunnel segments (Folio E.08) and coastal bridge '
                  'piers without sending divers into hazardous currents. This is a proposal, not a '
                  'deployed practice.',
 'act4_deepening': 'Looking ahead, synthetic biology, computational materials science, and civil '
                   'engineering could work together on these materials. One could imagine using '
                   'physics-informed models to choose nutrient carrier geometry and spore '
                   'distribution for marine and underground settings, and inspection robots with '
                   'ultrasonic transducers feeding velocity data into digital twins that follow '
                   'crack closure over the seasons. These are ideas for research, not current '
                   'practice described by a source here. Open questions continue to '
                   'guide active research: engineering bacterial strains capable of rapid calcite '
                   'precipitation in freezing sub-zero temperatures, developing nutrient carriers '
                   'that do not reduce the compressive strength of high-performance concrete '
                   'mixes, and formulating standardized building codes for life-cycle durability '
                   'assessments. If those questions are answered, biological healing could help '
                   'concrete structures last longer with less repair.',
 'cf_bridge': 'Standalone Civil Materials Flagship & Thread Continuation (E.01 -> E.09): Written '
              'for structural and materials civil engineers interested in durable marine and '
              'underground concrete. A loose analogy, not a shared model: both this folio and '
              'airway mucus involve calcium ions and reaction-diffusion, since calcium also helps '
              'hold mucin gels together. The equations here are not a model of mucus, and nothing '
              'in this folio is clinical information.',
 'sources': ['Jonkers, H. M., Thijssen, A., Muyzer, G., Copuroglu, O., & Schlangen, E. (2010). '
             'Application of bacteria as self-healing agent for the development of sustainable '
             'concrete. Ecological Engineering, 36(2), 230–235. DOI: '
             '10.1016/j.ecoleng.2008.12.036.',
             'Wiktor, V., & Jonkers, H. M. (2011). Quantification of crack-healing in novel '
             'bacteria-based self-healing concrete. Cement and Concrete Composites, 33(7), '
             '763–770. DOI: 10.1016/j.cemconcomp.2011.03.012.',
             'Washburn, E. W. (1921). The dynamics of capillary flow. Physical Review, 17(3), '
             '273–283. DOI: 10.1103/PhysRev.17.273.',
             'Lucas, R. (1918). Ueber das Zeitgesetz des kapillaren Aufstiegs von Flüssigkeiten. '
             'Kolloid-Zeitschrift, 23(1), 15–22. DOI: 10.1007/BF01461107.',
             'Snieder, R. (2006). The theory of coda wave interferometry. Pure and Applied '
             'Geophysics, 163(2–3), 455–473. DOI: 10.1007/s00024-005-0026-6.',
             'CSI MasterFormat, Section 03 30 00 Cast-in-Place Concrete (used here only as a '
             'filing label; no threshold in this folio comes from a standard).',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068. Named as a tool a '
             'reader could use for reaction-diffusion models; this folio did not run it.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Autogenous '
        'bacterial concrete crack cross-section with Lucas-Washburn capillary meniscus, '
        'rhombohedral CaCO3 crystal bridges, and ultrasonic coda-wave healing curve">\n'
        '            <line x1="40" y1="188" x2="640" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <rect x="55" y="38" width="115" height="140" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <rect x="205" y="38" width="115" height="140" fill="var(--tp-stone)" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <polygon id="tp-e09-crack-void" points="170,38 205,38 196,178 179,178" '
        'fill="var(--tp-minium)" fill-opacity="0.18" stroke="var(--tp-minium)" '
        'stroke-width="1.5"/>\n'
        '            <g id="tp-e09-calcite-crystals">\n'
        '              <polygon points="171,62 188,54 204,64 188,74" fill="var(--tp-verdigris)" '
        'fill-opacity="0.88" stroke="var(--tp-prussian)" stroke-width="1.2"/>\n'
        '              <polygon points="173,98 188,88 202,98 188,109" fill="var(--tp-verdigris)" '
        'fill-opacity="0.88" stroke="var(--tp-prussian)" stroke-width="1.2"/>\n'
        '              <polygon points="176,134 188,125 199,134 188,144" '
        'fill="var(--tp-verdigris)" fill-opacity="0.88" stroke="var(--tp-prussian)" '
        'stroke-width="1.2"/>\n'
        '            </g>\n'
        '            <path id="tp-e09-coda-wave" d="M 70 110 Q 120 75 188 110 T 305 110" '
        'fill="none" stroke="var(--tp-prussian)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <text x="55" y="26" font-size="10.5" font-weight="600" '
        'fill="currentColor">Crack Capillary Bridge &amp; CaCO3 Rhombohedra</text>\n'
        '            <text id="tp-e09-svg-crack-text" x="55" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Model: w_0 = 0.30 mm → w_rem = 0.018 mm (94.0% closure)</text>\n'
        '            <line x1="365" y1="24" x2="365" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="382" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Michaelis–Menten Calcite Closure &amp; CWI Recovery</text>\n'
        '            <path id="tp-e09-heal-curve" d="M 390 168 Q 475 78 630 52" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <path id="tp-e09-leak-curve" d="M 390 55 Q 465 152 630 176" fill="none" '
        'stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <circle id="tp-e09-op-dot" cx="535" cy="68" r="6" '
        'fill="var(--tp-prussian)"/>\n'
        '            <text x="392" y="148" font-size="9.5" fill="var(--tp-verdigris)">CaCO3 Seal '
        'Fraction η_seal(t)</text>\n'
        '            <text id="tp-e09-cwi-text" x="392" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Idealized flow reduction: −99.98% (cubic w³ law)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a self-healing marine concrete crack '
        'cross-section bridged by glowing rhombohedral calcium carbonate crystals precipitated by '
        'Bacillus spores and scanned by ultrasonic coda-wave interferometry wavefronts would look '
        'like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.09-V (Imagining What It Would Look Like) · Artistic '
            'civil-materials visualization (continuing Folios E.01 & E.07) imagining '
            'Lucas–Washburn capillary imbibition waking dormant Bacillus spores to bridge a '
            'concrete microcrack with rhombohedral CaCO₃ crystals under ultrasonic coda-wave '
            'monitoring.'}

DISPATCH = {'kicker': 'FRONTIER CIVIL MATERIALS DISPATCH · CONTINUING E.01 & E.07 · BACTERIAL SELF-HEALING '
           'CONCRETE',
 'headline': 'Capillary Imbibition & Dormant Bacillus Spores: A Model of Self-Sealing Concrete '
             'Microcracks',
 'body': 'Continuing the capillary pore mechanics of Folio E.01 and the structural monitoring of '
         'Folio E.07, this folio models bacterial self-healing concrete in the line of Jonkers et '
         'al. (Ecol. Eng. 2010, DOI 10.1016/j.ecoleng.2008.12.036) and proposes coda-wave '
         'monitoring. In its illustrative model, 94% closure of a 0.30 mm crack cuts ideal '
         'parallel-plate flow by 99.98%.'}

META_3D = ('Lucas–Washburn Capillary & Calcite Self-Healing Fissure',
 'X: Crack Width Coordinate w · Z: Capillary Depth z(t) · Y: CaCO₃ Mineralization & CWI Recovery')

ES_TRANSLATION = {'title_es': 'Concreto Autocurativo Bacteriano y Cristalino: Imbibición Capilar de Lucas–Washburn, '
             'Precipitación de Calcita de Fick–Michaelis–Menten y Gemelos Digitales de Ondas Coda',
 'subtitle_es': 'Continuando los Folios E.01 y E.07: cómo las esporas de Bacillus pseudofirmus y '
                'los aditivos cristalinos pueden sellar microfisuras por mineralización de CaCO₃, '
                'con una propuesta de monitoreo por interferometría ultrasónica de ondas coda.',
 'why_es': 'Igual que una cortadura en la piel activa plaquetas y fibrina para cerrar la herida '
           'desde adentro, una microfisura en concreto bio-activo succiona agua por capilaridad y '
           'despierta bacterias latentes que tejen una cicatriz de piedra caliza.',
 'plain_es': 'En palabras sencillas, el concreto es el material de construcción más utilizado del '
             'planeta, pero tiene una gran debilidad: se agrieta con facilidad cuando se somete a '
             'esfuerzos de tensión. Con el paso de los años, cualquier puente carretero o túnel '
             'subterráneo desarrolla microfisuras diminutas. Aunque midan menos de medio '
             'milímetro, el agua de lluvia y las sales se filtran por ellas, oxidando las varillas '
             'de acero internas y obligando a costosas reparaciones. El concreto autocurativo es '
             'una respuesta que se investiga: se mezclan en el concreto esporas bacterianas '
             'latentes junto con un nutriente. Se eligen esporas porque resisten el concreto seco '
             'y alcalino; cuánto tiempo siguen viables todavía se estudia. Cuando se abre una '
             'grieta, la humedad entra por capilaridad y puede despertar a las bacterias, que '
             'consumen su alimento y producen carbonato de calcio capaz de rellenar en parte o por '
             'completo una fisura fina antes de que el agua alcance el acero.',
 'deep_es': 'El proceso de autocuración biológica enfrenta dos factores contrapuestos: la '
            'velocidad de penetración del agua por succión capilar y la tasa de precipitación '
            'mineral de calcita producida por las bacterias. Cuando una fisura se abre, la ley de '
            'Lucas–Washburn gobierna la rápida entrada de humedad hacia el interior del elemento '
            'estructural. Al mismo tiempo, las esporas de Bacillus metabolizan el lactato de '
            'calcio siguiendo una cinética enzimática de Michaelis–Menten para precipitar '
            'carbonato de calcio en las paredes de la grieta. En el modelo de este folio, el '
            'límite de curación es un supuesto de diseño de 0.45 mm de ancho, por debajo del cual '
            'el crecimiento de cristales logra más del noventa por ciento de cierre. Según la ley '
            'cúbica de Poiseuille para una grieta ideal y lisa, cerrar el 94% del ancho reduce el '
            'flujo de agua en un 99.98%; las grietas reales son rugosas, así que es una '
            'idealización. Este folio propone, sin haberlo demostrado, usar sensores ultrasónicos '
            'de ondas coda para seguir la recuperación de rigidez.',
 'bridge_es': 'Solo una analogía, no un modelo común: tanto este folio como el moco de las vías '
              'respiratorias involucran iones de calcio y reacción-difusión, porque el calcio '
              'también ayuda a mantener unidos los geles de mucina. Estas ecuaciones no modelan el '
              'moco y nada en este folio es información clínica.'}
