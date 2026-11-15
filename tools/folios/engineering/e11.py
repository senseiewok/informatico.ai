#!/usr/bin/env python3
"""Folio E.11 (ENGINEERING): Continuum Topology Optimization & Skyscraper Inerter Damping: SIMP Penalization, Michell Funicular Trusses & Trabecular Bone Mechanics."""
from __future__ import annotations

SLUG = 'e11'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.11',
 'slug': 'e11',
 'pillar': 'engineering',
 'category_code': 'E',
 'parent_folios': ['E.10', 'A.01'],
 'lineage_mode': 'CONTINUATION · Continues E.10 3DCP Additive Construction & A.01 Funicular Shell '
                 'Geometry',
 'title': 'Continuum Topology Optimization & Skyscraper Inerter Damping: SIMP Penalization, '
          'Michell Funicular Trusses & Trabecular Bone Mechanics',
 'subtitle': "Continuing Folio E.10's robotic 3D concrete printing and A.01's funicular vaults: "
             'how Bendsøe–Sigmund SIMP topology optimization, Michell minimum-weight trusses, and '
             'flywheel inerters could reduce the material in floors while managing wind sway, '
             'shown as an illustrative design study.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'TOPOLOGY & INERTER · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'min_ρ c(ρ) = Uᵀ K(ρ) U · E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) · F_inerter = b '
                  '(ü_2 − ü_1)',
 'colophon': {'identifier': 'E.11 · SIMP Topology Optimization & Inerter Damping · Eurocode 2 / '
                            'ACI 318',
              'kernels': 'Bendsøe–Sigmund SIMP Penalization · Michell Orthogonal Hencky Nets · '
                         'Smith Inerter b',
              'benchmarks': 'V/V_0 = 0.35 · p = 3.0 ⇒ 1 − V/V_0 = 65% less slab concrete volume · '
                            'b/m = 0.18 inerter ratio (drift reduction not computed)',
              'bridge': "Continues E.10/A.01 · Trabecular Bone Remodeling (Wolff's Law) ↔ Robotic "
                        '3DCP Funicular Floor Ribs'},
 'sliders': [{'label': 'Target Material Volume Fraction (V / V_0)',
              'min': 0.2,
              'max': 0.8,
              'step': 0.01,
              'value': 0.35,
              'unit': 'V/V_0 = '},
             {'label': 'Inerter Apparent-Mass Ratio (μ_b = b / m)',
              'min': 0.02,
              'max': 0.4,
              'step': 0.02,
              'value': 0.18,
              'unit': 'μ_b = '}],
 'steps': ["Stage 1 (Wolff's Trabecular Bone Remodeling & Principal Stress Trajectories): Under "
           'gravity and wind loads, a continuum finite-element model (FEniCS/dolfinx is one '
           'open-source tool a reader could use; this folio ran no FE model) gives principal '
           'tensile and compressive stress trajectories σ_1, σ_2.',
           'Stage 2 (SIMP Power-Law Penalization & Helmholtz PDE Filtering): Element stiffness '
           'E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) with p = 3 pushes intermediate densities toward '
           '0 or 1, while a filter radius r_min suppresses checkerboard patterns and mesh '
           'dependency.',
           'Stage 3 (Toward Michell-like Layouts): For simple load cases, optimized layouts tend to '
           "resemble Anthony Michell's 1904 minimum-weight trusses. Keeping V/V_0 = 0.35 means 65% "
           'less concrete volume in the optimized slab region than a solid slab of the same '
           'envelope; whole-building savings would be smaller.',
           'Stage 4 (Flywheel Inerter): A ball-screw or rack-and-pinion flywheel inerter F = b(ü_2 − '
           'ü_1) has inertance b much larger than its own mass: for a ring flywheel on a screw, b = '
           'm_fly (2π r / P)², so r = 45 mm and lead P = 20 mm give b ≈ 200 m_fly (illustrative). '
           'Inerter-based devices have been studied for structural vibration suppression (Lazar et '
           'al. 2013); the drift reduction in the lab is illustrative.'],
 'readouts': [{'label': 'Compliance Ratio (rough scaling, c / c_0)',
               'value': '≈ 2.9× (c ∝ 1/(V/V_0), illustrative)'},
              {'label': 'Slab Concrete Volume Reduction',
               'value': '−65% (1 − V/V_0; CO2e assumed proportional)'},
              {'label': 'Inerter Apparent Mass Gain',
               'value': '≈ 200× flywheel mass (r = 45 mm, P = 20 mm)'},
              {'label': 'Model Filter Status',
               'value': 'FILTERED · no checkerboard in illustrative layout'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 41 00 (filing label)',
                'title': 'Topology-Optimized Funicular Ribbed Floor Slabs & Tuned Inerter Mass '
                         'Dampers (Design Study)',
                'body': 'Design study: formwork-free 3D-printed ribbed slabs shaped by '
                        'Helmholtz-filtered SIMP topology optimization (p = 3, r_min = 45 mm assumed) '
                        'paired with ball-screw flywheel inerters in tall-building outriggers. Not '
                        'designed to or checked against any code.',
                'meta': 'Method: Sigmund (2001) DOI 10.1007/s001580050176 · Inerter: Smith (2002) '
                        'DOI 10.1109/TAC.2002.803532'},
 'sidenote_1': {'kicker': 'SIDENOTE E.11-A · CROSS-FIELD ANALOGY · YOUR THIGH BONE & A FLYWHEEL',
                'body': 'Your femur is dense along the main load paths and lighter elsewhere, an '
                        "observation behind Wolff's Law. Topology optimization removes material in a "
                        'similar spirit. Lighter floors make tall buildings livelier in wind, which '
                        'is where inerter-based dampers could help; the inerter is widely described '
                        'as first used in Formula 1 suspensions (Lazar et al. 2013).'},
 'sidenote_2': {'kicker': 'SIDENOTE E.11-B · SENSITIVITIES & OPEN-SOURCE SOLVERS',
                'body': 'Adjoint sensitivities ∂c/∂ρ_e = −p ρ_e^(p−1)(E_0 − E_min) u_eᵀ k_0 u_e '
                        '(as in Sigmund 2001) could be computed in open-source FEniCS/dolfinx. '
                        'Neural surrogates such as physics-informed neural networks (Raissi et al. '
                        '2019) have been proposed to speed up such loops; this folio claims no '
                        'speed-up.'},
 'skill': {'filename': 'simp-topology-inerter-damping-SKILL.md',
           'name': 'simp-topology-inerter-damping',
           'description': 'AI-agnostic structural engineering skill for Bendsøe-Sigmund SIMP '
                          'continuum topology optimization, Helmholtz PDE sensitivity filtering, '
                          'Michell funicular trusses, and tuned inerter dampers.',
           'rules': ['Penalize intermediate element densities via SIMP law E_e(rho_e) = E_min + '
                     'rho_e^p * (E_0 - E_min) with p >= 3 and E_min = 1e-9 * E_0.',
                     'Apply Helmholtz PDE density filter -r_min^2 * laplacian(rho_tilde) + '
                     'rho_tilde = rho to guarantee mesh-independent minimum member size.',
                     'Size two-terminal flywheel inerter inertance b (kg) via F = b * (a_2 - a_1) '
                     'to achieve target apparent-mass ratio mu_b = b / m_modal.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Grounding pass 2026-11-14): Withdrew the "WEF Net-Zero PASS" '
                           'verdict, the unsupported 1.14x compliance, 44% drift, 15 ms and 1,000x '
                           'figures, and the claim that Smith invented the inerter for Formula 1 '
                           '(the F1 link is now cited to Lazar et al. 2013 as a secondary account). '
                           'Corrected a Raissi PINN DOI that was credited to Fourier Neural '
                           'Operators, credited SIMP to Bendsøe 1989 rather than the 2001 99-line '
                           'code, replaced an invented 1904 scene, and removed an AI-vendor '
                           'repository and statements that the folio ran FEniCS.',
                'opus': 'Review: all DOIs checked against Crossref and the Scite index on '
                        '2026-11-14; 1 − 0.35 = 65% and (2π·45/20)² ≈ 200 recomputed by hand.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Civil Engineering flagship '
                           'continuing Folio E.10 (DOI 10.1016/j.cemconres.2018.04.005) via SIMP '
                           'continuum topology optimization, Michell trusses, and skyscraper '
                           'inerter damping.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B): '
                        'Reviewed SIMP adjoint sensitivity, Helmholtz filter length scale, and '
                        'Smith inerter transfer function. The word "Verified" is withdrawn in REV '
                        '1.1: no FE run or measurement backed the headline numbers.'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1007/s001580050176',
           'fetched_on': '2026-11-08',
           'citing_publications': 2752,
           'supporting': 18,
           'mentioning': 1181,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Sigmund 2001, "A 99 line topology optimization code '
                      'written in Matlab" (DOI 10.1007/s001580050176), fetched 2026-11-08: 2,752 '
                      'citing publications (18 supporting, 1,181 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['E.10', 'A.01'],
 'lineage_mode': 'CONTINUATION · Continues E.10 3DCP Additive Construction & A.01 Funicular Shell '
                 'Geometry',
 'scite': {'doi': '10.1007/s001580050176',
           'fetched_on': '2026-11-08',
           'citing_publications': 2752,
           'supporting': 18,
           'mentioning': 1181,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Sigmund 2001, "A 99 line topology optimization code '
                      'written in Matlab" (DOI 10.1007/s001580050176), fetched 2026-11-08: 2,752 '
                      'citing publications (18 supporting, 1,181 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this folio.'},
 'act1_title': 'Act I — Cool Fact & Human Story: Why a Solid Concrete Floor Slab Carries So '
               'Much of Its Own Weight',
 'act1_dropcap': 'In 1904 the Australian engineer Anthony Michell published "The limits of '
                 'economy of material in frame-structures" in the Philosophical Magazine (Michell '
                 '1904). He asked how a truss carrying a given load could use the least material, '
                 'and showed that the answers are often curved, crossing families of tension and '
                 'compression members rather than rectangular frames. Twelve years earlier, in '
                 '1892, the anatomist Julius Wolff had argued that bone adapts its internal '
                 'structure to the loads it carries. The resemblance between the two is a '
                 'popular analogy, not a proof. In Michell\'s day builders had no practical way to '
                 'cast concrete or metal into such intricate shapes, so solid slabs remained the '
                 'norm.',
 'act1_plain_bridge': 'In plain words, solid concrete floors are heavy, and in a long-span slab a '
                      'large part of what the concrete carries is its own weight, because flat '
                      'formwork is simple to build. This folio does not put a sourced percentage '
                      'on that share. It matters because cement production is commonly estimated '
                      'at up to about eight percent of carbon dioxide emissions worldwide (an '
                      'estimate not sourced in this folio). Nature solves this problem far more intelligently: '
                      'your thigh bone is not a solid block of mineral, but a hollow cylinder '
                      'supported by internal struts where forces actually flow. Computer '
                      'algorithms can mimic this idea, removing concrete where stress is low. '
                      'Combined with robotic printing and compact flywheel dampers (inerters), '
                      'this folio sketches how a floor region could use about sixty-five percent '
                      'less concrete while sway is kept in check. It is a design study, not a '
                      'tested building.',
 'act1_body': "For a century, building Michell-like optimal trusses in concrete was rarely "
              'economic because intricate molds cost more than the concrete saved. Solid '
              'Isotropic Material with Penalization (SIMP) topology optimization, introduced by '
              'Martin Bendsøe (1989, DOI 10.1007/BF01650949) and made widely accessible by Ole '
              "Sigmund's 99-line code (2001, DOI 10.1007/s001580050176), removes low-stress "
              'material from a finite-element mesh, and printable concretes (Roussel 2018, DOI '
              '10.1016/j.cemconres.2018.04.005) could in principle build the resulting ribs '
              'without formwork. Removing slab mass makes tall buildings lighter and can make '
              'them more responsive to wind. One way to add dynamic resistance without dead '
              'weight is the inerter, a mechanical network element introduced by Malcolm C. '
              'Smith (IEEE Trans. Autom. Control 2002, DOI 10.1109/TAC.2002.803532), later '
              'studied for structural vibration suppression (Lazar et al. 2013). Driving a '
              'flywheel through a ball screw, a 300 kg inerter with the 200x ratio above would '
              'have an inertance of 60 tonnes (300 x 200 = 60,000 kg); this is an illustrative '
              'calculation, not a product rating.',
 'act1_stakes': 'The global stakes of structural optimization connect urban growth directly to '
                'climate resilience. With urban populations expanding, cities must construct '
                'billions of square meters of floor area over the coming decades. Pouring '
                'conventional solid concrete slabs squanders non-renewable sand supplies and '
                'drives massive greenhouse gas emissions from cement kilns. Yet simply thinning '
                'concrete members using classical rules introduces catastrophic risks: slender '
                'slabs deflect excessively, crack across tension zones, and transmit footstep '
                'vibrations throughout the building. In supertall towers, lighter floors lower the '
                'natural structural frequency, bringing the building into resonance with wind '
                'gusts and causing discomfort for occupants. Traditional tuned mass dampers can '
                'need a pendulum of hundreds of tonnes in the top floors, occupying valuable '
                'space. Pairing topology-optimized floor geometry with tuned flywheel inerters is '
                'one proposed way to ease this trade-off; this folio does not show that it '
                'outperforms conventional damping.',
 'pullquote': '"Nature does not build a solid femur, and a floor need not be a solid slab: in this '
              'design study, SIMP topology optimization keeps 35% of the concrete, while a '
              'flywheel inerter can act like a mass far larger than its own."',
 'chronology': [('1892',
                 'Julius Wolff publishes his law of bone transformation: bone adapts its internal '
                 'structure to mechanical load.'),
                ('1904',
                 'Anthony G. M. Michell publishes "The limits of economy of material in '
                 'frame-structures" (DOI 10.1080/14786440409463229).'),
                ('1989–2001',
                 'Martin Bendsøe introduces the material-distribution approach behind SIMP (DOI '
                 "10.1007/BF01650949); Ole Sigmund's 99-line educational code follows in 2001 "
                 '(DOI 10.1007/s001580050176).'),
                ('2002–2013',
                 'Malcolm Smith introduces the inerter (DOI 10.1109/TAC.2002.803532); Lazar, '
                 'Neild and Wagg study an inerter-based device for structural vibration '
                 'suppression (DOI 10.1002/eqe.2390).')],
 'act2_title': 'Act II — Cross-Field Intuition: Trabecular Bone Remodeling Meets the Flywheel '
               'Inerter',
 'act2_analogy': 'Everyday analogy: Look at a human femur: it is not a solid rock, but a hollow '
                 'tube reinforced inside by crisscrossing struts along the paths where your weight '
                 'bears down. Pairing bone-like floor slabs with a flywheel inerter is like giving '
                 'a lightweight gymnast extra momentum: the floor is lighter, yet when wind pushes '
                 'on the building, the spinning flywheel adds apparent inertia against sway.',
 'act2_plain_primer': 'To examine how advanced optimization lightens structures while preserving '
                      'stability, our interactive model provides two primary sliders. The first '
                      'control is the Target Material Volume Fraction, which specifies what '
                      'portion of the original solid concrete slab is retained. As you drag this '
                      'slider down from eighty percent to thirty-five percent, the optimization '
                      'algorithm progressively dissolves low-stress concrete, leaving behind a web '
                      'of arched compression ribs and tension ties that mimic natural bone '
                      'structures. The second control is the Inerter Apparent-Mass Ratio, which '
                      'adjusts the virtual inertial resistance provided by the mechanical flywheel '
                      'damper in the building core. Because shedding structural weight makes a '
                      'tower more susceptible to wind gusts, increasing this inerter ratio adds '
                      'apparent dynamic mass. By balancing these two controls, you can explore, in '
                      'an illustrative model, how cutting slab concrete by sixty-five percent '
                      'interacts with wind response.',
 'distill_diagram': {'analogy_title': 'Trabecular Bone & Flywheel Damper',
                     'analogy_sub': 'Hollow bone arches save mass while spinning flywheels add '
                                    'inertia',
                     'force_a_title': 'Target Volume Fraction (V/V_0)',
                     'force_a_sub': 'Carves away lazy, low-stress concrete to form Michell '
                                    'funicular ribs',
                     'force_b_title': 'Inerter Apparent Mass (mu_b)',
                     'force_b_sub': 'Multiplies virtual resistance to suppress wind sway without '
                                    'weight',
                     'threshold_title': 'Checkerboard Mesh & Dynamic Resonance Limit',
                     'threshold_pass': 'Optimized (model): clean funicular paths and lower '
                                       'illustrative wind drift',
                     'threshold_fail': 'Failure: Unfiltered checkerboard mesh or excessive typhoon '
                                       'sway'},
 'act2_intuition': 'In SIMP continuum topology optimization, a design domain discretized into '
                   'finite elements seeks to minimize structural compliance c(rho) = U^T K(rho) U '
                   'under a total volume constraint V(rho) <= V_target. To prevent the formation '
                   'of non-physical intermediate densities, element elastic moduli are penalized '
                   'according to the power law E_e(rho_e) = E_min + rho_e^p (E_0 - E_min), '
                   'typically with exponent p = 3. Because intermediate densities yield '
                   'disproportionately low stiffness relative to mass, adjoint sensitivity '
                   'gradients rapidly polarize densities toward zero or one. A Helmholtz PDE '
                   'filter -r_min^2 laplacian(rho_tilde) + rho_tilde = rho imposes a '
                   'characteristic length scale r_min, suppressing checkerboard numerical '
                   'instabilities so layouts approach Michell-like trusses. As a rough rule of '
                   "thumb (this folio's approximation, not a sourced result), the compliance of a "
                   'stiffness-optimal layout grows roughly as 1/(V/V_0), so keeping 35% of the '
                   'material gives c/c_0 of about 1/0.35 = 2.9 against the solid slab. '
                   'Simultaneously, '
                   'building vibration under dynamic wind excitation is mitigated by a '
                   'two-terminal inerter. The device converts relative linear displacement into '
                   'high-speed flywheel rotation, exerting an inertial resisting force F = b (a_2 '
                   '- a_1). By tuning the apparent mass b = m_fly (2 pi r / P)^2, engineers adjust '
                   'structural resonant frequencies without adding real dead weight.',
 'act2_deepening': 'At a deeper theoretical level, the convergence of SIMP topology optimization '
                   'onto orthogonal funicular trusses reveals the mathematical kinship between '
                   "continuum mechanics and biological morphogenesis. Julius Wolff's 1892 "
                   'hypothesis stated that bone adapts to mechanical stress; for simple load cases, '
                   'compliance-minimizing layouts tend to follow principal-stress directions, as '
                   "Michell's theory predicts. The parallel with bone is an analogy. At "
                   'element interfaces, the Helmholtz filter acts as an implicit diffusion '
                   'operator, preventing singular point loads from generating infinitely fine, '
                   'unprintable micro-struts. Meanwhile, the mechanical inerter breaks the '
                   'classical trade-off of structural dynamics. In a traditional tuned mass '
                   'damper, the supplemental mass must physically reside inside the building, '
                   'imposing massive static gravity loads on columns and foundations. An inerter '
                   'decouples gravitational weight from dynamic resistance: the ball-screw '
                   'mechanism turns small displacements into fast flywheel rotation, creating '
                   'large apparent inertia; paired with a damper, it can help absorb vibration '
                   'energy.',
 'walkthrough': ['Experiment 1 (SIMP Volume Fraction V/V_0): Drag Target Volume Fraction from 0.80 '
                 'down to 0.35. Watch lazy low-stress concrete dissolve away into a crisp Michell '
                 'funicular arch-and-tie rib network.',
                 'Experiment 2 (Inerter Apparent-Mass Ratio μ_b): Increase Inerter Mass Ratio b/m '
                 'from 0.02 to 0.18. Observe the illustrative wind-response curve fall without '
                 'adding structural dead weight (the size of the drop is not computed from a '
                 'dynamic model).',
                 'Experiment 3 (Counterfactual Knockout ⚡): Click [⚡ Counterfactual] in the SVG '
                 'toolbar to knock out Helmholtz PDE filtering and watch checkerboard mesh '
                 'instability fracture the load path.'],
 'act4_title': "Act IV — Imagining Humanity's Future: Open-Source Solvers + AI Surrogates for "
               'Lighter Floors',
 'act4_human_ai': 'By coupling open-source FEniCS/dolfinx finite-element scripts with neural '
                  'surrogates such as physics-informed neural networks (Raissi et al. 2019, DOI '
                  '10.1016/j.jcp.2018.10.045), an architect could one day sketch a school or '
                  'hospital floor plan and get a quick approximate rib layout to refine with a full '
                  'finite-element check. This is a proposal; the folio claims no speed or carbon '
                  'figure for it.',
 'act4_deepening': 'Looking ahead, generative topology optimization, construction robotics, and '
                   'neural surrogates could change how floors are designed. Surrogates trained on '
                   'many finite-element solutions might let designers explore rib layouts '
                   'interactively, and the resulting geometry could be sent to 3D concrete '
                   'printers that deposit mortar along principal stress lines without plywood '
                   'formwork. These are research directions, not current practice this folio '
                   'sources. Open frontier challenges center on '
                   'integrating non-linear plastic buckling constraints directly into SIMP '
                   'formulation loops, certifying multi-axis inerter damper assemblies for '
                   'century-long seismic reliability, and developing circular recycling protocols '
                   "for fiber-reinforced cementitious composites. By harmonizing nature's "
                   'structural logic with modern computational mechanics and control theory, civil '
                   'engineers could build lighter, resilient spaces with less embodied carbon.',
 'cf_bridge': 'Standalone Structural Topology & Damping Flagship (E.10 -> E.11): Engineered for '
              'structural, civil, and mechanical engineers designing minimum-weight slabs and '
              'tall-building tuned inerter dampers.',
 'sources': ['Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. '
             'Structural and Multidisciplinary Optimization, 21, 120–127. DOI: '
             '10.1007/s001580050176.',
             'Smith, M. C. (2002). Synthesis of mechanical networks: the inerter. IEEE '
             'Transactions on Automatic Control, 47(10), 1648–1662. DOI: 10.1109/TAC.2002.803532.',
             'Bendsøe, M. P. (1989). Optimal shape design as a material distribution problem. '
             'Structural Optimization, 1(4), 193–202. DOI: 10.1007/BF01650949.',
             'Bendsøe, M. P., & Sigmund, O. (2003). Topology Optimization: Theory, Methods, and '
             'Applications. Springer.',
             'Michell, A. G. M. (1904). The limits of economy of material in frame-structures. '
             'Philosophical Magazine, 8(47), 589–597. DOI: 10.1080/14786440409463229.',
             'Lazar, I. F., Neild, S. A., & Wagg, D. J. (2013). Using an inerter-based device for '
             'structural vibration suppression. Earthquake Engineering & Structural Dynamics, '
             '43(8), 1129–1147. DOI: 10.1002/eqe.2390.',
             'Roussel, N. (2018). Rheological requirements for printable concretes. Cement and '
             'Concrete Research, 112, 76–85. DOI: 10.1016/j.cemconres.2018.04.005.',
             'Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural '
             'networks. Journal of Computational Physics, 378, 686–707. DOI: '
             '10.1016/j.jcp.2018.10.045.',
             'Open-source tool a reader could use: FEniCS/dolfinx finite-element engine '
             '(https://github.com/FEniCS/dolfinx). This folio did not run it.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="SIMP Continuum '
        'Topology Optimization Michell Funicular Rib Slab and Flywheel Inerter Damper">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">SIMP Trabecular Slab (V/V_0 = 0.35 · −65% slab volume)</text>\n'
        '            <rect x="44" y="42" width="320" height="118" rx="6" fill="var(--tp-stone)" '
        'fill-opacity="0.22" stroke="currentColor" stroke-opacity="0.25" stroke-dasharray="4,3"/>\n'
        '            <path d="M 52 152 Q 204 38 356 152" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="5"/>\n'
        '            <path d="M 88 152 Q 204 68 320 152" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="3.2"/>\n'
        '            <line x1="52" y1="152" x2="356" y2="152" stroke="var(--tp-minium)" '
        'stroke-width="2.6"/>\n'
        '            <line x1="125" y1="92" x2="155" y2="152" stroke="var(--tp-prussian)" '
        'stroke-width="2"/>\n'
        '            <line x1="204" y1="68" x2="204" y2="152" stroke="var(--tp-prussian)" '
        'stroke-width="2.2"/>\n'
        '            <line x1="283" y1="92" x2="253" y2="152" stroke="var(--tp-prussian)" '
        'stroke-width="2"/>\n'
        '            <circle cx="52" cy="152" r="5" fill="var(--tp-minium)"/>\n'
        '            <circle cx="356" cy="152" r="5" fill="var(--tp-minium)"/>\n'
        '            <text x="48" y="176" font-size="9.5" fill="var(--tp-verdigris)">Michell '
        'Hencky-Net Compression Arch + Tension Tie</text>\n'
        '            <line x1="388" y1="24" x2="388" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="406" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Flywheel Inerter Damper F = b(ü_2 − ü_1)</text>\n'
        '            <g transform="translate(495, 106)">\n'
        '              <circle cx="0" cy="0" r="38" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3" stroke-dasharray="8,4"/>\n'
        '              <circle cx="0" cy="0" r="24" fill="var(--tp-verdigris)" fill-opacity="0.18" '
        'stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '              <circle cx="0" cy="0" r="5" fill="var(--tp-minium)"/>\n'
        '              <line x1="-68" y1="0" x2="-38" y2="0" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '              <line x1="38" y1="0" x2="68" y2="0" stroke="var(--tp-prussian)" '
        'stroke-width="2.5"/>\n'
        '            </g>\n'
        '            <text x="406" y="176" font-size="9.5" fill="var(--tp-prussian)">Apparent Mass '
        'b ≈ 200× flywheel mass (illustrative)</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Illustrative '
        'layout · not an FE result</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a topology-optimized trabecular concrete vaulted '
        'ceiling with Michell funicular ribs and a precision flywheel inerter damper core would '
        'look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.11-V (Imagining What It Would Look Like) · Artistic '
            'civil-engineering visualization (continuing Folios E.10 & A.01) imagining a '
            'formwork-free trabecular concrete floor slab paired with a high-inertia flywheel '
            'damper.'}

DISPATCH = {'kicker': 'FRONTIER STRUCTURAL OPTIMIZATION DISPATCH · CONTINUING E.10 & A.01 · SIMP & INERTERS',
 'headline': 'A Design Study: SIMP Topology Optimization and Flywheel Inerters for Lighter Floor '
             'Slabs',
 'body': 'This folio sketches how Bendsøe–Sigmund SIMP topology optimization (Sigmund 2001, DOI '
         '10.1007/s001580050176), printable concretes (Roussel 2018, DOI '
         '10.1016/j.cemconres.2018.04.005) and Smith\'s inerter (DOI 10.1109/TAC.2002.803532) '
         'could together replace solid flat slabs with bone-like ribs while inerters help manage '
         'wind sway. Its figures are illustrative.'}

META_3D = ('SIMP Compliance & Inerter Transfer Function Surface',
 'X: Volume Fraction V/V_0 · Z: Inerter Ratio μ_b · Y: Normalized Structural Compliance c/c_0')

ES_TRANSLATION = {'title_es': 'Optimización Topológica Continua SIMP y Amortiguadores Inerter en Rascacielos: '
             'Armaduras de Michell y Mecánica Ósea Trabecular',
 'subtitle_es': 'Continuando los Folios E.10 y A.01: cómo la optimización topológica SIMP de '
                'Bendsøe–Sigmund, las armaduras mínimas de Michell y los inerters de volante '
                'podrían reducir el material de las losas sin descuidar la oscilación por viento, '
                'como estudio de diseño ilustrativo.',
 'why_es': 'Tu fémur es denso a lo largo de las trayectorias de carga y más ligero en otras '
           'partes; unir nervaduras tipo hueso con un volante de inercia (inerter) es una idea '
           'para losas con menos concreto que sigan controlando la oscilación.',
 'plain_es': 'En palabras sencillas, las losas macizas de concreto son pesadas, y en un claro '
             'largo buena parte de lo que carga el concreto es su propio peso, porque la cimbra '
             'plana es sencilla de armar. Este folio no da un porcentaje con fuente para esa '
             'proporción. Importa porque la producción de cemento suele estimarse en hasta cerca '
             'del ocho por ciento de las emisiones mundiales de dióxido de carbono (estimación '
             'sin fuente en este folio). La naturaleza resuelve este problema con mucha mayor '
             'elegancia: el fémur humano no es un bloque sólido de hueso, sino una estructura '
             'hueca reforzada por arcos internos donde realmente viajan las fuerzas. Hoy en día, '
             'algoritmos de optimización topológica siguen una idea parecida y eliminan material '
             'donde el esfuerzo es bajo. Combinados con amortiguadores de volante (inerters), este '
             'folio esboza una zona de losa con cerca de sesenta y cinco por ciento menos '
             'concreto y la oscilación bajo control. Es un estudio de diseño, no un edificio '
             'probado.',
 'deep_es': 'La optimización estructural de entrepisos equilibra dos demandas contrapuestas: '
            'reducir la masa para abatir la huella de carbono y mantener la rigidez dinámica para '
            'evitar oscilaciones excesivas por viento o sismo. Mediante el método SIMP, el '
            'algoritmo penaliza las densidades intermedias con una ley potencial en la '
            'computadora, guiando la distribución de material hacia arcos de compresión y tensores '
            'inspirados en las armaduras de Michell. Para evitar patrones inestables de tablero de '
            'ajedrez, un filtro diferencial de Helmholtz asegura dimensiones mínimas imprimibles. '
            'Sin embargo, al retirar hasta dos tercios del concreto, la estructura se vuelve más '
            'ligera y sensible al viento. Para contrarrestar esto sin añadir peso muerto, los '
            'ingenieros acoplan inerters mecánicos que transforman el desplazamiento lineal en '
            'rotación de alta velocidad, generando una masa aparente mucho mayor que la propia. '
            'Este diseño conjunto es una propuesta: podría permitir imprimir losas nervadas sin '
            'cimbra con menos cemento, pero este folio no lo demuestra.',
 'bridge_es': 'La optimización topológica SIMP con filtrado PDE de Helmholtz (que un lector podría '
              'ejecutar en FEniCS/dolfinx; este folio no lo hizo) produce nervaduras funiculares '
              'que podrían imprimirse en 3D sin cimbra.'}
