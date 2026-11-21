#!/usr/bin/env python3
"""Folio E.13 (ENGINEERING): Biot 3D Poroelasticity, Skempton Undrained Coupling & Mohr–Coulomb Fault Slip Margin in Geologic CO2 Storage."""
from __future__ import annotations

SLUG = 'e13'

PILLAR = 'engineering'

_SCITE = {
    'doi': '10.1063/1.1712886',
    'fetched_on': '2026-11-20',
    'citing_publications': 4896,
    'supporting': 29,
    'mentioning': 4865,
    'contrasting': 2,
    'retracted': False,
    'summary': (
        'Scite Smart Citation Index entry for Biot 1941, "General Theory of Three-Dimensional Consolidation" '
        '(Journal of Applied Physics, DOI 10.1063/1.1712886), fetched 2026-11-20: 4,896 citing records '
        '(29 supporting, 4,865 mentioning, 2 contrasting) and no retraction notice. '
        'These counts describe that foundational paper, not this folio.'
    ),
}

FOLIO = {
    'folio_id': 'E.13',
    'slug': 'e13',
    'pillar': 'engineering',
    'category_code': 'E',
    'parent_folios': ['E.01', 'E.05'],
    'lineage_mode': 'CONTINUATION · Continues E.01 Porous Continuum & E.05 Terzaghi Effective Stress',
    'title': 'Biot 3D Poroelasticity, Skempton Undrained Coupling & Mohr–Coulomb Fault Slip Margin in Geologic CO2 Storage',
    'subtitle': (
        "Continuing Folio E.01's porous percolation and E.05's 1D Terzaghi consolidation: an illustrative "
        'geomechanical study coupling Biot\'s 3D effective-stress coefficient α = 1 − K_d/K_s, Rice–Cleary '
        'Skempton pore-pressure response B, and cohesionless Mohr–Coulomb fault slip tendency τ/σ\'_n across '
        'sedimentary storage basins and critically stressed crystalline basement.'
    ),
    'date_published': '2026-11-20',
    'date_redated': '2026-11-20',
    'current_edition': 'REV 1.0',
    'status_badge': 'POROELASTIC GEOMECHANICS · REV 1.0',
    'primary_kernel': 'skills/engineering/e13/verify_e13_biot_poroelasticity.py',
    'governing_law': "α = 1 − K_d / K_s · Δp_u = +B Δσ_mean · |τ| / (σ_n − α_fault(p_0 + Δp_inj)) < μ_f",
    'colophon': {
        'identifier': 'E.13 · Biot Poroelasticity & Fault Slip Margin · REV 1.0',
        'kernels': 'Biot 3D Consolidation (1941) · Rice–Cleary Skempton B (1976) · Mohr–Coulomb Fault Slip Margin',
        'benchmarks': (
            'Model values (sedimentary k_0 = 0.72, Δp_inj = 4.5 MPa): α = 0.667 · B = 0.394 (brine) / 0.053 (CO2) · '
            "τ/σ'_n = 0.404 < 0.60 · Δp_crit = 9.40 MPa"
        ),
        'bridge': 'Continues E.01/E.05',
    },
    'sliders': [
        {
            'label': 'Injection Reservoir Overpressure (Δp_inj)',
            'min': 0.0,
            'max': 20.0,
            'step': 0.5,
            'value': 4.5,
            'unit': ' MPa',
        },
        {
            'label': 'Horizontal-to-Vertical Stress Ratio (k_0 = σ_h / σ_v)',
            'min': 0.56,
            'max': 1.20,
            'step': 0.02,
            'value': 0.72,
            'unit': 'k_0 = ',
        },
    ],
    'steps': [
        (
            "Stage 1 (Biot–Willis 3D Effective Stress, Continuing E.05): Whereas Terzaghi's 1D soil limit treats "
            'solid grains as incompressible (α → 1), stiff porous sandstone with drained bulk modulus K_d = 12.0 GPa '
            'and solid mineral grain modulus K_s = 36.0 GPa carries part of the hydrostatic stress in its grain skeleton, '
            'yielding α = 1 − K_d / K_s = 0.667 (Biot 1941, DOI 10.1063/1.1712886; Biot & Willis 1957, DOI 10.1115/1.4011606).'
        ),
        (
            'Stage 2 (Skempton Undrained Pore-Pressure Response B): Under compression-positive geomechanics '
            '(Δp_u = +B Δσ_mean), Skempton (1954, DOI 10.1680/geot.1954.4.4.143) and Rice & Cleary (1976, '
            'DOI 10.1029/RG014i002p00227) write B = (1/K_d − 1/K_s) / [1/K_d − 1/K_s + φ(1/K_f − 1/K_s)]. '
            'For φ = 0.20 and brine bulk modulus K_f = 2.2 GPa, B = 0.394; replacing brine with compressible '
            'supercritical CO2 (K_f = 0.20 GPa) lowers B to 0.053 in the folio model.'
        ),
        (
            'Stage 3 (Mohr–Coulomb Fault Slip Margin & Stress-Regime Contrast): On a cohesionless fault dipping 60° '
            '(fault-plane angle β = 30° from vertical σ_v, normal 30° from σ_h; σ_v = 50.0 MPa, hydrostatic p_0 = 20.0 MPa, '
            'μ_f = 0.60, α_fault = 1.0, and uncoupled total stress σ_h = k_0 σ_v), a sedimentary stress ratio k_0 = 0.72 gives σ_n = 39.50 MPa, '
            'τ = 6.062 MPa, and Δp_crit = 9.40 MPa; at Δp_inj = 4.5 MPa, slip tendency τ/σ\'_n = 0.404 stays below 0.60. '
            'In a critically stressed crystalline basement (k_0 = 0.60), Δp_crit drops to 0.57 MPa and Δp_inj = 4.5 MPa '
            'raises τ/σ\'_n to 0.825 (> 0.60).'
        ),
        (
            'Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in stiff '
            'porous sedimentary storage reservoirs where stress ratio k_0 keeps Δp_inj < Δp_crit and compressible '
            'supercritical CO2 lowers undrained B while keeping overpressure moderate (Vilarrasa & Carrera 2015, '
            'DOI 10.1073/pnas.1413284112), fault slip tendency remains below μ_f; this hypothesis is falsified in any '
            'site where pore pressure reaches critically stressed basement faults (Zoback & Gorelick 2012, '
            'DOI 10.1073/pnas.1202473109; Ellsworth 2013, DOI 10.1126/science.1225942), drives σ\'_n ≤ 0, or where '
            'coupled poroelastic stress transfer pushes |τ|/σ\'_n ≥ μ_f.'
        ),
    ],
    'readouts': [
        {'label': 'Biot α & Skempton B (Brine / CO2)', 'value': 'α = 0.667 · B = 0.394 / 0.053 (model)'},
        {'label': "Fault Slip Tendency (|τ| / σ'_n)", 'value': '0.404 < 0.60 (Δp_crit = 9.40 MPa, model)'},
        {'label': 'Shear & Hydraulic Margins', 'value': 'Slip +4.90 MPa · Tensile +11.50 MPa (model)'},
        {'label': 'Mohr–Coulomb Fault Status', 'value': 'BELOW SLIP THRESHOLD (model, uncoupled σ_h)'},
    ],
    'spec_plate': {
        'division': 'SUBSURFACE GEOMECHANICS / CSI 31 00 00 (FILING LABEL · DESIGN STUDY)',
        'title': 'Deep Saline Aquifer CO2 Storage Reservoir & Caprock Pressure-Management Envelope',
        'body': (
            'Illustrative geomechanical screening study, not a site-specific reservoir permit or injection design: '
            'tracks Biot matrix coupling (α = 0.667, passive lateral stress-path index η_poro = 0.444), cohesionless '
            'Mohr–Coulomb fault slip tendency (α_fault = 1.0, μ_f = 0.60, holding σ_h = k_0 σ_v uncoupled from '
            'Δp_inj), and minimum-principal-stress hydraulic fracture margin (min(σ_v, σ_h) − p_0 − Δp_inj = 11.50 MPa '
            'at defaults). Field characterization and coupled 3D multiphase flow-geomechanics modeling are required for '
            'any real injection project.'
        ),
        'meta': (
            'Primary anchors: Biot 1941 (DOI 10.1063/1.1712886) · Rice & Cleary 1976 (DOI 10.1029/RG014i002p00227) · '
            'Zoback & Gorelick 2012 (DOI 10.1073/pnas.1202473109) · Vilarrasa & Carrera 2015 (DOI 10.1073/pnas.1413284112) · '
            'Model values, not field measurements'
        ),
    },
    'sidenote_1': {
        'kicker': 'SIDENOTE E.13-A · OPEN SCIENTIFIC DEBATE · SEDIMENTARY RESERVOIRS VS. BASEMENT FAULTS',
        'body': (
            'Zoback & Gorelick (2012, DOI 10.1073/pnas.1202473109) warned that large-scale geologic carbon dioxide '
            'injection into brittle continental-interior rocks carries a substantial probability of triggering small-to-moderate '
            'earthquakes that could threaten caprock seal integrity. Vilarrasa & Carrera (2015, DOI 10.1073/pnas.1413284112; '
            'reply DOI 10.1073/pnas.1511302112) countered that soft sedimentary basins are less critically stressed than '
            'crystalline basement, while brine displacement and dissolution limit overpressure. Ellsworth (2013, '
            'DOI 10.1126/science.1225942) documented how deep wastewater injection near basement faults drove midcontinent '
            'seismicity, showing why basal fault proximity governs operational risk.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE E.13-B · MATRIX α, FAULT α_fault & UNCOUPLED TOTAL-STRESS CAVEAT',
        'body': (
            'Intact porous sandstone shares load across mineral grain contacts (α = 1 − K_d/K_s = 0.667), giving a lateral '
            'poroelastic stress-path index η_poro = α(1 − 2ν)/(1 − ν) = 0.444 at ν = 0.25. Along a damaged or open fault '
            'surface, conservative Mohr–Coulomb screening uses α_fault = 1.0 consistently in both σ\'_n = σ_n − α_fault(p_0 + Δp_inj) '
            'and Δp_crit. In this reduced closed-form model, η_poro is reported passively while total horizontal stress '
            'remains uncoupled at σ_h = k_0 σ_v rather than adding η_poro Δp_inj.'
        ),
    },
    'skill': {
        'filename': 'biot-poroelasticity-fault-slip-SKILL.md',
        'name': 'biot-poroelasticity-fault-slip',
        'description': (
            'AI-agnostic civil geomechanics skill for Biot 3D poroelasticity (alpha = 1 - K_d/K_s), '
            'Rice-Cleary Skempton B coupling, and cohesionless Mohr-Coulomb fault slip margin under subsurface fluid injection.'
        ),
        'rules': [
            (
                'Compute intact-matrix Biot-Willis coefficient alpha = 1 - K_d / K_s (requiring 0 < K_d < K_s) and '
                'Skempton undrained coefficient B = (1/K_d - 1/K_s) / [1/K_d - 1/K_s + phi*(1/K_f - 1/K_s)] under '
                'compression-positive sign convention delta_p_u = +B * delta_sigma_mean.'
            ),
            (
                'Keep fault-plane Terzaghi effective stress alpha_fault = 1.0 distinct from matrix alpha, and apply '
                'alpha_fault consistently in both sigma_n_eff = sigma_n - alpha_fault*(p_0 + delta_p_inj) and '
                'critical_delta_p = (sigma_n - |tau|/mu_f)/alpha_fault - p_0; state explicitly when total stress sigma_h '
                'is held uncoupled from eta_poro * delta_p_inj.'
            ),
            (
                'Check both shear slip tendency |tau| / sigma_n_eff < mu_f and tensile hydraulic margin '
                'min(sigma_v, sigma_h) - (p_0 + delta_p_inj) > 0; treat sigma_n_eff <= 0 explicitly as tensile failure '
                'with undefined shear slip tendency.'
            ),
            (
                'Frame injection stability as a site-dependent Tier T1-T2 hypothesis bounded by stress ratio k_0 and '
                'basement fault proximity; never extrapolate closed-form screening outputs into site-specific permit claims.'
            ),
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.0',
            'date': '2026-11-20',
            'summary': (
                'REV 1.0 (Published 2026-11-20): Volume VII Civil & Geomechanical Engineering monograph continuing '
                'Folios E.01 & E.05 via Biot 3D poroelasticity (1941), Skempton & Rice–Cleary undrained pore-pressure '
                'coupling (1954, 1976), and Mohr–Coulomb fault slip stability across the Zoback–Gorelick (2012) vs. '
                'Vilarrasa–Carrera (2015) geologic CO2 storage debate.'
            ),
            'opus': (
                'Verification note: all eight DOIs in this folio were checked against Crossref and the Scite index on '
                '2026-11-20 with zero retraction notices; all numerical outputs are recomputed offline by '
                'skills/engineering/e13/verify_e13_biot_poroelasticity.py and represent illustrative closed-form model '
                'outputs under uncoupled total horizontal stress rather than field measurements.'
            ),
        }
    ],
    'volume': 7,
    'volume_code': 'VOL. 07',
    'reading_time': '22 MIN READ',
    'word_count': '4,700 WORDS',
    'scite': dict(_SCITE),
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,700 WORDS',
    'parent_folios': ['E.01', 'E.05'],
    'lineage_mode': 'CONTINUATION · Continues E.01 Porous Continuum & E.05 Terzaghi Effective Stress',
    'scite': dict(_SCITE),
    'act1_title': 'Act I — Cool Fact & Human Story: Why Rock Grains Share the Load When Fluid Is Pumped Underground',
    'act1_dropcap': (
        'In 1925, Karl Terzaghi explained how a saturated clay settles by assuming that every mineral grain and every '
        'drop of pore water is completely rigid, so fluid carries all of a sudden load before slowly draining away '
        '(Folio E.05). Sixteen years later, in 1941, the Belgian-American applied physicist Maurice Anthony Biot asked '
        'what happens in three dimensions when the porous rock skeleton itself is stiff—like deep sandstone—and both the '
        'solid mineral grains and the pore fluid compress under stress (Journal of Applied Physics, DOI 10.1063/1.1712886). '
        'Biot wrote down a linear three-dimensional theory of consolidation in which fluid pressure and solid elastic '
        'strain are two halves of one coupled system. In 1954, Alec Skempton measured how much undrained pore pressure '
        'jumps when confining stress rises on soils and rocks (Géotechnique, DOI 10.1680/geot.1954.4.4.143), and in 1957 '
        'Biot and Willis identified the measurable elastic coefficients linking bulk rock stiffness K_d to solid grain '
        'stiffness K_s (Journal of Applied Mechanics, DOI 10.1115/1.4011606). Today, that century-old mathematical '
        'framework sits at the center of one of civil and geo-environmental engineering\'s sharpest debates: can '
        'compressed carbon dioxide be injected two kilometers underground for decades without waking dormant faults?'
    ),
    'act1_plain_bridge': (
        'In plain words, deep underground rock is not a hollow tank; it is more like a hard, wet sandstone sponge '
        'pressed down by two kilometers of rock above it. When engineers pump compressed carbon dioxide or wastewater '
        'into the microscopic pores of that sponge, the rising fluid pressure pushes outward against the grains and '
        'slightly pries apart any crack or fault cutting through the rock. At the same time, the weight of the rock '
        'still presses those fault faces together through friction. If the rock is soft enough and the pressure is kept '
        'gentle, friction holds and the fault stays quiet. If the pressure reaches a nearby brittle fault that is already '
        'close to its breaking point, the drop in clamping force can let the fault slip and produce an earthquake. This '
        'folio walks through the exact balance between rock compressibility, fluid compressibility, and fault friction, '
        'using an illustrative closed-form model rather than a site measurement.'
    ),
    'act1_body': (
        'Two decades after Biot and Willis (1957), James R. Rice and Michael P. Cleary reformulated linear poroelasticity '
        'in terms of drained and undrained Poisson ratios, fluid bulk modulus K_f, and Skempton\'s pore-pressure '
        'coefficient B (Reviews of Geophysics, 1976, DOI 10.1029/RG014i002p00227). Their formulation clarifies why the '
        'phase of the pore fluid itself changes the mechanical coupling: in a sandstone with drained bulk modulus '
        'K_d = 12.0 GPa, solid quartz grain modulus K_s = 36.0 GPa, and porosity φ = 0.20, the Biot–Willis coefficient is '
        'α = 1 − K_d / K_s = 0.667. When the pores hold saline brine (K_f = 2.2 GPa), Skempton\'s coefficient is B = 0.394, '
        'meaning an undrained increase in mean compressive stress Δσ_mean raises pore pressure by Δp_u = +0.394 Δσ_mean. '
        'When compressible supercritical carbon dioxide (K_f = 0.20 GPa) displaces brine in the model, B drops to 0.053. '
        'Meanwhile, along an open or damaged fault cutting the reservoir or underlying crystalline rock, conservative '
        'Mohr–Coulomb stability screening sets the fault effective-stress coefficient to the Terzaghi limit α_fault = 1.0, '
        'distinct from the intact rock-matrix value α = 0.667.'
    ),
    'act1_stakes': (
        'The stakes of poroelastic fault mechanics span both industrial decarbonization and seismic hazard. In 2012, '
        'Mark D. Zoback and Steven M. Gorelick argued in PNAS (DOI 10.1073/pnas.1202473109) that large-volume CO2 '
        'injection into brittle continental interiors carries a high likelihood of triggering small-to-moderate '
        'earthquakes that could breach overlying caprock seals. In 2013, William L. Ellsworth documented in Science '
        '(DOI 10.1126/science.1225942) how deep wastewater disposal in Oklahoma and other midcontinent basins elevated '
        'pore pressure along critically stressed crystalline basement faults, shifting regional earthquake rates. In '
        '2015, Víctor Vilarrasa and Jesús Carrera countered in PNAS (DOI 10.1073/pnas.1413284112; reply DOI '
        '10.1073/pnas.1511302112) that soft sedimentary aquifers have higher stress ratios k_0 and lower stiffness '
        'than crystalline basement, while low CO2 viscosity and brine migration restrain pressure buildup near the '
        'wellbore. Separating where those two regimes meet—in a quantitative, falsifiable screening model—is the goal '
        'of this folio.'
    ),
    'pullquote': (
        '"Rock grains carry part of the load inside an intact sandstone matrix (α = 0.667), yet an open fault plane '
        'feels nearly the full fluid pressure (α_fault = 1.0)—and that contrast separates a quiet sedimentary basin '
        'from a critically stressed basement fault."'
    ),
    'chronology': [
        (
            '1941',
            'Maurice A. Biot publishes the general three-dimensional theory of consolidation coupling elastic skeleton '
            'deformation and pore-fluid diffusion (Journal of Applied Physics, DOI 10.1063/1.1712886).'
        ),
        (
            '1954',
            'Alec W. Skempton introduces the pore-pressure coefficients A and B relating undrained pore-pressure '
            'increments to total stress changes (Géotechnique, DOI 10.1680/geot.1954.4.4.143).'
        ),
        (
            '1957',
            'Biot and D. G. Willis map the theoretical consolidation moduli onto measurable drained, unjacketed, and '
            'fluid compressibility constants, defining α = 1 − K_d / K_s (Journal of Applied Mechanics, DOI 10.1115/1.4011606).'
        ),
        (
            '1976',
            'James R. Rice and Michael P. Cleary publish exact stress-diffusion solutions and express Skempton B in '
            'terms of constituent compressibilities K_d, K_s, and K_f (Reviews of Geophysics, DOI 10.1029/RG014i002p00227).'
        ),
        (
            '2012–2013',
            'Zoback & Gorelick (DOI 10.1073/pnas.1202473109) warn of injection-triggered fault slip in CO2 storage, '
            'while Ellsworth (DOI 10.1126/science.1225942) reviews wastewater-injection seismicity on basement faults.'
        ),
        (
            '2015',
            'Vilarrasa & Carrera (DOI 10.1073/pnas.1413284112; reply DOI 10.1073/pnas.1511302112) argue that soft '
            'sedimentary storage formations remain less critically stressed and experience lower overpressure than basement rock.'
        ),
    ],
    'act2_title': 'Act II — Cross-Field Intuition: Sandstone Sponges, Fluid Cushions & Fault Clamping',
    'act2_analogy': (
        'Everyday analogy: Picture pressing down on two sponges locked inside a vise—one stiff ceramic-foam block '
        'filled with water and one filled with carbonated soda gas—while a slanted wooden joint inside the block is '
        'held shut only by friction. When you pump extra pressure into the pores, the fluid pushes outward on the '
        'slanted joint. If the vise squeezes tightly from the sides (high horizontal stress ratio k_0), the joint '
        'resists sliding even under several megapascals of injection pressure; if the side vise is slack (low k_0 in '
        'critically stressed basement), a tiny pressure rise lets the joint slip.'
    ),
    'act2_plain_primer': (
        'Our interactive geomechanics laboratory exposes two primary parameters from the screening model. The first '
        'slider is Injection Reservoir Overpressure (Δp_inj, from 0.0 to 20.0 MPa), which adds fluid pressure above '
        'the ambient 20.0 MPa hydrostatic baseline at roughly 2 km depth. Raising Δp_inj lowers the effective normal '
        'stress σ\'_n clamping a 60°-dipping cohesionless fault and reduces the tensile hydraulic fracture margin '
        'against the minimum principal stress min(σ_v, σ_h). The second slider is the Horizontal-to-Vertical Stress '
        'Ratio (k_0 = σ_h / σ_v, from 0.56 to 1.20), which sets how tightly the crust squeezes horizontally relative to '
        'the 50.0 MPa vertical overburden. Dragging k_0 down toward 0.60 models a critically stressed basement fault '
        'where critical overpressure Δp_crit collapses from 9.40 MPa to 0.57 MPa; dragging k_0 above 1.0 enters a '
        'reverse-faulting regime where vertical overburden σ_v becomes the minimum principal stress.'
    ),
    'distill_diagram': {
        'analogy_title': 'Saturated Sandstone Sponge & Clamped Fault',
        'analogy_sub': 'Grain-skeleton stiffness shares total load while pore pressure reduces fault clamping',
        'force_a_title': 'Injection Overpressure (Δp_inj)',
        'force_a_sub': 'Raises pore pressure p = p_0 + Δp_inj, lowering effective normal stress σ\'_n on faults',
        'force_b_title': 'Horizontal Stress Ratio (k_0)',
        'force_b_sub': 'Sets lateral clamping σ_h = k_0 σ_v and ambient shear demand τ on dipping faults',
        'threshold_title': 'Mohr–Coulomb Slip & Tensile Boundaries',
        'threshold_pass': 'Model below slip: |τ|/σ\'_n < 0.60 and min(σ_v, σ_h) > p_0 + Δp_inj',
        'threshold_fail': 'Slip or tensile breach: |τ|/σ\'_n ≥ 0.60 or σ\'_n ≤ 0 (hydraulic opening)',
    },
    'act2_intuition': (
        'In Biot\'s isotropic 3D poroelasticity, the intact sandstone matrix shares hydrostatic stress between mineral '
        'grains and pore fluid via α = 1 − K_d / K_s = 1 − 12/36 = 0.667. Under undrained loading (Δp_u = +B Δσ_mean, '
        'compression-positive), Rice & Cleary (1976) express Skempton\'s coefficient as B = (1/K_d − 1/K_s) / '
        '[1/K_d − 1/K_s + φ(1/K_f − 1/K_s)], giving B = 0.394 for brine (K_f = 2.2 GPa) and B = 0.053 for supercritical '
        'CO2 (K_f = 0.20 GPa) at φ = 0.20. On a cohesionless fault dipping 60° (fault-plane angle β = 30° from vertical '
        'σ_v = 50.0 MPa, p_0 = 20.0 MPa, friction μ_f = 0.60), resolving the 2D stress tensor with uncoupled total '
        'horizontal stress σ_h = k_0 σ_v gives σ_n = ½(σ_v + σ_h) − ½(σ_v − σ_h)cos(2β) and |τ| = |½(σ_v − σ_h)sin(2β)|. '
        'Applying Terzaghi\'s open-fault effective stress (α_fault = 1.0) yields σ\'_n = σ_n − α_fault(p_0 + Δp_inj) '
        'and critical overpressure Δp_crit = (σ_n − |τ|/μ_f)/α_fault − p_0. Notice the modeling boundary: the lateral '
        'poroelastic stress-path index η_poro = α(1 − 2ν)/(1 − ν) = 0.444 is reported passively, while σ_h = k_0 σ_v '
        'is held uncoupled from Δp_inj.'
    ),
    'act2_deepening': (
        'Separating intact-matrix Biot coupling α from fault-plane Terzaghi effective stress α_fault = 1.0 prevents '
        'a subtle physical error. If an analyst mistakenly substitutes matrix α = 0.667 into the fault-plane normal '
        'stress σ\'_n = σ_n − α(p_0 + Δp_inj), the model artificially cushions the fault by 33% of pore pressure, '
        'inflating the predicted critical overpressure at k_0 = 0.72 from 9.40 MPa to 24.09 MPa and masking real slip '
        'risk in critically stressed basement (where k_0 = 0.60 actually fails at Δp_crit = 0.57 MPa, not 10.85 MPa). '
        'At the same time, omitting poroelastic total-stress buildup η_poro Δp_inj in σ_h makes this closed-form '
        'screening tool conservative on normal-faulting clamping during injection, while reminding practitioners that '
        'real reservoir design requires coupled 3D multiphase flow and geomechanics simulation. In reverse-faulting '
        'regimes (k_0 > 1.0), horizontal stress exceeds vertical overburden, so min(σ_v, σ_h) switches to σ_v = 50.0 MPa '
        'for hydraulic fracture screening and |τ| remains non-negative via the absolute value of ½(σ_v − σ_h)sin(2β).'
    ),
    'walkthrough': [
        (
            'Experiment 1 (Sedimentary Storage Margin vs. Overpressure Δp_inj): Keep k_0 = 0.72 and sweep Δp_inj from '
            '4.5 MPa upward past 9.40 MPa. Watch fault slip tendency |τ|/σ\'_n climb from 0.404 past the μ_f = 0.60 '
            'threshold at Δp_crit = 9.40 MPa, then cross into hydraulic tensile opening (σ\'_n ≤ 0) above 19.50 MPa '
            'or σ_h − p = 0 at Δp_inj = 16.0 MPa.'
        ),
        (
            'Experiment 2 (Critically Stressed Basement k_0 = 0.60): Return Δp_inj to 4.5 MPa and drag k_0 down from '
            '0.72 to 0.60. Observe how Δp_crit collapses from 9.40 MPa to 0.57 MPa and slip tendency jumps to 0.825 '
            '(above 0.60), reproducing the Zoback & Gorelick / Ellsworth sensitivity to critically stressed basement faults.'
        ),
        (
            'Experiment 3 (Reverse-Faulting Regime k_0 > 1.0 & Overlays): Drag k_0 above 1.00 toward 1.20 to inspect '
            'the thrust-faulting regime where σ_3 = min(σ_v, σ_h) switches to σ_v = 50.0 MPa, and toggle the 4-Lens '
            'Observatory tabs (3D Surface, Phase Portraits, Kirchhoff Ribbon, Polar Radar) to inspect parameter margins.'
        ),
    ],
    'act4_title': 'Act IV — Imagining Humanity\'s Future: Falsifiable Subsurface Screening & Open Geomechanics',
    'act4_human_ai': (
        'Geologic carbon storage and geothermal reservoirs sit beneath the soil and cities where people live and draw '
        'groundwater. Making subsurface pressure-management math transparent—separating what intact rock grains carry '
        '(α = 0.667), how pore-fluid compressibility modulates undrained response (B = 0.394 for brine vs. 0.053 for '
        'supercritical CO2), and when a fault reaches friction μ_f—allows civil engineers, regulators, and AI '
        'verification scripts to inspect assumptions line by line before a borehole is drilled. This folio states an '
        'open, site-dependent Tier T1–T2 hypothesis rather than a blanket promise of safety.'
    ),
    'act4_deepening': (
        'In the Zoback & Gorelick (2012) versus Vilarrasa & Carrera (2015) exchange, both sides rely on the same Biot '
        'and Mohr–Coulomb physics; they disagree on which geological parameters dominate at continental scale. Under '
        'the Tier T1–T2 hypothesis stated here, stiff porous sedimentary reservoirs with moderate horizontal stress '
        'ratios (k_0 = 0.72) and modest injection overpressure (Δp_inj < Δp_crit = 9.40 MPa) remain below Mohr–Coulomb '
        'slip, aided by supercritical CO2\'s low Skempton coupling (B = 0.053). That hypothesis is explicitly falsified '
        'in any site where pore-pressure plumes migrate downward into critically stressed basement faults (k_0 ≤ 0.60, '
        'where Δp_crit ≤ 0.57 MPa or negative pre-injection), where total pore pressure breaches min(σ_v, σ_h) in '
        'tensile fracture, or where coupled poroelastic shear transfer drives |τ|/σ\'_n ≥ μ_f. Pairing open Python '
        'verifiers with explicit negative controls ensures that screening models never hide these failure boundaries.'
    ),
    'cf_bridge': 'Continues E.01/E.05',
    'sources': [
        (
            'Biot, M. A. (1941). General Theory of Three-Dimensional Consolidation. Journal of Applied Physics, 12(2), '
            '155–164. DOI: 10.1063/1.1712886.'
        ),
        (
            'Skempton, A. W. (1954). The Pore-Pressure Coefficients A and B. Géotechnique, 4(4), 143–147. '
            'DOI: 10.1680/geot.1954.4.4.143.'
        ),
        (
            'Biot, M. A., & Willis, D. G. (1957). The Elastic Coefficients of the Theory of Consolidation. Journal of '
            'Applied Mechanics, 24(4), 594–601. DOI: 10.1115/1.4011606.'
        ),
        (
            'Rice, J. R., & Cleary, M. P. (1976). Some basic stress diffusion solutions for fluid-saturated elastic '
            'porous media with compressible constituents. Reviews of Geophysics, 14(2), 227–241. '
            'DOI: 10.1029/RG014i002p00227.'
        ),
        (
            'Zoback, M. D., & Gorelick, S. M. (2012). Earthquake triggering and large-scale geologic storage of carbon '
            'dioxide. Proceedings of the National Academy of Sciences, 109(26), 10164–10168. '
            'DOI: 10.1073/pnas.1202473109.'
        ),
        (
            'Ellsworth, W. L. (2013). Injection-Induced Earthquakes. Science, 341(6142), 1225942. '
            'DOI: 10.1126/science.1225942.'
        ),
        (
            'Vilarrasa, V., & Carrera, J. (2015). Geologic carbon storage is unlikely to trigger large earthquakes and '
            'reactivate faults through which CO2 could leak. Proceedings of the National Academy of Sciences, 112(19), '
            '5938–5943. DOI: 10.1073/pnas.1413284112.'
        ),
        (
            'Vilarrasa, V., & Carrera, J. (2015). Reply to Zoback and Gorelick: Geologic carbon storage remains a safe '
            'strategy to significantly reduce CO2 emissions. Proceedings of the National Academy of Sciences, 112(30), '
            'E3980. DOI: 10.1073/pnas.1511302112.'
        ),
        (
            'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and '
            'classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), '
            '882–898. DOI: 10.1162/qss_a_00146.'
        ),
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Mohr-Coulomb fault slip envelope, '
        'Biot matrix coupling alpha = 0.667 vs fault alpha_fault = 1.0, and sedimentary vs crystalline basement critical overpressure">\n'
        '            <line x1="40" y1="184" x2="340" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <line x1="40" y1="30" x2="40" y2="184" stroke="currentColor" stroke-opacity="0.35"/>\n'
        '            <text x="46" y="22" font-size="10.5" font-weight="600" fill="currentColor">Mohr–Coulomb Failure Envelope (μ_f = 0.60)</text>\n'
        '            <line x1="40" y1="184" x2="213" y2="30" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,3"/>\n'
        '            <path d="M 114 184 A 45 67 0 0 1 204 184" fill="var(--tp-verdigris)" fill-opacity="0.14" stroke="var(--tp-prussian)" stroke-width="2.4"/>\n'
        '            <circle id="tp-svg-eng-point" cx="136" cy="126" r="6" fill="var(--tp-verdigris)"/>\n'
        '            <text x="155" y="48" font-size="9" fill="var(--tp-minium)">|τ| = μ_f σ\'_n</text>\n'
        '            <text x="108" y="172" font-size="9" fill="var(--tp-prussian)">Sedimentary k_0 = 0.72 (Δp_crit = 9.40 MPa)</text>\n'
        '            <line x1="365" y1="24" x2="365" y2="192" stroke="currentColor" stroke-opacity="0.2"/>\n'
        '            <text x="382" y="22" font-size="10.5" font-weight="600" fill="currentColor">Skempton B &amp; Regime Contrast</text>\n'
        '            <rect x="384" y="42" width="256" height="58" rx="6" fill="var(--tp-stone)" fill-opacity="0.28" stroke="var(--tp-prussian)" stroke-width="1.6"/>\n'
        '            <text x="398" y="64" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">Matrix α = 0.667 · Fault α_fault = 1.0</text>\n'
        '            <text x="398" y="84" font-size="9" fill="var(--tp-verdigris)">Skempton B: 0.394 (Brine) vs 0.053 (CO2)</text>\n'
        '            <rect x="384" y="114" width="256" height="56" rx="6" fill="var(--tp-verdigris)" fill-opacity="0.12" stroke="var(--tp-verdigris)" stroke-width="1.4"/>\n'
        '            <text x="398" y="136" font-size="9.5" font-weight="600" fill="var(--tp-prussian)">Basement k_0 = 0.60 → Δp_crit = 0.57 MPa</text>\n'
        '            <text x="398" y="156" font-size="9" fill="var(--tp-minium)">At Δp_inj = 4.5 MPa: τ/σ\'_n = 0.825 &gt; 0.60</text>\n'
        '            <text x="40" y="206" font-size="10" fill="var(--tp-verdigris)">Closed-form model (uncoupled σ_h = k_0 σ_v) · Recomputed by verify_e13_biot_poroelasticity.py</text>\n'
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a deep geological CO2 storage cross-section with stratified limestone '
        'overburden, an arching low-permeability caprock seal, a porous sandstone reservoir with diffusing fluid plume '
        'around a vertical wellbore, and a 60-degree dipping basement fault would look like (artistic impression, not '
        'a measured structure or specification)'
    ),
    'caption': (
        'Conceptual Vision Plate E.13-V (Imagining What It Would Look Like) · Artistic geological cutaway imagining '
        'an intact arching caprock over a porous sandstone storage reservoir and a dipping crystalline basement fault. '
        'Exact geometry, specifications, and governing equations are kept strictly intact in deterministic Plate E.13-A '
        'and Plate E.13-B below.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER GEOMECHANICS DISPATCH · POROELASTICITY & INDUCED SEISMICITY',
    'headline': 'Biot 3D Poroelasticity, Skempton Fluid Contrast & the Sedimentary-vs-Basement Fault Debate',
    'body': (
        'Whether large-scale CO2 storage reactivates faults hinges on stress regime and fluid compressibility: '
        'Zoback & Gorelick (2012, DOI 10.1073/pnas.1202473109) and Ellsworth (2013, DOI 10.1126/science.1225942) '
        'highlight critically stressed basement faults (Δp_crit = 0.57 MPa at k_0 = 0.60 in this model), whereas '
        'Vilarrasa & Carrera (2015, DOI 10.1073/pnas.1413284112) emphasize softer sedimentary basins (Δp_crit = 9.40 MPa '
        'at k_0 = 0.72) and low-viscosity CO2 behavior (B = 0.053 vs. 0.394 brine).'
    ),
}

META_3D = (
    'Biot 3D Poroelasticity & Mohr–Coulomb Fault Slip Surface',
    'X: Overpressure Δp_inj (MPa) · Z: Stress Ratio k_0 · Y: Slip Margin Δp_crit − Δp_inj',
)

ES_TRANSLATION = {
    'title_es': 'Poroelasticidad 3D de Biot, Acoplamiento de Skempton y Margen de Deslizamiento de Fallas en Almacenamiento de CO2',
    'subtitle_es': (
        'Continuación de los Folios E.01 y E.05: estudio geomecánico ilustrativo que acopla el coeficiente de Biot '
        'α = 1 − K_d/K_s, la respuesta no drenada de Skempton B de Rice–Cleary y la tendencia de deslizamiento de Mohr–Coulomb '
        'entre cuencas sedimentarias y basamento cristalino.'
    ),
    'why_es': (
        'Como una esponja rígida de piedra prensada bajo dos kilómetros de roca, un yacimiento profundo reparte el peso '
        'entre sus granos y el fluido de sus poros; mantener la presión de inyección bajo el umbral de fricción evita '
        'deslizar fallas en el modelo del folio.'
    ),
    'plain_es': (
        'En palabras sencillas, la roca profunda del subsuelo no es un tanque hueco, sino una esponja dura de arenisca '
        'aplastada por kilómetros de estratos encima. Cuando los ingenieros inyectan dióxido de carbono comprimido o agua '
        'en sus poros microscópicos, la presión del fluido empuja hacia afuera y reduce la fuerza que mantiene apretadas '
        'las fallas geológicas. Mientras la fricción lateral (razón de esfuerzos k_0) supere ese empuje, la falla '
        'permanece estable en el modelo; si la presión alcanza una falla frágil ya cercana a su límite, la fricción puede '
        'ceder y disparar microsismos.'
    ),
    'deep_es': (
        'En la poroelasticidad isotrópica de Biot (1941, DOI 10.1063/1.1712886; Biot y Willis 1957, DOI 10.1115/1.4011606), '
        'una arenisca porosa con módulo drenado K_d = 12.0 GPa y módulo mineral K_s = 36.0 GPa tiene coeficiente α = 0.667. '
        'Bajo la formulación de Rice y Cleary (1976, DOI 10.1029/RG014i002p00227) y Skempton (1954, DOI 10.1680/geot.1954.4.4.143) '
        'con convención positiva en compresión (Δp_u = +B Δσ_mean), la porosidad φ = 0.20 y salmuera (K_f = 2.2 GPa) '
        'dan B = 0.394, mientras que CO2 supercrítico (K_f = 0.20 GPa) reduce B a 0.053. En una falla sin cohesión con '
        'α_fault = 1.0 y fricción μ_f = 0.60, una cuenca sedimentaria (k_0 = 0.72) soporta Δp_crit = 9.40 MPa (τ/σ\'_n = 0.404 '
        'a Δp_inj = 4.5 MPa), en tanto que un basamento críticamente esforzado (k_0 = 0.60) cae a Δp_crit = 0.57 MPa '
        '(τ/σ\'_n = 0.825). El modelo reporta η_poro = 0.444 de forma pasiva y mantiene σ_h = k_0 σ_v desacoplado de Δp_inj. '
        'La hipótesis de nivel T1–T2 de estabilidad sedimentaria queda falsada si la sobrepresión alcanza fallas de basamento '
        '(Zoback y Gorelick 2012, DOI 10.1073/pnas.1202473109; Ellsworth 2013, DOI 10.1126/science.1225942), si σ\'_n ≤ 0 '
        'o si el acoplamiento poroelástico completo eleva |τ|/σ\'_n ≥ μ_f.'
    ),
    'bridge_es': (
        'El contraste entre el coeficiente de matriz intacta α = 0.667 y el límite de Terzaghi en falla abierta α_fault = 1.0 '
        'separa los márgenes de almacenamiento sedimentario del deslizamiento en basamento críticamente esforzado (modelo ilustrativo).'
    ),
}
