#!/usr/bin/env python3
"""Folio A.06 (ARCHITECTURE): Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis and Hot-Water Recirculation (Design Study)."""
from __future__ import annotations

SLUG = 'a06'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.06',
 'slug': 'a06',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Net-Zero Water & Greywater Constructed Wetlands: Subsurface Darcy Filtration, UV-C Photolysis and Hot-Water Recirculation (Design Study)',
 'subtitle': 'How a modeled subsurface reed bed removes about 95% of greywater BOD_5 outside, while 60 °C recirculation and a 254 nm UV-C reactor are design targets meant to limit growth of opportunistic waterborne bacteria inside.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/tectonic_verify.py',
 'colophon': {'identifier': 'A.06 · Hydro-Tectonics',
              'kernels': 'Kadlec-Knight k-C* · Chick-Watson 5.4-Log UV-C',
              'benchmarks': 'Model values: 95.1% BOD_5 removal · 5.4-log UV-C design dose',
              'bridge': 'Biofilm-Control Plumbing'},
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
 'steps': ['Stage 1 (Subsurface Horizontal Darcy Filtration): Greywater flows through washed basalt gravel '
           '(φ = 0.38, K_s = 120 m/d) with its water level 150 mm below the gravel surface and no open water surface '
           '(a 0.80 m deep bed: 0.65 m saturated below a 150 mm dry layer).',
           'Stage 2 (Rhizosphere Biofilm Oxidation): Phragmites root-zone oxygen transfer drives Kadlec-Knight '
           'exponential BOD_5 decay from 140 mg/L to 6.8 mg/L (τ = 3.2 d) in the folio model, with the folio\'s assumed C* = 3.0 mg/L and k = 1.12 per day.',
           'Stage 3 (Dead-Leg-Free 60 °C Potable Recirculation): Copper-silver / stainless manifold designed to target v ≥ 0.6 m/s and T ≥ 60 °C up to every point-of-use mixing valve (design target, not measured).',
           'Stage 4 (254 nm UV-C Photolysis & Thermal Trap Purge): Delivers H = 45 mJ/cm² UV-C fluence (a 5.4-log reduction in the folio\'s Chick-Watson model) plus self-heating sink traps.'],
 'readouts': [{'label': 'Wetland BOD_5 Reduction', 'value': '95.1% (140 → 6.8 mg/L)'},
              {'label': 'UV-C Log Reduction (Model)', 'value': '5.4-Log (45 mJ/cm²)'},
              {'label': 'Thermal Loop Design Target', 'value': '60.0 °C (v = 0.65 m/s)'},
              {'label': 'Design Check (Model)', 'value': 'MODEL VALUES ABOVE FOLIO TARGETS (85% BOD, 4-LOG)'}],
 'sidenote_1': {'kicker': 'SIDENOTE A.06-A · SUBSURFACE HYDRAULIC GRADE LINE',
                'body': 'Keeping the Darcy water table 150 mm below the gravel surface (a 0.80 m bed with 0.65 m saturated depth) is meant to limit mosquito breeding, odor, and human contact with untreated greywater.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.06-B · SPECIFICATION PLATE · CSI 22 13 00 / 22 42 00',
                'body': 'Offset drain clinical washbasin with an automated 65 °C thermal P-trap cycle, intended to reduce droplet dispersal from the drain. Kotay et al. (2017, DOI 10.1128/AEM.03327-16) modeled sink-trap dispersal with a marker organism; this fixture is a design proposal and has not been tested.'},
 'skill': {'filename': 'netzero-water-pathogen-plumbing-SKILL.md',
           'name': 'netzero-water-pathogen-plumbing',
           'description': 'AI-agnostic architectural hydro-engineering skill for Kadlec-Knight subsurface constructed wetlands and biofilm-control clinical plumbing design targets.',
           'rules': ["Size subsurface horizontal-flow wetlands via Darcy's law Q = K_s A_c S and Kadlec-Knight "
                     'kinetics C_out = C* + (C_in - C*) exp(-k_v * tau).',
                     'This folio\'s own design target (not a standard or a clinical requirement): potable hot-water recirculation >= 60 C at velocity >= 0.6 m/s, '
                     'with no stagnant dead-legs.',
                     'Apply the folio\'s design targets of a 4-log model reduction (254 nm UV-C fluence H >= 34 mJ/cm^2 at 0.12 log per mJ/cm^2) and non-splashing offset drains; report log reductions as model values, never as measured outcomes.']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. Earlier editions said the design '
                           'eradicates pathogens and showed a zero-biofilm verdict; nothing here was measured, '
                           'so those statements are withdrawn and every number is labeled as a model value. '
                           'The opening scene about Käthe '
                           'Seidel was not sourced and is replaced by a plain account. '
                           'A later review corrected the title (the CSI 22 13 00 label and "pathogen-control" are removed), '
                           'stated the assumed wetland constants and a consistent bed depth, and softened the readout verdict '
                           'and the Spanish text.',
                'opus': 'Review: new references checked by DOI in Crossref and the Scite index.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Modeled 95.1% Kadlec-Knight BOD_5 greywater reduction and a 5.4-log Chick-Watson UV-C design dose with a 60 °C thermal loop.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' wording is withdrawn in REV 1.2: nothing was measured, and ASHRAE 188 does not prescribe this design.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph coupling net-zero subsurface '
                           'greywater wetlands with clinical plumbing.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified inactivation\' wording is withdrawn in REV 1.2: nothing was measured.'}],
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
 'act1_title': 'Act I — From Roman Cisterns to Net-Zero Bio-Engineered Wetlands & Hot-Water Recirculation Design',
 'act1_dropcap': 'In the 1950s, German botanist Käthe Seidel began testing common wetland plants to treat wastewater. The idea was that common wetland plants and the microbes around their roots could do part of a treatment plant\'s work. Later engineers routed wastewater horizontally through gravel beds planted with reeds such as Phragmites australis, keeping the water below a dry stone surface. Reusing water inside a building raises the opposite challenge. A designer has to encourage living biology in the outdoor gravel bed while limiting microbial growth inside indoor drinking-water pipes.',
 'act1_body': 'Vymazal (2005, DOI 10.1016/j.ecoleng.2005.07.010) traces Seidel\'s 1950s experiments to modern horizontal subsurface-flow wetlands. In Treatment Wetlands (DOI 10.1201/9781420012514), Robert Kadlec and Scott Wallace describe the first-order k-C* model used to size those beds. In this folio\'s worked example, that model yields a 95.1 percent reduction in BOD_5, though real beds vary with loading, temperature, and age. Building plumbing can also harbor biofilms of opportunistic organisms. ASHRAE Standard 188, Legionellosis: Risk Management for Building Water Systems, addresses Legionella risk; it does not prescribe this folio\'s design. Here, exterior non-potable greywater recycling stays isolated from interior potable networks. Open tools such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) for transport equations and the SINDy method (Brunton et al. 2016, DOI 10.1073/pnas.1517384113; implemented in dynamicslab/pysindy) for fitting rate laws could study such a system, but this folio does not run them. Its hot recirculation loop and 254-nanometer UV-C reactor are design targets meant to limit biofilm growth near the point of use, not a tested installation.',
 'pullquote': '"A net-zero water building must master two opposite biological regimes: cultivating a thriving '
              'microbial rhizosphere outside in the gravel wetland while holding microbial growth down inside every sink trap and shower manifold."',
 'chronology': [('1950s–1960s',
                 'Käthe Seidel experiments with wetland plants for wastewater treatment in Germany (Vymazal 2005, DOI 10.1016/j.ecoleng.2005.07.010).'),
                ('1996',
                 'Robert Kadlec & Robert Knight publish Treatment Wetlands; the second edition (Kadlec & Wallace 2008) is DOI 10.1201/9781420012514.'),
                ('2015',
                 'ASHRAE publishes Standard 188, Legionellosis: Risk Management for Building Water Systems.'),
                ('2017',
                 'Kotay et al. use a fluorescent marker organism to model bacterial dispersion from hand-washing sink traps (DOI 10.1128/AEM.03327-16).')],
 'act2_title': 'Act II — How It Actually Works: Kadlec–Knight Darcy Beds + Chick–Watson UV-C Fluence',
 'act2_intuition': 'Dual-boundary building water design pairs outdoor bioremediation with indoor photochemical disinfection. Outside, subsurface gravel '
                   'wetlands follow the first-order Kadlec-Knight plug-flow model, C_out = C* + (C_in - C*) * exp(-k_v '
                   '* tau_HRT) (Kadlec & Wallace, Treatment Wetlands, 2nd ed., DOI 10.1201/9781420012514). '
                   'A dry basalt gravel cap avoids an open water surface while Phragmites '
                   'root zones oxygenate micro-aerobic biofilms, giving 95.1% BOD_5 removal across a 3.2-day retention time in the model (with C_in = 140 mg/L and the folio\'s assumed C* = 3.0 mg/L and k = 1.12 per day, C_out = 3.0 + 137 × e^(−1.12 × 3.2) = 6.8 mg/L). Inside the potable loop, ASHRAE Standard 188 addresses Legionella risk management in building water systems; it does not prescribe this design. The folio\'s own targets are continuous recirculation at or above 60 degrees Celsius and 0.6 meters per second, with no stagnant dead-legs. Downstream, an inline 254-nanometer UV-C '
                   'reactor delivers H = 45 millijoules per square centimeter, which the folio\'s Chick-Watson model converts to a 5.4-log reduction (0.12 log per mJ/cm²). That rate constant is a design assumption. Hijnen et al. (2006, DOI 10.1016/j.watres.2005.10.030) review UV inactivation credit across viruses, bacteria, and protozoa; this folio\'s inference is that a single constant cannot represent every organism. '
                   'Nothing here was simulated in DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) or the SINDy method (Brunton et al. 2016, DOI 10.1073/pnas.1517384113; implemented in dynamicslab/pysindy); they are named as tools a reader could use to test the design.',
 'act2_analogy': 'Think of the difference between a stagnant garden hose in summer sun and a fast mountain brook. Warm water sitting in a hose turns murky and slimy within days, while a stream tumbling over clean gravel under bright alpine sunlight stays oxygenated and clear. This design borrows that contrast: buried gravel beds filter outdoor greywater, while hot circulation and ultraviolet light are meant to limit microbial growth in indoor pipes. Where the picture stops: an alpine stream has no buried root zone or heated return loop, turbid water scatters ultraviolet light, and, by this folio\'s inference, a single UV rate constant cannot represent every organism.',
 'walkthrough': ['Experiment 1 (Subsurface Wetland Sizing): Check that a 48 m^2 basalt-gravel bed (porosity phi = 0.38, 0.80 m deep with a 150 mm dry layer on top, so 0.65 m saturated depth) at 3.7 m^3/d gives a retention time of 48 × 0.65 × 0.38 / 3.7 = 3.2 days and, with assumed C* = 3.0 mg/L and k = 1.12 per day, 95.1% BOD_5 removal (140 → 6.8 mg/L); the >= 85% target holds from tau = 2.0 d upward on the 0.2 d slider grid.',
                 'Experiment 2 (Chick–Watson UV-C Dose & Fixed Thermal Target): Trace how 254 nm UV-C fluence at H = 45 mJ/cm^2 '
                 'gives a 5.4-log reduction in the single-constant model (meeting the >= 4-log target from 34 mJ/cm^2 upward on the 1 mJ/cm^2 slider grid). The 60.0 °C (v = 0.65 m/s) thermal loop readout stays fixed as a design target and does not change with either slider.',
                 'Experiment 3 (Sink-Trap Droplet Design Proposal): Inspect the CSI 22 13 00 self-heating thermal trap detail (proposed, untested) meant to reduce drain-splash droplets at clinical washbasins.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification Bridge',
 'act4_human_ai': 'Digital-twin hydraulic solvers could track return-loop temperatures, velocities, and UV-C transmittance to flag dead-leg stagnation zones across hospital floors. Spectral transport solvers in DedalusProject/dedalus '
                  '(https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) paired with '
                  'sparse kinetic rate identification in the SINDy method (Brunton et al. 2016, DOI 10.1073/pnas.1517384113; implemented in dynamicslab/pysindy) could monitor hydraulic loading and UV-C fluence margins. This is a proposal, not a deployed system.',
 'cf_bridge': 'Kotay et al. (2017, DOI 10.1128/AEM.03327-16) used a fluorescent marker organism to model how bacteria can disperse from hand-washing sink-trap reservoirs. This folio is a plumbing design study. It reports no clinical outcome and is not infection-control advice.',
 'sources': ['ASHRAE Standard 188 (2021 edition; first published 2015). Legionellosis: Risk Management for Building Water Systems.',
             'Kadlec, R. H., & Wallace, S. (2008). Treatment Wetlands (2nd ed.). CRC Press. DOI: '
             '10.1201/9781420012514.',
             'Kotay, S., Chai, W., Guilford, W., Barry, K., & Mathers, A. J. (2017). Spread from the Sink to the Patient: In Situ '
             'Study Using Green Fluorescent Protein (GFP)-Expressing Escherichia coli To Model Bacterial Dispersion from '
             'Hand-Washing Sink-Trap Reservoirs. Applied and Environmental Microbiology, 83(8), e03327-16. DOI: '
             '10.1128/AEM.03327-16.',
             'Hijnen, W. A. M., Beerendonk, E. F., & Medema, G. J. (2006). Inactivation credit of UV radiation for viruses, '
             'bacteria and protozoan (oo)cysts in water: A review. Water Research, 40(1), 3–22. DOI: '
             '10.1016/j.watres.2005.10.030.',
             'Vymazal, J. (2005). Horizontal sub-surface flow and hybrid constructed wetlands systems for wastewater '
             'treatment. Ecological Engineering, 25(5), 478–490. DOI: 10.1016/j.ecoleng.2005.07.010.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). Dedalus: A flexible '
             'framework for numerical simulations with spectral methods (DedalusProject/dedalus, '
             'https://github.com/DedalusProject/dedalus). Physical Review Research, 2(2), 023068. DOI: '
             '10.1103/PhysRevResearch.2.023068.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse '
             'identification of nonlinear dynamical systems. Proceedings of the National Academy of Sciences, 113(15), '
             '3932–3937. DOI: 10.1073/pnas.1517384113.',
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
        'UV-C (design targets)</text>\n'
        '            <text x="385" y="92" font-size="11" fill="var(--tp-minium)">Chick-Watson H = 45 mJ/cm² → 5.4-Log '
        'Reduction</text>\n'
        '            <text x="385" y="148" font-size="11" fill="currentColor">Design target: limit sink-trap biofilm (not measured)</text>\n'
        '          </svg>',
 'history_lead': 'In the 1950s, German botanist Käthe Seidel began testing common wetland plants to treat wastewater. The idea was that common wetland plants and the microbes around their roots could do part of a treatment plant\'s work. Later engineers routed wastewater horizontally through gravel beds planted with reeds such as Phragmites australis, keeping the water below a dry stone surface. Reusing water inside a building raises the opposite challenge. A designer has to encourage living biology in the outdoor gravel bed while limiting microbial growth inside indoor drinking-water pipes.',
 'act1_plain_bridge': 'Most buildings treat water as a one-way street. Clean drinking water flows from taps and showers, gets used once, and leaves through the sewer. Meanwhile, lukewarm water sitting still in indoor pipes can grow slimy bacterial coatings, much like a garden hose left in summer sun. In hospitals and other clean buildings, water must perform two opposite tasks at once. Outside, buried gravel beds planted with sturdy reeds filter sink and shower water through their root zones. That cleaned water can then supply toilets and gardens instead of drinking taps. Inside the drinking-water pipes, the design does the reverse. Water keeps circulating at hot temperatures and passes through an intense ultraviolet light chamber. This ultraviolet light damages the genetic material of waterborne bacteria so fewer can multiply, adding one more barrier before the tap.',
 'history_body': 'Vymazal (2005, DOI 10.1016/j.ecoleng.2005.07.010) traces Seidel\'s 1950s experiments to modern horizontal subsurface-flow wetlands. In Treatment Wetlands (DOI 10.1201/9781420012514), Robert Kadlec and Scott Wallace describe the first-order k-C* model used to size those beds. In this folio\'s worked example, that model yields a 95.1 percent reduction in BOD_5, though real beds vary with loading, temperature, and age. Building plumbing can also harbor biofilms of opportunistic organisms. ASHRAE Standard 188, Legionellosis: Risk Management for Building Water Systems, addresses Legionella risk; it does not prescribe this folio\'s design. Here, exterior non-potable greywater recycling stays isolated from interior potable networks. Open tools such as DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) for transport equations and the SINDy method (Brunton et al. 2016, DOI 10.1073/pnas.1517384113; implemented in dynamicslab/pysindy) for fitting rate laws could study such a system, but this folio does not run them. Its hot recirculation loop and 254-nanometer UV-C reactor are design targets meant to limit biofilm growth near the point of use, not a tested installation.',
 'act1_stakes': 'From Roman aqueducts to modern municipal grids, buildings have mostly used water once and sent it to sewers. Low-flow fixtures and reclaimed greywater cisterns reduce municipal demand, but conservation by rule of thumb can introduce another risk. Lower flow in oversized pipes can leave stagnant dead-legs where water sits lukewarm, between thirty and forty degrees Celsius. In that range, opportunistic waterborne bacteria can colonize pipe walls and form biofilms that are harder to disinfect, and droplets from showerheads or sink drains can carry those organisms to people. Balancing water reuse with indoor microbial control requires separating outdoor wetland biology from indoor thermal and ultraviolet design targets.',
 'act2_plain_primer': 'The interactive panel below varies two model parameters for this building concept. The first slider sets the outdoor gravel wetland retention time in days. Longer retention gives root-zone microbes more time to break down soaps and organic waste; the design check looks for at least 85 percent removal in the model. The second slider sets the indoor ultraviolet reactor fluence. Higher fluence raises the single-constant model log reduction; the design check looks for at least a 4-log model reduction. The third readout, a 60 degrees Celsius thermal loop at 0.65 meters per second (above the 0.6 meters per second minimum target), stays fixed as a design target and is not computed from either slider. The readouts are model outputs, not measurements. They are not a safety threshold and not infection-control advice.',
 'distill_diagram': {'analogy_title': 'Mountain Stream vs Stagnant Hose',
                     'analogy_sub': 'Steady flow and ultraviolet light discourage microbial slime',
                     'force_a_title': 'Wetland Retention Time (τ_HRT)',
                     'force_a_sub': 'Extended gravel contact maximizes rhizosphere organic removal',
                     'force_b_title': 'UV-C Reactor Fluence (H_UV)',
                     'force_b_sub': 'Germicidal photon dose damages bacterial DNA',
                     'threshold_title': 'Folio Design Targets (Model)',
                     'threshold_pass': 'At least 85% BOD removal and a 4-log UV-C design dose',
                     'threshold_fail': 'Below a design target: short retention or low UV-C dose'},
 'intuition_lead': 'Dual-boundary building water design pairs outdoor bioremediation with indoor photochemical disinfection. Outside, subsurface gravel '
                   'wetlands follow the first-order Kadlec-Knight plug-flow model, C_out = C* + (C_in - C*) * exp(-k_v '
                   '* tau_HRT) (Kadlec & Wallace, Treatment Wetlands, 2nd ed., DOI 10.1201/9781420012514). '
                   'A dry basalt gravel cap avoids an open water surface while Phragmites '
                   'root zones oxygenate micro-aerobic biofilms, giving 95.1% BOD_5 removal across a 3.2-day retention time in the model (with C_in = 140 mg/L and the folio\'s assumed C* = 3.0 mg/L and k = 1.12 per day, C_out = 3.0 + 137 × e^(−1.12 × 3.2) = 6.8 mg/L). Inside the potable loop, ASHRAE Standard 188 addresses Legionella risk management in building water systems; it does not prescribe this design. The folio\'s own targets are continuous recirculation at or above 60 degrees Celsius and 0.6 meters per second, with no stagnant dead-legs. Downstream, an inline 254-nanometer UV-C '
                   'reactor delivers H = 45 millijoules per square centimeter, which the folio\'s Chick-Watson model converts to a 5.4-log reduction (0.12 log per mJ/cm²). That rate constant is a design assumption. Hijnen et al. (2006, DOI 10.1016/j.watres.2005.10.030) review UV inactivation credit across viruses, bacteria, and protozoa; this folio\'s inference is that a single constant cannot represent every organism. '
                   'Nothing here was simulated in DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI 10.1103/PhysRevResearch.2.023068) or the SINDy method (Brunton et al. 2016, DOI 10.1073/pnas.1517384113; implemented in dynamicslab/pysindy); they are named as tools a reader could use to test the design.',
 'act2_deepening': "The wetland and the potable loop never share water. In the reed bed, Darcy's law Q = K_s * A_c * S sets horizontal seepage through basalt gravel, so overloading the bed cuts retention time and sends unoxidized organic matter and cloudier outflow downstream. If greywater were later treated with UV for non-potable reuse, turbid effluent would scatter light and demand a higher dose. Here, the two networks stay isolated: the potable UV-C reactor never receives greywater. At clinical basins, offset drains and self-heating P-traps are proposed to reduce drain droplets (untested).",
 'act4_deepening': 'Building engineers and AI digital-twin agents could monitor plumbing networks alongside periodic manual sampling; this is a proposal, and no such system exists here. Sensors across pipe risers could track flow velocity, return-loop temperature, and UV transmittance. If occupancy drops on an inpatient floor over a holiday weekend, an agent could flag likely stagnation for staff review, while weather-aware controls could adjust greywater dosing across wetland cells before heavy rain. An open question, not a result: could inline biosensors monitor microbial communities in building plumbing? That idea is untested, and this folio draws no conclusion.'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a regenerative hospital courtyard with subsurface constructed '
        'botanical wetlands and a UV-C water manifold would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate A.06-V (Imagining What It Would Look Like) · Artistic architectural section '
            'imagining a hospital courtyard integrating terraced subsurface gravel-reed wetlands above a '
            'stainless-steel UV-C water purification vault.'}

DISPATCH = {'kicker': 'FRONTIER PLUMBING-DESIGN DISPATCH · LEGIONELLA RISK MANAGEMENT & HOT-WATER RECIRCULATION',
 'headline': 'Sink Drains as Bacterial Reservoirs: What Thermal Recirculation and UV-C Are Designed to Limit',
 'body': 'Kotay et al. (2017, DOI 10.1128/AEM.03327-16) used a fluorescent marker organism to model bacterial dispersion from hand-washing sink traps. This folio pairs an external Kadlec–Knight greywater wetland with an internal 45 mJ/cm² UV-C and 60 °C recirculation loop as a design response; the 5.4-log figure is a model value, not a measured result.'}

META_3D = ('Terraced Subsurface Wetland & UV-C Fluence Basin',
 'X: Hydraulic Residence Path · Z: Reed-Bed Width · Y: Kadlec–Knight BOD Decay & UV-C Dose')

ES_TRANSLATION = {'title_es': 'Agua Neta Cero y Humedales Construidos para Aguas Grises: Filtración Subsuperficial de Darcy, Fotólisis UV-C y Recirculación de Agua Caliente (Estudio de Diseño)',
 'subtitle_es': 'Cómo un lecho subsuperficial de carrizos, modelado, elimina alrededor del 95% de la DBO_5 de las aguas grises en el exterior, mientras la recirculación a 60 °C y un reactor UV-C de 254 nm son metas de diseño para limitar el crecimiento de bacterias oportunistas transmitidas por el agua en el interior.',
 'why_es': 'Una manguera estancada al sol desarrolla biopelículas en pocos días, mientras que un arroyo de montaña en '
           'flujo continuo bajo luz ultravioleta tiende a permanecer limpio. Donde termina la imagen: un arroyo no tiene lecho enterrado ni circuito caliente, el agua turbia dispersa la luz ultravioleta y, según la inferencia de este folio, una sola constante no representa a todos los organismos.',
 'plain_es': 'Casi todos los edificios usan el agua en un solo sentido. El agua potable entra por lavabos y regaderas, se usa una vez y se va al drenaje. Mientras tanto, el agua tibia estancada en tuberías interiores puede formar capas viscosas de bacterias, como una manguera olvidada al sol. En hospitales y edificios limpios, el agua debe cumplir dos tareas opuestas. Afuera, lechos enterrados de grava con carrizos filtran el agua gris mediante sus raíces para reutilizarla en inodoros y riego. Adentro, el diseño busca lo contrario en la red potable. El agua circula caliente sin detenerse y pasa por una cámara de luz ultravioleta intensa. Esa luz daña el material genético de las bacterias para que menos puedan multiplicarse, una barrera adicional antes del grifo.',
 'deep_es': 'Este estudio separa la biorremediación exterior de las metas de diseño térmicas y UV-C interiores. En el humedal subsuperficial, las aguas grises fluyen bajo grava seca donde, en el modelo a τ = 3.2 días, la rizosfera reduce 95.1% de la DBO_5 (C_ent = 140 mg/L y los valores supuestos del folio C* = 3.0 mg/L y k = 1.12 por día, C_sal = 3.0 + 137 × e^(−1.12 × 3.2) = 6.8 mg/L; meta ≥ 85% desde τ = 2.0 d en pasos de 0.2 d). En la red potable, el circuito a 60.0 °C y 0.65 m/s (sobre la meta mínima de 0.6 m/s, sin ramales muertos) se muestra como meta de diseño fija y no cambia con los controles. El reactor UV-C de 254 nm modela 5.4 reducciones logarítmicas a 45 mJ/cm² (meta ≥ 4-log desde 34 mJ/cm² en pasos de 1 mJ/cm² del control); es un valor de diseño, no una medición. Herramientas abiertas como Dedalus o PySINDy podrían usarse para estudiar un sistema así; este folio no las ejecutó, y el lavabo con desagüe desfasado es una propuesta sin probar.'}
