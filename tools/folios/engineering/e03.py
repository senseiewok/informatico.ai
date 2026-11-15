#!/usr/bin/env python3
"""Folio E.03 (ENGINEERING): Sub-Wavelength Acoustic Metamaterial Helmholtz Arrays and Viscothermal Boundary-Layer Damping."""
from __future__ import annotations

SLUG = 'e03'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.03',
 'slug': 'e03',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Sub-Wavelength Acoustic Metamaterial Helmholtz Arrays and Viscothermal Boundary-Layer '
          'Damping',
 'subtitle': 'How coiled-space resonators and viscothermal boundary layers δ_v = √(2ν/ω) can '
             'absorb low-frequency sound in panels far thinner than a quarter wavelength; the '
             'design study on this page targets about 1/19 of a wavelength.',
 'date_published': '2026-10-31',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.3',
 'status_badge': 'CIVIL & ACOUSTICS · REV 1.3',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'δ_v = √(2ν/ω) · Z_s = ρ_0 c_0 ⇒ α = 1.0 · CSI 09 84 13',
 'colophon': {'identifier': 'E.03 · Acoustic Metamaterials & Viscothermal Damping · CSI 09 84 13',
              'kernels': 'δ_v = √(2ν/ω) · Z_s = R_v + i ω M_a − i ρ c² / (ω V_cav)',
              'benchmarks': 'Model values: δ_v = 0.174 mm at 160 Hz · α = 0.9996 for Z_s/Z_0 = '
                            '1.04 at resonance',
              'bridge': 'Oscillatory Boundary Layers ↔ Airway Oscillation Devices (an analogy)'},
 'sliders': [{'label': 'Resonant Frequency (f_0)',
              'min': 80.0,
              'max': 400.0,
              'step': 5.0,
              'value': 160.0,
              'unit': ' Hz'},
             {'label': 'Resonator Neck Radius (r_neck)',
              'min': 0.2,
              'max': 2.5,
              'step': 0.05,
              'value': 0.65,
              'unit': ' mm'}],
 'steps': ['Stage 1 (Oscillatory Stokes Boundary Layer): At f_0 = 160 Hz, the viscous boundary '
           'layer in air is δ_v = √(2ν/ω) = 0.174 mm.',
           'Stage 2 (Complex Effective Density & Bulk Modulus): When neck radius r_neck = 0.65 mm '
           'approaches 3.7 δ_v, viscous shear dissipates acoustic kinetic energy.',
           'Stage 3 (Critical Impedance Matching, Z_s = Z_0): Reactance vanishes at Helmholtz '
           'resonance ω_0 while resistance matches ρ_0 c_0 ≈ 413 Pa·s/m. The page sets the '
           'resistance to 1.04 ρ_0 c_0 at the default neck radius, a fixed model value.',
           'Stage 4 (Broadband Detuned Array): A design idea, not a built panel: several '
           'detuned coiled cavities could spread absorption over roughly 125–315 Hz in a panel '
           'about 110 mm deep (1/19 of the 2.14 m wavelength at 160 Hz).'],
 'readouts': [{'label': 'Viscous Boundary Layer (δ_v)', 'value': '0.174 mm (at 160 Hz)'},
              {'label': 'Normalized Surface Impedance', 'value': 'Z_s / Z_0 = 1.04 + 0.00 i (model, at resonance)'},
              {'label': 'Peak Absorption Coefficient', 'value': 'α_peak = 0.9996 (model, near critical match)'},
              {'label': 'Acoustic Verdict', 'value': 'DESIGN TARGET · NOT TESTED'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 09 84 13 / 09 54 26',
                'title': 'Micro-Slit Timber Helmholtz Metamaterial Ceiling Baffle (Node E-09)',
                'body': 'Illustrative design sketch, not a tested product: a fiber-free, '
                        'CNC-slotted timber panel with internal coiled cavities aimed at '
                        '125–315 Hz. The figures α_w = 0.90 (which would be Class A under ISO '
                        '11654) are design targets; nothing was measured.',
                'meta': 'Design sketch · ISO 354 (reverberation-room measurement) would be the '
                        'test to run; none was run and no certification exists'},
 'sidenote_1': {'kicker': 'SIDENOTE E.03-A · AN ANALOGY: OSCILLATING FLOW IN THE AIRWAYS',
                'body': 'The Womersley number Wo = r √(ω/ν) compares a channel radius with the '
                        'viscous boundary layer of an oscillating flow, in a resonator neck or '
                        'in any tube. Airway clearance devices also make air oscillate, so the '
                        'same dimensionless number can be written for them; that is an analogy '
                        'offered by this folio, not a model of any therapy.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.03-B · SPECIFICATION PLATE · CSI 09 84 13 / 09 54 26',
                'body': 'Design sketch of a micro-slit timber Helmholtz ceiling baffle with a '
                        'target α_w = 0.90 and no loose mineral fibers. These are targets, not '
                        'test results.'},
 'skill': {'filename': 'acoustic-helmholtz-metamaterial-SKILL.md',
           'name': 'acoustic-helmholtz-metamaterial',
           'description': 'AI-agnostic acoustics and wave-mechanics engineering skill for '
                          'sub-wavelength Helmholtz resonator arrays, Stinson viscothermal '
                          'boundary-layer impedance, and critical coupling.',
           'rules': ['Compute viscous boundary layer thickness delta_v = sqrt(2 * nu / omega) and '
                     'Womersley number Wo = r_neck * sqrt(omega / nu) = sqrt(2) * r_neck / '
                     'delta_v (so the ratio r_neck / delta_v equals Wo / sqrt(2)).',
                     'Enforce critical coupling condition Re(Z_surface) = rho_0 * c_0 and '
                     'Im(Z_surface) = 0 at target resonance omega_0 for unity absorption.',
                     'Include an end-correction length in the effective neck inductance; the '
                     'approximate form delta_l = 0.85 * r_neck * (1 - 1.25 * sqrt(porosity)) is '
                     "this folio's working choice and should be checked against an acoustics "
                     'reference before design use.']},
 'revisions': [{'edition': 'REV 1.3',
                'date': '2026-11-14',
                'summary': 'REV 1.3 (Redated 2026-11-14): Grounding revision. The sputum '
                           'yield-stress and oscillatory-stress figures (11.5 Pa, 14.8 Pa), the '
                           'claim that chest-wall oscillation "liquefies" mucus, and the claim '
                           'that this would multiply nanoparticle penetration were withdrawn as '
                           'unsourced; the airway link is now an analogy. The panel test and '
                           'certification wording was withdrawn, the invented 1863 scene was '
                           'replaced with plain dates, and the absorption readout was recomputed '
                           'for zero reactance at resonance (0.9996). Critical coupling is now '
                           'cited to Romero-García et al. (2016). A later review corrected the '
                           'Womersley number definition (Wo = √2 r/δ_v), made the absorption '
                           'range agree (125–315 Hz) and softened claims about what such panels '
                           'achieve.',
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository name with the GitHub API. No '
                        'simulation or acoustic test was run for this folio; its numbers are '
                        'outputs of the closed-form model on the page.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-02',
                'summary': 'REV 1.2 (Redated 2026-11-02): Verified sub-wavelength Helmholtz '
                           'viscothermal acoustic metamaterials (delta_v = sqrt(2*nu/omega), CSI '
                           '09 84 13) and oscillatory shear liquefaction of CF sputum '
                           'plugs with 4-Seat Multi-Lineage Council review.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): checked that '
                        'delta_v = 0.174 mm follows from the page formula. The word "Verified" in '
                        'this note and in the notes below, the sputum liquefaction claim and the '
                        'stress figures 14.8 Pa and 11.5 Pa are withdrawn in REV 1.3.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-01',
                'summary': 'REV 1.1 (Redated 2026-11-01): Added Womersley oscillatory shear bridge '
                           'to 15 Hz airway oscillation and CSI 09 84 13 cleanroom panel '
                           'spec.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'reflection coefficient |R|² = 0.002 at Z_s/Z_0 = 1.04 + 0.08i.'},
               {'edition': 'REV 1.0',
                'date': '2026-10-31',
                'summary': 'REV 1.0 (Published 2026-10-31): Initial Stinson viscothermal Helmholtz '
                           'metamaterial monograph.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified δ_v '
                        '= 0.174 mm.'}],
 'volume': 2,
 'volume_code': 'VOL. 02',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1146/annurev-matsci-070616-124032',
           'fetched_on': '2026-11-08',
           'citing_publications': 658,
           'supporting': 4,
           'mentioning': 307,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Yang & Sheng 2017 (DOI '
                      '10.1146/annurev-matsci-070616-124032), as recorded 2026-11-08: 658 citing '
                      'publications (4 supporting, 307 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1146/annurev-matsci-070616-124032',
           'fetched_on': '2026-11-08',
           'citing_publications': 658,
           'supporting': 4,
           'mentioning': 307,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Yang & Sheng 2017 (DOI '
                      '10.1146/annurev-matsci-070616-124032), as recorded 2026-11-08: 658 citing '
                      'publications (4 supporting, 307 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'},
 'act1_title': "Act I — Helmholtz Resonators, Rayleigh's Viscothermal Layers, and "
               'Deep-Subwavelength Metamaterials',
 'act1_dropcap': 'In 1863 the German physician and physicist Hermann von Helmholtz published '
                 'Die Lehre von den Tonempfindungen (On the Sensations of Tone). In it he '
                 'described hollow resonators with a narrow neck, tuned by their volume and '
                 'opening, which he used to pick out single tones from a complex sound. The '
                 'resonator now carries his name. Later in the nineteenth century, physicists '
                 'including Lord Rayleigh analysed how viscous friction and heat conduction at '
                 'the walls of narrow tubes turn sound energy into heat. In 1991 Michael Stinson '
                 'published a general treatment of plane sound waves in narrow and wide tubes '
                 'of any cross-section (DOI 10.1121/1.400379), which is still a standard '
                 'reference for these viscothermal losses.',
 'act1_plain_bridge': 'Have you ever blown gently across the top of an empty glass bottle to make '
                      'a low musical hum? That pleasant tone is a physical resonance. The air '
                      'trapped in the bottle neck bounces back and forth against the springy '
                      'cushion of air resting inside the main chamber. Acoustic engineers use this '
                      'exact same bottle effect to swallow loud, unwanted sounds. Normally, '
                      'absorbing low-pitched rumble like freeway noise or industrial exhaust '
                      'takes thick, bulky absorbers. But by folding long, narrow passages into '
                      'spiral mazes inside a compact wall panel, researchers have shown that deep '
                      'sound can be absorbed in much thinner structures. When the incoming sound '
                      'waves squeeze through these tiny corridors, air rubs against the solid '
                      'walls, turning vibration into a little heat. This is one way designers '
                      'hope to treat low-frequency noise in ventilation systems and buildings '
                      'without giving up as much floor space.',
 'act1_body': 'Over the past two decades, acoustics researchers have folded long, narrow '
              'channels into thin sub-wavelength cells. Conventional porous or micro-perforated '
              'absorbers typically need a depth on the order of a quarter wavelength, which makes '
              'absorbing sound below about two hundred hertz bulky. Labyrinthine and '
              'coiled-space designs can absorb low-frequency sound in panels much thinner than '
              'that (reviewed by Yang and Sheng, Annual Review of Materials Research, DOI '
              '10.1146/annurev-matsci-070616-124032); the design on this page targets about one '
              'nineteenth of the wavelength. Inside these tightly coiled '
              'channels, viscous friction and heat exchange govern wave dissipation through the '
              'Stinson viscothermal boundary layers delta_v = sqrt(2 nu / omega) and delta_h = '
              'sqrt(2 kappa / (rho_0 C_p omega)) (Stinson 1991, DOI 10.1121/1.400379). When a '
              "resonator's internal losses exactly balance the energy it leaks back out, the "
              'critical coupling condition holds and absorption at resonance can reach 100% '
              '(Romero-García et al. 2016, Scientific Reports, DOI 10.1038/srep19519). In '
              'impedance terms this means Z_eff = rho_0 c_0 with no reactance, so incoming '
              'sound is not reflected back into the room.',
 'act1_stakes': 'Resonator models that leave out the viscothermal boundary layers can predict '
                'the wrong resonance and the wrong amount of damping, so a built absorber may '
                'miss the tone it was meant to treat. How large the error is depends on the '
                'geometry; this page does not give a general figure. Low-frequency noise from '
                'fans, ducts and machinery is hard to control precisely because ordinary '
                'absorbers need so much depth. Designing for impedance matching, with the '
                'boundary-layer losses included, is the approach the critical-coupling '
                'literature takes to make compact absorbers work.',
 'pullquote': '"A resonator absorbs best not when it is most lossy, but when its losses '
              'exactly balance the energy it leaks back out."',
 'chronology': [('1863',
                 'Hermann von Helmholtz describes his tuned cavity resonators in Die Lehre von den '
                 'Tonempfindungen.'),
                ('1896',
                 "The second edition of Lord Rayleigh's The Theory of Sound treats sound in "
                 'narrow tubes with viscous and thermal losses.'),
                ('1991',
                 'Michael R. Stinson publishes his treatment of plane sound waves in narrow and '
                 'wide tubes of arbitrary cross-section (DOI 10.1121/1.400379).'),
                ('2016',
                 'Romero-García and colleagues demonstrate perfect and broadband absorption by '
                 'critically coupled sub-wavelength resonators (DOI 10.1038/srep19519).')],
 'act2_title': 'Act II — How It Actually Works: Critical Coupling & Viscothermal Loss',
 'act2_analogy': 'Think of an acoustic resonator like a child on a playground swing. Pushing the '
                 'swing at its natural tempo builds huge motion with very little effort. In our '
                 'acoustic system, incoming sound waves act as the rhythmically pushing hands, and '
                 'the air trapped in the resonator cavity is the swinging child. If the neck of '
                 'the bottle has just the right amount of friction, it absorbs all the energy of '
                 'the push without bouncing any sound back, converting the noise into gentle '
                 'warmth.',
 'act2_plain_primer': 'To control this acoustic damper, our model provides two physical '
                      'adjustments that mirror the swing analogy. The first adjustment is the '
                      'Resonant Frequency, which sets the natural tempo of the acoustic chamber. '
                      'Just as shortening the chains on a swing makes it pump faster, shrinking '
                      'the internal volume of the cavity tunes the device to target higher-pitched '
                      'tones, while enlarging the cavity targets deep, low rumbling sounds. The '
                      'second adjustment is the Resonator Neck Radius, which governs the amount of '
                      'friction the air encounters as it rushes in and out. Narrowing this neck '
                      'constricts the opening, forcing the oscillating air into intimate contact '
                      'with the solid walls where viscous friction absorbs energy. If the neck is '
                      'too wide, the air glides through with barely any resistance; if it is too '
                      'narrow, sound cannot enter the bottle. Tuning both dials aligns the tempo '
                      'and friction so that, in the model, the resonator absorbs nearly all of the '
                      'sound at its resonance.',
 'distill_diagram': {'analogy_title': 'Playground Swing & Tuned Resonator',
                     'analogy_sub': 'Friction absorbs push energy when pushed at exact natural '
                                    'rhythm.',
                     'force_a_title': 'Resonant Frequency (f_0)',
                     'force_a_sub': 'Cavity spring stiffness setting natural oscillation tempo.',
                     'force_b_title': 'Resonator Neck Radius (r_neck)',
                     'force_b_sub': 'Controls viscous boundary-layer friction and thermal loss.',
                     'threshold_title': 'Critical Impedance Match (Z_eff = ρ_0 c_0)',
                     'threshold_pass': 'Perfect Absorption: Energy dissipated with zero '
                                       'reflection.',
                     'threshold_fail': 'Impedance Mismatch: Sound reflects or fails to enter '
                                       'neck.'},
 'act2_intuition': 'Perfect acoustic absorption occurs when the radiative leakage rate of a '
                   'resonator precisely balances its internal viscothermal dissipation rate — a '
                   'physical condition known as critical coupling (Z_eff = rho_0 c_0). With the '
                   "page's model resistance of 1.04 rho_0 c_0 and zero reactance at resonance, "
                   'the absorption coefficient is alpha = 1 − (0.04/2.04)² ≈ 0.9996. When sound '
                   'enters the narrow neck of radius r_neck, oscillatory air motion forms a '
                   'viscous boundary layer delta_v = sqrt(2 nu / omega) along the inner perimeter '
                   'where shear stress converts acoustic momentum into heat. Simultaneously, '
                   'thermal diffusion creates a thermal boundary layer delta_h where pressure '
                   'fluctuations undergo irreversible thermodynamic relaxation. In the ideal '
                   'model, matching the internal resistance to the free-field acoustic impedance '
                   'removes the reflected wave; no numerical simulation was run for this folio. By '
                   'tuning the neck radius relative to the viscothermal '
                   'layer thickness, engineers ensure the acoustic impedance possesses zero '
                   'imaginary reactance and an acoustic resistance identical to air, allowing deep '
                   'sub-wavelength panels to absorb loud low-frequency sound without requiring '
                   'heavy mass or bulky wall envelopes.',
 'act2_deepening': 'The coupled multi-scale physics between the acoustic cavity and the neck '
                   'boundary layer is governed by the ratio of neck radius to viscous penetration '
                   'depth. At high frequencies or with wide openings, the viscous boundary layer '
                   'occupies only a small fraction of the neck area, allowing the central air plug '
                   'to oscillate almost frictionlessly. In this under-damped regime, the resonator '
                   'stores acoustic energy reactively and reflects the majority of the incoming '
                   'sound wave. Conversely, when the neck radius shrinks toward the thickness of '
                   'the viscous boundary layer, the shear zones from opposing walls coalesce, '
                   'heavily over-damping the resonator and choking acoustic volume velocity. '
                   'Critical coupling occurs at the exact intermediate transition where internal '
                   'viscothermal dissipation equals external radiation damping. At this optimal '
                   'balance point, destructive interference between the incoming wave and the tiny '
                   'leakage wave annihilates all acoustic reflection. This produces a deep '
                   'absorption notch whose bandwidth and peak frequency are exquisitely sensitive '
                   'to ambient temperature and fluid viscosity.',
 'walkthrough': ['Experiment 1 (Critical Impedance Match): Inspect the model absorption peak '
                 'alpha ≈ 0.9996 at the Helmholtz resonance, where Im(Z_s) = 0 and Re(Z_s) = '
                 '1.04 rho_0 c_0.',
                 'Experiment 2 (Neck Radius): Move the neck radius away from 0.65 mm and watch '
                 'the model resistance drift from rho_0 c_0 and the peak absorption fall: too '
                 'wide and the resonator is under-damped, too narrow and it is over-damped.',
                 'Experiment 3 (4-Stage Stepper): Follow the stepper from the oscillatory '
                 'boundary layer to the detuned-array design idea.'],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification '
               'Bridge',
 'act4_human_ai': 'A proposal, not something this folio has done: a differentiable Stinson '
                  'viscothermal model could sit inside an optimization loop that turns a target '
                  'room absorption spectrum into a 3D-printable coiled geometry. Readers who '
                  'want to try this could use open spectral solvers such as '
                  'DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, DOI '
                  '10.1103/PhysRevResearch.2.023068) or the FEniCS/dolfinx finite-element library '
                  '(one of its method papers: DOI 10.1145/3524456). Neither was run here. '
                  'References were checked in the Scite index (DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'A research direction, not settled practice: generative design, with '
                   'people and algorithms working together, could help with hard architectural '
                   'noise problems. In such a workflow, designers would define target sound absorption spectra for noisy hospital cooling '
                   'towers, data centers, or high-speed rail corridors, while evolutionary '
                   'algorithms search thousands of labyrinthine space-coiling topologies to '
                   'discover optimal sub-wavelength metamaterials. Physics-based surrogate solvers '
                   'evaluate viscothermal boundary layer losses and structural rigidity in '
                   'seconds, passing high-performing candidate designs to finite-element '
                   'verification pipelines. Human engineers review the generated geometries to '
                   'ensure manufacturing feasibility with additive polymer printing and long-term '
                   'durability under harsh outdoor weathering. Open research frontiers explore '
                   'adaptive metamaterials with electro-pneumatically actuated necks capable of '
                   'dynamically shifting their absorption frequencies to track moving machinery '
                   'speeds. By marrying automated algorithmic optimization with rigorous '
                   'mechanical and acoustic testing, engineers might one day produce '
                   'ultra-compact sound-absorbing facade panels. That is a proposal: this folio '
                   'has built and tested nothing, and how much such panels would reduce urban '
                   'noise is not known.',
 'cf_bridge': 'An analogy, offered modestly: airway clearance devices such as chest-wall '
              'oscillation vests and oscillatory positive expiratory pressure (OPEP) devices '
              'also make air move back and forth, and sputum is a yield-stress, thixotropic '
              'material (Figueroa-Landeta et al. 2025, DOI 10.1038/s41598-025-16178-z). Whether '
              'and how much oscillation changes sputum is a clinical research question: in one '
              'small crossover trial in people with Cystic Fibrosis, Radtke et al. (2018, DOI '
              '10.1186/s12890-018-0661-1) measured sputum rheology after exercise with and '
              'without OPEP. This page does not model the airways, makes no claim about any '
              'therapy, and is not medical advice.',
 'sources': ['Yang, M., & Sheng, P. (2017). Sound Absorption Structures: From Porous Media to '
             'Acoustic Metamaterials. Annual Review of Materials Research, 47, 83–114. DOI: '
             '10.1146/annurev-matsci-070616-124032.',
             'Stinson, M. R. (1991). The propagation of plane sound waves in narrow and wide '
             'circular tubes, and generalization to uniform tubes of arbitrary cross-sectional '
             'shape. The Journal of the Acoustical Society of America, 89(2), 550–558. DOI: '
             '10.1121/1.400379.',
             'Romero-García, V., Theocharis, G., Richoux, O., Merkel, A., Tournat, V., et al. '
             '(2016). Perfect and broadband acoustic absorption by critically '
             'coupled sub-wavelength resonators. Scientific Reports, 6, 19519. DOI: '
             '10.1038/srep19519.',
             'Figueroa-Landeta, M., et al. (2025). Thixo-viscoelastoplastic rheological '
             'characterisation of human mucus using a multimode BMP constitutive equation '
             'approach. Scientific Reports, 15, 43747. DOI: 10.1038/s41598-025-16178-z.',
             'Radtke, T., et al. (2018). Acute effects of combined exercise and oscillatory '
             'positive expiratory pressure therapy on sputum properties and lung diffusing '
             'capacity in cystic fibrosis: a randomized, controlled, crossover trial. BMC '
             'Pulmonary Medicine, 18, 99. DOI: 10.1186/s12890-018-0661-1.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). '
             'Dedalus: A flexible framework for numerical simulations with spectral methods '
             '(DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review '
             'Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Viscothermal '
        'Helmholtz absorption peak at critical coupling (model)">\n'
        '            <line x1="60" y1="180" x2="620" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <path d="M 70 175 Q 240 170 310 32 Q 380 170 590 175" '
        'fill="var(--tp-prussian)" fill-opacity="0.16" stroke="var(--tp-prussian)" '
        'stroke-width="2.5"/>\n'
        '            <line x1="60" y1="95" x2="620" y2="95" stroke="var(--tp-minium)" '
        'stroke-width="1.8" stroke-dasharray="5,4"/>\n'
        '            <circle cx="310" cy="32" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="195" y="22" font-size="11" fill="var(--tp-verdigris)">Critical '
        'Coupling Peak (model): α ≈ 0.9996 at f_0</text>\n'
        '            <text x="415" y="88" font-size="11" fill="var(--tp-minium)">Reference line: '
        'α = 0.5 (illustrative)</text>\n'
        '            <text x="225" y="202" font-size="11" fill="currentColor">Frequency around '
        'the Helmholtz resonance f_0</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a labyrinthine coiled-space acoustic and seismic '
        'metamaterial wall panel and foundation lattice would look like (artistic impression, not '
        'a measured structure)',
 'caption': 'Conceptual Vision Plate E.03-V (Imagining What It Would Look Like) · Artistic '
            'structural cutaway imagining a sub-wavelength labyrinthine coiled-space acoustic '
            'metamaterial panel mounted above a periodic seismic wave-shielding foundation '
            'lattice.'}

DISPATCH = {'kicker': 'FRONTIER METAMATERIAL DISPATCH · SUB-WAVELENGTH ACOUSTIC DAMPING',
 'headline': 'Critically Coupled Resonators Absorb Low-Frequency Sound in Thin Panels',
 'body': "Building on Helmholtz (1863) and Stinson's viscothermal theory (1991, DOI "
         '10.1121/1.400379), coiled-space and labyrinthine absorbers can work at depths far '
         'below a quarter wavelength (review: DOI 10.1146/annurev-matsci-070616-124032). '
         'Romero-García and colleagues (2016, DOI 10.1038/srep19519) showed that when a '
         "resonator's losses balance its leakage, absorption at resonance can reach 100%."}

META_3D = ('Coiled Helmholtz Labyrinthine Ring Resonator',
 'X/Z: Sub-Wavelength Cell Plane · Y: Acoustic Impedance & Quarter-Wave Absorption Well')

ES_TRANSLATION = {'title_es': 'Arreglos de Metamateriales Acústicos Sub-Longitud de Onda de Helmholtz y '
             'Amortiguamiento Viscotérmico',
 'subtitle_es': 'Cómo los resonadores en espacio enrollado y las capas límite viscotérmicas '
                'δ_v = √(2ν/ω) pueden absorber sonido grave en paneles mucho más delgados que un '
                'cuarto de longitud de onda; el estudio de diseño de esta página apunta a cerca '
                'de 1/19 de la longitud de onda.',
 'why_es': 'Un laberinto acústico enrollado obliga a las ondas sonoras graves a recorrer un camino '
           'largo dentro de un panel delgado, disipando el ruido de baja frecuencia en calor '
           'microscópico.',
 'bridge_es': 'Una analogía modesta: los chalecos de oscilación de la pared torácica y los '
              'dispositivos de PEP oscilatorio también hacen oscilar el aire, y el esputo es un '
              'material con esfuerzo de fluencia. Cuánto cambia el esputo con la oscilación es '
              'una pregunta de investigación clínica; esta página no modela ninguna terapia ni '
              'es consejo médico.',
 'plain_es': 'En 1863, el médico y físico alemán Hermann von Helmholtz publicó Die Lehre von den '
             'Tonempfindungen, donde describió resonadores huecos con un cuello estrecho que '
             'usaba para aislar tonos puros dentro de sonidos complejos. Más adelante en el siglo '
             'XIX, físicos como Lord Rayleigh analizaron cómo el aire que vibra en tubos '
             'estrechos roza contra las paredes y convierte la energía sonora en calor. En nuestra vida cotidiana, '
             'todos hemos soplado sobre la boca de una botella vacía para generar un silbido '
             'grave; ese tono musical surge del rebote del aire dentro del cuello contra el '
             'volumen de la botella. Los ingenieros acústicos aprovechan este principio para '
             'absorber ruidos no deseados. Normalmente, absorber ruido grave exige absorbedores '
             'gruesos y voluminosos. Al enrollar canales largos y delgados en paneles '
             'compactos, los investigadores han mostrado que el sonido grave puede absorberse en '
             'estructuras mucho más delgadas. El aire roza contra los canales interiores y '
             'convierte la vibración en un poco de calor. Es una de las formas con las que '
             'los diseñadores esperan tratar el ruido de baja frecuencia en sistemas de '
             'ventilación y edificios sin ceder tanto espacio útil.',
 'deep_es': 'La absorción acústica casi perfecta se logra al emparejar dos fuerzas contrarias: la '
            'fuga de radiación sonora de la cavidad y la disipación interna en las capas límite '
            'viscotérmicas. Este fenómeno se conoce como acoplamiento de impedancia crítica. '
            'Cuando la onda sonora entra al cuello del resonador, la fricción del aire genera una '
            'capa límite viscosa y otra térmica donde la energía se convierte en calor. Si el '
            'radio del cuello es demasiado amplio, el aire pasa sin suficiente resistencia y el '
            'sonido rebota; si es excesivamente angosto, el aire no logra penetrar en la cavidad. '
            'El punto óptimo equilibra la frecuencia natural y la fricción del cuello; en el '
            'modelo ideal, eso elimina la onda reflejada. Como propuesta, no como práctica '
            'establecida, un modelo viscotérmico diferenciable podría ayudar a proponer '
            'geometrías enrolladas imprimibles en 3D a partir de un espectro de absorción '
            'objetivo; esta página no construyó ni probó ninguna.'}
