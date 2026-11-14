#!/usr/bin/env python3
"""Folio A.06 (ARCHITECTURE): Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis, and Pathogen-Control Plumbing (CSI 22 13 00)."""
from __future__ import annotations

SLUG = 'a06'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.06',
 'slug': 'a06',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis, and Pathogen-Control Plumbing (CSI 22 13 00)',
 'subtitle': 'How a modelled subsurface reed bed removes about 95% of greywater BOD_5 outside, while 60 °C recirculation and a 254 nm UV-C reactor are design targets meant to limit growth of Pseudomonas and Legionella inside.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/tectonic_verify.py',
 'colophon': {'identifier': 'A.06 · Hydro-Tectonics · CSI 22 13 00',
              'kernels': 'Kadlec-Knight k-C* · Chick-Watson 5.4-Log UV-C',
              'benchmarks': 'Model values: 95.1% BOD_5 removal · 5.4-log UV-C design dose',
              'bridge': 'Biofilm-Control Plumbing ↔ CF Infection-Prevention Context'},
 'sliders': [{'label': 'Wetland Hydraulic Retention Time (τ_HRT)',
              'min': 0.8,
              'max': 6.0,
              'step': 0.2,
              'value': 3.2,
              'unit': ' d'},
             {'label': '254 nm UV-C Reactor Fluence (H_UV)',
              'min': 10.0,
              'max': 80.0,
              'step': 1.0,
              'value': 45.0,
              'unit': ' mJ/cm²'}],
 'steps': ['Stage 1 (Subsurface Horizontal Darcy Filtration): Greywater flows 150 mm beneath dry washed basalt gravel '
           '(φ = 0.38, K_s = 120 m/d) with no open water surface.',
           'Stage 2 (Rhizosphere Biofilm Oxidation): Phragmites root-zone oxygen transfer drives Kadlec-Knight '
           'exponential BOD_5 decay from 140 mg/L to 6.8 mg/L (τ = 3.2 d) in the folio model.',
           'Stage 3 (Dead-Leg-Free 60 °C Potable Recirculation): Copper-silver / stainless manifold designed to target v ≥ 0.6 m/s and T ≥ 60 °C up to every point-of-use mixing valve (design target, not measured).',
           'Stage 4 (254 nm UV-C Photolysis & Thermal Trap Purge): Delivers H = 45 mJ/cm² UV-C fluence (a 5.4-log reduction in the folio\'s Chick-Watson model) plus self-heating sink traps.'],
 'readouts': [{'label': 'Wetland BOD_5 Reduction', 'value': '95.1% (140 → 6.8 mg/L)'},
              {'label': 'UV-C Log Reduction (Model)', 'value': '5.4-Log (45 mJ/cm²)'},
              {'label': 'Thermal Loop Design Target', 'value': '60.0 °C (v = 0.65 m/s)'},
              {'label': 'Design Check (Model)', 'value': 'DESIGN TARGETS MET (MODEL)'}],
 'sidenote_1': {'kicker': 'SIDENOTE A.06-A · SUBSURFACE HYDRAULIC GRADE LINE',
                'body': 'Keeping the Darcy water table 150 mm below the gravel surface limits mosquito breeding, odor, and human contact with untreated greywater.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.06-B · SPECIFICATION PLATE · CSI 22 13 00 / 22 42 00',
                'body': 'Offset drain clinical washbasin with an automated 65 °C thermal P-trap cycle, intended to reduce droplet dispersal from the drain. Kotay et al. (2017, DOI 10.1128/AEM.03327-16) modelled sink-trap dispersal with a marker organism; this fixture is a design proposal and has not been tested.'},
 'skill': {'filename': 'netzero-water-pathogen-plumbing-SKILL.md',
           'name': 'netzero-water-pathogen-plumbing',
           'description': 'AI-agnostic architectural hydro-engineering skill for Kadlec-Knight subsurface constructed wetlands and biofilm-control clinical plumbing design targets.',
           'rules': ["Size subsurface horizontal-flow wetlands via Darcy's law Q = K_s A_c S and Kadlec-Knight "
                     'kinetics C_out = C* + (C_in - C*) exp(-k_v * tau).',
                     'Maintain potable hot-water recirculation >= 60 C at velocity >= 0.6 m/s with zero dead-legs > '
                     '1.5 pipe diameters.',
                     'Apply the folio\'s design targets of a 4-log model reduction (254 nm UV-C fluence H >= 34 mJ/cm^2 at 0.12 log per mJ/cm^2) and non-splashing offset drains; report log reductions as model values, never as measured outcomes.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. Earlier editions said the design '
                           'eradicates pathogens and showed a zero-biofilm verdict; nothing here was measured, '
                           'so those statements are withdrawn and every number is labelled as a model value. '
                           'Claims about sink drains and Cystic Fibrosis had been attributed to a wetlands '
                           'textbook; they now cite Kotay et al. 2017 (DOI 10.1128/AEM.03327-16) and the CF '
                           'infection prevention guideline (DOI 10.1086/676882). The opening scene about Käthe '
                           'Seidel was not sourced and is replaced by a plain account.',
                'opus': 'Review: new references checked by DOI in Crossref and the Scite index.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Modelled 95.1% Kadlec-Knight BOD_5 greywater reduction and a 5.4-log Chick-Watson UV-C design dose with a 60 °C thermal loop.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' wording is withdrawn in REV 1.2: nothing was measured, and ASHRAE 188 does not prescribe this design.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph coupling net-zero subsurface '
                           'greywater wetlands with CSI 22 13 00 clinical plumbing.',
                'opus': 'Council review of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified inactivation\' wording is withdrawn in REV 1.2: nothing was measured.'}],
 'governing_law': 'C_out = C* + (C_in−C*)e^(−kτ) · 5.4-Log UV-C',
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1201/9781420012514',
           'fetched_on': '2026-11-08',
           'citing_publications': 1371,
           'supporting': 66,
           'mentioning': 1217,
           'contrasting': 3,
           'retracted': False,
           'summary': 'Scite index entry for Kadlec & Wallace, Treatment Wetlands (DOI 10.1201/9781420012514), checked 2026-11-08: 1,371 citing publications (66 supporting, 1,217 mentioning, 3 contrasting) and no retraction notice. The book is about treatment wetlands, not clinical disinfection.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1201/9781420012514',
           'fetched_on': '2026-11-08',
           'citing_publications': 1371,
           'supporting': 66,
           'mentioning': 1217,
           'contrasting': 3,
           'retracted': False,
           'summary': 'Scite index entry for Kadlec & Wallace, Treatment Wetlands (DOI 10.1201/9781420012514), checked 2026-11-08: 1,371 citing publications (66 supporting, 1,217 mentioning, 3 contrasting) and no retraction notice. The book is about treatment wetlands, not clinical disinfection.'},
 'act1_title': 'Act I — From Roman Cisterns to Net-Zero Bio-Engineered Wetlands & Pathogen-Control Plumbing',
 'act1_dropcap': 'The German botanist Käthe Seidel began experiments with wetland plants for wastewater treatment in the 1950s (see Vymazal 2005, DOI 10.1016/j.ecoleng.2005.07.010, for this history). The idea was that common wetland plants, and the microbes around their roots, could do part of the work of a treatment plant. Later designers ran wastewater horizontally through gravel beds planted with reeds such as Phragmites australis, keeping the water below a dry surface.'
                 ' Recycling water inside a building raises a second problem, which this folio takes up: how to encourage living biology outside while keeping microbial growth in the indoor plumbing under control.',
 'act1_body': 'In high-performance regenerative architecture, water management must resolve the tension between '
              'ecological closed-loop conservation and stringent microbiological safety. In their foundational '
              'monograph Treatment Wetlands (DOI 10.1201/9781420012514), Robert Kadlec and Scott Wallace describe the first-order k-C* model used to size subsurface constructed wetlands. In this folio\'s worked example that model gives a 95.1 percent reduction in BOD_5; real beds vary with loading, temperature and age. Building water systems can also harbor biofilms of opportunistic organisms. ASHRAE Standard 188, Legionellosis: Risk Management for Building Water Systems, addresses Legionella risk; it does not prescribe this folio\'s design. The design here strictly isolates exterior non-potable greywater recycling from '
              'interior potable distribution networks. Open tools such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) for transport equations and dynamicslab/pysindy (DOI 10.1073/pnas.1517384113) for fitting rate laws could be used to study such a system; this folio does not run them. Its recirculating thermal loop and 254-nanometer UV-C reactor are design targets meant to limit biofilm growth near the point of use, not a tested installation.',
 'pullquote': '"A net-zero water building must master two opposite biological regimes: cultivating a thriving '
              'microbial rhizosphere outside in the gravel wetland while holding microbial growth down inside every sink trap and shower manifold."',
 'chronology': [('1950s–1960s',
                 'Käthe Seidel experiments with wetland plants for wastewater treatment in Germany.'),
                ('1996',
                 'Robert Kadlec & Robert Knight publish Treatment Wetlands; the second edition (Kadlec & Wallace 2008) is DOI 10.1201/9781420012514.'),
                ('2015',
                 'ASHRAE publishes Standard 188, Legionellosis: Risk Management for Building Water Systems.'),
                ('2017',
                 'Kotay et al. use a fluorescent marker organism to model bacterial dispersion from hand-washing sink traps (DOI 10.1128/AEM.03327-16).')],
 'act2_title': 'Act II — How It Actually Works: Kadlec–Knight Darcy Beds + Chick–Watson UV-C Fluence',
 'act2_intuition': 'The dual-boundary engineering of sustainable building water systems couples outdoor ecological '
                   'bioremediation with indoor photochemical disinfection. Outside the envelope, subsurface gravel '
                   'wetlands follow the first-order Kadlec-Knight plug-flow model, C_out = C* + (C_in - C*) * exp(-k_v '
                   '* tau_HRT), as described in Kadlec and Wallace (Treatment Wetlands, 2nd ed., DOI 10.1201/9781420012514). '
                   'Operating beneath a dry basalt gravel mulch cap avoids an open water surface while Phragmites '
                   'root zones supply oxygen to micro-aerobic biofilms, giving 95.1% BOD_5 removal across a 3.2-day retention time in the model. Inside the potable loop, ASHRAE Standard 188 addresses Legionella risk management in building water systems; it does not prescribe this design. The folio\'s own targets are continuous recirculation at or above 60 degrees Celsius and 0.6 meters per second, with no stagnant dead-legs. Downstream, an inline annular 254-nanometer UV-C '
                   'photoreactor delivers a germicidal fluence of H = 45 millijoules per square centimeter, which the folio\'s Chick-Watson model converts to a 5.4-log reduction (0.12 log per mJ/cm²). That rate constant is a design assumption. Hijnen et al. (2006, DOI 10.1016/j.watres.2005.10.030) review UV inactivation credit across viruses, bacteria and protozoa; the folio\'s own inference is that a single constant cannot represent every organism. '
                   'Nothing here was simulated in DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) or dynamicslab/pysindy (DOI 10.1073/pnas.1517384113); they are named as tools a reader could use to test the design.',
 'act2_analogy': 'Everyday analogy: Think of the difference between a swampy puddle and a high-alpine brook. A warm '
                 'puddle of rainwater sitting on a garden hose turns murky and slimy within days. In contrast, a '
                 'tumbling mountain stream flowing rapidly over clean granite gravel under intense alpine sunshine '
                 'stays sparkling, oxygenated, and clean. Bio-engineered plumbing aims to imitate that mountain stream: '
                 'subsurface gravel beds naturally filter outdoor greywater, while continuous hot circulation and '
                 'ultraviolet light help keep indoor pipes clean.',
 'walkthrough': ['Experiment 1 (Subsurface Wetland Sizing): Check that a 48 m^2 basalt-gravel bed (porosity phi = 0.38, depth 0.65 m) at a design flow of 3.7 m^3/d gives a 3.2-day retention time and, in the model, a 95.1% BOD_5 reduction.',
                 'Experiment 2 (Chick–Watson UV-C Inactivation): Trace how 254 nm UV-C fluence at H = 45 mJ/cm^2 '
                 'gives a 5.4-log reduction in the folio\'s single-constant model.',
                 'Experiment 3 (Sink-Trap Droplet Design Proposal): Inspect the CSI 22 13 00 self-heating thermal trap detail (proposed, untested) meant to reduce drain-splash droplets at clinical washbasins.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification Bridge',
 'act4_human_ai': 'Digital-twin hydraulic network solvers could monitor return-loop temperatures, flow velocities, and UV-C sensor transmittance to find dead-leg stagnation zones across hospital floors. Reactive advection-dispersion-reaction PDE solvers in DedalusProject/dedalus '
                  '(https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) combined with '
                  'sparse kinetic rate identification in dynamicslab/pysindy (DOI 10.1073/pnas.1517384113) could let a building digital twin track hydraulic loading rates and UV-C fluence margins. This is a proposal, not a deployed system.',
 'cf_bridge': 'Kotay et al. (2017, DOI 10.1128/AEM.03327-16) used a fluorescent marker organism to model how bacteria can disperse from hand-washing sink-trap reservoirs. An infection prevention and control guideline for Cystic Fibrosis has been published (Saiman et al. 2014, \'Infection Prevention and Control Guideline for Cystic Fibrosis: 2013 Update\', DOI 10.1086/676882). This folio is a plumbing design study. It reports no clinical outcome and is not infection-control advice; people with CF should follow their care team.',
 'sources': ['ASHRAE Standard 188 (2021 edition; first published 2015). Legionellosis: Risk Management for Building Water Systems.',
             'Kadlec, R. H., & Wallace, S. (2008). Treatment Wetlands (2nd ed.). CRC Press. DOI: '
             '10.1201/9781420012514.',
             'Kotay, S., Chai, W., Guilford, W., Barry, K., & Mathers, A. J. (2017). Spread from the Sink to the Patient: In Situ '
             'Study Using Green Fluorescent Protein (GFP)-Expressing Escherichia coli To Model Bacterial Dispersion from '
             'Hand-Washing Sink-Trap Reservoirs. Applied and Environmental Microbiology, 83(8), e03327-16. DOI: '
             '10.1128/AEM.03327-16.',
             'Saiman, L., et al. (2014). Infection Prevention and Control Guideline for Cystic Fibrosis: 2013 Update. '
             'Infection Control & Hospital Epidemiology, 35(S1), S1–S67. DOI: 10.1086/676882.',
             'Hijnen, W. A. M., Beerendonk, E. F., & Medema, G. J. (2006). Inactivation credit of UV radiation for viruses, '
             'bacteria and protozoan (oo)cysts in water: A review. Water Research, 40(1), 3–22. DOI: '
             '10.1016/j.watres.2005.10.030.',
             'Vymazal, J. (2005). Horizontal sub-surface flow and hybrid constructed wetlands systems for wastewater '
             'treatment. Ecological Engineering, 25(5), 478–490. DOI: 10.1016/j.ecoleng.2005.07.010.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). Dedalus: A flexible '
             'framework for numerical simulations with spectral methods (DedalusProject/dedalus, '
             'https://github.com/DedalusProject/dedalus). Physical Review Research, 2(2), 023068. DOI: '
             '10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations '
             'and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
             '882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Subsurface Kadlec-Knight wetland BOD '
        'decay and a 5.4-log Chick-Watson UV-C design dose (model)">\n'
        '            <rect x="45" y="45" width="265" height="135" fill="var(--tp-verdigris)" fill-opacity="0.10" '
        'stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <path d="M 60 65 Q 160 155 295 162" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="2.5"/>\n'
        '            <text x="60" y="34" font-size="11" fill="var(--tp-verdigris)">Subsurface Darcy Wetland (τ = 3.2 d '
        '· 95.1% BOD Removal)</text>\n'
        '            <text x="70" y="95" font-size="11" fill="currentColor">Inlet: 140 mg/L → Outlet: 6.8 mg/L</text>\n'
        '            <rect x="355" y="45" width="280" height="135" fill="var(--tp-prussian)" fill-opacity="0.10" '
        'stroke="var(--tp-prussian)" stroke-width="2"/>\n'
        '            <line x1="375" y1="62" x2="615" y2="165" stroke="var(--tp-minium)" stroke-width="2.8"/>\n'
        '            <text x="360" y="34" font-size="11" fill="var(--tp-prussian)">Potable Loop: 60°C Purge + 254 nm '
        'UV-C (CSI 22 13 00)</text>\n'
        '            <text x="385" y="92" font-size="11" fill="var(--tp-minium)">Chick-Watson H = 45 mJ/cm² → 5.4-Log '
        'Reduction</text>\n'
        '            <text x="385" y="148" font-size="11" fill="currentColor">Design target: limit sink-trap biofilm (not measured)</text>\n'
        '          </svg>',
 'history_lead': 'The German botanist Käthe Seidel began experiments with wetland plants for wastewater treatment in the 1950s (see Vymazal 2005, DOI 10.1016/j.ecoleng.2005.07.010, for this history). The idea was that common wetland plants, and the microbes around their roots, could do part of the work of a treatment plant. Later designers ran wastewater horizontally through gravel beds planted with reeds such as Phragmites australis, keeping the water below a dry surface.'
                 ' Recycling water inside a building raises a second problem, which this folio takes up: how to encourage living biology outside while keeping microbial growth in the indoor plumbing under control.',
 'act1_plain_bridge': 'Water in modern buildings is usually treated as a wasteful one-way street: clean drinking water '
                      'flows into our sinks and showers, gets used once, and flushes straight down the sewer. At the '
                      'same time, water sitting quietly inside lukewarm pipes can grow slimy bacterial coatings, like '
                      'a forgotten garden hose left in the summer sun. In hospitals and clean buildings, water must '
                      'perform two opposite jobs at once. Outside in the courtyard, gravel garden beds planted with '
                      'sturdy reeds filter sink and shower water naturally through plant roots, cleaning it so it can '
                      "be reused for flushing toilets and watering gardens. Meanwhile, inside the building's drinking "
                      'pipes, water is kept constantly circulating at hot temperatures and passes through intense '
                      'ultraviolet light chambers. This ultraviolet light damages the genetic material of waterborne bacteria so that fewer of them can multiply, adding one more barrier on the way to the tap.',
 'history_body': 'In high-performance regenerative architecture, water management must resolve the tension between '
                 'ecological closed-loop conservation and stringent microbiological safety. In their foundational '
                 'monograph Treatment Wetlands (DOI 10.1201/9781420012514), Robert Kadlec and Scott Wallace describe the first-order k-C* model used to size subsurface constructed wetlands. In this folio\'s worked example that model gives a 95.1 percent reduction in BOD_5; real beds vary with loading, temperature and age. Building water systems can also harbor biofilms of opportunistic organisms. ASHRAE Standard 188, Legionellosis: Risk Management for Building Water Systems, addresses Legionella risk; it does not prescribe this folio\'s design. The design here strictly isolates exterior non-potable greywater '
                 'recycling from interior potable distribution networks. Open tools such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) for transport equations and dynamicslab/pysindy (DOI 10.1073/pnas.1517384113) for fitting rate laws could be used to study such a system; this folio does not run them. Its recirculating thermal loop and 254-nanometer UV-C reactor are design targets meant to limit biofilm growth near the point of use, not a tested installation.',
 'act1_stakes': 'From Roman aqueducts to nineteenth-century municipal water grids, urban architecture operated on an '
                'unsustainable linear throughput model: extract potable water from distant reservoirs, use it once, '
                'and dump municipal effluent into coastal waterways. In response to regional water shortages, early '
                'green building initiatives aggressively introduced low-flow plumbing fixtures, reclaimed greywater '
                'cisterns, and unmonitored storage tanks. Conservation by rule of thumb can create a new risk. Reducing flow rates in oversized pipes can leave stagnant dead-legs where water sits lukewarm, between thirty and forty degrees Celsius. Under these conditions, opportunistic waterborne bacteria can colonize pipe walls and form biofilms that are harder to disinfect. Droplets from showerheads and sink drains are one route by which such organisms can reach people. Realizing true net-zero water requires mastering both ecological '
                'wetland biology outside and clinical thermal disinfection inside.',
 'act2_plain_primer': 'In the interactive laboratory below, you calibrate the dual biological barriers of a net-zero '
                      'water building. The first slider sets the hydraulic retention time of the outdoor gravel '
                      'wetland bed, measuring how many days greywater spends percolating through the reed root '
                      'systems. Extending this retention time gives the beneficial microbes living in the gravel more '
                      'time to consume soaps and organic nutrients, yielding clean, polished water ready for toilet '
                      'flushing and garden irrigation. The second slider controls the germicidal ultraviolet radiation '
                      'dose delivered inside the indoor potable water reactor. As you turn up this ultraviolet fluence '
                      'dial, ultraviolet light damages bacterial genetic material and keeps more of the organisms from reproducing. By balancing adequate '
                      'natural wetland residence time with an adequate ultraviolet dose, the model building recycles water while meeting its two design targets. The readouts are model outputs, not measurements. They are not a safety threshold and not infection-control advice; people with CF should follow their care team.',
 'distill_diagram': {'analogy_title': 'Mountain Stream vs Stagnant Hose',
                     'analogy_sub': 'Steady flow and ultraviolet light discourage microbial slime',
                     'force_a_title': 'Wetland Retention Time (τ_HRT)',
                     'force_a_sub': 'Extended gravel contact maximizes rhizosphere organic removal',
                     'force_b_title': 'UV-C Reactor Fluence (H_UV)',
                     'force_b_sub': 'Germicidal photon dose damages bacterial DNA',
                     'threshold_title': 'Folio Design Targets (Model)',
                     'threshold_pass': 'At least 85% BOD removal and a 4-log UV-C design dose',
                     'threshold_fail': 'Below a design target: short retention or low UV-C dose'},
 'intuition_lead': 'The dual-boundary engineering of sustainable building water systems couples outdoor ecological '
                   'bioremediation with indoor photochemical disinfection. Outside the envelope, subsurface gravel '
                   'wetlands follow the first-order Kadlec-Knight plug-flow model, C_out = C* + (C_in - C*) * exp(-k_v '
                   '* tau_HRT), as described in Kadlec and Wallace (Treatment Wetlands, 2nd ed., DOI 10.1201/9781420012514). '
                   'Operating beneath a dry basalt gravel mulch cap avoids an open water surface while Phragmites '
                   'root zones supply oxygen to micro-aerobic biofilms, giving 95.1% BOD_5 removal across a 3.2-day retention time in the model. Inside the potable loop, ASHRAE Standard 188 addresses Legionella risk management in building water systems; it does not prescribe this design. The folio\'s own targets are continuous recirculation at or above 60 degrees Celsius and 0.6 meters per second, with no stagnant dead-legs. Downstream, an inline annular 254-nanometer UV-C '
                   'photoreactor delivers a germicidal fluence of H = 45 millijoules per square centimeter, which the folio\'s Chick-Watson model converts to a 5.4-log reduction (0.12 log per mJ/cm²). That rate constant is a design assumption. Hijnen et al. (2006, DOI 10.1016/j.watres.2005.10.030) review UV inactivation credit across viruses, bacteria and protozoa; the folio\'s own inference is that a single constant cannot represent every organism. '
                   'Nothing here was simulated in DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) or dynamicslab/pysindy (DOI 10.1073/pnas.1517384113); they are named as tools a reader could use to test the design.',
 'act2_deepening': "The wetland and the potable loop work at different scales and never share water. In the subsurface reed bed, Darcy's law Q = K_s * A_c * S sets the horizontal seepage through basalt gravel. If the hydraulic retention time is cut too short by overloading the bed with greywater, organic matter passes through the root zone unoxidized and the outlet turns more turbid. That matters for reuse: if greywater were later disinfected with UV for non-potable uses, turbid effluent would scatter the light and need a higher dose. In this design the potable UV-C reactor never receives greywater; the two systems stay separate. At clinical sink basins, offset drains and self-heating P-traps are proposed to reduce drain droplets (untested).",
 'act4_deepening': 'In modern architectural hydro-engineering, building engineers and AI digital twin agents could manage water quality with predictive analytics. This is a proposal; no such system exists here. Alongside periodic manual testing, plumbing networks could monitor flow velocities, return-loop temperatures, and UV transmittance sensors across every vertical pipe riser. If occupancy drops on an inpatient hospital floor over a holiday weekend, an agent could detect likely stagnation and start targeted high-temperature flush cycles meant to reduce it. Outside, weather-aware algorithms could adjust greywater dosing across wetland gravel cells ahead of heavy rain. An active '
                   'frontier challenge focuses on closed-loop decentralized biosensors: can microfluidic '
                   'DNA-sequencing chips integrated directly into clinical plumbing manifolds continuously monitor '
                   'microbial biodiversity, autonomously alerting infection control teams to emerging '
                   'antibiotic-resistant genetic markers before waterborne biofilms can colonize patient care areas? '
                   'Such integration would make net-zero water a public-health design question as well as a conservation goal.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a regenerative hospital courtyard with subsurface constructed '
        'botanical wetlands and a UV-C water manifold would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate A.06-V (Imagining What It Would Look Like) · Artistic architectural section '
            'imagining a hospital courtyard integrating terraced subsurface gravel-reed wetlands above a '
            'stainless-steel UV-C water purification vault.'}

DISPATCH = {'kicker': 'FRONTIER PLUMBING-DESIGN DISPATCH · LEGIONELLA RISK MANAGEMENT & PATHOGEN-CONTROL PLUMBING',
 'headline': 'Sink Drains as Bacterial Reservoirs: What Thermal Recirculation and UV-C Are Designed to Limit',
 'body': 'Kotay et al. (2017, DOI 10.1128/AEM.03327-16) used a fluorescent marker organism to model bacterial dispersion from hand-washing sink traps. This folio pairs an external Kadlec–Knight greywater wetland with an internal 45 mJ/cm² UV-C and 60 °C recirculation loop as a design response; the 5.4-log figure is a model value, not a measured result.'}

META_3D = ('Terraced Subsurface Wetland & UV-C Fluence Basin',
 'X: Hydraulic Residence Path · Z: Reed-Bed Width · Y: Kadlec–Knight BOD Decay & UV-C Dose')

ES_TRANSLATION = {'title_es': 'Humedales Construidos de Agua Neta Cero: Filtración Subsuperficial de Darcy, Fotólisis UV-C y Plomería para Control de Patógenos (CSI 22 13 00)',
 'subtitle_es': 'Cómo un lecho subsuperficial modelado reduce alrededor del 95% de la DBO_5 de las aguas grises en el exterior, mientras la recirculación a 60 °C y un reactor UV-C de 254 nm son metas de diseño para limitar el crecimiento de Pseudomonas y Legionella en el interior.',
 'why_es': 'Una manguera estancada al sol desarrolla biopelículas en pocos días, mientras que un arroyo de montaña en '
           'flujo continuo bajo luz ultravioleta tiende a permanecer limpio.',
 'bridge_es': 'Kotay et al. 2017 usaron un organismo marcador para modelar cómo las bacterias pueden dispersarse desde el sifón de un lavabo (DOI 10.1128/AEM.03327-16). Existe una guía de prevención y control de infecciones para Fibrosis Quística (Saiman et al. 2014, DOI 10.1086/676882). Este folio es un estudio de diseño de plomería: no reporta resultados clínicos, no es una recomendación de control de infecciones y no sustituye las indicaciones del equipo de atención.',
 'plain_es': 'El agua en los edificios modernos suele tratarse como un recurso desechable de un solo uso: entra agua '
             'potable limpia por los grifos, se utiliza una sola vez y se va directamente al drenaje. Al mismo tiempo, '
             'el agua tibia estancada dentro de tuberías mal diseñadas puede acumular biopelículas viscosas de '
             'bacterias, como una manguera de jardín olvidada bajo el sol de verano. En edificios ecológicos y '
             'hospitales modernos, el agua debe cumplir dos funciones opuestas a la vez. En los jardines exteriores, '
             'lechos de grava sembrados con carrizos y juncos filtran de manera natural las aguas grises de lavabos y '
             'regaderas mediante las raíces de las plantas, tratándolas para reutilizarlas en inodoros y riego. '
             'Mientras tanto, en las tuberías interiores, el agua caliente se mantiene en circulación continua a sesenta grados antes de las válvulas mezcladoras y pasa por cámaras de luz ultravioleta que dañan el material genético de las bacterias para que menos de ellas puedan multiplicarse, como una barrera más antes del grifo.',
 'deep_es': 'La ingeniería hidrosanitaria sustentable opera bajo un esquema biológico dual: biorremediación ecológica en el exterior y control térmico y por luz ultravioleta en el interior (metas de diseño). En el humedal subsuperficial, las '
            'aguas grises fluyen bajo una capa seca de grava volcánica donde, en el modelo del folio, la rizosfera reduce alrededor del noventa y cinco por ciento de la DBO_5; mantener el agua bajo la grava limita el contacto con la superficie. En las '
            'redes interiores de agua potable, el diseño del folio usa recirculación continua a sesenta grados Celsius para evitar zonas de estancamiento donde proliferan patógenos oportunistas como '
            'Pseudomonas y Legionella. Complementariamente, un reactor ultravioleta en línea de 254 nanómetros aplica '
            'una dosis germicida que, en el modelo del folio, equivale a 5.4 reducciones logarítmicas; es un valor de diseño, no una medición. En la práctica profesional, los ingenieros modelan estos sistemas mediante '
            'herramientas computacionales en computadora, diseñando lavabos clínicos con desagües desfasados que '
            'buscan reducir las gotas y salpicaduras del desagüe.'}
