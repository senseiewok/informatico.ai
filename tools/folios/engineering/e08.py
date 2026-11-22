#!/usr/bin/env python3
"""Folio E.08 (ENGINEERING): Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement Troughs & GNN Subsurface Digital Twins."""
from __future__ import annotations

SLUG = 'e08'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.08',
 'slug': 'e08',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Earth-Pressure-Balance Tunnel Boring Machines (EPB-TBM), Peck–Mair Gaussian Settlement '
          'Troughs & GNN Subsurface Digital Twins',
 'subtitle': "How Ralph Peck and Robert Mair's conservation-of-volume Gaussian settlement trough "
             'S(y) = S_max exp(−y² / 2i²) governs urban underground tunneling, coupled with Graph '
             'Neural Network subsurface digital twins.',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'CIVIL & GEOTECH TUNNELING · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'S(y) = S_max exp(−y² / 2i²) · V_s = V_L (π D² / 4) · i = K (z_0 − z) · CSI 31 '
                  '71 19',
 'colophon': {'identifier': 'E.08 · EPB-TBM Tunneling & Peck–Mair Settlement · CSI 31 71 19',
              'kernels': 'Peck–Mair Gaussian Trough · Anagnostou–Kovári Face Equilibrium · GNN '
                         'Twin',
              'benchmarks': 'D = 9.8 m · z_0 = 24.0 m · V_L = 0.75% ⇒ S_max = 18.8 mm',
              'bridge': 'EPB Foam Yield-Stress Conditioning ↔ Yield-Stress Gel Flow (analogy only)'},
 'sliders': [{'label': 'TBM Face Support Pressure (P_face)',
              'min': 80.0,
              'max': 360.0,
              'step': 5.0,
              'value': 210.0,
              'unit': ' kPa'},
             {'label': 'Geotechnical Volume Loss Ratio (V_L)',
              'min': 0.2,
              'max': 2.5,
              'step': 0.05,
              'value': 0.75,
              'unit': '%'}],
 'steps': ['Stage 1 (Chamber Balance, Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X): At z_0 = 24.0 m, P_face = 210 kPa is an assumed point under stated assumptions, not a soil-profile check.',
           'Stage 2 (Soil Conditioning, Merritt & Mair 2006, DOI 10.1680/geot.2006.56.9.605; Budach & Thewes 2015, DOI 10.1016/j.tust.2015.08.006): Foam may condition clay or coarse ground in the screw conveyor; about 120 mm slump is illustrative.',
           'Stage 3 (Peck Trough, DOI 10.1680/geot.1993.43.2.315): V_L = 0.75% across D = 9.8 m gives V_s = 0.566 m³ per meter and S_max = 18.8 mm at i = 12.0 m.',
           'Stage 4 (Proposed GNN Twin): Torque and grout pressures could suggest updates to keep β_max < 1/500 (cf. Skempton & MacDonald 1956, DOI 10.1680/ipeds.1956.12202). Untested; no network was built.'],
 'readouts': [{'label': 'Trough Inflection Width (i = K z_0)',
               'value': '12.0 m (K = 0.50, z_0 = 24 m)'},
              {'label': 'Centerline Max Settlement (S_max)', 'value': '18.8 mm (at V_L = 0.75%)'},
              {'label': 'Max Trough Slope (β_max)', 'value': '1 / 1,050 (< 1/500 model limit)'},
              {'label': 'Geotechnical TBM Verdict', 'value': 'WITHIN MODEL WINDOW (ASSUMED FACE BALANCE)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 31 71 19 / PRECAST SEGMENTAL LINING',
                'title': '9.8 m Earth-Pressure-Balance TBM & Precast Fiber-Reinforced Segmental '
                         'Lining',
                'body': 'Pressurized EPB shield excavation with two-component tail-void grouting, '
                        'EPDM-gasketed C60/75 precast rings, and proposed InSAR + GNN monitoring. '
                        'Design sketch only, not a project specification.',
                'meta': 'Anchor: Mair, Taylor & Bracegirdle 1993, DOI 10.1680/geot.1993.43.2.315 · β ≤ 1/500 is the limit chosen for this model'},
 'sidenote_1': {'kicker': 'SIDENOTE E.08-A · CONSERVATION OF SOIL VOLUME IN PECK–MAIR TROUGHS',
                'body': 'Integrating S(y) = S_max exp(−y² / 2i²) over (−∞, +∞) gives V_s = √(2π) i '
                        'S_max = V_L (π D² / 4). With i = K z_0, S_max scales as 1 / z_0 and '
                        'maximum slope falls at y = ±i.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.08-B · SPECIFICATION PLATE · CSI 31 71 19 / GNN SUBSURFACE '
                          'TWIN',
                'body': 'A Graph Neural Network might link borehole strata and lining rings under Mohr–Coulomb constraints to estimate settlement about tens of meters ahead. Untested proposal, not yet built or verified.'},
 'skill': {'filename': 'epb-tbm-peck-settlement-SKILL.md',
           'name': 'epb-tbm-peck-settlement',
           'description': 'AI-agnostic geotechnical and tunneling civil engineering skill for '
                          'EPB-TBM face pressure equilibrium, Peck-Mair Gaussian settlement '
                          'troughs, and GNN subsurface digital twins.',
           'rules': ['Compute trough inflection distance i = K * (z_0 - z) (K about 0.5 for clays at the surface, lower for sands; treat constant K below the surface as a simplification) and tunnel cross-sectional area A_t = pi * D^2 / '
                     '4.',
                     'Calculate centerline maximum settlement S_max = (V_L * A_t) / (sqrt(2 * pi) '
                     '* i) and maximum transverse slope beta_max = 0.6065 * S_max / i at y = +/- '
                     'i.',
                     'Verify EPB face pressure P_face stays between active collapse pressure '
                     'sigma_h,active + u_0 and passive blowout pressure sigma_v0.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The Graph Neural Network digital twin is now described as a proposal: no network was built, and the claims of 50 m look-ahead forecasts, "GNN PASS" and a "Rankine pass" verdict are withdrawn. The 1/500 slope limit is labeled as the choice of this model, not a value taken from a named standard, and the page now says that a constant K below the surface is a simplification of what Mair, Taylor & Bracegirdle (1993) reported. The Brunel opening is cut back to the commonly told account, and the foam note is marked as an analogy.',
                'opus': 'Review: references checked by DOI in the Scite index on 2026-11-14; S_max = 18.8 mm and the slope 1/1,050 were recomputed by hand from the stated law.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): Inaugural Volume IV geotechnical & '
                           'underground tunneling monograph uniting Peck-Mair Gaussian settlement '
                           'troughs (DOI 10.1680/geot.1993.43.2.315) with EPB-TBM chamber '
                           'mechanics and GNN subsurface digital twins.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'exact Gaussian integral V_s = sqrt(2*pi)*i*S_max = 0.565 m^3/m and S_max '
                        '= 18.8 mm at V_L = 0.75%, D = 9.8 m, i = 12.0 m. This was an arithmetic check only; no other verification is claimed.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1680/geot.1993.43.2.315',
           'fetched_on': '2026-11-08',
           'citing_publications': 575,
           'supporting': 6,
           'mentioning': 183,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Mair, Taylor & Bracegirdle 1993 (DOI 10.1680/geot.1993.43.2.315), fetched 2026-11-08: 575 citing publications (6 supporting, 183 mentioning, 0 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1680/geot.1993.43.2.315',
           'fetched_on': '2026-11-08',
           'citing_publications': 575,
           'supporting': 6,
           'mentioning': 183,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Mair, Taylor & Bracegirdle 1993 (DOI 10.1680/geot.1993.43.2.315), fetched 2026-11-08: 575 citing publications (6 supporting, 183 mentioning, 0 contrasting) and no retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': "Act I — From Marc Brunel's Thames Shield to Earth-Pressure-Balance TBMs & "
               'Subsurface AI Digital Twins',
 'act1_dropcap': 'In 1818 the French-born engineer Marc Isambard Brunel patented an iron tunneling '
                 'shield beneath London. Accounts of the invention recall the shipworm, a marine '
                 'mollusk whose shell plates rasp through wet timber while lining the burrow with a '
                 'calcareous tube. Work began in 1825, and after river floods and a seven-year '
                 'halt, Marc and Isambard Kingdom Brunel opened their Thames Tunnel in 1843. Miners '
                 'worked inside thirty-six cast-iron cells, advancing timber boards a few inches at '
                 'a time while bricklayers built the masonry arch right behind them. Their shield '
                 'showed that waterlogged clay, silt, and sand could be tunneled under an active '
                 'port without trenching. Advancing those frames still disturbed the ground '
                 'overhead, leaving engineers with a lasting question: how does removing earth deep '
                 'underground reshape the street and buildings above?',
 'act1_plain_bridge': 'In plain words, digging a subway tunnel under a busy city works like '
                      'drawing sand from an hourglass base. Twenty meters down, a boring machine '
                      "cuts wet clay. Cutting relieves part of the earth's natural support "
                      'pressure. Even a few millimeters of inward slip let surrounding soil creep '
                      'into tiny gaps around the moving shield. Because saturated clay deforms with '
                      'little immediate volume change, that deep movement rises slowly through the '
                      'overlying ground layers. At street level, a broad, shallow bowl-shaped dip '
                      'forms. If one side of a historic brick building sinks more than another, '
                      'mortar joints crack and buried utility pipes strain. Crews limit that dip by '
                      'pressurizing conditioned soil paste at the cutting face and grouting behind '
                      'each concrete ring. This folio also sketches, as an untested proposal, how '
                      'graph-based machine learning could help forecast ground movement from machine '
                      'data.',
 'act1_body': 'Skempton and Chrimes (1994, DOI 10.1680/geot.1994.44.2.191) reconstructed the '
              'geology and flooding of that Thames drive from original records. In 1969, Ralph B. '
              'Peck synthesized soft-ground tunnel data in Mexico City and fit surface settlement '
              'with an inverted Gaussian curve. In 1993, Robert J. Mair, R. N. Taylor, and A. '
              'Bracegirdle (DOI 10.1680/geot.1993.43.2.315) showed that subsurface clay troughs are '
              'also Gaussian, though wider at depth than a constant width factor gives. This folio '
              'works at the surface with a constant 0.5 factor for clays. Earth-Pressure-Balance '
              'Tunnel Boring Machines (EPB-TBMs) about ten meters wide balance face pressures with '
              'conditioned muck (Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X; Mair '
              '2008, DOI 10.1680/geot.2008.58.9.695). Thrust and grout data could feed a Graph '
              'Neural Network (GNN) forecast; no model was built, accuracy is not claimed, and CSI '
              'MasterFormat 31 71 19 is named only for classification.',
 'act1_stakes': 'Urban tunneling must protect masonry buildings and utilities overhead (Mair 2008, '
                'DOI 10.1680/geot.2008.58.9.695). Losing face pressure in silt or sand can trigger '
                'inflow and a sinkhole, whereas excess pressure heaves pavement and strains pipes '
                '(Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X). Differential '
                'settlement is often the tighter limit because uneven sinking shears mortar joints. '
                'Skempton and MacDonald (1956, DOI 10.1680/ipeds.1956.12202) gave about one in five '
                'hundred as an angular-distortion limit against wall cracking. Boscardin and Cording '
                '(1989, DOI 10.1061/(ASCE)0733-9410(1989)115:1(1)) showed that excavation damage '
                'couples angular distortion with horizontal tensile strain. This folio uses one in '
                'five hundred on trough slope as an illustrative model limit, not a code rule.',
 'pullquote': '"Every fraction of a percent of volume loss V_L at the TBM cutterhead propagates '
              'upward through the soil continuum as a conservation-of-volume Gaussian settlement '
              'trough at the city street above."',
 'chronology': [('1825',
                 'Marc & Isambard Kingdom Brunel drive the Thames Tunnel shield (Skempton & '
                 'Chrimes 1994, DOI 10.1680/geot.1994.44.2.191).'),
                ('1969',
                 'Ralph B. Peck relates soft-ground surface settlement troughs to an inverted '
                 'Gaussian curve and volume loss.'),
                ('1993',
                 'Mair, Taylor & Bracegirdle publish clay subsurface settlement profiles in Géotechnique (DOI 10.1680/geot.1993.43.2.315).'),
                ('1996',
                 'Anagnostou & Kovári publish EPB shield face stability conditions (DOI 10.1016/0886-7798(96)00017-X).'),
                ('2026',
                 'Design-study proposal pairing EPB-TBM telemetry with a physics-constrained GNN subsurface twin.')],
 'act2_title': 'Act II — How It Actually Works: EPB Chamber Pressure Balance + Peck–Mair Gaussian '
               'Troughs',
 'act2_analogy': 'Push a wooden spatula sideways deep inside thick chocolate pudding. '
                 'Draw pudding out too fast and the top dips into a wide, shallow hollow; press '
                 'too hard and the surface bulges upward. Soft saturated clay above a tunnel shield '
                 'deforms in a similar short-term constant-volume way when small voids open. The '
                 'analogy stops in layered or free-draining ground, because sand and gravel change '
                 'volume and arch loads in ways uniform pudding cannot.',
 'act2_plain_primer': 'Two sliders drive the workbench below. TBM Face Support Pressure sets the '
                      'assumed chamber paste pressure; with no soil profile stated, moving it '
                      'updates the pressure label and stage preview without changing the numerical '
                      'settlement readouts. Geotechnical Volume Loss Ratio sets the percentage of '
                      'tunnel area lost into gaps around the shield, directly setting centerline '
                      'settlement and trough slope. Stepping volume loss from one point five five '
                      'percent to one point six zero percent crosses the one in five hundred slope '
                      'limit near one point five eight percent and trips the model alert.',
 'distill_diagram': {'analogy_title': 'Spatula Slicing Thick Pudding',
                     'analogy_sub': 'Underground voids propagate upward as smooth surface dips',
                     'force_a_title': 'Chamber Face Pressure (P_face)',
                     'force_a_sub': 'Balances earth and pore-water pressure to prevent ground '
                                    'collapse',
                     'force_b_title': 'Volume Loss Ratio (V_L)',
                     'force_b_sub': 'Quantifies lost ground propagating into surface settlement',
                     'threshold_title': 'Active Collapse vs. Passive Heave Window',
                     'threshold_pass': 'Within model window: Trough slope stays under 1/500 (V_L '
                                       'below ~1.58%)',
                     'threshold_fail': 'Failure: Face collapse creates surface sinkhole or street '
                                       'heave'},
 'act2_intuition': 'As an EPB-TBM of diameter D advances at depth z_0, chamber pressure P_face '
                   "balances horizontal effective stress and pore pressure sigma_h0 = K_0 sigma'_v "
                   '+ u_0 (Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X). Below '
                   'active support, inward soil yield creates volume loss V_L, giving undrained '
                   'clay trough volume V_s = V_L (pi D^2 / 4). Peck (1969) and Mair, Taylor & '
                   'Bracegirdle (1993, DOI 10.1680/geot.1993.43.2.315) model settlement by S(y) = '
                   'S_max exp(-y^2 / [2 i^2]) with i = K (z_0 - z), S_max = V_s / (sqrt(2 pi) i), '
                   'and peak slope beta_max = 0.6065 S_max / i at y = +-i. For D = 9.8 m, V_L = '
                   '0.75%, K = 0.5, and z_0 = 24 m, V_s = 0.566 m^3/m, i = 12.0 m, S_max = 18.8 mm, '
                   'and beta_max = 1/1,050, within the 1/500 model threshold (cf. Skempton & '
                   'MacDonald 1956, DOI 10.1680/ipeds.1956.12202). In the widget, P_face = 210 kPa '
                   'is an assumed operating point uncoupled from V_L.',
 'act2_deepening': 'Plenum pressure control relies on conditioned muck rheology. Untreated clay can '
                   'clog the cutterhead and screw conveyor. Surfactant-polymer foam turns excavated '
                   'soil into a low-permeability paste that dissipates pressure steadily along the '
                   'conveyor (Merritt & Mair 2006, DOI 10.1680/geot.2006.56.9.605; Budach & Thewes '
                   '2015, DOI 10.1016/j.tust.2015.08.006; the slump of 120 to 180 millimeters used '
                   'here is illustrative). Two-component tail-void grout limits ground relaxation '
                   'behind the shield (Mair 2008, DOI 10.1680/geot.2008.58.9.695). A Graph Neural '
                   'Network could represent boreholes, sensors, and rings as graph nodes; that '
                   'proposal was neither built nor tested here.',
 'walkthrough': ['Experiment 1 (Assumed Chamber Pressure): Drag TBM Face Support Pressure P_face '
                 'around its 210 kPa default. With no soil profile stated, P_face updates the '
                 'pressure label and stage preview without altering V_L, S_max, or β_max readouts '
                 '(Anagnostou & Kovári 1996, DOI 10.1016/0886-7798(96)00017-X).',
                 'Experiment 2 (Peck–Mair Trough & 1/500 Limit): Sweep Volume Loss Ratio V_L (%) '
                 'from 0.40% to 1.80% (DOI 10.1680/geot.1993.43.2.315). Watch S_max deepen and the '
                 'verdict flip past the 1/500 model slope limit (~1.58% crossover) on the step from '
                 '1.55% to 1.60%.',
                 'Experiment 3 (Four-Stage Spine & Proposed GNN): Step through Stages 1 to 4 to '
                 'inspect assumed chamber balance, screw-conveyor conditioning (DOI '
                 '10.1680/geot.2006.56.9.605), Peck integration, and the untrained GNN proposal.'],
 'act4_title': 'Act IV — Geotechnical Tunneling Telemetry, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'In urban tunneling, a GNN digital twin could pair cutterhead torque, conveyor mass flow, and InSAR radar to suggest foam and grout adjustments. Readers can explore elastoplastic excavation in FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI 10.1145/3524456) and sparse system identification in dynamicslab/pysindy (Brunton et al. 2016, DOI 10.1073/pnas.1517384113); neither was run here.',
 'act4_deepening': 'Tunneling engineers could pair empirical mechanics with machine-learning '
                   'surrogates as an exploratory tool, though no such system is simulated here. '
                   'Open field problems remain central (Mair 2008, DOI 10.1680/geot.2008.58.9.695): '
                   'three-dimensional response at skewed junctions, multi-year clay drainage '
                   'consolidation, and distributed fiber-optic strain sensing in precast rings. '
                   'Every data-driven forecast still requires validation against field settlement '
                   'arrays.',
 'cf_bridge': 'Standalone geotechnical folio for tunneling engineers. As a vocabulary analogy only, surfactant foam lowers clay yield stress in the screw conveyor, and yield-stress rheology also describes gels in other fields. This folio models no biological fluid, and nothing here bears on health or treatment.',
 'sources': ['Skempton, A. W., & MacDonald, D. H. (1956). The allowable settlements of buildings. '
             'Proceedings of the Institution of Civil Engineers, 5(6), 727–768. DOI: '
             '10.1680/ipeds.1956.12202.',
             'Peck, R. B. (1969). Deep excavations and tunneling in soft ground. Proc. 7th ICSMFE, '
             'Mexico City, State-of-the-Art Vol., 225–290.',
             'Boscardin, M. D., & Cording, E. J. (1989). Building Response to Excavation-Induced '
             'Settlement. J. Geotech. Eng. (ASCE), 115(1), 1–21. DOI: '
             '10.1061/(ASCE)0733-9410(1989)115:1(1).',
             'Mair, R. J., Taylor, R. N., & Bracegirdle, A. (1993). Subsurface settlement profiles '
             'above tunnels in clays. Géotechnique, 43(2), 315–320. DOI: '
             '10.1680/geot.1993.43.2.315.',
             'Skempton, A. W., & Chrimes, M. M. (1994). Thames Tunnel: geology, site investigation '
             'and geotechnical problems. Géotechnique, 44(2), 191–216. DOI: '
             '10.1680/geot.1994.44.2.191.',
             'Anagnostou, G., & Kovári, K. (1996). Face stability conditions with '
             'earth-pressure-balanced shields. Tunnelling and Underground Space Technology, 11(2), '
             '165–173. DOI: 10.1016/0886-7798(96)00017-X.',
             'Merritt, A. S., & Mair, R. J. (2006). Mechanics of tunnelling machine screw '
             'conveyors: model tests. Géotechnique, 56(9), 605–615. DOI: '
             '10.1680/geot.2006.56.9.605.',
             'Mair, R. J. (2008). Tunnelling and geotechnics: new horizons. Géotechnique, 58(9), '
             '695–736. DOI: 10.1680/geot.2008.58.9.695.',
             'Budach, C., & Thewes, M. (2015). Application ranges of EPB shields in coarse ground '
             'based on laboratory research. Tunnelling and Underground Space Technology, 50, '
             '296–304. DOI: 10.1016/j.tust.2015.08.006.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing equations from data by sparse identification of nonlinear dynamical systems (https://github.com/dynamicslab/pysindy). PNAS, 113(15), 3932–3937. DOI: 10.1073/pnas.1517384113.',
             'CSI MasterFormat 31 71 19, Tunnel Excavation by TBM (classification only).',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (https://github.com/FEniCS/dolfinx). ACM Trans. Math. Softw., 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quant. Sci. Stud., 2(3), 882–898. DOI: 10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Peck-Mair Gaussian '
        'surface settlement trough S(y) above an Earth-Pressure-Balance Tunnel Boring Machine">\n'
        '            <line x1="40" y1="42" x2="640" y2="42" stroke="currentColor" '
        'stroke-opacity="0.35" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-e08-trough-path" d="M 60 42 Q 210 43 265 62 Q 340 88 415 62 Q '
        '470 43 620 42" fill="var(--tp-minium-soft)" stroke="var(--tp-minium)" stroke-width="3"/>\n'
        '            <line x1="340" y1="42" x2="340" y2="188" stroke="currentColor" '
        'stroke-opacity="0.25" stroke-dasharray="3,3"/>\n'
        '            <line x1="250" y1="36" x2="250" y2="68" stroke="var(--tp-prussian)" '
        'stroke-width="1.5"/>\n'
        '            <line x1="430" y1="36" x2="430" y2="68" stroke="var(--tp-prussian)" '
        'stroke-width="1.5"/>\n'
        '            <circle id="tp-e08-tbm-shield" cx="340" cy="148" r="34" '
        'fill="var(--tp-stone)" stroke="var(--tp-prussian)" stroke-width="3"/>\n'
        '            <circle cx="340" cy="148" r="26" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="1.8" stroke-dasharray="5,3"/>\n'
        '            <text x="52" y="18" font-size="10.5" font-weight="600" '
        'fill="currentColor">Peck–Mair Gaussian Settlement Trough S(y) = S_max exp(−y² / '
        '2i²)</text>\n'
        '            <text id="tp-e08-smax-text" x="352" y="88" font-size="10.5" font-weight="600" '
        'fill="var(--tp-minium)">S_max = 18.8 mm (V_L = 0.75% · i = 12.0 m)</text>\n'
        '            <text x="195" y="35" font-size="9.5" fill="var(--tp-prussian)">−i = −12.0 '
        'm</text>\n'
        '            <text x="436" y="35" font-size="9.5" fill="var(--tp-prussian)">+i = +12.0 '
        'm</text>\n'
        '            <text id="tp-e08-tbm-text" x="195" y="204" font-size="10.5" '
        'fill="var(--tp-verdigris)">EPB-TBM (D = 9.8 m · z_0 = 24.0 m) · P_face = 210 kPa · GNN '
        'Twin (proposed)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a 10-meter Earth-Pressure-Balance Tunnel Boring '
        'Machine excavating beneath historic urban foundations with a translucent Peck-Mair '
        'Gaussian settlement trough above would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate E.08-V (Imagining What It Would Look Like) · Artistic '
            'geotechnical cross-section imagining an Earth-Pressure-Balance Tunnel Boring Machine '
            '(EPB-TBM) boring through saturated clay beneath a city street while a Graph Neural '
            'Network digital twin monitors the Peck–Mair Gaussian settlement trough.'}

DISPATCH = {'kicker': 'FRONTIER GEOTECHNICAL DISPATCH · EPB-TBM TELEMETRY & GNN SUBSURFACE DIGITAL TWINS',
 'headline': 'Could Graph Neural Networks and Peck–Mair Gaussian Troughs Forecast Urban Settlement Ahead of the Cutterhead?',
 'body': "Building on Peck (1969) and Mair, Taylor & Bracegirdle (1993, DOI 10.1680/geot.1993.43.2.315; Mair 2008, DOI 10.1680/geot.2008.58.9.695), this folio proposes feeding TBM torque, chamber pressure, and InSAR radar to a physics-constrained GNN. Default slope is 1/1,050; no network was trained."}

META_3D = ('EPB-TBM Peck–Mair Gaussian Settlement Trough',
 'X: Transverse Offset x / i · Z: Tunnel Face Advance · Y: Subsurface Volume-Loss Settlement S(x)')

ES_TRANSLATION = {'title_es': 'Tuneladoras de Equilibrio de Presión de Tierras (EPB-TBM), Cubetas Gaussianas de '
             'Peck–Mair y Gemelos Subterráneos GNN',
 'subtitle_es': 'Cómo la cubeta gaussiana de asentamiento por conservación de volumen de Peck y '
                'Mair S(y) = S_max exp(−y² / 2i²) gobierna la excavación urbana con TBM, acoplada '
                'con Redes Neuronales de Grafos (GNN).',
 'why_es': 'Empujar una espátula de madera de lado dentro de budín espeso de chocolate abre arriba '
           'una depresión suave más ancha que la espátula, de volumen similar al desplazado en '
           'arcilla no drenada; la analogía se detiene en arenas y gravas drenadas o '
           'estratificadas, que cambian de volumen.',
 'plain_es': 'En palabras sencillas, excavar un túnel de metro bajo una ciudad activa se parece a '
             'sacar arena de la base de un reloj de arena. Veinte metros abajo, la tuneladora '
             'corta arcilla saturada. Ese corte alivia parte del empuje natural del terreno. Basta '
             'que el suelo ceda unos milímetros para que la tierra vecina ocupe el hueco alrededor '
             'del escudo en avance. Como la arcilla saturada casi no cambia de volumen al '
             'instante, ese movimiento profundo sube lentamente por los estratos superiores. En la '
             'calle aparece entonces una depresión ancha y suave llamada cubeta de asentamiento. '
             'Si un edificio histórico de ladrillo se hunde disparejo, las juntas se agrietan y '
             'las tuberías subterráneas se esfuerzan. Las cuadrillas reducen ese descenso '
             'sosteniendo pasta acondicionada a presión en el frente e inyectando lechada anular '
             'tras cada anillo. Este folio plantea además, como propuesta no probada, usar redes '
             'de grafos para pronosticar movimientos del terreno.',
 'deep_es': 'En campo, la estabilidad exige equilibrar la presión de cámara con el empuje del '
            'terreno y del agua (Anagnostou y Kovári 1996, DOI 10.1016/0886-7798(96)00017-X), '
            'acondicionando la arcilla en el tornillo sinfín e inyectando lechada anular (Merritt y '
            'Mair 2006, DOI 10.1680/geot.2006.56.9.605; Mair 2008, DOI 10.1680/geot.2008.58.9.695). '
            'En este laboratorio, P_face = 210 kPa es un punto supuesto que no altera V_L, mientras '
            'que V_L gobierna la cubeta de Peck y Mair (1993, DOI 10.1680/geot.1993.43.2.315). Con '
            'D = 9.8 m, V_L = 0.75 %, K = 0.5 y z_0 = 24 m resulta S_max = 18.8 mm y pendiente '
            '1/1,050, bajo el límite ilustrativo de 1/500 (cf. Skempton y MacDonald 1956, DOI '
            '10.1680/ipeds.1956.12202; Boscardin y Cording 1989, DOI '
            '10.1061/(ASCE)0733-9410(1989)115:1(1)). La red GNN propuesta no se entrenó.',
 'bridge_es': 'El acondicionamiento con espumas reduce el esfuerzo de fluencia de la arcilla en el tornillo sinfín, vocabulario común con otros geles. Es solo una analogía: este folio no modela fluidos biológicos ni trata de salud.'}
