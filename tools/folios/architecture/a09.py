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
 'subtitle': 'Completing Folios A.02, E.04, and A.08: an explanatory model—not a structural design '
             "method—adapting Stephen Timoshenko's 1925 bilayer curvature formula to wood plies "
             'that bend with humidity.',
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'HYGROSCOPIC TIMBER · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 '
                  '18 00',
 'colophon': {'identifier': 'A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00',
              'kernels': 'Timoshenko Bilayer Curvature · Orthotropic Wood Sorption (α_T vs. α_L)',
              'benchmarks': 'Model values: ΔMC = +6.0% · h = 6.0 mm · m = 2 · n = 10.6 ⇒ κ = 1.42 '
                            'm⁻¹ · δ_tip = 128.2 mm (slider) / 128.6 mm (unrounded ½ κ L²)',
              'bridge': 'Completes A.02/E.04 · Wood Cell-Wall Swelling'},
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
 'steps': ['Stage 1 (Orthotropic Cell-Wall Sorption): Below fiber saturation (assumed ~28% MC), '
           'this model assumes European beech swells tangentially at α_T = 0.0032 per %MC '
           '(0.32%/%MC) and longitudinally at α_L = 0.00012 per %MC (0.012%/%MC); both are assumed '
           'round constants.',
           'Stage 2 (Timoshenko Adaptation, DOI 10.1364/JOSA.11.000233): Bonding passive '
           'longitudinal restraint ply 1 (h_1, E_1) to active tangential ply 2 (h_2, E_2) with Δε '
           '= (α_T − α_L)ΔMC = 0.01848 and assumed m = h_1/h_2 = 2, n = E_1/E_2 = 10.6 gives f = '
           '0.4621 and κ = 1.4234 m⁻¹ (1.42 m⁻¹ rounded; m = n = 1 gives 4.62 m⁻¹).',
           'Stage 3 (Slider Heuristic & Boundary): At L = 425 mm, unrounded κ = 1.4234 m⁻¹ gives ½ '
           'κ L² = 128.6 mm (124.7 mm arc), while the page slider scales from 1.42 m⁻¹ to 128.2 mm '
           '(240 mm cap) and scales vent area in [12%, 92%]. Not for real structures.',
           'Stage 4 (Self-Shaping Mass Timber): Grönquist et al. (2019, DOI '
           '10.1126/sciadv.aax1311) modeled self-shaping wood bilayers for curved mass timber, '
           'applied in Urbach Tower components (Wood et al. 2020).'],
 'readouts': [{'label': 'Timoshenko Curvature (κ, Model)', 'value': '1.42 m⁻¹ (R = 0.70 m)'},
              {'label': 'Petal Tip Deflection (δ_tip, Model)', 'value': '128.2 mm (at L = 425 mm)'},
              {'label': 'Vent Opening (Illustrative)', 'value': '64.5% Free Area (Illustrative)'},
              {'label': 'Model Check', 'value': 'ACTUATION WITHOUT MOTORS (MODEL)'}],
 'spec_plate': {'division': 'EXPLANATORY MODEL · CSI 06 18 00 / EN 1995-1-1 (NOT A DESIGN SPEC)',
                'title': 'Illustrative Concept: European Beech Hygroscopic Bilayer & Self-Shaping '
                         'Timber',
                'body': 'Explanatory concept only, not a design method or tested assembly: '
                        'cross-grained Fagus sylvatica bilayer elements with assumed ratios. None '
                        'of these numbers may be used on a real structure; no finite-element or '
                        'cycle test ran.',
                'meta': 'Timoshenko 1925 (DOI 10.1364/JOSA.11.000233) · Reichert et al. 2015 (DOI '
                        '10.1016/j.cad.2014.02.010) · Grönquist et al. 2019 (DOI '
                        '10.1126/sciadv.aax1311)'},
 'sidenote_1': {'kicker': 'SIDENOTE A.09-A · TIMOSHENKO (1925) GEOMETRY FACTOR',
                'body': "In Timoshenko's strip formula (DOI 10.1364/JOSA.11.000233), for fixed "
                        'modulus ratio n = E_1/E_2, curvature per unit thickness peaks when E_1 '
                        'h_1² = E_2 h_2².'},
 'sidenote_2': {'kicker': 'SIDENOTE A.09-B · HYSTERESIS & SIMULATED INTERFACE STRESS',
                'body': 'Grönquist et al. (2019, DOI 10.1126/sciadv.aax1311) modeled single-curved '
                        'mass timber (Wood et al. 2020), while Peng et al. (2023, DOI '
                        '10.1186/s10086-023-02105-1) observed cyclic sorption hysteresis and '
                        'simulated finite-element peak stress at the active-passive layer '
                        'interface; doubly curved shells remain untested here.'},
 'skill': {'filename': 'hygroscopic-timber-timoshenko-bilayer-SKILL.md',
           'name': 'hygroscopic-timber-timoshenko-bilayer',
           'description': 'Explanatory companion adapting Stephen Timoshenko bilayer curvature '
                          '(1925) to assumed wood moisture swelling. Explanation only, not a '
                          'design method; none of its numbers may be used on a real structure.',
           'rules': ["Explanation only, not a design method: none of this folio's assumed numbers "
                     '(alpha_T = 0.0032/%MC, alpha_L = 0.00012/%MC, m = 2, n = 10.6, kappa = 1.42 '
                     'm^-1, 128.2 or 128.6 mm, 64.5%) may be used on a real structure.',
                     'Adapt Timoshenko (1925, DOI 10.1364/JOSA.11.000233) with passive '
                     'longitudinal restraint ply 1 (h_1, E_1) and active tangential ply 2 (h_2, '
                     'E_2), computing Delta_epsilon = (alpha_T - alpha_L) * Delta_MC below fiber '
                     'saturation with assumed m = h_1/h_2 and n = E_1/E_2.',
                     'Separate unrounded kappa = 1.4234 m^-1 (128.6 mm parabolic, 124.7 mm arc at '
                     'L = 425 mm) from the page slider (1.42 m^-1 giving 128.2 mm with 240 mm cap, '
                     'vent 64.5% * (kappa/1.42) in [12%, 92%], label switch below 0.45 m^-1).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The curvature 1.42 '
                           'm⁻¹ did not follow from the stated formula without the ply ratios, so '
                           'the assumed m = 2 and n = 10.6 are now stated (equal plies would give '
                           '4.62 m⁻¹). The opening scenes about Timoshenko and Menges were not '
                           'sourced and are replaced by a plain account; beech skins are no longer '
                           'attributed to the Stuttgart projects. The PASS verdict and the '
                           '10,000-cycle claim are withdrawn.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; '
                        'arithmetic recomputed from the stated formula.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): First edition, completing Folios A.02, '
                           "E.04 & A.08 with Timoshenko's 1925 bilayer curvature formula (DOI "
                           '10.1364/JOSA.11.000233) and hygroscopic wood skins.',
                'opus': 'Review of the formula only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier '
                        "'verified' wording is withdrawn in REV 1.1: the published curvature "
                        'needed ply ratios that were not stated, and nothing was measured.'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-24',
           'citing_publications': 2504,
           'supporting': 48,
           'mentioning': 1478,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry [observed: Scite ML citation classification, accessed '
                      '2026-11-24] for Timoshenko, Analysis of Bi-Metal Thermostats (DOI '
                      '10.1364/JOSA.11.000233): 2,504 citing publications (distinct from statement '
                      'tallies: 48 supporting, 1,478 mentioning, 0 contrasting) and no retraction '
                      'notice. Counts describe that 1925 paper, not this wood model.'}}

LONGFORM_DATA = {'reading_time': '19 MIN READ',
 'word_count': '4,300 WORDS',
 'parent_folios': ['A.02', 'E.04', 'A.08'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.02 Timber Gridshells, E.04 Moisture Sorption '
                 '& A.08 Zero-Energy Envelopes',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-24',
           'citing_publications': 2504,
           'supporting': 48,
           'mentioning': 1478,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry [observed: Scite ML citation classification, accessed '
                      '2026-11-24] for Timoshenko, Analysis of Bi-Metal Thermostats (DOI '
                      '10.1364/JOSA.11.000233): 2,504 citing publications (distinct from statement '
                      'tallies: 48 supporting, 1,478 mentioning, 0 contrasting) and no retraction '
                      'notice. Counts describe that 1925 paper, not this wood model.'},
 'act1_title': 'Act I — Completing Folios A.02, E.04 & A.08: Wood Bilayers That Bend With Humidity',
 'act1_dropcap': 'In 1925, Ukrainian-born engineer Stephen Timoshenko derived a curvature formula '
                 'for two bonded metal strips that expand unequally when heated. Seventy-two years '
                 'later, Colin Dawson, Julian Vincent, and Anne-Marie Rocca showed in Nature how '
                 'dead pine cone scales open in dry air and close in rain through two fibrous '
                 'layers. Architects and wood scientists in Stuttgart and Zurich later applied '
                 'that two-layer effect to thin veneers and timber boards that curve as air '
                 'humidity shifts, without motors or wiring. Unlike machined beams, these wooden '
                 'bilayers take their shape during controlled drying or ambient weather changes. '
                 'Predicting real wood curvature still requires modeling sharp moisture gradients, '
                 'wetting-drying lag, and natural grain variation across boards. This folio adapts '
                 "Timoshenko's strip formula to a wood bilayer as an explanation, not a design "
                 'method, and none of its numbers may be used on a real structure.',
 'act1_plain_bridge': 'In plain words, a wooden house door swells during a humid summer and sticks '
                      'inside its frame. Wood absorbs air moisture unevenly. Plant cell walls '
                      'expand strongly across the wood grain, yet barely change length along the '
                      'grain. Gluing one thin veneer cut across the grain onto a second veneer cut '
                      'along the grain turns that uneven swelling into bending. When air humidity '
                      'rises, the cross-grain ply tries to lengthen while the lengthwise ply '
                      'resists, forcing the bonded strip into a curve. Shaped as small exterior '
                      'facade flaps, such wooden strips curl open and closed with changing weather '
                      'using no motor, sensor, or wire. Real outdoor timber still creeps, lags '
                      'between wetting and drying cycles, and concentrates stress along its bond '
                      'interface. Everything on this page is an educational illustration rather '
                      'than an engineering calculation, so no figure printed here may size a '
                      'building part.',
 'act1_body': 'Dead plant tissues move without motors when adjacent cell-wall layers swell '
              'unequally with humidity: Dawson, Vincent, and Rocca (1997, DOI 10.1038/37745) '
              'showed this in pine cone scales, and Eder, Schäffner, Burgert, and Fratzl (2020, '
              'DOI 10.1002/adma.202001412) reviewed how cellulose microfibril orientation governs '
              'water-driven actuation in dead wood. Stephen Timoshenko (1925, DOI '
              '10.1364/JOSA.11.000233) derived closed-form curvature for heated bi-metal strips. '
              'Reichert, Menges, and Correa (2015, DOI 10.1016/j.cad.2014.02.010) studied '
              'humidity-responsive wood veneer skins, while Grönquist et al. (2019, DOI '
              '10.1126/sciadv.aax1311) modeled self-shaping wood bilayers for curved mass timber '
              "(Wood et al. 2020). This folio adapts Timoshenko's formula with assumed constants "
              'as an explanation, not a design method, and none of its numbers may be used on a '
              'real structure.',
 'act1_stakes': 'Curved mass-timber parts are simple to draw digitally, yet Grönquist et al. '
                '(2019, DOI 10.1126/sciadv.aax1311) note that conventional fabrication requires '
                'intensive manufacturing and machining. Self-shaping bilayers offer an alternative '
                'when simulations capture moisture gradients and board-to-board material '
                'variability (Grönquist et al. 2019). At veneer scale, Reichert, Menges, and '
                'Correa (2015, DOI 10.1016/j.cad.2014.02.010) investigated passive humidity-driven '
                'building skins. Even so, Peng et al. (2023, DOI 10.1186/s10086-023-02105-1) '
                'observed cyclic adsorption-desorption hysteresis in perpendicular wood bilayers, '
                'and their finite-element simulation placed maximum stress at the interface '
                'between the active and passive layers.',
 'pullquote': 'In a hygroscopic wood bilayer, moisture sensing and bending motion arise from '
              'cellulose fiber orientation across two bonded plies rather than separate motors.',
 'chronology': [('1925',
                 'Stephen Timoshenko publishes the elastic curvature formula for bi-metal '
                 'thermostat strips in JOSA (DOI 10.1364/JOSA.11.000233).'),
                ('1997',
                 'Dawson, Vincent & Rocca show how dead pine cone scales open and close via two '
                 'fibrous layers in Nature (DOI 10.1038/37745).'),
                ('2015',
                 'Reichert, Menges & Correa publish Meteorosensitive architecture on '
                 'humidity-driven wood veneer skins (DOI 10.1016/j.cad.2014.02.010).'),
                ('2019–2020',
                 'Grönquist et al. model large-scale self-shaping wood bilayers (DOI '
                 '10.1126/sciadv.aax1311), applied to Urbach Tower curved parts (Wood et al. '
                 '2020).')],
 'act2_title': 'Act II — Simplified Mechanics: Timoshenko Strip Curvature & Assumed Wood '
               'Anisotropy',
 'act2_analogy': 'Wet one strip of heavy paper with a sponge and glue it flat against a dry strip. '
                 'As the damp sheet swells against its dry partner, the pair curls into an arc, '
                 'just as dead pine cone scales close in rain and open in sun. Cross-grained wood '
                 'veneers bend by that principle. Where the analogy stops: real exterior timber '
                 'experiences wetting-drying hysteresis, bond-interface shear, wind flutter, and '
                 'long-term creep that paper strips and pine cones do not face on a building.',
 'act2_plain_primer': 'Two controls drive the simplified calculation below. Wood Moisture Content '
                      'Shift sets the modeled change in bound water below fiber saturation, '
                      'raising curvature proportionally. Total Timber Bilayer Thickness sets the '
                      'combined two-ply depth in millimeters, trading smaller curvature for higher '
                      'bending stiffness. Dragging either slider updates the four readout cards '
                      'from a rounded baseline of 1.42 per meter, with tip movement capped at '
                      '240.0 millimeters. Meanwhile, the illustrative free-area card scales '
                      'between 12.0 and 92.0 percent, the status label switches at 0.45 per meter, '
                      'and the bottom SVG captions stay static.',
 'distill_diagram': {'analogy_title': 'Wet-on-Dry Paper & Pine Cone Scale',
                     'analogy_sub': 'Unequal swelling across two bonded plies bends the strip '
                                    'without motors',
                     'force_a_title': 'Wood Moisture Content Shift (ΔMC)',
                     'force_a_sub': 'Raises modeled misfit strain across assumed tangential vs '
                                    'longitudinal grain',
                     'force_b_title': 'Total Timber Bilayer Thickness (h)',
                     'force_b_sub': 'Trades inverse curvature scaling (1/h) against cubic '
                                    'stiffness (h³)',
                     'threshold_title': 'Model Baseline: κ = 1.42 m⁻¹ (Slider Heuristic)',
                     'threshold_pass': '128.2 mm slider tip (240 mm cap); vent card scales 12%–92%',
                     'threshold_fail': 'Below κ = 0.45 m⁻¹ switches label; hysteresis & shear '
                                       'omitted'},
 'act2_intuition': 'Timoshenko (1925, DOI 10.1364/JOSA.11.000233) analyzed thermal expansion in '
                   'bi-metal strips; this folio mixes that formula with idealized moisture '
                   'swelling below fiber saturation (assumed ~28% moisture content) using assumed '
                   'round constants. Setting the assumed tangential swelling coefficient α_T = '
                   '0.0032 per %MC and longitudinal swelling coefficient α_L = 0.00012 per %MC '
                   '(~27:1), a Wood Moisture Content Shift ΔMC = 6.0% produces differential misfit '
                   'strain Δε = (α_T − α_L) ΔMC = 0.01848 (0.0185 rounded). Bonding passive '
                   'longitudinal restraint ply 1 (thickness h_1, elastic modulus E_1) to active '
                   'tangential ply 2 (thickness h_2, elastic modulus E_2) at Total Timber Bilayer '
                   'Thickness h = h_1 + h_2 = 6.0 mm, with assumed thickness ratio m = h_1/h_2 = 2 '
                   'and assumed modulus ratio n = E_1/E_2 = 10.6, gives geometry factor f(m, n) = '
                   '6(1 + m)² / [3(1 + m)² + (1 + mn)(m² + 1/(mn))] = 0.4621 and unrounded '
                   'curvature κ = f(m, n) Δε / h = 1.4234 m⁻¹ (1.42 m⁻¹ rounded; equal plies m = n '
                   '= 1 give 4.62 m⁻¹). Across an assumed cantilever length L = 425 mm, unrounded '
                   'κ gives parabolic tip deflection ½ κ L² = 128.6 mm (124.7 mm circular arc), '
                   'whereas the page slider scales from rounded 1.42 m⁻¹ to print 128.2 mm (124.4 '
                   'mm arc).',
 'act2_deepening': 'In the simplified elastic strip, curvature κ scales as 1/h while bending '
                   'stiffness scales with h³: doubling thickness halves modeled curvature while '
                   'multiplying flexural stiffness eightfold, separating thin veneers (Reichert, '
                   'Menges & Correa 2015, DOI 10.1016/j.cad.2014.02.010) from thicker mass-timber '
                   'laminates (Grönquist et al. 2019, DOI 10.1126/sciadv.aax1311). Linear '
                   'elasticity omits key wood effects: Peng et al. (2023, DOI '
                   '10.1186/s10086-023-02105-1) observed cyclic sorption hysteresis that widened '
                   'at lower thickness ratios and simulated finite-element peak stress at the '
                   'active-passive layer interface, while EN 1995-1-1 rolling shear, creep, wind '
                   'flutter, and rain-tightness remain unmodeled here.',
 'walkthrough': ['Experiment 1 (Wood Moisture Content Shift ΔMC & 240 mm Cap): Drag ΔMC from 1.0% '
                 'to 12.0%; slider κ scales linearly, tip deflection caps at 240.0 mm (ΔMC ≥ 11.5% '
                 'at h = 6.0 mm), and vent area clamps to [12.0%, 92.0%].',
                 'Experiment 2 (Total Timber Bilayer Thickness h & 0.45 m⁻¹ Switch): Drag h from '
                 '3.0 to 14.0 mm (at ΔMC = 6.0%, slider κ drops from 2.84 to 0.61 m⁻¹); lowering '
                 'ΔMC too so pre-rounded slider κ = 1.42 × (ΔMC/6) × (6/h) falls below 0.45 m⁻¹ '
                 '(e.g., 3.0% and 9.5 mm, κ = 0.4484 m⁻¹) switches the status card to LOW '
                 'HYGROSCOPIC STROKE (MODEL).',
                 'Experiment 3 (Stage Presets vs Static SVG Captions): Click Stage buttons 1–4 to '
                 'tween both sliders across presets, updating the readout cards, 3D preview, and '
                 'reactive overlay elements while the two bottom SVG captions (1.42 m⁻¹, 128 mm, '
                 '64.5%) and circle #tp-a09-op-dot remain static.'],
 'act4_title': 'Act IV — Open Questions: Hygro-Mechanical Simulation, Hysteresis & Weathering',
 'act4_human_ai': 'Linking Folios A.02, A.03, and E.04, Grönquist et al. (2019, DOI '
                  '10.1126/sciadv.aax1311) used time- and moisture-dependent simulations to study '
                  'shape prediction, moisture gradients, and material variability in curved mass '
                  'timber. This folio ran no simulation and is not a design method.',
 'act4_deepening': 'Open finite-element tools such as FEniCS/dolfinx (Scroggs et al. 2022, DOI '
                   '10.1145/3524456, https://github.com/FEniCS/dolfinx) could model coupled '
                   'moisture diffusion and elasticity; none ran here. Peng et al. (2023, DOI '
                   '10.1186/s10086-023-02105-1) observed cyclic sorption hysteresis and simulated '
                   'finite-element peak stress at the active-passive layer interface, while '
                   'outdoor creep and weathering remain unmodeled; no number here may be used on a '
                   'real structure.',
 'cf_bridge': 'Explanatory Architecture Monograph (A.02 + E.04 + A.08 → A.09): Adapts Timoshenko '
              '(1925) to assumed wood anisotropy; explanation only, not a structural design '
              'method.',
 'sources': ['Timoshenko, S. (1925). Analysis of bi-metal thermostats. Journal of the Optical '
             'Society of America, 11(3), 233–255. DOI: 10.1364/JOSA.11.000233.',
             'Dawson, C., Vincent, J. F. V., & Rocca, A.-M. (1997). How pine cones open. Nature, '
             '390(6661), 668. DOI: 10.1038/37745.',
             'Reichert, S., Menges, A., & Correa, D. (2015). Meteorosensitive architecture: '
             'Biomimetic building skins based on materially embedded and hygroscopically enabled '
             'responsiveness. Computer-Aided Design, 60, 50–69. DOI: 10.1016/j.cad.2014.02.010.',
             'Grönquist, P., Wood, D., Hassani, M. M., Wittel, F. K., Menges, A., & Rüggeberg, M. '
             '(2019). Analysis of hygroscopic self-shaping wood at large scale for curved mass '
             'timber structures. Science Advances, 5(9), eaax1311. DOI: 10.1126/sciadv.aax1311.',
             'Eder, M., Schäffner, W., Burgert, I., & Fratzl, P. (2020). Wood and the Activity of '
             'Dead Tissue. Advanced Materials, 33(28), 2001412. DOI: 10.1002/adma.202001412.',
             'Peng, H., Liu, Z., Zhu, J., Jiang, J., Lyu, J., & Zhan, T. (2023). Bending responses '
             'of self-shaping wood bilayers: comparison between adsorption and desorption '
             'processes. Journal of Wood Science, 69(1), 29. DOI: 10.1186/s10086-023-02105-1.',
             'Wood, D., Grönquist, P., Bechert, S., Aldinger, L., Riggenbach, D., Lehmann, K., '
             'Rüggeberg, M., Burgert, I., Knippers, J., & Menges, A. (2020). From machine control '
             'to material programming: Self-shaping wood manufacturing of a high performance '
             'curved CLT structure—Urbach Tower. Fabricate 2020, 50–57.',
             'CEN. EN 1995-1-1, Eurocode 5: Design of timber structures, Part 1-1 (first published '
             '2004); CSI MasterFormat 06 18 00 Glued-Laminated Construction. Named for context; '
             "neither sets this folio's values.",
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). '
             'Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal '
             'and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM '
             'Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Timoshenko '
        'hygroscopic wood bilayer curvature schematic and illustrative aperture curve">\n'
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
        'fill="currentColor">Timoshenko Beech Bilayer (Assumed α_T vs. α_L)</text>\n'
        '            <text id="tp-a09-svg-curv-text" x="55" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Static Caption: κ = 1.42 m⁻¹ · δ_tip ≈ 128 mm</text>\n'
        '            <line x1="355" y1="24" x2="355" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="372" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Curvature κ(ΔMC, h) &amp; Illustrative Vent Scaling</text>\n'
        '            <path id="tp-a09-curv-line" d="M 380 172 L 625 56" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <circle id="tp-a09-op-dot" cx="502" cy="114" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="382" y="70" font-size="9.5" fill="var(--tp-verdigris)">Explanatory '
        'Model: κ ∝ (α_T − α_L) ΔMC / h</text>\n'
        '            <text id="tp-a09-vent-text" x="382" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Static Caption: 64.5% · Not a Design Method</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a biomimetic hygroscopic cross-laminated beech '
        'timber facade pavilion opening its curved Timoshenko bilayer petals autonomously in '
        'response to sunlight and humidity would look like (artistic impression, not a measured '
        'structure or specification)',
 'caption': 'Conceptual Vision Plate A.09-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (completing Folios A.02, E.04 & A.08) imagining a '
            "hygroscopic European beech bilayer skin whose petals curve via Stephen Timoshenko's "
            '1925 strip curvature relation.'}

DISPATCH = {'kicker': 'FRONTIER BIOMIMETIC TIMBER DISPATCH · A.09 · REV 1.1',
 'headline': "Explanatory Model: Timoshenko's 1925 Strip Formula & Hygroscopic Wood Bilayers",
 'body': 'Adapting Timoshenko (1925, DOI 10.1364/JOSA.11.000233) with assumed 27:1 wood swelling '
         'anisotropy alongside Reichert et al. (2015, DOI 10.1016/j.cad.2014.02.010), Grönquist et '
         'al. (2019, DOI 10.1126/sciadv.aax1311), and Peng et al. (2023, DOI '
         '10.1186/s10086-023-02105-1). Explanation only, not a design method; no figure may be '
         'used on a real structure.'}

META_3D = ('Timoshenko Hygroscopic Beech Bilayer Shell Manifold',
 'X: Spanwise Petal Coordinate · Z: Moisture Shift ΔMC · Y: Timoshenko Curvature κ & Tip Opening')

ES_TRANSLATION = {'title_es': 'Pieles Arquitectónicas Programables de Madera Higroscópica: Curvatura Bicapa de '
             'Timoshenko, Hinchamiento Ortotrópico y Fachadas Climáticas de Energía Cero',
 'subtitle_es': 'Completando los Folios A.02, E.04 y A.08: un modelo explicativo —no un método de '
                'diseño estructural— que adapta la fórmula bicapa de Stephen Timoshenko (1925) a '
                'láminas de madera que se curvan con la humedad.',
 'why_es': 'Al mojar una tira gruesa de papel y pegarla contra otra seca, el par se curva igual '
           'que las escamas muertas de una piña de pino bajo lluvia y sol. Las chapas de madera '
           'con vetas cruzadas usan ese principio. Dónde termina la analogía: en exterior aparecen '
           'histéresis, cortante en la unión, viento y fluencia ausentes en el papel.',
 'bridge_es': 'Modelo explicativo (no un método de diseño): las cuatro tarjetas escalan desde 1.42 '
              'm⁻¹ redondeado (tope de 240.0 mm y área entre 12.0% y 92.0%), con leyendas SVG '
              'inferiores estáticas.',
 'plain_es': 'En palabras sencillas, una puerta de madera en verano húmedo absorbe vapor de agua y '
             'se atora en su marco. Las paredes celulares de la madera se expanden mucho a lo '
             'ancho de la veta, pero casi nada a lo largo. Al pegar una chapa cortada a través de '
             'la fibra contra otra cortada a lo largo, esa diferencia convierte la humedad en '
             'curvatura. Cuando sube la humedad del aire, la capa transversal intenta alargarse y '
             'la longitudinal la frena, doblando toda la pieza. Colocadas como aletas de fachada, '
             'esas tiras se curvan con el clima sin motores ni cables. Aun así, en exteriores la '
             'madera sufre fluencia, histéresis entre mojado y secado y esfuerzos en la interfaz '
             'entre capas. Este folio es una explicación educativa, no un método de diseño, y '
             'ninguno de sus números puede usarse en una estructura real.',
 'deep_es': 'El folio adapta la ecuación bimetálica de Timoshenko (1925, DOI '
            '10.1364/JOSA.11.000233) bajo saturación de fibra (~28% MC asumido) con capa pasiva '
            'longitudinal 1 (h_1, E_1), capa activa tangencial 2 (h_2, E_2) y constantes redondas '
            'asumidas (α_T = 0.0032/%MC, α_L = 0.00012/%MC, m = h_1/h_2 = 2, n = E_1/E_2 = 10.6, h '
            '= 6.0 mm, L = 425 mm). A ΔMC = 6.0%, κ = 1.4234 m⁻¹ sin redondear da ½ κ L² = 128.6 '
            'mm (124.7 mm en arco), mientras el deslizador parte de 1.42 m⁻¹ para mostrar 128.2 mm '
            '(tope 240.0 mm), área 64.5% × (κ / 1.42) en [12.0%, 92.0%] y cambio de etiqueta bajo '
            '0.45 m⁻¹. Grönquist et al. (2019, DOI 10.1126/sciadv.aax1311) modelaron madera '
            'autocurvable y Peng et al. (2023, DOI 10.1186/s10086-023-02105-1) observaron '
            'histéresis y simularon mediante elementos finitos esfuerzo máximo en la interfaz '
            'entre capas; ninguna cifra sirve para diseño real.'}
