#!/usr/bin/env python3
"""Folio E.02 (ENGINEERING): Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie Placement."""
from __future__ import annotations

SLUG = 'e02'

PILLAR = 'engineering'

FOLIO = {'folio_id': 'E.02',
 'slug': 'e02',
 'pillar': 'engineering',
 'category_code': 'E',
 'title': 'Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie '
          'Placement',
 'subtitle': "How Eugene Bingham's and Winslow Herschel and Ronald Bulkley's yield-stress "
             'rheology describes pipe pressure drops, central plug-flow cores, and the risk of '
             'line blockage when concrete is pumped.',
 'date_published': '2026-10-26',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.4',
 'status_badge': 'CIVIL & CONSTRUCTION · REV 1.4',
 'primary_kernel': 'tools/continuum_verify.py',
 'governing_law': 'τ = τ_0 + K γ̇^n · r_p / R = τ_0 / τ_w · ΔP/L = 2τ_w/R',
 'colophon': {'identifier': 'E.02 · Concrete Yield Rheology · CSI 03 30 00',
              'kernels': 'τ = τ_0 + K γ̇^n · Buckingham–Reiner Plug Flow',
              'benchmarks': 'Model values: 125 mm pipe · τ_w = 75.0 Pa and r_p/R = 37.3% at '
                            'defaults',
              'bridge': 'Concrete Slickline'},
 'sliders': [{'label': 'Concrete Yield Stress (τ_0)',
              'min': 5.0,
              'max': 100.0,
              'step': 1.0,
              'value': 28.0,
              'unit': ' Pa'},
             {'label': 'Pumping Pressure Gradient (ΔP/L)',
              'min': 0.5,
              'max': 8.0,
              'step': 0.1,
              'value': 2.4,
              'unit': ' kPa/m'}],
 'steps': ['Stage 1 (Unmobilized Solid Arrest, τ_w ≤ τ_0): When wall shear stress falls below '
           'yield stress τ_0, the concrete locks into zero-flow solid arrest.',
           'Stage 2 (Central Unsheared Plug Core, r ≤ r_p): For τ_w > τ_0, an unsheared solid plug '
           'of radius r_p/R = τ_0/τ_w translates along the pipe center.',
           'Stage 3 (Annular Shear-Thinning Layer): Shear is confined to the annulus r_p < r ≤ R. '
           'The page uses a power-law index n = 0.65 and consistency K = 8.5 Pa·sⁿ, fixed '
           'illustrative values rather than measured ones.',
           'Stage 4 (Polycarboxylate Dispersion): PCE superplasticizers disperse cement grains '
           'and lower the yield stress; how much depends on the mix and dose, and the page does '
           'not model a specific reduction.'],
 'readouts': [{'label': 'Wall Shear Stress', 'value': '75.0 Pa'},
              {'label': 'Plug Core Radius Ratio', 'value': '37.3% (23.3 mm)'},
              {'label': 'Discharge Output', 'value': '6.6 m³/hr (8.6 yd³/hr) · model, K = 8.5 Pa·sⁿ, n = 0.65'},
              {'label': 'Pumping State', 'value': 'MOBILIZED IN THE MODEL (τ_w > τ_0)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 03 30 00 / ACI 304.2R',
                'title': 'High-Performance Concrete Slickline Pumping & Tremie Placement',
                'body': 'Illustrative design sketch, not a tested specification: a pumpable '
                        'self-consolidating mix (target slump flow 650 mm, measured by the ASTM '
                        'C1611 slump-flow test), a 125 mm steel line and a PCE superplasticizer, '
                        'with the design rule that wall shear stress must exceed yield stress '
                        'along the run.',
                'meta': 'Design sketch · ACI 304.2R is the ACI guide to placing concrete by '
                        'pumping; no field data or telemetry stand behind this plate'},
 'sidenote_1': {'kicker': 'SIDENOTE E.02-A · PLUG FLOW KINEMATICS & BUCKINGHAM–REINER',
                'body': 'In the ideal yield-stress model, concrete in the central core r ≤ r_p '
                        'sees shear stress below τ_0, so it does not shear: the core moves as one '
                        'piece at velocity u_plug. Real pumped concrete also forms a thin '
                        'paste-rich layer at the wall, which this simple model leaves out.'},
 'sidenote_2': {'kicker': 'SIDENOTE E.02-B · SPECIFICATION PLATE · CSI 03 30 00 / ACI 304.2R',
                'body': 'Design sketch of a pumped self-consolidating concrete (target slump flow '
                        '650 mm, 125 mm steel line, PCE dispersant).'},
 'skill': {'filename': 'herschel-bulkley-yield-rheology-SKILL.md',
           'name': 'herschel-bulkley-yield-rheology',
           'description': 'AI-agnostic civil and non-Newtonian fluid mechanics skill for '
                          'Herschel-Bulkley and Bingham concrete pumping rheology, plug-flow '
                          'radius r_p/R = tau_0/tau_w, and thixotropic dispersion.',
           'rules': ['Check slickline yield mobilization: pumping requires wall shear stress '
                     'tau_w = (DeltaP * R)/(2L) > tau_0 (plug ratio r_p / R = tau_0 / tau_w < 1).',
                     'Evaluate Buckingham-Reiner volumetric flow multiplier Q / Q_Newtonian = 1 - '
                     '(4/3)*(tau_0/tau_w) + (1/3)*(tau_0/tau_w)^4 for Bingham plastics.',
                     'Account for shear-thinning power-law index n < 1 in the sheared annulus, and '
                     'state that real pumped concrete also forms a paste-rich lubrication layer '
                     'at the wall that a homogeneous model leaves out.']},
 'revisions': [{'edition': 'REV 1.4',
                'date': '2026-11-14',
                'summary': 'REV 1.4 (Redated 2026-11-14): Grounding revision. The 2016 pumping '
                           'paper is now credited to its real authors (Feys, Khayat & Khatib), '
                           'the discharge readout was recomputed from the page model (not 48.2 '
                           'm³/hr), and the invented 1922 laboratory scene was replaced with '
                           'plain dates. A later review corrected the discharge to 6.6 m³/hr, the '
                           "page model's full Herschel–Bulkley integral (the earlier 7.2 m³/hr "
                           'rested on a hidden factor), described the wall lubrication layer as '
                           'something the model leaves out, labelled the feedback argument as '
                           "the folio's own inference, and softened outcome promises.",
                'opus': 'Review: every DOI in the folio was checked in Crossref and the Scite '
                        'index on 2026-11-14, and the repository name with the GitHub API. No '
                        'simulation, telemetry or field test stands behind this folio; its '
                        'numbers come from the closed-form model on the page.'},
               {'edition': 'REV 1.3',
                'date': '2026-11-02',
                'summary': 'REV 1.3 (Redated 2026-11-02): Verified Herschel-Bulkley yield-stress '
                           'concrete rheology (tau = tau_0 + K * gamma_dot^n), 125 mm steel '
                           'slickline plug core (r_p/R = tau_0/tau_w), Buckingham-Reiner velocity '
                           'profile, and PCE dispersion (ACI 304.2R, CSI 03 30 00).',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): checked that '
                        'tau_w = 75.0 Pa and r_p/R = 37.3% follow from the page formulas. The word '
                        '"Verified" in this note and in the notes below, and the '
                        'PCE-to-mucolytic bridge, are withdrawn in REV 1.4.'},
               {'edition': 'REV 1.2',
                'date': '2026-11-01',
                'summary': 'REV 1.2 (Redated 2026-11-01): Unified 125 mm steel slickline '
                           'Herschel-Bulkley concrete pumping & tremie placement observatory with '
                           'PCE-to-mucolytic yield-stress bridge.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified wall '
                        'shear stress τ_w = (ΔP·R)/(2L) = 75.0 Pa at ΔP/L = 2.40 kPa/m and plug '
                        'ratio r_p/R = 37.3%.'},
               {'edition': 'REV 1.1',
                'date': '2026-10-29',
                'summary': 'REV 1.1 (Redated 2026-10-29): Added Buckingham-Reiner fourth-order '
                           'plug-flow polynomial verification.',
                'opus': 'Multi-Family Council Audit (Gemini 4 Argon + Qwen 3.8 27B): Verified '
                        'zero-flow arrest when τ_w ≤ τ_0.'}],
 'volume': 1,
 'volume_code': 'VOL. 01',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.cemconcomp.2015.11.002',
           'fetched_on': '2026-11-08',
           'citing_publications': 151,
           'supporting': 0,
           'mentioning': 46,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Feys, Khayat & Khatib 2016 (DOI '
                      '10.1016/j.cemconcomp.2015.11.002), as recorded 2026-11-08: 151 citing '
                      'publications (0 supporting, 46 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1016/j.cemconcomp.2015.11.002',
           'fetched_on': '2026-11-08',
           'citing_publications': 151,
           'supporting': 0,
           'mentioning': 46,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Feys, Khayat & Khatib 2016 (DOI '
                      '10.1016/j.cemconcomp.2015.11.002), as recorded 2026-11-08: 151 citing '
                      'publications (0 supporting, 46 mentioning, 0 contrasting) and no '
                      'retraction notice. These counts describe that one paper, not this '
                      'folio.'},
 'act1_title': 'Act I — From Bingham Plasticity to High-Rise Concrete Slickline Pumping & Tremie '
               'Placement',
 'act1_dropcap': 'In 1922 the American chemist Eugene Bingham published Fluidity and '
                 'Plasticity, a book that set out how materials such as paints and clay '
                 'suspensions behave like solids until a threshold stress is passed and then '
                 'flow. That threshold is the yield stress, and the simplest law built on it, '
                 'with a constant plastic viscosity above the threshold, still carries his '
                 'name. In 1926 Winslow Herschel and Ronald Bulkley published consistency '
                 'measurements on solutions of rubber in benzene and generalized the law: above '
                 'the yield stress, the extra stress grows as a power of the shear rate rather '
                 'than in simple proportion. Together these two laws are the starting point of '
                 'yield-stress rheology.',
 'act1_plain_bridge': 'Think about squeezing a fresh tube of toothpaste in the morning. When the '
                      'tube rests on the counter, the paste holds its shape like a solid block. It '
                      'never drips or runs. But the moment your fingers squeeze with enough force, '
                      'the paste suddenly yields and flows smoothly through the nozzle. Fresh wet '
                      'concrete in a construction pipeline behaves in a similar way. When '
                      'building skyscrapers or pouring deep bridge foundations, crews must pump '
                      'thousands of tons of wet concrete through long steel pipes. If the pumps '
                      'push hard enough, a slippery film forms against the inner pipe wall. This '
                      'thin lubricating layer lets a solid core of concrete glide forward '
                      'effortlessly. But if the pump pressure drops too low, or if the mix becomes '
                      'too stiff during a pause, the concrete can lock into a solid plug. '
                      'Understanding this balance helps explain why pump pressure and mix '
                      'stiffness matter on a job.',
 'act1_body': 'Pumping concrete up tall buildings or down into deep foundations depends on '
              'rheology. In the simple yield-stress picture used on this page, if the pressure '
              'gradient cannot raise the wall shear stress above the yield stress, the concrete '
              'does not flow; once it does, the flow splits into a central plug that moves '
              'without shearing and a sheared region near the wall. Real pumped concrete adds a '
              'further feature: cement paste and fine material migrate toward the pipe wall and '
              'form a lubrication layer, and the rheology of that layer strongly affects pumping '
              'pressure (De Schutter & Feys 2016, DOI 10.21809/rilemtechlett.2016.15; Feys, '
              'Khayat & Khatib 2016, DOI 10.1016/j.cemconcomp.2015.11.002). Fresh concrete is '
              'also thixotropic: at rest it rebuilds structure and its yield stress rises, which '
              'Nicolas Roussel described with a widely used model (2006, DOI '
              '10.1016/j.cemconres.2006.05.025). After a long pause, the pressure needed to '
              'restart the line can therefore be higher than the pressure needed to keep it '
              'moving.',
 'act1_stakes': 'Treating fresh concrete as an ordinary Newtonian fluid misses both the '
                'yield stress and the rebuild of structure at rest, and those are what decide '
                'whether a line keeps moving. A blocked line has to be cleared, which delays '
                'the pour and can expose crews to stored pressure; this page does not quantify '
                'how often that happens. Pushing the other way, too much superplasticizer can '
                'make a mix segregate, so that coarse aggregate separates from the paste. One '
                'approach a contractor could take is to watch line pressure during pumping and '
                'compare it with a rheological model; the page offers such a model as a '
                'teaching tool, not as a field-tested control method.',
 'pullquote': '"Fresh concrete in a 125 mm steel slickline is neither simple solid nor simple '
              'liquid: it is a yield-stress suspension where a rigid central plug rides on an '
              'ultra-thin sheared lubrication boundary layer."',
 'chronology': [('1922',
                 "Eugene Bingham's book Fluidity and Plasticity sets out the two-parameter "
                 'yield-stress plastic law tau = tau_0 + mu_p * gamma_dot.'),
                ('1926',
                 'Winslow Herschel & Ronald Bulkley generalize yield-stress rheology with the '
                 'power-law index n (tau = tau_0 + K * gamma_dot^n) (DOI 10.1007/BF01432034).'),
                ('2016',
                 'Feys, Khayat & Khatib examine how rheology, tribology, flow rate and pipe '
                 'radius influence pumping pressure (DOI 10.1016/j.cemconcomp.2015.11.002).'),
                ('2017',
                 'ACI Committee 304 publishes ACI 304.2R-17, its guide to placing concrete by '
                 'pumping methods.')],
 'act2_title': 'Act II — How It Actually Works: Wall Shear Stress vs. Unsheared Plug Core',
 'act2_analogy': 'Squeezing frosting through a pastry piping bag or toothpaste through a nozzle '
                 'does not deform the entire substance evenly. If you look closely at the moving '
                 'stream, a solid cylinder in the exact center slides forward completely intact, '
                 'like a piston riding on a slippery track. Only the outer sliver of paste '
                 'touching the nozzle wall experiences shearing forces. The center stays solid '
                 'because the internal forces there never rise high enough to overcome its resting '
                 'yield strength.',
 'act2_plain_primer': 'To see how this works on a job site, picture two primary controls operating '
                      'our concrete delivery pipeline. The first control is the Concrete Yield '
                      'Stress, which represents the internal stickiness or resting strength of the '
                      'wet mixture. If you raise this dial, the cement particles cling to one '
                      'another more stubbornly, demanding a greater push before they agree to '
                      'slide. The second control is the Pumping Pressure Gradient, which '
                      'represents the brute force applied by the hydraulic pistons pushing the '
                      'fluid down the pipe. Turning this pressure dial up increases the shearing '
                      'friction generated along the steel pipe walls. If the pump pushes hard '
                      'enough, the wall shear overcomes the resting strength and the center plug '
                      'glides forward, with all the shearing confined to the outer ring. (Real '
                      'concrete also forms a paste-rich lubrication layer at the wall; the model '
                      'leaves that layer out.) But if the yield stress dial climbs above the wall '
                      'shear stress, the plug expands to fill the entire pipe and, in the model, '
                      'flow stops.',
 'distill_diagram': {'analogy_title': 'Toothpaste Tube & Central Plug Flow',
                     'analogy_sub': 'In the model, a solid core glides inside a sheared outer ring.',
                     'force_a_title': 'Concrete Yield Stress (τ_0)',
                     'force_a_sub': 'Internal resting strength resisting initial shear '
                                    'deformation.',
                     'force_b_title': 'Pressure Gradient (ΔP/L)',
                     'force_b_sub': 'Hydraulic driving force generating wall shear stress τ_w.',
                     'threshold_title': 'Plug Yield Criterion (τ_w vs τ_0)',
                     'threshold_pass': 'Mobilized Flow: Wall shear τ_w exceeds τ_0, plug glides.',
                     'threshold_fail': 'Locked Slickline: Wall shear τ_w drops below τ_0, pipe '
                                       'jams.'},
 'act2_intuition': 'In a cylindrical steel slickline of radius R = 62.5 mm, axial momentum '
                   'conservation dictates that shear stress varies linearly from zero at the pipe '
                   'centerline to a maximum value at the inner wall: tau(r) = (DeltaP * r) / (2 '
                   'L), with wall shear stress tau_w = (DeltaP * R) / (2 L). Because a '
                   'Herschel–Bulkley suspension cannot undergo irreversible shear strain wherever '
                   'local stress tau(r) remains below the yield stress tau_0, a central core '
                   'cylinder of radius r_p = R * (tau_0 / tau_w) translates forward as an '
                   'unsheared solid plug at uniform velocity u_plug. All velocity gradients '
                   'concentrate within the outer sheared annulus r_p < r <= R. At the default '
                   'settings (tau_0 = 28 Pa, DeltaP/L = 2.4 kPa/m) this gives tau_w = 75.0 Pa '
                   'and r_p = 23.3 mm. The discharge readout uses the fixed illustrative values K '
                   '= 8.5 Pa·s^n and n = 0.65 and is the full Herschel–Bulkley pipe integral of '
                   'the page model, about 6.6 m³/hr (8.6 yd³/hr). Because the model has no wall '
                   'lubrication layer, it likely understates what real pumps deliver. As a proposal, not something this folio has done, '
                   'pressure and flow records from a pump could be fitted with a data-driven '
                   'method such as sparse identification of nonlinear dynamics (Brunton, Proctor '
                   '& Kutz 2016, DOI 10.1073/pnas.1517384113; open-source code in '
                   'dynamicslab/pysindy) to estimate tau_0, K and n while pumping.',
 'act2_deepening': 'The physical mechanics of the wall layer involve particle migration. As '
                   'fresh concrete flows, coarse aggregate moves slightly toward the pipe center '
                   'and cement paste and fine material gather at the wall, forming a lubrication '
                   'layer (De Schutter & Feys 2016, DOI 10.21809/rilemtechlett.2016.15). Its '
                   'thickness varies with the mix; the page does not assign it a value. This '
                   'layer carries much of the shear, so the dense core meets less friction. The '
                   "rest of this paragraph is the folio's own inference, not a result from the "
                   'cited papers, and no simulation was run. If the pressure gradient drops, the '
                   'wall shear stress decreases and the unsheared central plug widens toward the '
                   'pipe wall. As the plug widens, the volumetric flow rate falls according to '
                   'the Buckingham–Reiner relation, which would lower the shear rate near the '
                   'wall and could let thixotropic structure rebuild. If that happened, the '
                   'feedback could slow the flow further, which is one reason pump pressure and '
                   'yield stress might need to be watched together.',
 'walkthrough': ['Experiment 1 (Slickline Lockup): Drag Pumping Pressure Gradient DeltaP/L down '
                 'below 0.90 kPa/m at tau_0 = 28 Pa. Watch wall shear stress tau_w drop below '
                 'tau_0, highlighting the rheology tuning window where PCE dispersant mobilizes '
                 'the core.',
                 'Experiment 2 (PCE Superplasticizer Dosing): Lower Concrete Yield Stress tau_0 '
                 'from 68 Pa down to 20 Pa (standing in for polycarboxylate ether dispersion). At '
                 'tau_w = 75 Pa, watch the central plug core shrink from about 91% to 27% of the '
                 'pipe radius while model output Q rises. Above 75 Pa the line is locked.',
                 'Experiment 3 (4-Stage Stepper): Click Stages 1 to 4 to trace unmobilized solid '
                 'arrest, central plug translation, annular shear-thinning lubrication, and '
                 'thixotropic dispersion.'],
 'act4_title': 'Act IV — Civil Construction Telemetry & the Structural & Civil Engineering '
               'Specification Bridge',
 'act4_human_ai': 'A proposal, not a description of current practice: pump-line pressure '
                  'sensors could feed a Buckingham–Reiner or Herschel–Bulkley model that warns '
                  'when the predicted plug approaches the full pipe radius. Readers who want to '
                  'try this could fit pressure-flow records with sparse identification '
                  '(dynamicslab/pysindy, https://github.com/dynamicslab/pysindy, DOI '
                  '10.1073/pnas.1517384113) or build pipe-flow models with the FEniCS/dolfinx '
                  'finite-element library (one of its method papers: DOI 10.1145/3524456). '
                  'Neither tool was run for this folio. ACI 304.2R-17 is the ACI guide to '
                  'placing concrete by pumping; it is named for context and does not contain '
                  "this page's model or thresholds. References were checked in the Scite index "
                  '(DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Looking ahead, researchers are exploring sensor-rich pumping and 3D '
                   'concrete printing, where machine-learning models might estimate yield stress '
                   'and the rate of structural rebuild from line data and suggest changes to '
                   'pumping or admixture dosing. These are research directions, not established '
                   'site practice, and this folio has not tested them. Open questions include '
                   'how lubrication layers behave at pipe bends and how newer low-carbon binders, '
                   'such as calcined clay cements, change yield stress and thixotropy. Human '
                   'judgment on site stays central; no model can guarantee a placement.',
 'sources': ['Bingham, E. C. (1922). Fluidity and Plasticity. McGraw-Hill, New York.',
             'Herschel, W. H., & Bulkley, R. (1926). Konsistenzmessungen von Gummi-Benzollösungen. '
             'Kolloid-Zeitschrift, 39(4), 291–300. DOI: 10.1007/BF01432034.',
             'ACI Committee 304 (2017). Guide to Placing Concrete by Pumping Methods (ACI '
             '304.2R-17). American Concrete Institute.',
             'Feys, D., Khayat, K. H., & Khatib, R. (2016). How do concrete rheology, tribology, '
             'flow rate and pipe radius influence pumping pressure? Cement and Concrete '
             'Composites, 66, 38–46. DOI: 10.1016/j.cemconcomp.2015.11.002.',
             'De Schutter, G., & Feys, D. (2016). Pumping of Fresh Concrete: Insights and '
             'Challenges. RILEM Technical Letters, 1, 76–80. DOI: '
             '10.21809/rilemtechlett.2016.15.',
             'Roussel, N. (2006). A thixotropy model for fresh fluid concretes: Theory, '
             'validation and applications. Cement and Concrete Research, 36(10), 1797–1806. '
             'DOI: 10.1016/j.cemconres.2006.05.025.',
             'Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). Discovering governing '
             'equations from data by sparse identification of nonlinear dynamical systems '
             '(dynamicslab/pysindy, https://github.com/dynamicslab/pysindy). PNAS, 113(15), '
             '3932–3937. DOI: 10.1073/pnas.1517384113.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="High-performance '
        'concrete pumping pipe cross-section showing central unsheared plug core and radial '
        'velocity profile">\n'
        '            <circle cx="160" cy="110" r="64" fill="var(--tp-stone)" stroke="currentColor" '
        'stroke-width="3"/>\n'
        '            <circle cx="160" cy="110" r="54" fill="none" stroke="var(--tp-verdigris)" '
        'stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>\n'
        '            <circle id="tp-e02-svg-plug-circle" cx="160" cy="110" r="24" '
        'fill="var(--tp-prussian)" opacity="0.85"/>\n'
        '            <text x="75" y="24" font-size="11" font-weight="600" fill="currentColor">125 '
        'mm Pipe Cross-Section (r_p vs R)</text>\n'
        '            <text id="tp-e02-svg-plug-text" x="75" y="198" font-size="10" '
        'fill="var(--tp-prussian)">Plug Core: r_p = 23.3 mm (37% R)</text>\n'
        '            <line x1="310" y1="20" x2="310" y2="200" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="345" y="24" font-size="11" font-weight="600" '
        'fill="currentColor">Buckingham–Reiner Velocity Profile u(r)</text>\n'
        '            <line x1="480" y1="40" x2="480" y2="180" stroke="currentColor" '
        'stroke-width="2"/>\n'
        '            <text x="415" y="55" font-size="9.5" fill="var(--tp-slate)">Wall r = '
        '+R</text>\n'
        '            <text x="415" y="114" font-size="9.5" fill="var(--tp-slate)">Center r = '
        '0</text>\n'
        '            <text x="415" y="175" font-size="9.5" fill="var(--tp-slate)">Wall r = '
        '-R</text>\n'
        '            <line id="tp-e02-svg-velocity-plug" x1="590" y1="92" x2="590" y2="128" '
        'stroke="var(--tp-minium)" stroke-width="3.5"/>\n'
        '            <path id="tp-e02-svg-velocity-path" d="M 480 50 Q 560 75 590 92 L 590 128 Q '
        '560 145 480 170" fill="var(--tp-minium-soft)" stroke="var(--tp-minium)" '
        'stroke-width="2.5"/>\n'
        '            <text x="485" y="198" font-size="10" fill="var(--tp-minium)">Velocity '
        'Profile: Flat Plug u_plug + Sheared Annulus</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a high-rise concrete pumping slickline cutaway '
        'with laminar boundary slip-layer and Herschel-Bulkley plug core would look like (artistic '
        'impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate E.02-V (Imagining What It Would Look Like) · Artistic cutaway '
            'visualization imagining the thin mortar lubricating slip-layer surrounding the '
            'unyielded Herschel-Bulkley plug core (r_p = 2*tau_0 / (Delta_P/L)) inside a high-rise '
            'steel slickline pipe.'}

DISPATCH = {'kicker': 'FRONTIER ENGINEERING DISPATCH · CONCRETE PUMPING TRIBOLOGY',
 'headline': 'The Paste Layer at the Pipe Wall Shapes Concrete Pumping Pressure',
 'body': 'The Bingham (1922) and Herschel–Bulkley (1926) laws treat concrete as a uniform '
         'yield-stress fluid. Pumping research adds a lubrication layer of cement paste that forms '
         'at the pipe wall: Feys, Khayat & Khatib (Cement and Concrete Composites, 2016, DOI '
         '10.1016/j.cemconcomp.2015.11.002) examined how rheology, tribology, flow rate and pipe '
         'radius influence pumping pressure, and De Schutter & Feys (2016, DOI '
         '10.21809/rilemtechlett.2016.15) reviewed how that layer forms.'}

META_3D = ('Herschel–Bulkley Cylindrical Plug-Core Dome',
 'X/Z: Pipe Cross-Section Radius r/R · Y: Axial Bingham Plug & Shear Velocity u(r)')

ES_TRANSLATION = {'title_es': 'Reología de Esfuerzo de Fluencia de Herschel–Bulkley: Bombeo de Concreto de Alto '
             'Desempeño y Colocación Tremie',
 'subtitle_es': 'Cómo la reología de esfuerzo de fluencia de Bingham y de Herschel y Bulkley '
                'describe las caídas de presión en tuberías, los núcleos de flujo tapón y el '
                'riesgo de bloqueo al bombear concreto.',
 'why_es': 'Al exprimir pasta dental o mortero por un tubo no se deforma todo el volumen: un '
           'cilindro sólido central se desliza intacto como un tapón sobre una delgada capa '
           'lubricante sometida a corte.',
 'plain_es': 'En 1922, el químico Eugene Bingham publicó Fluidity and Plasticity, donde explicó '
             'que materiales como pinturas y suspensiones de arcilla no fluyen de manera '
             'convencional: requieren un esfuerzo mínimo antes de comenzar a moverse. En 1926, '
             'Winslow Herschel y Ronald Bulkley publicaron mediciones con soluciones de hule en '
             'benceno y generalizaron la idea: una vez en marcha, la resistencia de estos '
             'fluidos cambia según la velocidad del movimiento. Para visualizar esto en la vida diaria, piensen en cómo sale la '
             'pasta de dientes de su envase: mantiene una forma sólida y firme sobre el cepillo, '
             'pero fluye dócilmente cuando ustedes aprietan el tubo con suficiente fuerza. En la '
             'construcción de grandes edificios y puentes, el concreto fresco que se bombea por '
             'tuberías de acero se comporta de forma parecida. En el modelo de esta página, la '
             'mezcla forma un cilindro sólido en el centro; en el concreto real, además, la '
             'pasta de cemento forma una capa lubricante junto a la pared del tubo.',
 'deep_es': 'El bombeo eficiente de concreto de alto desempeño depende del equilibrio entre dos '
            'fuerzas fundamentales: el esfuerzo de fluencia interno de la mezcla y el esfuerzo '
            'cortante generado por la presión del bombeo contra las paredes de la tubería. Cuando '
            'el gradiente de presión supera el umbral de fluencia, se genera un perfil de flujo '
            'tapón donde el núcleo central se traslada sin deformarse. El concreto real, además, '
            'forma una capa lubricante de pasta junto a la pared, que este modelo no incluye. '
            'Si la presión cae por debajo de '
            'este límite crítico o si el concreto reposa durante una pausa de colocación, los '
            'enlaces de hidratación aumentan el esfuerzo de fluencia en reposo, y reiniciar el '
            'bombeo puede requerir más presión. Como propuesta, no como práctica establecida, '
            'los sensores de presión de la línea podrían alimentar un modelo reológico que avise '
            'cuando el tapón se acerque a llenar el tubo. Esta página ofrece ese modelo como '
            'herramienta de aprendizaje; ningún cálculo sustituye las pruebas de colocación.'}
