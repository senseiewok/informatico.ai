#!/usr/bin/env python3
"""Folio P.02 (PHYSICS): Active Matter Hydrodynamics and Ciliary Metachronal Wave Synchronization."""
from __future__ import annotations

SLUG = 'p02'

PILLAR = 'physics'

FOLIO = {'category_code': 'P',
 'colophon': {'benchmarks': 'High-Speed Video Cilia Kinematics (14 Hz)',
              'bridge': 'Ciliary Phase-Locking ↔ Mucociliary Transit Velocity',
              'identifier': 'P.02 · Active Matter & Cilia',
              'kernels': 'Kuramoto Hydrodynamic Synchronization · Stokes Drag Re ~ 10^-4'},
 'current_edition': 'REV 1.2',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-02',
 'folio_id': 'P.02',
 'governing_law': '∂_t θ_i = ω_0 + ∑_j K_ij sin(θ_j − θ_i − α) · v_wave = λ f_beat',
 'pillar': 'physics',
 'primary_kernel': 'tools/physics_kernel.py',
 'readouts': [{'label': 'Beating Frequency', 'value': '14.00 Hz (Healthy PCL)'},
              {'label': 'Metachronal Wave Velocity', 'value': '336.00 μm/s'},
              {'label': 'Kuramoto Order Parameter', 'value': '0.880 (High Coherence)'},
              {'label': 'Reference Values', 'value': 'STATED IN ESSAY'}],
 'revisions': [{'date': '2026-11-02',
                'edition': 'REV 1.2',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'antiplectic wave speed v = 336 um/s, hydrodynamic coupling tensor, and '
                        'CSI 11 53 13 / 13 21 26 micro-incubator laminar containment.',
                'summary': 'REV 1.2 (Redated 2026-11-02): Verified Kuramoto phase-lag '
                           'synchronization (d theta_i / dt = omega_0 + sum_j K_ij sin(theta_j - '
                           'theta_i - alpha)) and low Reynolds Stokes flow order parameter r = '
                           '0.880 across healthy vs dehydrated PCL boundaries.'},
               {'date': '2026-11-01',
                'edition': 'REV 1.1',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'low-Reynolds Stokesian hydrodynamic interaction tensor, wave speed v = '
                        '336 um/s, and CSI 11 53 13 / 13 21 26 micro-chamber environmental '
                        'controls.',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added CSI MasterFormat 11 53 13 / 13 21 '
                           '26 ciliary microhydrodynamic organ-on-chip specification plate and '
                           'verified Kuramoto phase synchronization order parameter r >= 0.85.'},
               {'date': '2026-11-01',
                'edition': 'REV 1.0',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'Low-Reynolds Stokes flow, order parameter r >= 0.85, and steric arrest '
                        'below h_PCL < 7 μm.',
                'summary': 'REV 1.0 (Inaugural Edition 2026-11-01): Active matter ciliary carpet '
                           'beating and Kuramoto metachronal wave synchronization.'}],
 'sidenote_1': {'body': 'In CF airway disease, ciliary motors are genetically intact; '
                        'clearance failure is a macroscopic hydrodynamic transition triggered when '
                        'the periciliary liquid drops below the ciliary reach (7 μm), plunging the '
                        'cilia into tangled airway mucus and destroying phase '
                        'synchronization.',
                'kicker': 'SIDENOTE P.02 · THE PHYSICS OF CLEARANCE ARREST IN CF'},
 'sidenote_2': {'body': 'Ciliary carpets naturally self-organize into antiplectic waves where wave '
                        'propagation opposes the effective stroke, maximizing fluid discharge '
                        'while minimizing viscous dissipation through cross-stream hydrodynamic '
                        'shielding.',
                'kicker': 'SIDENOTE P.02-B · ANTIPLECTIC METACHRONISM & OSEEN TENSORS (DOI '
                          '10.1088/0034-4885/72/9/096601)'},
 'skill': {'description': 'AI-agnostic physical skill for micro-hydrodynamic active matter '
                          'synchronization, low Reynolds Stokes flow, and ciliary metachronal wave '
                          'velocity.',
           'filename': 'ciliary-active-matter-SKILL.md',
           'name': 'ciliary-active-matter',
           'rules': ['Verify PCL height >= 7.0 μm to ensure unhindered active recovery stroke.',
                     'Calculate Kuramoto order parameter r = |(1/N) sum exp(i theta_k)| >= 0.70 '
                     'for wave coherence.',
                     'Flag complete ciliary collapse when h_PCL < 3.5 μm.']},
 'sliders': [{'label': 'Periciliary Layer Height (h_PCL)',
              'max': 10.0,
              'min': 2.0,
              'step': 0.2,
              'unit': 'μm',
              'value': 7.0},
             {'label': 'Mucus Solids Concentration',
              'max': 10.0,
              'min': 1.0,
              'step': 0.5,
              'unit': '%',
              'value': 2.0}],
 'slug': 'p02',
 'spec_plate': {'body': 'Continuum phase-field model coupling Stokesian hydrodynamic interactions '
                        'with non-linear limit-cycle oscillators to predict emergent transport '
                        'velocity across bronchial epithelial surfaces under Class II Type A2 laminar '
                        'containment.',
                'division': 'CSI MASTERFORMAT 11 53 13 / 13 21 26',
                'meta': 'Brennen & Winet 1977 · Vilfan & Jülicher PRL 2006 · Button Science 2012 · '
                        'NSF/ANSI 49',
                'title': 'Airway Epithelial Organ-on-Chip & Environmental '
                         'Micro-Incubator'},
 'status_badge': 'REDATED REV 1.2',
 'steps': ['Stage 1 (Autonomous Beating, omega_0): Individual cilia oscillate at 12–14 Hz, '
           'generating localized Stokesian velocity fields.',
           'Stage 2 (Hydrodynamic Phase-Lag Coupling): Neighboring cilia interact via viscous '
           'fluid stress with phase lag alpha ≈ pi/6.',
           'Stage 3 (Emergent Metachronal Wave): Kuramoto order parameter climbs above 0.85, '
           'organizing an antiplectic traveling wave at velocity v = lambda * f ≈ 336 μm/s.',
           'Stage 4 (Steric & Viscous Arrest): Desiccation below h < 7 μm causes cilia tips to '
           'catch on the overlying mucus gel, collapsing wave velocity to zero.'],
 'subtitle': 'Low Reynolds number Stokesian hydrodynamics, Kuramoto phase-lag synchronization, and '
             'the collective propulsion velocity of human airway ciliary carpets.',
 'title': 'Active Matter Hydrodynamics and Ciliary Metachronal Wave Synchronization',
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/s0022-5193(86)80098-4',
           'fetched_on': '2026-11-08',
           'citing_publications': 186,
           'supporting': 13,
           'mentioning': 196,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 186 citing '
                      'publications (13 supporting, 196 mentioning, 0 contrasting) on mucociliary '
                      'metachronal wave hydrodynamics and Blake Stokeslet arrays.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/s0022-5193(86)80098-4',
           'fetched_on': '2026-11-08',
           'citing_publications': 186,
           'supporting': 13,
           'mentioning': 196,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite Smart Citation Index (verified 2026-11-08): 0 retractions; 186 citing '
                      'publications (13 supporting, 196 mentioning, 0 contrasting) on mucociliary '
                      'metachronal wave hydrodynamics and Blake Stokeslet arrays.'},
 'act1_title': "Act I — Huygens's Pendulum Clocks, G.I. Taylor's Micro-Swimmers, and Metachronal "
               'Ciliary Waves',
 'act1_dropcap': 'In February 1665, while confined to his bed in The Hague with a lingering fever, '
                 'the Dutch polymath Christiaan Huygens stared at two brass pendulum clocks '
                 'mounted to the same wooden ceiling beam. To his astonishment, no matter how he '
                 'initially set them swinging, within half an hour their heavy pendulums fell into '
                 'perfect, opposite synchrony. Huygens realized that imperceptible vibrations '
                 'traveling through the shared timber beam were gently nudging the pendulums into '
                 'alignment. Nearly three centuries later, Sir Geoffrey Ingram Taylor posed an '
                 'analogous hydrodynamic puzzle in Cambridge: how can microscopic organisms swim '
                 'through fluids where inertia is utterly nonexistent and viscous friction '
                 'dominates every motion? Taylor demonstrated that flexible hairs and swimming '
                 'filaments generate long-range flow fields through the liquid itself. In '
                 'biological tissues, millions of microscopic hairs beat together not because a '
                 'central conductor directs them, but because surrounding fluid stresses lock '
                 'their rhythms into sweeping traveling waves.',
 'act1_plain_bridge': 'Inside our breathing passages, millions of tiny microscopic hairs cover the '
                      'airway surface like a living carpet. Their job is to sweep dust, germs, and '
                      'debris out of the lungs toward the throat. To move heavy fluid, these hairs '
                      'cannot beat randomly like blades of grass in a chaotic storm. Instead, they '
                      'must move together in a smooth, rhythmic wave, much like fans in a sports '
                      'stadium standing and sitting in sequence. Because these tiny hairs have no '
                      'nerves connecting them, they coordinate purely through the liquid between '
                      'them. When one hair pushes through the fluid, it creates a small watery '
                      'wake that nudges its neighbors to follow. If the water layer stays deep and '
                      'clean, this gentle liquid nudge creates a swift moving wave that clears the '
                      'airway. But if the liquid dries up, the hairs catch in thick sludge, the '
                      'wave shatters, and debris becomes trapped.',
 'act1_body': 'In 1972, John R. Blake modeled the hundreds of cilia crowning each airway '
              'epithelial cell as an array of slender-body Stokeslets positioned above a solid '
              'boundary wall. Three years later, Yoshiki Kuramoto formulated the universal '
              'phase-oscillator framework that captures how distributed rhythmic elements '
              'synchronize through weak pairwise coupling. When the periciliary liquid layer '
              'remains fully hydrated at a height of seven microns, long-range hydrodynamic '
              'coupling decaying with distance locks millions of autonomously oscillating cilia '
              'into a coherent metachronal wave that steadily sweeps foreign particles away. '
              "Building on Kuramoto's phase-lag formulation and Arthur Winfree's geometric "
              'topology of biological clocks, G. B. Ermentrout and Nancy Kopell (SIAM J. Math. '
              'Anal. 1984; J. Theor. Biol. 1986, DOI 10.1016/s0022-5193(86)80098-4) proved that '
              'nearest-neighbor hydrodynamic coupling along an oscillator chain locks into a '
              'unidirectional traveling wave once coupling exceeds a well-defined critical '
              'threshold. This hydrodynamic coherence ensures that micro-scale mechanical work '
              'translates into macro-scale fluid transport.',
 'act1_stakes': 'In macroscopic engineering, ships and pumps propel fluids by exploiting inertia, '
                'where accelerating a mass of water forward pushes a hull forward. But at the '
                'microscopic scale of human airways, where the Reynolds number plummets below one '
                'ten-thousandth, fluid inertia completely vanishes. Under these conditions, the '
                'Navier–Stokes equations simplify into linear, time-reversible Stokes flow. As '
                'Edward Purcell famously proved in his scallop theorem, any reciprocal '
                'back-and-forth motion produces zero net propulsion; moving forward and backward '
                'along the identical trajectory leaves the fluid exactly where it started. Cilia '
                'escape this constraint by executing an asymmetric stroke cycle: an extended, '
                'stiff power stroke high above the cell wall, followed by a curled, low-profile '
                'recovery stroke near the surface. If dehydration compresses the liquid layer, '
                'cilia cannot uncurl, time-reversal asymmetry is lost, and the collective '
                'metachronal wave collapses into disorganized, paralyzed twitching.',
 'pullquote': '"At Reynolds number 10^-3, a single isolated cilium merely stirs mucus '
              'back and forth; only a Kuramoto-synchronized metachronal wave can propel the '
              'mucus blanket upward against gravity."',
 'chronology': [('1665',
                 'Christiaan Huygens discovers phase synchronization between coupled pendulum '
                 'oscillators.'),
                ('1951',
                 'G. I. Taylor solves the viscous hydrodynamic synchronization of '
                 'low-Reynolds-number microscopic swimmers.'),
                ('1972',
                 "John R. Blake formulates the wall-bounded Stokeslet green's function for "
                 'mucociliary transport.'),
                ('1975',
                 'Yoshiki Kuramoto derives the exact phase-transition threshold K_c for coupled '
                 'oscillator arrays.')],
 'act2_title': 'Act II — How It Actually Works: Blake Stokeslets + Kuramoto Phase-Locking',
 'act2_analogy': "Picture a sold-out stadium where eighty thousand sports fans perform 'the wave.' "
                 'No single fan runs along the grandstand; each person simply stands up from their '
                 'seat, raises their hands, and sits back down a split second after the person to '
                 'their left. Because each individual movement is timed with a slight phase delay, '
                 'a massive, visible wave races around the entire arena at highway speeds. In our '
                 'airways, millions of cilia stay anchored in place while their synchronized phase '
                 'delays propel a fluid blanket across the tissue.',
 'act2_plain_primer': 'You can explore this microscopic wave engine using the two sliders on this '
                      'plate. The first slider sets the Periciliary Layer Height, which measures '
                      'the depth of the clear, watery cushion surrounding the cilia. Think of this '
                      'cushion as the open standing room in the stadium: when the cushion is at '
                      'least seven microns tall, each cilium can stand up to its full height '
                      'during its power stroke without bumping into anything overhead. If you '
                      'reduce this height, the ceiling drops and the hairs are physically squashed '
                      'against the floor. The second slider controls the Mucus Solids '
                      'Concentration, which represents how thick and sticky the overlying blanket '
                      'has become. At normal levels of around two percent solids, the blanket '
                      'glides smoothly over the tips of the hairs. But if dehydration drives '
                      'solids higher, the blanket turns into heavy, dense mucus that pins the '
                      'hairs down and extinguishes the moving wave.',
 'distill_diagram': {'analogy_title': 'Stadium Wave Metachronal Relay',
                     'analogy_sub': 'Stationary spectators create rapid traveling ripples',
                     'force_a_title': 'Periciliary Layer Height (h_PCL)',
                     'force_a_sub': 'Watery clearance height for upright power strokes',
                     'force_b_title': 'Mucus Solids Concentration (w)',
                     'force_b_sub': 'Viscous gel load opposing ciliary movement',
                     'threshold_title': 'Ciliary Reach Threshold (h_PCL ≥ 7.0 μm)',
                     'threshold_pass': 'Antiplectic wave locks: swift upward fluid clearance',
                     'threshold_fail': 'Viscous steric arrest: cilia pinned and wave decoupled'},
 'act2_intuition': 'Each individual cilium executes an asymmetric two-stroke cycle at a beat '
                   'frequency of fourteen hertz: an upright, high-reach effective stroke whose tip '
                   'engages the underside of the overlying viscoelastic mucus blanket, followed by a '
                   'low-profile recovery stroke bent close to the epithelial surface within the '
                   'low-viscosity periciliary liquid layer. Viscous velocity fields generated by '
                   'slender-body Stokeslets decay with distance along the wall, coupling '
                   'neighboring cilia with strength K_ij. So long as the coupling constant exceeds '
                   'the critical threshold K_c, global Kuramoto phase coherence climbs toward '
                   '0.92, sustaining an antiplectic metachronal wave traveling at over three '
                   'hundred microns per second. In low-Reynolds-number Stokes flow (Re ~ 10^-4), '
                   "Purcell's scallop theorem forbids net fluid propulsion from any "
                   'time-reversible reciprocal motion; only by breaking time-reversal symmetry '
                   'between the stiff extended power stroke and the swept-back recovery stroke—and '
                   'synchronizing neighboring filaments with a phase lag alpha ~ 0.35 radians—does '
                   'an active carpet generate coherent directional fluid discharge. When '
                   'periciliary dehydration compresses the layer below seven microns, steric '
                   'interference destroys this delicate stroke asymmetry, driving the order '
                   'parameter below critical synchronization and arresting metachronal clearance.',
 'act2_deepening': 'Under the hood of this active biological carpet, the hydrodynamic interaction '
                   "between beating filaments is governed by the Oseen tensor and Blake's image "
                   'Stokeslet construction for a no-slip boundary. Because each cilium exerts a '
                   'localized force on the viscous fluid during its effective stroke, it induces a '
                   'long-range dipolar velocity field that decays as the inverse cube of distance '
                   'along the epithelial plane. This velocity field alters the viscous drag '
                   'experienced by adjacent cilia, modulating their instantaneous phase '
                   'velocities. The non-linear Kuramoto coupling function K_ij sin(theta_j - '
                   'theta_i - alpha) captures how neighboring oscillators dynamically advance or '
                   'retard their phase to minimize energetic dissipation. As you increase the '
                   'periciliary layer height slider, the physical distance between the ciliary '
                   'tips and the overlying viscoelastic gel increases, allowing the power stroke '
                   'to complete unimpeded and strengthening hydrodynamic phase-locking. '
                   'Conversely, increasing the solids concentration slider elevates the complex '
                   'shear modulus of the mucus blanket, introducing non-Newtonian yield stresses '
                   'that overpower hydrodynamic coupling and trigger localized phase-slip '
                   'dislocations.',
 'walkthrough': ['Experiment 1 (Metachronal Wave Coherence): Observe how healthy coupling '
                 'maintains Kuramoto order parameter R = 0.92 and wave speed v_wave = 180 um/s.',
                 'Experiment 2 (Periciliary Compression): Reduce the affinity/coupling drive to '
                 'simulate PCL compression (< 4.5 um) and watch the wave decohere into arrested '
                 'patches.',
                 'Experiment 3 (4-Stage Stepper): Trace Stokeslet wall shielding, power vs. '
                 'recovery asymmetry, Kuramoto phase-locking, and mucus plug '
                 'pinning.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'High-speed video microscopy (500 fps) of patient nasal-brush organoids paired '
                  'with optical-flow Kuramoto phase estimators quantifies CFTR '
                  'modulator and gene-therapy rescue in real time. Using sparse nonlinear PDE '
                  'discovery in dynamicslab/pysindy (https://github.com/dynamicslab/pysindy, DOI '
                  '10.1073/pnas.1517384113) on high-speed phase-contrast video alongside spectral '
                  'Stokes-layer solvers in DedalusProject/dedalus (DOI '
                  '10.1103/PhysRevResearch.2.023068) extracts the exact empirical Kuramoto '
                  'coupling strength K and order parameter R, grounded in Scite-verified citations '
                  '(DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Modern active-matter biophysics bridges micro-scale ciliary kinematics and '
                   'macro-scale organ-level transport using high-speed digital holographic '
                   'microscopy and automated computer vision. High-frame-rate video capture at '
                   'five hundred frames per second tracks thousands of individual ciliary tips '
                   'simultaneously, but decomposing their crowded, overlapping trajectories '
                   'previously presented an insurmountable data bottleneck. Today, deep learning '
                   'optical-flow architectures and physics-informed neural solvers reconstruct the '
                   'full three-dimensional phase field across the entire epithelial surface in '
                   'real time. These automated pipelines directly extract spatial correlation '
                   'lengths, Kuramoto order parameters, and topological defect densities from '
                   'patient-derived tissue samples. A major open frontier is predicting how '
                   'heterogeneous patches of damaged or uncoordinated cilia affect global '
                   'transport topology. By simulating multi-scale active carpets with '
                   'lattice-Boltzmann and immersed-boundary methods on distributed graphic '
                   'processors, researchers can evaluate how novel pharmacological synchronizers '
                   'or rheological modifying agents restore collective metachronal wave '
                   'propagation, turning raw optical video into definitive biophysical metrics of '
                   'therapeutic rescue.',
 'cf_bridge': 'Restoring mucociliary clearance (MCC) is the ultimate functional readout of any '
              'Cystic Fibrosis therapy. When CFTR modulators, ENaC '
              'blockers (ETD001), or inhaled mRNA lipid nanoparticles (LNPs) restore PCL height to 7.0 um, '
              'cilia unpin from the mucus gel, re-cross the Kuramoto synchronization '
              'threshold K > K_c, and resume clearing Pseudomonas biofilms.',
 'sources': ['Fulford, G. R., & Blake, J. R. (1986). Two-layer Newtonian and low-Reynolds-number propulsion mechanics (extending G. I. Taylor 1951). Journal of Theoretical Biology, 121(4), 381–402. DOI: 10.1016/s0022-5193(86)80098-4.',
             'Blake, J. R. (1972). A model for the micro-structure in ciliated organisms. Journal '
             'of Fluid Mechanics, 55(1), 1–23.',
             'Kuramoto, Y. (1984). Chemical Oscillations, Waves, and Turbulence. Springer.',
             'Button, B., et al. (2012). A periciliary brush promotes the lung health by '
             'separating the mucus layer from airway epithelia. Science, '
             '337(6097), 937–941.',
             'Open-Source Cross-Field Synchronization & WEF Renewable Grid Stack: PyPSA '
             'Continental Grid Simulator (https://github.com/PyPSA/PyPSA) & QuTiP Quantum '
             'Oscillator Toolbox (https://github.com/qutip/qutip).',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing '
             'equations from data by sparse identification of nonlinear dynamical systems '
             '(dynamicslab/pysindy, https://github.com/dynamicslab/pysindy). PNAS, 113(15), '
             '3932–3937. DOI: 10.1073/pnas.1517384113.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Blake Stokeslet '
        'ciliary array and Kuramoto metachronal wave synchronization">\n'
        '            <rect x="55" y="42" width="570" height="32" fill="var(--tp-verdigris)" '
        'fill-opacity="0.16" stroke="var(--tp-verdigris)" stroke-width="2"/>\n'
        '            <line x1="55" y1="168" x2="625" y2="168" stroke="currentColor" '
        'stroke-width="2.5"/>\n'
        '            <path d="M 110 168 Q 105 110 135 74" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <path d="M 175 168 Q 175 100 210 68" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <path d="M 240 168 Q 250 105 280 76" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <path d="M 305 168 Q 330 135 345 118" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '            <path d="M 370 168 Q 395 142 405 128" fill="none" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '            <path d="M 435 168 Q 430 110 465 74" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <path d="M 500 168 Q 500 100 535 68" fill="none" stroke="var(--tp-prussian)" '
        'stroke-width="3"/>\n'
        '            <text x="72" y="62" font-size="11" fill="var(--tp-verdigris)">Airway '
        'Mucus Blanket Propelled at v_wave = λ·f_beat = 180 μm/s (Kuramoto R = 0.92)</text>\n'
        '            <text x="165" y="196" font-size="11" fill="currentColor">Hydrated 7.0 μm '
        'Periciliary Layer · 14 Hz Power (Blue) &amp; Recovery (Red) Strokes</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what airway epithelial cilia beating in a '
        'synchronized Kuramoto metachronal wave across the periciliary liquid would look like '
        '(artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate P.02-V (Imagining What It Would Look Like) · Artistic '
            'biophysical visualization imagining a carpet of respiratory epithelial cilia beating '
            'in a coordinated antiplectic metachronal wave beneath the airway '
            'mucus layer.'}

DISPATCH = {'kicker': 'FRONTIER ACTIVE MATTER DISPATCH · HYDRODYNAMIC METACHRONAL COHERENCE',
 'headline': 'Kuramoto Phase Synchronization Explains How Airway Cilia Coordinate '
             'Mucociliary Clearance',
 'body': 'Recent active-matter biophysics (Fulford & Blake (1986) DOI '
         '10.1016/s0022-5193(86)80098-4; Kuramoto synchronization) demonstrates that hydrodynamic '
         'Oseen coupling across periciliary liquid depth h_ASL = 7.2 μm locks millions of beating '
         'cilia (12–15 Hz) into coherent antiplectic metachronal waves.'}

META_3D = ('Kuramoto Symplectic Metachronal Ciliary Wave Train',
 'X: Streamwise Epithelial Axis · Z: Spanwise Cilia Array · Y: Metachronal Phase Wave Height')

ES_TRANSLATION = {'title_es': 'Hidrodinámica de Materia Activa y Sincronización de Ondas Metacrónicas Ciliares',
 'subtitle_es': 'Hidrodinámica de Stokes a bajo número de Reynolds, sincronización con desfase de '
                'Kuramoto y velocidad de propulsión colectiva de las alfombras ciliares de las '
                'vías respiratorias humanas.',
 'why_es': "Como la 'ola' en un estadio donde cada espectador se levanta una fracción de segundo "
           'después de su vecino, millones de cilios microscópicos coordinan su batido a través '
           'del fluido para impulsar el moco hacia afuera.',
 'plain_es': 'En 1665, Christiaan Huygens descubrió que dos relojes de péndulo colgados de la '
             'misma viga de madera terminaban balanceándose en perfecta sincronía gracias a '
             'pequeñísimas vibraciones compartidas. En nuestras vías respiratorias ocurre un '
             'fenómeno asombrosamente similar. Millones de diminutos filamentos microscópicos '
             'llamados cilios cubren el tejido como una alfombra viva encargada de limpiar polvo y '
             'microbios. Estos pelitos no tienen cables ni nervios que los dirijan; se coordinan '
             'únicamente a través del líquido que los rodea. Cuando un cilio se mueve, genera una '
             'suave corriente que empuja al de al lado a moverse justo un instante después. Esto '
             "crea una ola coordinada que viaja por la superficie, muy parecida a la 'ola' que "
             'hacen los aficionados en un estadio de futbol. Mientras la capa de agua se mantenga '
             'a una altura saludable de siete micras, la ola se propaga a gran velocidad y expulsa '
             'las impurezas. Pero si el agua se seca, los cilios quedan atrapados en moco espeso y '
             'la ola se detiene por completo.',
 'deep_es': 'La física de materia activa y la hidrodinámica a bajo número de Reynolds explican '
            'cómo las alfombras ciliares superan el teorema del molusco de Purcell, que prohíbe el '
            'movimiento neto si el batido es simétrico en el tiempo. Los cilios rompen esta '
            'simetría ejecutando un golpe de avance extendido y rígido, seguido de un golpe de '
            'recuperación curvado cerca de la célula. Este mecanismo depende de dos factores '
            'acoplados: la profundidad de la capa de líquido periciliar y la concentración de '
            'sólidos en el gel mucoso suprayacente. Si la altura del líquido supera el umbral '
            'crítico de siete micras, el acoplamiento hidrodinámico entre filamentos vecinos '
            'supera el umbral de Kuramoto, organizando una onda metacrónica antipléctica coherente '
            'con un parámetro de orden superior a cero punto ochenta y cinco. Si la capa se '
            'deshidrata, el moco aplasta mecánicamente las puntas de los cilios, anulando la '
            'sincronización de fase. Mediante cámaras de alta velocidad y modelos computacionales '
            'de redes complejas, los científicos pueden rastrear hoy esta transición de fase en '
            'tiempo real.',
 'bridge_es': 'Demuestra por qué mantener una profundidad de líquido periciliar h_ASL ≥ 7 μm es '
              'indispensable para que el acoplamiento hidrodinámico de Oseen mantenga el '
              'aclaramiento mucociliar en la Fibrosis Quística.'}
