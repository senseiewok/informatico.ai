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
 'subtitle': "Continuing Folios E.10 and A.01: an explanatory model—not a structural design "
             'method—on how Bendsøe–Sigmund SIMP topology optimization, Michell trusses, and '
             'flywheel inerters relate to slab mass and wind sway.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'TOPOLOGY & INERTER · REV 1.1',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'min_ρ c(ρ) = Uᵀ K(ρ) U · E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) · F_inerter = b '
                  '(ü_2 − ü_1)',
 'colophon': {'identifier': 'E.11 · SIMP Topology Optimization & Inerter Damping · CSI 03 41 00',
              'kernels': 'Bendsøe–Sigmund SIMP · Lazarov–Sigmund PDE Filter · Smith Inerter b',
              'benchmarks': 'V/V_0 = 0.35 · p = 3.0 ⇒ 65% less slab-zone volume · μ_b = 0.18 '
                            '(readouts 3–4 fixed text)',
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
 'steps': ['Stage 1 (Stress Trajectories): A continuum finite-element model (FEniCS/dolfinx is '
           'one open-source option; none was run here) maps principal stress paths σ_1, σ_2.',
           'Stage 2 (SIMP & Filtering): E_e(ρ_e) = E_min + ρ_e^p (E_0 − E_min) with assumed p = 3 '
           '(Bendsøe 1989; Sigmund 2001 cone filter radius r_min) pairs with the Lazarov & '
           'Sigmund (2011, DOI 10.1002/nme.3072) Helmholtz PDE density filter −r² ∇²ρ̃ + ρ̃ = ρ '
           '(with PDE length r = r_min / (2√3)).',
           'Stage 3 (Slider Heuristic): Idealized point-load layouts recall Michell (1904) nets. '
           'At V/V_0 = 0.35, Readout 1 computes 1 / max(0.05, V/V_0) ≈ 2.9× and Readout 2 '
           'computes −65% slab-zone volume; not for real structures.',
           'Stage 4 (Flywheel Inerter): Smith\'s F = b(ü_2 − ü_1) with an assumed thin rim (I = '
           'm_fly r²) gives b = m_fly (2π r / P)² = 199.86 m_fly ≈ 200× at r = 45 mm, P = 20 mm '
           '(solid disk ≈ 100×); Lazar, Neild & Wagg (2014) studied inerters for building '
           'vibration. Readouts 3–4 remain fixed text.'],
 'readouts': [{'label': 'Compliance Ratio (rough scaling, c / c_0)',
               'value': '≈ 2.9× (c ∝ 1/(V/V_0), illustrative)'},
              {'label': 'Slab Concrete Volume Reduction',
               'value': '−65% (1 − V/V_0; CO2e assumed proportional)'},
              {'label': 'Inerter Apparent Mass Gain',
               'value': '≈ 200× thin-ring mass (r = 45 mm, P = 20 mm; fixed text)'},
              {'label': 'Model Filter & Boundary Status',
               'value': 'EXPLANATORY MODEL · NOT A DESIGN METHOD (fixed text)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 41 00 (filing label)',
                'title': 'Topology-Optimized Ribbed Floor Slabs & Flywheel Inerters (Explanatory)',
                'body': 'Explanatory sketch, not a structural design method: ribbed slab concept '
                        'combining SIMP (assumed p = 3) and Helmholtz PDE filtering (assumed '
                        'cone radius r_min = 45 mm, PDE length r = r_min / (2√3) ≈ 13.0 mm) with '
                        'flywheel inerters. None of these untested numbers may be used on a real '
                        'structure or for code compliance.',
                'meta': 'SIMP: Bendsøe (1989) & Sigmund (2001) · PDE Filter: Lazarov & Sigmund '
                        '(2011) DOI 10.1002/nme.3072 · Inerter: Smith (2002)'},
 'sidenote_1': {'kicker': 'SIDENOTE E.11-A · CROSS-FIELD ANALOGY · YOUR THIGH BONE & A FLYWHEEL',
                'body': 'Your femur is dense along load paths and porous elsewhere (Wolff 1892). '
                        'Lighter floors may respond more to wind, where inerters have been '
                        'studied; Lazar, Neild & Wagg (2014) note Formula 1 suspensions as an '
                        'early use.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.11-B · SENSITIVITIES & OPEN-SOURCE SOLVERS',
                'body': 'Adjoint sensitivities ∂c/∂ρ_e = −p ρ_e^(p−1)(E_0 − E_min) u_eᵀ k_0 u_e '
                        '(Sigmund 2001) could be computed in FEniCS/dolfinx, and surrogates '
                        '(Raissi et al. 2019) have been proposed; this folio claims no speed-up.'},
 'skill': {'filename': 'simp-topology-inerter-damping-SKILL.md',
           'name': 'simp-topology-inerter-damping',
           'description': 'Explanatory companion on Bendsøe-Sigmund SIMP optimization, Sigmund '
                          '(2001) sensitivity filtering, Lazarov-Sigmund (2011) Helmholtz PDE '
                          'density filtering, Michell trusses, and Smith (2002) inerters. '
                          'Explanation, not a design method; none of its numbers apply to real '
                          'structures.',
           'rules': ['Explanation, not a design method: none of these assumed numbers (V/V_0 = '
                     '0.35, c/c_0 approx 2.9x, -65%, r_min = 45 mm, r approx 13.0 mm, r_fly = 45 '
                     'mm, P = 20 mm, b approx 200 * m_fly, mu_b = 0.18) may be used on a real '
                     'structure.',
                     'Separate SIMP E_e(rho_e) = E_min + rho_e^p * (E_0 - E_min) and Sigmund '
                     '(2001, DOI 10.1007/s001580050176) cone sensitivity filtering (radius r_min) '
                     'from Lazarov & Sigmund (2011, DOI 10.1002/nme.3072) PDE density filtering '
                     '-r^2 * laplacian(rho_tilde) + rho_tilde = rho with r = r_min / (2*sqrt(3)).',
                     'Separate slider heuristics (1 / max(0.05, V/V_0) and -(1 - V/V_0)) from '
                     'fixed-text readouts (thin-ring b = m_fly * (2*pi*r/P)^2 = 199.86 * m_fly '
                     'vs solid disk approx 100 * m_fly; mu_b updates its label and schematic '
                     'overlay, driving zero numerical readouts).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Grounding pass 2026-11-14): Withdrew the "WEF Net-Zero PASS" '
                           'verdict, the unsupported 1.14x compliance, 44% drift, 15 ms and 1,000x '
                           'figures, and the claim that Smith invented the inerter for Formula 1 '
                           '(the F1 link is now cited to Lazar et al. 2014 as a secondary account). '
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
                'opus': 'Cross-model check (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B): '
                        'Reviewed SIMP adjoint sensitivity, Helmholtz filter length scale, and '
                        'Smith inerter transfer function. The word "Verified" is withdrawn in REV '
                        '1.1: no FE run or measurement backed the headline numbers.'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '24 MIN READ',
 'word_count': '5,350 WORDS',
 'scite': {'doi': '10.1007/s001580050176',
           'fetched_on': '2026-11-24',
           'citing_publications': 2786,
           'supporting': 18,
           'mentioning': 1184,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Sigmund 2001, "A 99 line topology optimization code '
                      'written in Matlab" (DOI 10.1007/s001580050176), fetched 2026-11-24: 2,786 '
                      'citing publications (18 supporting, 1,184 mentioning, 0 contrasting '
                      'statements) and no retraction notice. Citing publications count distinct '
                      'papers, not statement sums, and describe that paper, not this folio.'}}

LONGFORM_DATA = {'reading_time': '24 MIN READ',
 'word_count': '5,350 WORDS',
 'parent_folios': ['E.10', 'A.01'],
 'lineage_mode': 'CONTINUATION · Continues E.10 3DCP Additive Construction & A.01 Funicular Shell '
                 'Geometry',
 'scite': {'doi': '10.1007/s001580050176',
           'fetched_on': '2026-11-24',
           'citing_publications': 2786,
           'supporting': 18,
           'mentioning': 1184,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Sigmund 2001, "A 99 line topology optimization code '
                      'written in Matlab" (DOI 10.1007/s001580050176), fetched 2026-11-24: 2,786 '
                      'citing publications (18 supporting, 1,184 mentioning, 0 contrasting '
                      'statements) and no retraction notice. Citing publications count distinct '
                      'papers, not statement sums, and describe that paper, not this folio.'},
 'act1_title': 'Act I — Cool Fact & Human Story: Why a Solid Concrete Floor Slab Carries So '
               'Much of Its Own Weight',
 'act1_dropcap': 'Look at a flat concrete floor slab spanning a wide room, and then at Anthony '
                 'Michell\'s 1904 paper "The limits of economy of material in frame-structures" '
                 'in the Philosophical Magazine. Michell asked how a frame carrying given forces '
                 'between supports could use the least bar volume, showing that minimum-volume '
                 'layouts form orthogonal tension and compression members rather than solid '
                 'beams. Twelve years earlier, in 1892, the anatomist Julius Wolff had argued '
                 'that living trabecular bone adapts its internal struts to mechanical load. The '
                 'visual resemblance between spongy bone and Michell frames remains an analogy '
                 "rather than an identity. In Michell's era, builders lacked practical ways to "
                 'cast concrete into curved rib networks, so flat solid floor slabs became '
                 'standard practice. This folio offers an explanation, not a design method, and '
                 'none of its numbers may be used on a real structure.',
 'act1_plain_bridge': 'In plain words, flat concrete floor slabs are heavy because simple plywood '
                      'molds pour concrete everywhere, even where stress stays low. Across a wide '
                      'room, a substantial share of that concrete mainly supports its own dead '
                      'weight. Your thigh bone handles load differently. Instead of forming a '
                      'solid mineral rod, it pairs a dense outer shell with crisscrossing '
                      'internal struts. Topology optimization applies a similar idea on a '
                      'computer, trimming low-stress zones from a virtual mesh while keeping '
                      'stiffer ribs. Lighter floors may sway more noticeably in wind, so '
                      'researchers also study compact spinning-flywheel dampers called inerters '
                      'to resist motion. In this explanatory model, trimming about sixty-five '
                      'percent of a slab region illustrates that trade-off. Every figure here is '
                      'an untested model illustration, not a design method, and none may be used '
                      'on a real building.',
 'act1_body': 'Custom molds once made curved concrete ribs costly. Solid Isotropic Material with '
              'Penalization (SIMP) topology optimization, formulated by Martin Bendsøe (1989, '
              "DOI 10.1007/BF01650949) and shared via Ole Sigmund's 99-line code (2001, DOI "
              '10.1007/s001580050176), trims low-stress mesh elements, while Lazarov and Sigmund '
              '(2011, DOI 10.1002/nme.3072) introduced Helmholtz PDE density filtering to bound '
              'member size. Printable concretes whose rheology Nicolas Roussel analyzed (2018, '
              'DOI 10.1016/j.cemconres.2018.04.005) might deposit ribs without formwork, though '
              'no extrusion is modeled here. Because lighter floors may raise wind acceleration, '
              "Malcolm C. Smith's inerter (2002, DOI 10.1109/TAC.2002.803532), studied for "
              'building vibration by Lazar, Neild and Wagg (2014, DOI 10.1002/eqe.2390), adds '
              'apparent inertia: an assumed 300 kg thin-ring unit at roughly 200x gain yields an '
              'untested 60,000 kg estimate, not a product rating or structural design.',
 'act1_stakes': 'Thinning floor slabs without rigorous engineering carries severe structural '
                'hazards: under-sized ribs may crack in tension, fail in punching shear, buckle '
                'locally, or transmit footfall vibration. In tall frames, cutting floor mass may '
                'also shift natural frequencies toward wind gusts unless supplemental damping is '
                'provided. Roof pendulums add heavy static load to columns. Pairing optimized '
                'floor ribs with flywheel inerters is an untested research proposal for exploring '
                'that tension; this folio runs neither a finite-element check nor a dynamic wind '
                'simulation, and it does not show that inerters outperform conventional dampers.',
 'pullquote': '"Nature does not build a solid femur, and an explanatory model may explore '
              'retaining 35% of a slab zone while a thin-ring flywheel inerter supplies apparent '
              'inertia above its static mass."',
 'chronology': [('1892',
                 'Julius Wolff publishes his treatise on bone remodeling under mechanical load.'),
                ('1904',
                 'Anthony G. M. Michell publishes "The limits of economy of material in '
                 'frame-structures" (DOI 10.1080/14786440409463229).'),
                ('1989–2011',
                 'Martin Bendsøe introduces SIMP (DOI 10.1007/BF01650949); Ole Sigmund publishes '
                 'the 99-line code (2001, DOI 10.1007/s001580050176); Lazarov and Sigmund '
                 'introduce Helmholtz PDE filtering (2011, DOI 10.1002/nme.3072).'),
                ('2002–2014',
                 'Malcolm Smith introduces the inerter (DOI 10.1109/TAC.2002.803532); Lazar, '
                 'Neild and Wagg study inerter building vibration control (2014, DOI '
                 '10.1002/eqe.2390).')],
 'act2_title': 'Act II — Cross-Field Intuition: Trabecular Bone Remodeling Meets the Flywheel '
               'Inerter',
 'act2_analogy': 'Everyday analogy: A human femur is not a solid stone rod; it is a hollow tube '
                 'braced inside by spongy struts along load paths, while a spinning flywheel '
                 'resists push-pull acceleration through rotational inertia. The analogy stops at '
                 'repair and damping: living bone heals microcracks, whereas concrete cannot, and '
                 'an inerter acts between two attachment points.',
 'act2_plain_primer': 'Our workbench provides two sliders with bounded scope. Target Material '
                      'Volume Fraction sets what share of the modeled slab zone remains; dragging '
                      'it from eighty to thirty-five percent updates Readout 1 via an '
                      'illustrative inverse compliance estimate (about 2.9 times) and Readout 2 '
                      'to minus sixty-five percent. Inerter Apparent-Mass Ratio represents '
                      'inertance over modal mass; in the browser script it updates its label and '
                      'schematic wave while driving zero numerical readouts, leaving Readouts 3 '
                      'and 4 as fixed text.',
 'distill_diagram': {'analogy_title': 'Trabecular Bone & Flywheel Damper',
                     'analogy_sub': 'Hollow bone arches save mass while spinning flywheels add '
                                    'inertia',
                     'force_a_title': 'Target Volume Fraction (V/V_0)',
                     'force_a_sub': 'Scales illustrative slab-zone volume and 1/(V/V_0) '
                                    'compliance heuristic',
                     'force_b_title': 'Inerter Apparent Mass (mu_b)',
                     'force_b_sub': 'Adjusts slider label and schematic wave; drift readout not '
                                    'computed',
                     'threshold_title': 'PDE Filter Scale & Explanatory Boundary',
                     'threshold_pass': 'Filtered concept (model): length scale r_min set; not for '
                                       'real structures',
                     'threshold_fail': 'Unfiltered mesh: checkerboard artifacts or unmodeled '
                                       'buckling/sway'},
 'act2_intuition': 'In SIMP topology optimization, a discretized domain minimizes c(rho) = U^T '
                   'K(rho) U under V(rho) <= V_target using E_e(rho_e) = E_min + rho_e^p (E_0 - '
                   'E_min) with assumed p = 3. Sigmund (2001) used a cone sensitivity filter of '
                   'radius r_min, whereas Lazarov and Sigmund (2011, DOI 10.1002/nme.3072) '
                   'introduced the Helmholtz PDE density filter -r^2 laplacian(rho_tilde) + '
                   'rho_tilde = rho with PDE length r = r_min / (2 sqrt(3)). On slider input '
                   'after page load, Readout 1 evaluates the rough heuristic c/c_0 = 1 / '
                   'max(0.05, V/V_0), giving 1 / 0.35 = 2.857 (≈ 2.9×) without solving K(rho) U '
                   '= F. A two-terminal inerter exerts F = b (a_2 - a_1); assuming a thin rim '
                   '(I = m_fly r_fly^2) on a screw of lead P gives b = m_fly (2 pi r_fly / P)^2 '
                   '= 199.86 m_fly ≈ 200× at assumed r_fly = 45 mm and P = 20 mm, whereas a '
                   'solid disk (I = 0.5 m_fly r_fly^2) gives roughly 100×.',
 'act2_deepening': 'For idealized point-load frames, minimum-compliance layouts recall Anthony '
                   "Michell's 1904 orthogonal nets, echoing Julius Wolff's 1892 bone-adaptation "
                   'proposal as an analogy. Real building floors face multi-load envelopes, '
                   'openings, punching shear, fire resistance, and creep that scalar compliance '
                   'omits. Likewise, ball-screw inerters require supplemental damping, backlash '
                   'bounds, and brace stiffness checks (Lazar, Neild & Wagg 2014) left unmodeled '
                   'in this illustrative sketch.',
 'walkthrough': ['Experiment 1 (SIMP Volume Fraction V/V_0): Drag Target Volume Fraction from '
                 '0.80 to 0.35; Readout 1 updates via 1/(V/V_0) to ≈ 2.9× and Readout 2 to −65% '
                 'in the modeled slab zone.',
                 'Experiment 2 (Inerter Apparent-Mass Ratio μ_b): Drag Inerter Mass Ratio b/m '
                 'from 0.02 to 0.18; this updates the μ_b label and schematic overlay, while '
                 'Readouts 3–4 remain fixed text.',
                 'Experiment 3 (Counterfactual Knockout ⚡): Click [⚡ Counterfactual] to toggle '
                 'the BOUNDARY FRACTURE banner illustrating regularization need (a UI toggle, '
                 'not a finite-element mesh).'],
 'act4_title': "Act IV — Imagining Humanity's Future: Open-Source Solvers + AI Surrogates for "
               'Lighter Floors',
 'act4_human_ai': 'Pairing open-source finite-element libraries such as FEniCS/dolfinx (method '
                  'paper: Scroggs et al. 2022, DOI 10.1145/3524456) with surrogates such as '
                  'physics-informed neural networks (Raissi et al. 2019, DOI '
                  '10.1016/j.jcp.2018.10.045) might let researchers explore approximate rib '
                  'layouts before full nonlinear checks. This untested proposal claims no speed '
                  'or carbon figure.',
 'act4_deepening': 'Open research problems include adding nonlinear buckling, punching shear, and '
                   'multi-load constraints to PDE-filtered optimization, testing printed ribbed '
                   'slabs to failure, and measuring screw wear and backlash in inerter-damper '
                   'frames. None of those steps appear here; this page remains an untested '
                   'conceptual explanation rather than a structural method.',
 'cf_bridge': 'Standalone Structural Topology & Inerter Explanation (E.10 -> E.11): Written for '
              'readers studying minimum-compliance continuum formulations and two-terminal '
              'inertial networks; not for structural sizing.',
 'sources': ['Sigmund, O. (2001). A 99 line topology optimization code written in Matlab. '
             'Structural and Multidisciplinary Optimization, 21, 120–127. DOI: '
             '10.1007/s001580050176.',
             'Lazarov, B. S., & Sigmund, O. (2011). Filters in topology optimization based on '
             'Helmholtz-type differential equations. International Journal for Numerical Methods '
             'in Engineering, 86(6), 765–787. DOI: 10.1002/nme.3072.',
             'Smith, M. C. (2002). Synthesis of mechanical networks: the inerter. IEEE '
             'Transactions on Automatic Control, 47(10), 1648–1662. DOI: 10.1109/TAC.2002.803532.',
             'Bendsøe, M. P. (1989). Optimal shape design as a material distribution problem. '
             'Structural Optimization, 1(4), 193–202. DOI: 10.1007/BF01650949.',
             'Bendsøe, M. P., & Sigmund, O. (2003). Topology Optimization: Theory, Methods, and '
             'Applications. Springer.',
             'Michell, A. G. M. (1904). The limits of economy of material in frame-structures. '
             'Philosophical Magazine, 8(47), 589–597. DOI: 10.1080/14786440409463229.',
             'Lazar, I. F., Neild, S. A., & Wagg, D. J. (2014). Using an inerter-based device for '
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
        'fill="currentColor">SIMP Trabecular Slab (V/V_0 = 0.35 · −65% slab-zone volume)</text>\n'
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
        '            <text x="406" y="176" font-size="9.5" fill="var(--tp-prussian)">Thin-Ring '
        'b ≈ 200× mass (fixed text, illustrative)</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Schematic '
        'explanation · not an FE result or structure</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a topology-optimized trabecular concrete vaulted '
        'ceiling with Michell funicular ribs and a precision flywheel inerter damper core would '
        'look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.11-V (Imagining What It Would Look Like) · Artistic '
            'civil-engineering visualization (continuing Folios E.10 & A.01) imagining a '
            'formwork-free trabecular concrete floor slab paired with a flywheel damper.'}

DISPATCH = {'kicker': 'FRONTIER STRUCTURAL OPTIMIZATION DISPATCH · CONTINUING E.10 & A.01 · SIMP & INERTERS',
 'headline': 'Explanatory Model: SIMP Topology Optimization, PDE Filtering, and Flywheel '
             'Inerters for Lighter Floor Slabs',
 'body': 'This folio explains how Bendsøe–Sigmund SIMP optimization (Sigmund 2001, DOI '
         '10.1007/s001580050176), Lazarov–Sigmund Helmholtz PDE filtering (2011, DOI '
         '10.1002/nme.3072), printable-concrete rheology (Roussel 2018, DOI '
         "10.1016/j.cemconres.2018.04.005), and Smith's inerter (DOI 10.1109/TAC.2002.803532) "
         'frame slab mass versus wind sway. All numbers are illustrative and not for real '
         'structures.'}

META_3D = ('SIMP Compliance & Inerter Transfer Function Surface',
 'X: Volume Fraction V/V_0 · Z: Inerter Ratio μ_b · Y: Normalized Structural Compliance c/c_0')

ES_TRANSLATION = {'title_es': 'Optimización Topológica Continua SIMP y Amortiguadores Inerter en Rascacielos: '
             'Armaduras de Michell y Mecánica Ósea Trabecular',
 'subtitle_es': 'Continuando los Folios E.10 y A.01: modelo explicativo—no método de diseño '
                'estructural—sobre optimización SIMP de Bendsøe–Sigmund, armaduras de Michell e '
                'inerters de volante.',
 'why_es': 'Tu fémur es denso en las trayectorias de carga y poroso fuera de ellas; combinar '
           'nervaduras con un inerter ilustra ese equilibrio sin validez para obras reales.',
 'plain_es': 'En palabras sencillas, las losas macizas pesan porque una cimbra plana vacía '
             'concreto incluso donde el esfuerzo es bajo. En un claro amplio, buena parte del '
             'material carga su propio peso muerto. El fémur humano trabaja distinto. Combina una '
             'corteza densa con puntales internos cruzados. En computadora, la optimización '
             'topológica retira zonas de bajo esfuerzo en una malla virtual. Al aligerar el piso '
             'puede crecer la sensibilidad al viento, por lo que se estudian amortiguadores '
             'compactos de volante llamados inerters. Aquí, recortar cerca de sesenta y cinco por '
             'ciento de una zona ilustra ese compromiso. Es una explicación no probada, no un '
             'método de diseño, y ningún número puede usarse en estructuras reales.',
 'deep_es': 'Este análisis conceptual contrapone menor masa y control ante viento. En SIMP '
            '(Bendsøe 1989; filtro cónico de sensibilidad r_min de Sigmund 2001), p = 3 penaliza '
            'densidades intermedias, y el filtro PDE de Helmholtz de Lazarov y Sigmund (2011) '
            'usa −r² ∇²ρ̃ + ρ̃ = ρ con r = r_min / (2√3). En el deslizador, V/V_0 actualiza la '
            'razón heurística 1/(V/V_0) (≈ 2.9× en 0.35) y el −65% de volumen sin elementos '
            'finitos; los recuadros tercero y cuarto son texto fijo (b ≈ 200× para aro delgado '
            'I = m_fly r_fly²) y μ_b cambia su etiqueta y el esquema visual sin actualizar '
            'recuadros numéricos. Ninguna cifra aplica al diseño real de edificios.',
 'bridge_es': 'La optimización SIMP con filtro PDE de Helmholtz (ejecutable en FEniCS/dolfinx, no '
              'corrido aquí) ilustra nervaduras conceptuales sin validez estructural.'}
