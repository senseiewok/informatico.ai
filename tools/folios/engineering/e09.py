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
              'bridge': 'Continues E.01/E.07'},
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
                'body': 'For laminar flow between smooth parallel plates, discharge scales as Q ∝ '
                        'w³ (Witherspoon et al. 1980, DOI 10.1029/WR016i006p01016). Cutting crack '
                        'width by 90% would lower ideal flow 1,000-fold (0.1³ = 10⁻³), though real '
                        'rough fracture walls depart from smooth plates.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.09-B · CODA-WAVE INTERFEROMETRY',
                'body': 'Coda-Wave Interferometry (CWI) uses late-arriving, multiply scattered waves '
                        'to resolve tiny velocity changes Δv/v (Snieder 2006, DOI '
                        '10.1007/s00024-005-0026-6; Larose & Hall 2009, DOI 10.1121/1.3079771). '
                        'Here it is proposed, not tested, for bridge-deck healing (continuing Folio '
                        'E.07).'},
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
                           'figures are now labeled as model or design values. Corrected what the '
                           'Jonkers et al. 2010 paper is cited for, replaced an invented opening scene '
                           'and a misattributed Vitruvius/tobermorite claim, fixed a "999 percent" '
                           'arithmetic error.',
                'opus': 'Review: all DOIs checked against Crossref on 2026-11-14; cubic-law '
                        'arithmetic recomputed ((0.018/0.30)^3 = 2.16e-4).'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): Volume V civil materials monograph '
                           'continuing Folio E.01 & E.07 by uniting Lucas-Washburn capillary '
                           'imbibition, Jonkers bacterial CaCO3 mineralization (DOI '
                           '10.1016/j.ecoleng.2008.12.036), and Coda-Wave Interferometry.',
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B): Checked '
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
 'act1_dropcap': 'Concrete is strong in compression and weak in tension, so it cracks and lets '
                 'water and salts reach embedded steel (Van Tittelboom & De Belie 2013, DOI '
                 '10.3390/ma6062182). In the first century BCE, Vitruvius described how volcanic '
                 'ash from the Bay of Naples hardened even under water (De Architectura, Book II). '
                 'In 2010, Hendrik Jonkers and colleagues tested adding alkali-resistant, '
                 'spore-forming Bacillus bacteria and calcium lactate to concrete (DOI '
                 '10.1016/j.ecoleng.2008.12.036). Water entering a crack could wake dormant '
                 'spores to precipitate calcium carbonate in the gap (Jonkers et al. 2010).',
 'act1_plain_bridge': 'Concrete cracks easily when stretched, letting rain and de-icing salts seep '
                      'toward the reinforcing steel (Van Tittelboom & De Belie 2013, DOI '
                      '10.3390/ma6062182). Repairing hairline cracks by hand is costly and may '
                      'require closing roads or tunnels. Self-healing concrete adds dormant '
                      'mineral-forming bacteria and a calcium lactate nutrient to the mix (Jonkers '
                      'et al. 2010, DOI 10.1016/j.ecoleng.2008.12.036). Spores are used because '
                      'they can survive alkaline cement paste, though long-term viability is not yet '
                      'established (Jonkers et al. 2010). When a crack admits water, spores may '
                      'germinate and deposit calcium carbonate that could help seal narrow gaps '
                      '(Wiktor & Jonkers 2011, DOI 10.1016/j.cemconcomp.2011.03.012).',
 'act1_body': 'Capillary suction governed by the Lucas–Washburn law pulls water into a tensile '
              'microcrack (Lucas 1918, DOI 10.1007/BF01461107; Washburn 1921, DOI '
              '10.1103/PhysRev.17.273). Jonkers et al. (2010, DOI 10.1016/j.ecoleng.2008.12.036) '
              'screened alkali-resistant Bacillus spores as a self-healing additive. Wiktor and '
              'Jonkers (2011, DOI 10.1016/j.cemconcomp.2011.03.012) immobilized spores and '
              'calcium lactate in porous expanded-clay particles. After 100 days of immersion, '
              'bacterial specimens healed cracks up to about 0.46 mm wide, versus 0.18 mm in '
              'controls (Wiktor & Jonkers 2011). In an idealized smooth crack, cubic Poiseuille '
              'flow scales as w³ (Witherspoon et al. 1980, DOI 10.1029/WR016i006p01016), so a 90% '
              'width cut lowers laminar flow 1,000-fold under the stated assumptions. This folio '
              'also proposes embedded coda-wave transducers (Snieder 2006, DOI '
              '10.1007/s00024-005-0026-6; Larose & Hall 2009, DOI 10.1121/1.3079771); that '
              'pairing is an untested design idea, not a field system.',
 'act1_stakes': 'Replacing cracked concrete carries a direct carbon cost. Global process emissions '
                'from cement calcination (excluding kiln fuel) were estimated at 1.50 ± 0.12 Gt '
                'CO₂ in 2018, about 4% of global fossil-fuel CO₂ emissions (Andrew 2019, DOI '
                '10.5194/essd-11-1675-2019). In bridges, tunnels, and marine piers, cracks may let '
                'chloride ions reach steel bars and drive expansive corrosion (De Muynck et al. '
                '2010, DOI 10.1016/j.ecoleng.2009.02.006). Manual crack injection requires dry '
                'access that submerged or buried foundations lack (Van Tittelboom & De Belie 2013, '
                'DOI 10.3390/ma6062182). Autonomous sealing could extend service life if field '
                'durability holds, though this folio assigns no life-cycle estimate.',
 'pullquote': '"In bacterial self-healing concrete, a new crack can act as a capillary trigger '
              'that wakes dormant spores to deposit mineral in the gap."',
 'chronology': [('c. 30–15 BCE',
                 'Vitruvius, De Architectura (Book II), describes volcanic ash from the Bay of '
                 'Naples (pozzolana) that sets hard even under water.'),
                ('1918–1921',
                 'Richard Lucas (1918, DOI 10.1007/BF01461107) and Edward W. Washburn (1921, DOI '
                 '10.1103/PhysRev.17.273) publish the capillary imbibition law z(t) = sqrt(gamma r '
                 'cos(theta) t / (2 mu)).'),
                ('2010–2011',
                 'Jonkers et al. (2010, DOI 10.1016/j.ecoleng.2008.12.036) introduce Bacillus '
                 'spores in concrete; Wiktor & Jonkers (2011, DOI 10.1016/j.cemconcomp.2011.03.012) '
                 'report healing up to 0.46 mm versus 0.18 mm in controls.'),
                ('2026',
                 'This folio proposes pairing Ultrasonic Coda-Wave Interferometry (Snieder 2006, '
                 'DOI 10.1007/s00024-005-0026-6) with bacterial admixtures (a design idea, not a '
                 'deployed system).')],
 'act2_title': 'Act II — How It Actually Works: Lucas–Washburn Capillary Ingress + '
               'Michaelis–Menten Calcite Healing',
 'act2_analogy': 'Everyday analogy: When you get a small paper cut, blood platelets and fibrin '
                 'seal the wound from the edges inward. Self-healing concrete uses a crack in a '
                 'roughly similar way: capillary suction draws in water that wakes dormant spores '
                 'to deposit calcite across the gap (Jonkers et al. 2010, DOI '
                 '10.1016/j.ecoleng.2008.12.036). The analogy ends at biology, because cement '
                 'mineral precipitation has no living vascular tissue.',
 'act2_plain_primer': 'The interactive lab below varies two parameters. Initial Flexural Crack '
                      'Width sets the opening created by bending loads. In this model, cracks '
                      'around 0.30 mm draw water fast and approach closure within 28 days, an '
                      'illustrative model behavior rather than a test result. Wider cracks need '
                      'more mineral volume, reflecting experimental limits around 0.46 mm reported '
                      'by Wiktor and Jonkers (2011, DOI 10.1016/j.cemconcomp.2011.03.012). Spore '
                      'and Catalyst Activity scales the modeled precipitation rate. Raising it '
                      'accelerates calcite bridging and shows the steep cubic drop in idealized '
                      'Poiseuille flow (Witherspoon et al. 1980, DOI 10.1029/WR016i006p01016); real '
                      'rough cracks do not follow smooth plates.',
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
 'act2_intuition': 'Modeling a crack of initial width w_0 as an effective capillary tube of radius '
                   'r_eff = w_0 / 2 in the cylindrical Lucas–Washburn law gives penetration depth '
                   'z(t) = sqrt([gamma w_0 cos(theta) / (4 mu)] t) (Lucas 1918, DOI '
                   '10.1007/BF01461107; Washburn 1921, DOI 10.1103/PhysRev.17.273); a strict '
                   'planar slit replaces 4 mu with 3 mu. Once wet, alkaliphilic Bacillus spores '
                   'oxidize calcium lactate to precipitate calcite (Jonkers et al. 2010, DOI '
                   '10.1016/j.ecoleng.2008.12.036). This folio models closure via Michaelis–Menten '
                   'kinetics dw/dt = -2 V_m V_max [Ca2+] / (K_m + [Ca2+]), using calcite molar '
                   'volume V_m = 36.9 cm^3/mol. Under the stated assumptions for smooth parallel '
                   'plates (Witherspoon et al. 1980, DOI 10.1029/WR016i006p01016), 94% closure gives '
                   '(0.06)^3 = 2.2 x 10^-4 flow, a 99.98% cut. The caveat is that the closure law '
                   'and 94% value are illustrative, not fitted to data. Ultrasonic CWI could track '
                   'velocity shifts delta_v / v in scattered waves (Snieder 2006, DOI '
                   '10.1007/s00024-005-0026-6; Larose & Hall 2009, DOI 10.1121/1.3079771); a '
                   'proposed 55 kHz transducer frequency is an untested design choice.',
 'act2_deepening': 'Concrete pore water typically reaches about pH 12–13, destroying vegetative '
                   'bacteria (Jonkers et al. 2010, DOI 10.1016/j.ecoleng.2008.12.036; Van '
                   'Tittelboom & De Belie 2013, DOI 10.3390/ma6062182). Hardening cement paste '
                   'also shrinks pores below approximately 1 µm, which may restrict unprotected '
                   'spore survival (Jonkers et al. 2010). Immobilizing spores and calcium lactate '
                   'inside expanded-clay carriers helps protect viability until cracking opens the '
                   'capsule (Wiktor & Jonkers 2011, DOI 10.1016/j.cemconcomp.2011.03.012). '
                   'Microbial carbonate precipitation depends on dissolved oxygen and calcium '
                   'transport (De Muynck et al. 2010, DOI 10.1016/j.ecoleng.2009.02.006), so '
                   'deep-crack sealing could become transport-limited. Crystalline admixtures offer '
                   'an abiotic alternative that may react with unhydrated cement phases (Van '
                   'Tittelboom & De Belie 2013, DOI 10.3390/ma6062182).',
 'walkthrough': ['Experiment 1 (Crack Aperture vs. Cubic Leakage Cutoff): Drag Initial Crack Width '
                 'w_0 from 0.15 mm to 0.75 mm. Watch idealized smooth-plate flow scale as w_0^3 '
                 '(Witherspoon et al. 1980) and see how the model closes widths w_0 <= 0.45 mm '
                 '(a design assumption).',
                 'Experiment 2 (Catalyst Dosage): Increase Activity k_heal from 0.40x to 2.20x. '
                 'Observe the modeled calcite front bridge the gap and raise the illustrative '
                 'stiffness-recovery index.',
                 'Experiment 3 (Capillary Wetting to CWI): Step Stages 1–4 from Lucas–Washburn '
                 'wetting to rhombohedral calcite bridging and proposed CWI sensing (Snieder '
                 '2006; Larose & Hall 2009).'],
 'act4_title': 'Act IV — Infrastructure Longevity, Archive Lineage & Upstream Biophysical Threads',
 'act4_human_ai': "Pairing Folio E.01's capillary physics and Folio E.07's sensing with Coda-Wave "
                  'Interferometry (Larose & Hall 2009, DOI 10.1121/1.3079771) might help inspect '
                  'submerged tunnel segments (Folio E.08) and coastal piers. This remains an '
                  'untested proposal, not deployed practice.',
 'act4_deepening': 'Future work could link physics-informed models with ultrasonic transducers to '
                   'track seasonal crack healing; these are research ideas, not verified practice. '
                   'Open problems identified in reviews include cold-climate activity, carrier '
                   'effects on compressive strength, and standardized durability testing (De '
                   'Muynck et al. 2010, DOI 10.1016/j.ecoleng.2009.02.006; Van Tittelboom & De '
                   'Belie 2013, DOI 10.3390/ma6062182). Solving those issues could help concrete '
                   'structures last longer with less repair.',
 'cf_bridge': 'Standalone Civil Materials Flagship & Thread Continuation (E.01 -> E.09): Written '
              'for structural and materials civil engineers interested in durable marine and '
              'underground concrete.',
 'sources': ['Jonkers, H. M., Thijssen, A., Muyzer, G., Copuroglu, O., & Schlangen, E. (2010). '
             'Application of bacteria as self-healing agent for the development of sustainable '
             'concrete. Ecological Engineering, 36(2), 230–235. DOI: '
             '10.1016/j.ecoleng.2008.12.036.',
             'Wiktor, V., & Jonkers, H. M. (2011). Quantification of crack-healing in novel '
             'bacteria-based self-healing concrete. Cement and Concrete Composites, 33(7), '
             '763–770. DOI: 10.1016/j.cemconcomp.2011.03.012.',
             'De Muynck, W., De Belie, N., & Verstraete, W. (2010). Microbial carbonate '
             'precipitation in construction materials: A review. Ecological Engineering, 36(2), '
             '118–136. DOI: 10.1016/j.ecoleng.2009.02.006.',
             'Van Tittelboom, K., & De Belie, N. (2013). Self-Healing in Cementitious Materials—A '
             'Review. Materials, 6(6), 2182–2217. DOI: 10.3390/ma6062182.',
             'Witherspoon, P. A., Wang, J. S. Y., Iwai, K., & Gale, J. E. (1980). Validity of '
             'Cubic Law for fluid flow in a deformable rock fracture. Water Resources Research, '
             '16(6), 1016–1024. DOI: 10.1029/WR016i006p01016.',
             'Washburn, E. W. (1921). The dynamics of capillary flow. Physical Review, 17(3), '
             '273–283. DOI: 10.1103/PhysRev.17.273.',
             'Lucas, R. (1918). Ueber das Zeitgesetz des kapillaren Aufstiegs von Flüssigkeiten. '
             'Kolloid-Zeitschrift, 23(1), 15–22. DOI: 10.1007/BF01461107.',
             'Snieder, R. (2006). The theory of coda wave interferometry. Pure and Applied '
             'Geophysics, 163(2–3), 455–473. DOI: 10.1007/s00024-005-0026-6.',
             'Larose, E., & Hall, S. A. (2009). Monitoring stress related velocity variation in '
             'concrete with a 2×10⁻⁵ relative resolution using diffuse ultrasound. The Journal of '
             'the Acoustical Society of America, 125(4), 1853–1856. DOI: 10.1121/1.3079771.',
             'Andrew, R. M. (2019). Global CO₂ emissions from cement production, 1928–2018. Earth '
             'System Science Data, 11(4), 1675–1710. DOI: 10.5194/essd-11-1675-2019.',
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
 'subtitle_es': 'Continuando los Folios E.01 y E.07: cómo esporas de Bacillus (Jonkers et al. 2010) '
                'y aditivos cristalinos (Van Tittelboom & De Belie 2013) pueden sellar '
                'microfisuras, mostrado aquí como un modelo ilustrativo con monitoreo propuesto por '
                'ondas coda.',
 'why_es': 'Igual que una cortadura activa plaquetas y fibrina, una grieta fina succiona agua por '
           'capilaridad y podría despertar esporas latentes para precipitar calcita (Jonkers et al. '
           '2010). La analogía termina en la biología: la matriz mineral no tiene tejido vivo.',
 'plain_es': 'El concreto se agrieta al someterse a tensión y deja pasar agua y cloruros hacia el '
             'acero de refuerzo (Van Tittelboom & De Belie 2013, DOI 10.3390/ma6062182). Reparar '
             'fisuras a mano resulta costoso. Una línea de investigación mezcla esporas bacterianas '
             'resistentes a la alcalinidad y lactato de calcio como nutriente (Jonkers et al. 2010, '
             'DOI 10.1016/j.ecoleng.2008.12.036), aunque su viabilidad a largo plazo sigue en '
             'estudio. Al entrar agua por una fisura, las esporas pueden germinar y depositar '
             'carbonato de calcio: tras 100 días de inmersión, Wiktor y Jonkers (2011, DOI '
             '10.1016/j.cemconcomp.2011.03.012) observaron cierre hasta 0.46 mm frente a 0.18 mm '
             'en probetas de control.',
 'deep_es': 'El sellado combina imbibición capilar de Lucas–Washburn (Lucas 1918, DOI '
            '10.1007/BF01461107; Washburn 1921, DOI 10.1103/PhysRev.17.273) con precipitación '
            'bacteriana de calcita en una matriz de pH 12–13 (Jonkers et al. 2010; Van Tittelboom '
            '& De Belie 2013). En placas lisas ideales, el flujo sigue la ley cúbica Q ∝ w³ '
            '(Witherspoon et al. 1980, DOI 10.1029/WR016i006p01016): cerrar 94% de una fisura de '
            '0.30 mm reduce el flujo ideal en 99.98%, aunque las grietas reales son rugosas. El '
            'límite de 0.45 mm y la cinética de Michaelis–Menten aquí son supuestos ilustrativos. '
            'Este folio propone, sin probarlo, usar ondas coda (Snieder 2006; Larose & Hall 2009, '
            'DOI 10.1121/1.3079771) para vigilar la rigidez.'}
