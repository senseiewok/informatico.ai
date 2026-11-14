#!/usr/bin/env python3
"""Folio E.12 (ENGINEERING): Silicon-to-Grid Safety: Control Barrier Functions, Firefly-Synchronized Renewable Grids & the Case for a Verified Relay Processor."""
from __future__ import annotations

SLUG = 'e12'

PILLAR = 'engineering'

_SCITE = {'doi': '10.1109/TAC.2016.2638961',
          'fetched_on': '2026-11-08',
          'citing_publications': 3385,
          'supporting': 8,
          'mentioning': 2361,
          'contrasting': 0,
          'retracted': False,
          'summary': 'Scite index entry for Ames, Xu, Grizzle & Tabuada 2017 (DOI '
                     '10.1109/TAC.2016.2638961), checked 2026-11-08: 3,385 citing publications '
                     '(8 supporting, 2,361 mentioning, 0 contrasting) and no retraction notice. '
                     'These counts describe that one paper, not this folio.'}

FOLIO = {'folio_id': 'E.12',
 'slug': 'e12',
 'pillar': 'engineering',
 'category_code': 'E',
 'parent_folios': ['E.06', 'P.02', 'M.07'],
 'lineage_mode': 'SYNTHESIS · Synthesizes E.06 Infrastructure Resilience, P.02 Kuramoto '
                 'Synchronization & M.07 Optimal Control',
 'title': 'Silicon-to-Grid Safety: Control Barrier Functions, Firefly-Synchronized Renewable Grids & the Case for a Verified Relay Processor',
 'subtitle': "Synthesizing Folio E.06's critical infrastructure protection, P.02's Kuramoto "
             "oscillators, and M.07's optimal control: how virtual synchronous machine inverters "
             'and Control Barrier Functions can steady a low-inertia renewable grid, and what a '
             'machine-checked RISC-V processor would add underneath.',
 'date_published': '2026-11-07',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'SILICON-TO-GRID · REV 1.1',
 'primary_kernel': 'skills/engineering/e12/verify_e12.py',
 'governing_law': 'sup_u [L_f h(x) + L_g h(x) u] ≥ −α(h(x)) · M dΔω/dt + D Δω = P_m − P_e',
 'colophon': {'identifier': 'E.12 · RISC-V & Grid Control Barrier Functions',
              'kernels': 'Control Barrier Function h(x) ≥ 0 (Ames et al. 2017) · Swing Equation · '
                         'Kami / Coq (Rocq) processor-proof precedents',
              'benchmarks': 'Model values: RoCoF 0.42 Hz/s · h(x_grid) = +0.72 Hz · processor proof assumed, not shown',
              'bridge': 'Synthesizes E.06/P.02/M.07 · Firefly Phase-Locking ↔ Grid-Forming '
                        'Inverters'},
 'sliders': [{'label': 'Virtual Synchronous Inertia Constant (H_virt)',
              'min': 1.0,
              'max': 8.0,
              'step': 0.2,
              'value': 4.8,
              'unit': ' s'},
             {'label': 'CBF Barrier Rate (α_CBF; higher = later intervention)',
              'min': 0.5,
              'max': 5.0,
              'step': 0.1,
              'value': 2.4,
              'unit': ' s⁻¹'}],
 'steps': ['Stage 1 (Firefly-Style Phase-Locking on the Power Grid, Continuing P.02): Solar and '
           'battery grid-forming inverters hold a common rhythm through coupled phase angles θ_i, '
           'M d²θ_i/dt² + D dθ_i/dt = P_i − ∑ K_ij sin(θ_i − θ_j), a member of the coupled-oscillator family studied in \'Synchronization in complex oscillator networks and smart grids\' (Dörfler, Chertkov & Bullo 2013, DOI 10.1073/pnas.1212134110). The firefly is an analogy, not the same '
           'equation.',
           'Stage 2 (Synthetic Inertia via Virtual Synchronous Machines): In the folio model, when '
           'a 1.2 GW loss hits, battery inverters inject power proportional to −H_virt dω/dt, in '
           'the manner of synchronverters (Zhong & Weiss 2011, DOI 10.1109/TIE.2010.2048839), and at the default H_virt = 4.8 s the initial Rate of Change of Frequency (RoCoF) is 0.42 Hz/s. It stays below 0.5 Hz/s only for H_virt above about 4.0 s.',
           'Stage 3 (Control Barrier Function Quadratic Program Filter, Continuing M.07): A '
           'real-time QP filter enforces L_f h(x) + L_g h(x)u ≥ −α(h(x)). For the modelled '
           'dynamics, and while the QP stays feasible, the state x does not leave the safe set '
           'h(x) ≥ 0 (Ames et al. 2017, DOI 10.1109/TAC.2016.2638961).',
           'Stage 4 (Processor Layer, a Design Assumption): The filter is only as sound as the '
           'chip that runs it. Machine-checked RISC-V processors exist at small scale: Kami (Choi '
           'et al. 2017, DOI 10.1145/3110268) and the embedded system of Erbsen et al. (2021, DOI '
           '10.1145/3453483.3454065), both in the Coq proof assistant, now named Rocq. This folio knows of no published machine-checked proof for the processor of a grid protection relay; here it is assumed, not shown.'],
 'readouts': [{'label': 'Grid Frequency Nadir (f_min)', 'value': '59.82 Hz (model value)'},
              {'label': 'Initial RoCoF Before Filter', 'value': '0.42 Hz/s (< 0.50 model limit)'},
              {'label': 'CBF Barrier Margin h(x)', 'value': '+0.72 Hz above 59.1 Hz trip (model)'},
              {'label': 'CBF Filter State', 'value': 'IDLE · constraint slack (model)'}],
 'spec_plate': {'division': 'GRID-FORMING INVERTERS / CBF-QP / RISC-V (PROOF ASSUMED)',
                'title': 'Grid-Forming Virtual Synchronous Inverters with a Control Barrier '
                         'Function Safety Filter',
                'body': 'Distributed battery and solar grid-forming inverters governed by a '
                        'Control Barrier Function (CBF-QP) safety filter. The filter is specified '
                        'to run on a RISC-V processor whose formal proof is a design assumption '
                        'of this folio, modelled on published Coq (Rocq) and Kami work.',
                'meta': 'Anchors: Ames et al. 2017, DOI 10.1109/TAC.2016.2638961 · Dörfler, '
                        'Chertkov & Bullo 2013, DOI 10.1073/pnas.1212134110'},
 'sidenote_1': {'kicker': 'SIDENOTE E.12-A · CROSS-FIELD ANALOGY · FIREFLIES FLASHING AS ONE',
                'body': 'Coal and hydro turbines steadied the 60 Hz grid with spinning steel. '
                        'Solar panels have no moving parts, so grid-forming inverters are '
                        'programmed to behave like a rotating machine and to fall into step with '
                        'their neighbours, much as fireflies along a riverbank come to flash '
                        'together. The network that such inverters would sit in can be described '
                        'in the open-source toolbox PyPSA/PyPSA; the swing dynamics on this page '
                        "are the folio's own reduced model."},
 'sidenote_2': {'kicker': 'SIDENOTE E.12-B · VERIFIED HARDWARE · WHAT HAS BEEN PROVED SO FAR',
                'body': 'Kami (Choi et al. 2017, DOI 10.1145/3110268) is a library for the Coq '
                        'proof assistant, now named Rocq, for specifying and verifying hardware; '
                        'its case study covers multicore systems with pipelined cores '
                        'implementing the base integer subset of RISC-V. Erbsen et al. (2021, DOI '
                        '10.1145/3453483.3454065) report a simple embedded system whose '
                        'application software, device drivers, compiler and RISC-V processor are '
                        'one object in Coq with a machine-checked proof of functional '
                        'correctness. Neither is a grid relay. A verified protection processor '
                        'is the open step this folio argues for.'},
 'skill': {'filename': 'verified-riscv-cbf-grid-sync-SKILL.md',
           'name': 'verified-riscv-cbf-grid-sync',
           'description': 'AI-agnostic cyber-physical systems skill for Virtual Synchronous '
                          'Machine (VSM) grid-forming inverters, Control Barrier Function '
                          '(CBF-QP) forward invariance, and the published Coq (Rocq) and Kami '
                          'precedents for machine-checked RISC-V processors.',
           'rules': ['Enforce Nagumo forward invariance of safe set C = {x : h(x) >= 0} via CBF '
                     'constraint L_f h(x) + L_g h(x) * u >= -alpha * h(x).',
                     'Bound grid Rate of Change of Frequency |df/dt| <= f_0 * Delta_P / (2 * '
                     'H_virt * S_base); the folio model targets less than 0.5 Hz/s after the '
                     'loss of one large unit.',
                     'Treat processor correctness as a stated assumption. Cite published '
                     'machine-checked RISC-V work (Kami, DOI 10.1145/3110268; Erbsen et al. '
                     '2021, DOI 10.1145/3453483.3454065) and never claim a verified relay '
                     'processor without a public proof artifact.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. REV 1.0 rested its '
                           'processor layer on a 180-million-line RISC-V proof attributed to '
                           'Anthropic; no public source for that proof was found on 2026-11-13, '
                           'so it has been removed. The processor layer now cites Kami (DOI '
                           '10.1145/3110268) and Erbsen et al. 2021 (DOI '
                           '10.1145/3453483.3454065) and is marked as a design assumption. The '
                           'opening no longer places Yoshiki Kuramoto on a riverbank; the '
                           'firefly observations are credited to Buck & Buck 1968 (DOI '
                           '10.1126/science.159.3821.1319). Numbers on the page are labelled as '
                           'model values.',
                'opus': 'Review: new references checked by DOI in Crossref, and all but the PyPSA paper in the Scite index; one blind frontier review applied; '
                        'the Kami and Erbsen et al. descriptions were written from their '
                        'abstracts.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-07',
                'summary': 'REV 1.0 (Published 2026-11-07): Volume VI Cyber-Physical '
                           'Infrastructure monograph synthesizing E.06, P.02, and M.07 with '
                           'Control Barrier Functions (DOI 10.1109/TAC.2016.2638961) and '
                           'PyPSA/PyPSA.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B + Gemma 4 31B): '
                        'reviewed the swing equation and the CBF-QP Lie-derivative condition. Its '
                        'statement on the provenance of the processor proof is withdrawn in '
                        'REV 1.1.'}],
 'volume': 6,
 'volume_code': 'VOL. 06',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': dict(_SCITE)}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['E.06', 'P.02', 'M.07'],
 'lineage_mode': 'SYNTHESIS · Synthesizes E.06 Infrastructure Resilience, P.02 Kuramoto '
                 'Synchronization & M.07 Optimal Control',
 'scite': dict(_SCITE),
 'act1_title': 'Act I — Cool Fact & Human Story: What Synchronized Fireflies Teach a Grid '
               'Without Spinning Turbines',
 'act1_dropcap': 'Along tidal rivers in Southeast Asia, mangrove trees full of fireflies have '
                 'long been described flashing in unison. In 1968 the biologists John and '
                 'Elisabeth Buck published a study in Science on the mechanism of that rhythmic synchronous flashing (DOI 10.1126/science.159.3821.1319). In 1975 the physicist Yoshiki Kuramoto '
                 'wrote down a compact mathematical model of how a population of coupled '
                 'oscillators, each with its own natural rhythm, can entrain itself (DOI '
                 '10.1007/BFb0013365). Half a century later, power systems engineers face a '
                 'problem of the same shape. For a hundred years, continental power grids relied '
                 'on the physical momentum of spinning steel turbines inside coal and '
                 'hydroelectric stations to keep electrical frequency close to sixty cycles per '
                 'second. As power networks move to solar and battery arrays, that mechanical '
                 'momentum declines, and the same disturbance moves the frequency faster '
                 '(Milano et al. 2018, DOI 10.23919/PSCC.2018.8450880).',
 'act1_plain_bridge': 'In plain words, an electrical power grid is like a massive tandem bicycle '
                      'ridden by millions of generators across an entire continent. For over a '
                      'century, heavy steam and water turbines acted as giant spinning flywheels, '
                      'keeping the bicycle rolling steadily forward even when climbing steep '
                      'hills. Solar panels and modern batteries provide clean electricity, but '
                      'they have no spinning parts. If a lightning strike trips a major power line '
                      'on a hot summer afternoon, a grid with little momentum has less time to '
                      'recover its rhythm. To keep the lights on, electrical engineers program '
                      'battery inverters to behave like spinning machines and to fall into step '
                      'with each other, creating synthetic momentum out of digital control. But '
                      'software can make mistakes. To add a margin, engineers can wrap the '
                      'controller in a mathematical guardrail that blocks commands leading out of '
                      'the safe operating range. The guardrail is only as trustworthy as the chip '
                      'that runs it, which is why this folio also looks at processors whose '
                      'design has been checked by a proof assistant.',
 'act1_body': 'This folio stacks three layers and is careful about which of them are established. '
              'First, grid-forming battery inverters act as Virtual Synchronous Machines (VSMs): '
              'they emulate the swing equation of a rotating generator (Zhong & Weiss 2011, DOI '
              '10.1109/TIE.2010.2048839), and power-network swing dynamics belong to the same family of coupled-oscillator equations as the Kuramoto model (Dörfler, Chertkov & Bullo 2013, DOI 10.1073/pnas.1212134110). The open-source toolbox PyPSA/PyPSA (Brown, Hörsch & '
              'Schlachtberger 2018, DOI 10.5334/jors.188) describes the network side, meaning '
              'which generators, lines and storage exist; the swing dynamics shown here are the '
              "folio's own reduced model, not a PyPSA simulation. Second, to keep automated "
              'dispatch commands inside frequency limits, the controller uses Control Barrier '
              'Functions (Ames, Xu, Grizzle & Tabuada 2017, IEEE Trans. Autom. Control, DOI '
              '10.1109/TAC.2016.2638961). A real-time quadratic program changes the command as '
              'little as possible while keeping the safe operating set forward-invariant for the '
              "modelled dynamics. Folio M.07's constrained optimal control supplies related "
              'energy-management examples (Limebeer 2014, DOI 10.1080/00207179.2014.900705; Chao '
              'Sun 2015, DOI 10.1109/tcst.2014.2359176). Third, a sound algorithm can still fail '
              'on a faulty processor. Machine-checked processor proofs exist at small scale: Kami '
              '(Choi et al. 2017, DOI 10.1145/3110268), a Coq library for verifying hardware '
              'designs, and the embedded system of Erbsen et al. (2021, DOI '
              '10.1145/3453483.3454065), in which application software, device drivers, compiler '
              'and RISC-V processor are one object in Coq with a machine-checked proof of '
              'functional correctness. Coq is now named Rocq. This folio knows of no published machine-checked proof for the processor of a grid protection relay, so the verified processor is a design assumption.',
 'act1_stakes': 'The stakes of grid stability come from how much depends on uninterrupted '
                'electrical service. When frequency falls below emergency thresholds, automated '
                'protection disconnects equipment, and a cascade of such trips can black out a '
                'region within seconds. Hospitals, water treatment plants and cellular networks '
                'all depend on steady sixty-hertz power. As synchronous generation retires, the '
                'margin shrinks: for the same lost power, the rate of change of frequency rises '
                'in inverse proportion to the inertia that remains, leaving less time for '
                'operators and protection systems to respond. A protection controller is also a '
                'computer, and a logic or arithmetic fault in its processor could make it '
                'misbehave at the moment it is needed. Machine-checked verification is one way '
                'to remove that class of fault: it proves that a processor design meets its '
                'specification, under the assumptions the proof states. It says nothing about '
                'manufacturing defects, sensors or the grid model itself.',
 'pullquote': '"When a power grid runs on sunlight and software instead of spinning turbines, '
              'this folio argues for two layers: a Control Barrier Function that keeps the modelled state inside a safe set, and a processor whose correctness is proved, not assumed. The first is published mathematics. The second, for grid relays, is a design assumption here."',
 'chronology': [('1942',
                 'Mitio Nagumo proves the subtangentiality theorem for forward-invariant safe sets '
                 'in differential equations.'),
                ('1968',
                 'John and Elisabeth Buck report on the mechanism of rhythmic synchronous '
                 'flashing in fireflies (Science, DOI 10.1126/science.159.3821.1319).'),
                ('1975',
                 'Yoshiki Kuramoto proposes his model of self-entrainment in a population of '
                 'coupled nonlinear oscillators (DOI 10.1007/BFb0013365; Folio P.02).'),
                ('2011–2013',
                 'Zhong & Weiss describe synchronverters, inverters that mimic synchronous '
                 'generators; Dörfler, Chertkov & Bullo study synchronization in complex oscillator networks and smart grids.'),
                ('2017',
                 'Ames, Xu, Grizzle & Tabuada publish a journal treatment of Control Barrier Function quadratic programs for safety-critical systems (DOI 10.1109/TAC.2016.2638961); Choi et al. publish Kami, a Coq '
                 'library for verifying hardware (DOI 10.1145/3110268).'),
                ('2021',
                 'Erbsen et al. report a simple embedded system whose application software, device drivers, compiler and RISC-V processor are one object in Coq, with a machine-checked proof of functional correctness (DOI '
                 '10.1145/3453483.3454065).')],
 'act2_title': 'Act II — Cross-Field Intuition: Firefly Phase-Locking + Invisible Mathematical '
               'Guardrails',
 'act2_analogy': 'Everyday analogy: Imagine thousands of fireflies flashing in unison across a '
                 'dark valley without a conductor, while a guardrail along a curving mountain '
                 'highway nudges any drifting car back toward the center of the lane. Now '
                 "imagine that the guardrail's computer is a chip whose design has been checked "
                 'against its specification by a proof assistant. Those are the three layers '
                 'this folio studies. The first two are published engineering and mathematics; '
                 'the third has been demonstrated only on small systems.',
 'act2_plain_primer': 'To understand how clean power grids maintain stability, our interactive '
                      'laboratory lets you explore two primary parameters. The first control is '
                      'the Virtual Synchronous Inertia Constant, which governs how much synthetic '
                      'momentum battery inverters inject into the grid during a sudden '
                      'disturbance. Setting this value low leaves the model grid vulnerable: if a '
                      'major generator trips, electrical frequency falls quickly toward '
                      'protection levels. Increasing this inertia gives the grid virtual weight, '
                      'slowing the fall and keeping the model within its operating band. The '
                      'second control is the Barrier Rate in our Control Barrier Function. '
                      'This setting determines how firmly the mathematical filter intervenes as '
                      'frequency approaches the danger zone. A higher rate lets the state '
                      'approach the boundary faster before the filter acts; a lower rate '
                      'intervenes earlier. Together, these two controls illustrate how control '
                      'software and a safety filter can stand in for spinning turbines. All '
                      'numbers in the laboratory are outputs of this reduced model.',
 'distill_diagram': {'analogy_title': 'Firefly Swarm & Mountain Guardrail',
                     'analogy_sub': 'Phase synchronization guided by a safety limit',
                     'force_a_title': 'Virtual Inertia (H_virt)',
                     'force_a_sub': 'Injects synthetic momentum to slow rapid grid frequency '
                                    'falls',
                     'force_b_title': 'CBF Barrier Rate (alpha_CBF)',
                     'force_b_sub': 'Quadratic program filter enforces forward-invariant safe '
                                    'operation',
                     'threshold_title': 'Grid Frequency Nadir & Protection Boundary',
                     'threshold_pass': 'Stable: model RoCoF below 0.5 Hz/s and safety filter idle',
                     'threshold_fail': 'Alert: RoCoF above 0.5 Hz/s, or the safety filter must '
                                       'intervene'},
 'act2_intuition': 'In an inverter-dominated grid, each grid-forming converter i emulates the '
                   'classical swing equation 2 H_virt dDelta_omega_i/dt + D_p Delta_omega_i = '
                   'P_ref - P_elec, written per unit. When a sudden generation loss Delta_P '
                   'occurs, the initial Rate of Change of Frequency is RoCoF = f_0 Delta_P / (2 '
                   'H_virt S_base), so doubling the virtual inertia halves it. Grid safety also '
                   'requires keeping frequency deviation and converter currents within a closed '
                   "admissible set C = {x : h(x) >= 0}. By Nagumo's theorem, forward invariance of this safe set holds if the control input u satisfies the Control Barrier Function condition L_f h(x) + L_g h(x) u + alpha(h(x)) >= 0 at all times (for continuously differentiable h with nonzero gradient on the boundary, an extended class-K function alpha, and a locally Lipschitz closed loop)."
                   ' A '
                   'real-time Quadratic Program (CBF-QP) filters high-level power dispatch '
                   'commands, adjusting them minimally and only when the barrier constraint would otherwise be violated. The guarantee belongs to the model: it holds while '
                   'the QP is feasible, the inverter has the power headroom the QP asks for, and '
                   'the processor computes what the algorithm specifies. That last condition is what machine-checked hardware addresses. The laboratory on this page fixes Delta_P = 1.2 GW on a 17.86 GW base, so RoCoF = 2.016 / H_virt Hz/s; it assumes fast reserves close the deficit linearly over 0.86 s, and it places the protection boundary at 59.1 Hz, so h = f - 59.1 Hz. The 0.5 Hz/s limit and the 59.1 Hz boundary are choices of this model, not values taken from a grid standard.',
 'act2_deepening': 'At the intersection of power electronics and formal logic, stability requires '
                   'bridging continuous differential equations and discrete digital execution. In '
                   'a physical inverter, the continuous phase dynamic is digitized into '
                   'high-speed pulse-width modulation cycles running at kilohertz frequencies. If '
                   'numerical truncation errors or communication delays accumulate between '
                   'distributed battery nodes, the network can lose synchronism and drive '
                   'circulating currents through the converters. The Control Barrier Function '
                   'acts as an analytical shield against such perturbations: by evaluating the '
                   'Lie derivative of the barrier function h(x) along system trajectories, the '
                   'quadratic program computes the minimal control intervention needed to '
                   'preserve Nagumo invariance. At the silicon level, the published precedents '
                   'show what a proof can deliver. In Kami, a hardware design is specified and '
                   'verified inside Coq and then extracted toward FPGAs (Choi et al. 2017). '
                   'Erbsen et al. (2021) represent application software, device drivers, compiler and a RISC-V processor as one mathematical object in Coq, with a machine-checked proof of functional correctness. Carrying that method to a protection relay, with its interrupts, timing bounds and sensor interfaces, is not something this folio found in the literature it cites; it is the engineering gap the folio names.',
 'walkthrough': ['Experiment 1 (Virtual Synchronous Inertia H_virt): Drag Virtual Inertia H_virt from 1.2 s up to 4.8 s. In the model the post-fault frequency nadir lifts from 59.28 Hz to 59.82 Hz, and the initial RoCoF falls from 1.68 to 0.42 Hz/s.',
                 'Experiment 2 (Control Barrier Function Rate α_CBF): Set H_virt to 1.0 s: the filter is already ACTIVE and requests about 154 MW. Lower α_CBF from 2.4 to 0.5 s⁻¹ and the requested power grows to about 932 MW, while the nadir rises from 59.24 Hz to 59.71 Hz.',
                 'Experiment 3 (Quantum · WEF & Counterfactual Overlays): Click [⚛ Quantum · WEF] '
                 'and [⚡ Counterfactual] to inspect the overlays for grid synchronization and for '
                 'the processor-layer assumption.'],
 'act4_title': "Act IV — Imagining Humanity's Future: Clean Grids with Provable Safety Margins",
 'act4_human_ai': 'Open-source grid planners (https://github.com/PyPSA/PyPSA), Control Barrier '
                  'Function safety filters and machine-checked processors each exist today. '
                  'Joined together, they sketch a path by which a grid could retire fossil-fuel '
                  'peaker plants while keeping a safety argument that can be checked line by '
                  'line. Joining them is future work: this folio is a design study, not a '
                  'deployed system.',
 'act4_deepening': 'As energy infrastructure decarbonizes, proof assistants, control theory and '
                   'open hardware offer a way to make its safety arguments explicit. A plausible '
                   'next step is a substation controller built on an open RISC-V core with a '
                   'published proof, so that anyone can inspect both the design and the argument '
                   'for its correctness. Interconnecting millions of rooftop solar systems, '
                   'electric vehicle batteries and heat pumps could turn passive consumers into '
                   'active participants in frequency regulation. Major challenges remain: '
                   'scaling Control Barrier Function quadratic programs to transmission networks '
                   'with thousands of buses in real time, carrying proofs from high-level '
                   'specifications down to physical netlists, and designing barrier functions '
                   'that stay valid as the grid and its weather change. Replacing heuristics '
                   'with machine-checked proofs does not make a grid unbreakable. It makes the '
                   'assumptions visible, so that they can be tested.',
 'cf_bridge': 'Standalone Cyber-Physical Grid Safety folio (E.06 + P.02 + M.07 -> E.12): '
              'Engineered for power-systems, control, and formal hardware verification '
              'engineers.',
 'sources': ['Ames, A. D., Xu, X., Grizzle, J. W., & Tabuada, P. (2017). Control Barrier Function '
             'Based Quadratic Programs for Safety Critical Systems. IEEE Transactions on Automatic '
             'Control, 62(8), 3861–3876. DOI: 10.1109/TAC.2016.2638961.',
             'Dörfler, F., Chertkov, M., & Bullo, F. (2013). Synchronization in complex '
             'oscillator networks and smart grids. Proceedings of the National Academy of '
             'Sciences, 110(6), 2005–2010. DOI: 10.1073/pnas.1212134110.',
             'Zhong, Q.-C., & Weiss, G. (2011). Synchronverters: Inverters That Mimic '
             'Synchronous Generators. IEEE Transactions on Industrial Electronics, 58(4), '
             '1259–1267. DOI: 10.1109/TIE.2010.2048839.',
             'Milano, F., Dörfler, F., Hug, G., Hill, D. J., & Verbič, G. (2018). Foundations '
             'and Challenges of Low-Inertia Systems (Invited Paper). 2018 Power Systems '
             'Computation Conference (PSCC), 1–25. DOI: 10.23919/PSCC.2018.8450880.',
             'Choi, J., Vijayaraghavan, M., Sherman, B., Chlipala, A., & Arvind (2017). Kami: a '
             'platform for high-level parametric hardware specification and its modular '
             'verification. Proceedings of the ACM on Programming Languages, 1(ICFP), 1–30. DOI: '
             '10.1145/3110268.',
             'Erbsen, A., Gruetter, S., Choi, J., Wood, C., & Chlipala, A. (2021). Integration '
             'verification across software and hardware for a simple embedded system. '
             'Proceedings of the 42nd ACM SIGPLAN International Conference on Programming '
             'Language Design and Implementation (PLDI), 604–619. DOI: 10.1145/3453483.3454065.',
             'Buck, J., & Buck, E. (1968). Mechanism of Rhythmic Synchronous Flashing of '
             'Fireflies. Science, 159(3821), 1319–1327. DOI: 10.1126/science.159.3821.1319.',
             'Kuramoto, Y. Self-entrainment of a population of coupled non-linear oscillators. International Symposium on Mathematical Problems in Theoretical Physics, Lecture Notes in Physics 39, 420–422. Springer, 1975 (Crossref dates the online record 2005). DOI: 10.1007/BFb0013365.',
             'Brown, T., Hörsch, J., & Schlachtberger, D. (2018). PyPSA: Python for Power System '
             'Analysis. Journal of Open Research Software, 6(1), 4. DOI: 10.5334/jors.188. '
             'Repository: https://github.com/PyPSA/PyPSA.',
             'Limebeer, D. J. N., Perantoni, G., & Rao, A. V. (2014). Optimal control of Formula '
             'One car energy recovery systems. International Journal of Control, 87(10), '
             '2065–2080. DOI: 10.1080/00207179.2014.900705.',
             'Chao Sun, Moura, S. J., Hu, X., Hedrick, J. K., & Sun, F. (2015). Velocity '
             'Predictors for Predictive Energy Management in Hybrid Electric Vehicles. IEEE '
             'Transactions on Control Systems Technology, 23(3), 1197–1204. DOI: '
             '10.1109/tcst.2014.2359176.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Control Barrier '
        'Function safe set h(x) >= 0, grid-forming inverter frequency response, and the assumed '
        'RISC-V processor layer">\n'
        '            <line x1="35" y1="188" x2="645" y2="188" stroke="currentColor" '
        'stroke-opacity="0.3"/>\n'
        '            <text x="44" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">CBF-QP Forward-Invariant Safe Set C = {x : h(x) ≥ 0}</text>\n'
        '            <ellipse cx="195" cy="112" rx="135" ry="62" fill="var(--tp-verdigris)" '
        'fill-opacity="0.14" stroke="var(--tp-verdigris)" stroke-width="2.4"/>\n'
        '            <path d="M 88 145 Q 165 65 285 92" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <line x1="255" y1="84" x2="318" y2="54" stroke="var(--tp-minium)" '
        'stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <circle cx="285" cy="92" r="5.5" fill="var(--tp-verdigris)"/>\n'
        '            <text x="85" y="118" font-size="9.5" fill="var(--tp-prussian)">L_f h(x) + L_g '
        'h(x)u ≥ −α(h(x))</text>\n'
        '            <text x="235" y="48" font-size="9" fill="var(--tp-minium)">Blocked Unsafe '
        'Command</text>\n'
        '            <line x1="365" y1="24" x2="365" y2="192" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="382" y="24" font-size="10.5" font-weight="600" '
        'fill="currentColor">Processor Layer (assumed) + 60 Hz VSM Grid</text>\n'
        '            <rect x="386" y="46" width="242" height="52" rx="6" fill="var(--tp-stone)" '
        'fill-opacity="0.3" stroke="var(--tp-prussian)" stroke-width="1.8"/>\n'
        '            <text x="400" y="68" font-size="9.5" font-weight="600" '
        'fill="var(--tp-prussian)">RISC-V relay processor: proof assumed</text>\n'
        '            <text x="400" y="86" font-size="9" fill="var(--tp-verdigris)">Precedents: '
        'Kami 2017 · Erbsen et al. 2021</text>\n'
        '            <path d="M 386 146 Q 426 112 466 146 T 546 146 T 626 146" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.6"/>\n'
        '            <text x="386" y="176" font-size="9.5" fill="var(--tp-prussian)">Model VSM '
        'Frequency Nadir: 59.82 Hz (RoCoF 0.42 Hz/s)</text>\n'
        '            <text x="44" y="206" font-size="10" fill="var(--tp-verdigris)">Reduced swing '
        'model + CBF-QP: state stays inside the safe set (model result)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a renewable power grid control room with '
        'firefly-synchronized battery inverters, Control Barrier Function phase boundaries, and a '
        'RISC-V silicon wafer would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.12-V (Imagining What It Would Look Like) · Artistic '
            'cyber-physical infrastructure visualization (synthesizing Folios E.06, P.02 & M.07) '
            'imagining a renewable grid steadied by virtual synchronous inverters and a RISC-V '
            'protection processor. A formal proof of such a processor is a design assumption of '
            'this folio, not an existing artifact.'}

DISPATCH = {'kicker': 'FRONTIER CYBER-PHYSICAL DISPATCH · LOW-INERTIA GRIDS, CONTROL BARRIER FUNCTIONS & '
           'VERIFIED HARDWARE',
 'headline': 'Control Barrier Functions and Virtual Inertia for Low-Inertia Grids, with a '
             'Verified Processor as the Missing Layer',
 'body': 'Low-inertia grids are an active research field (Milano et al. 2018, DOI '
         '10.23919/PSCC.2018.8450880). This folio pairs Control Barrier Function QP filters (Ames '
         'et al. 2017, DOI 10.1109/TAC.2016.2638961) with a reduced virtual-inertia model, and '
         'points to machine-checked RISC-V work in Coq (Choi et al. 2017, DOI 10.1145/3110268; '
         'Erbsen et al. 2021, DOI 10.1145/3453483.3454065) as the precedent for a verified protection processor, which this folio assumes and does not show.'}

META_3D = ('Control Barrier Function Lyapunov–Nagumo & Grid RoCoF Surface',
 'X: Virtual Inertia H_virt · Z: CBF Damping α_CBF · Y: Barrier Safety Margin h(x)')

ES_TRANSLATION = {'title_es': 'Seguridad del Silicio a la Red Eléctrica: Funciones de Barrera de Control, Redes Renovables Sincronizadas y el Argumento a Favor de un Relevador con Procesador Verificado',
 'subtitle_es': 'Síntesis de los Folios E.06, P.02 y M.07: cómo los inversores síncronos '
                'virtuales y las Funciones de Barrera de Control (CBF) pueden estabilizar una '
                'red renovable de baja inercia, y qué aportaría debajo un procesador RISC-V '
                'verificado por máquina.',
 'why_es': 'Igual que miles de luciérnagas sincronizan su destello sin director de orquesta, los '
           'inversores con inercia virtual y un filtro matemático CBF pueden mantener la red eléctrica cerca de 60 Hz en el modelo del folio; un chip RISC-V con prueba formal sería la capa que falta.',
 'plain_es': 'En palabras sencillas, una red eléctrica continental es como una bicicleta tándem '
             'gigante pedaleada por millones de generadores al mismo tiempo. Durante más de un '
             'siglo, las pesadas turbinas de vapor y agua actuaron como gigantescos volantes de '
             'inercia que mantenían el pedaleo firme y constante a sesenta ciclos por segundo. Los '
             'paneles solares y las baterías modernas producen energía limpia, pero no tienen '
             'partes giratorias. Si un rayo desconecta una línea de alta tensión en una tarde '
             'calurosa, una red con poca inercia tiene menos tiempo para recuperar su ritmo. Para '
             'evitar apagones, los ingenieros programan los inversores de baterías para que se '
             'comporten como máquinas giratorias y se acompasen entre sí, creando inercia '
             'sintética mediante software. Pero los programas pueden fallar; por ello, el '
             'controlador puede envolverse en una barrera matemática que bloquea las órdenes que '
             'sacarían a la red de su zona segura. Esa barrera es tan confiable como el chip que '
             'la ejecuta, y por eso este folio también revisa los procesadores cuyo diseño ha '
             'sido comprobado con un asistente de pruebas.',
 'deep_es': 'La estabilidad de una red eléctrica renovable depende del balance entre dos '
            'factores: la inercia sintética de los inversores y la respuesta de la barrera de '
            'seguridad. Ante una falla, la tasa de cambio de frecuencia crece en proporción '
            'inversa a la inercia que queda. Para contrarrestar la caída, los inversores forman '
            'la red emulando la ecuación de oscilación de un generador, inyectando potencia activa proporcional a menos la derivada de la frecuencia (Zhong y Weiss 2011, DOI '
            '10.1109/TIE.2010.2048839). Al mismo tiempo, un programa cuadrático basado en '
            'Funciones de Barrera de Control (Ames et al. 2017, DOI 10.1109/TAC.2016.2638961) '
            'mantiene invariante hacia adelante la zona de operación segura del modelo, '
            'ajustando lo mínimo posible las órdenes de despacho. La tercera capa es una '
            'hipótesis de diseño: existen procesadores RISC-V con prueba verificada por máquina '
            'a pequeña escala, como Kami (Choi et al. 2017, DOI 10.1145/3110268) y el sistema '
            'embebido de Erbsen et al. (2021, DOI 10.1145/3453483.3454065), ambos en el '
            'asistente de pruebas Coq, hoy llamado Rocq. Este folio no conoce una prueba publicada, verificada por máquina, para el procesador de un relevador de protección de red. La prueba de 180 millones de líneas citada en la '
            'edición anterior se retiró porque no se encontró una fuente pública el 2026-11-13. '
            'Los valores numéricos de la página son resultados del modelo reducido del folio.',
 'bridge_es': 'La invariancia positiva de Nagumo en un filtro CBF-QP mantiene el estado del modelo dentro de la zona segura mientras el programa cuadrático sea factible y haya margen de potencia; un procesador RISC-V con prueba formal es la '
              'hipótesis de diseño que lo sostendría en hardware.'}
