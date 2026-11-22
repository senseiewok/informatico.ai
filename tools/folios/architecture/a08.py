#!/usr/bin/env python3
"""Folio A.08 (ARCHITECTURE): AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan Phase-Change Envelopes."""
from __future__ import annotations

SLUG = 'a08'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.08',
 'slug': 'a08',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'AI-Designed Daytime Radiative Sky-Cooling Photonic Roofs (8–13 μm Window) & Stefan '
          'Phase-Change Envelopes',
 'subtitle': 'A building-physics model pairing daytime radiative sky cooling across the 8–13 μm '
             'atmospheric window (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, '
             'DOI 10.1126/science.aat9513) with a proposed Stefan phase-change ceiling buffer '
             '(Carslaw & Jaeger 1959; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019).',
 'date_published': '2026-11-02',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'PHOTONIC ENVELOPES · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'P_net = P_rad(T) − P_atm(T_a) − (1 − R_sol)I_sol − h_c(T_a − T) · s(t) = '
                  '2λ_s√(α t) · CSI 07 54 00',
 'colophon': {'identifier': 'A.08 · Photonic Sky-Cooling & Stefan PCM · CSI 07 54 00',
              'kernels': 'Planck 8–13 μm Sky Window · Stefan Moving-Boundary PCM Storage',
              'benchmarks': 'Model values: R_solar = 97.0% · ε_LWIR = 95.0% · P_net = +86.4 W/m² (−6.2 °C)',
              'bridge': 'Passive Sub-Ambient Sky Cooling ↔ Cooler Storage Rooms (Open Question, Not Medical Cold Storage)'},
 'sliders': [{'label': 'Solar Waveband Reflectance (R_solar)',
              'min': 0.85,
              'max': 0.99,
              'step': 0.005,
              'value': 0.97,
              'unit': 'R = '},
             {'label': '8–13 μm Sky-Window Emissivity (ε_LWIR)',
              'min': 0.65,
              'max': 0.99,
              'step': 0.01,
              'value': 0.95,
              'unit': 'ε = '}],
 'steps': ['Stage 1 (Solar Reflection, 0.3–2.5 μm): In the model the roof reflects 97.0% of an assumed 1,000 W/m² of midday sunlight, absorbing (1 − 0.97) × 1,000 = 30 W/m² (Raman et al. 2014, DOI 10.1038/nature13883, report about 97% solar reflection).',
           'Stage 2 (Emission in the 8–13 μm Window): Through the 8–13 μm atmospheric transparency window (Catalanotti et al. 1975, DOI 10.1016/0038-092X(75)90062-6; Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270), the model assigns an illustrative net radiative sky exchange of about 116.4 W/m² at air temperature.',
           'Stage 3 (Sub-Ambient Equilibrium Below Air Temperature): Net cooling power is P_net = 116.4 − 30 = +86.4 W/m². Dividing by an assumed combined heat-exchange coefficient of about 13.9 W/(m²·K) gives a model roof surface about 6.2 °C below outdoor air under the stated assumptions (Raman et al. 2014, DOI 10.1038/nature13883, measured about 4.9 °C and 40.1 W/m²).',
           'Stage 4 (Stefan Phase-Change Thermal Ceiling Buffer): A proposed 21 °C PCM ceiling panel could absorb indoor heat along a moving melting front s(t) = 2λ_s√(α t) (Carslaw & Jaeger 1959; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019). The panel is an untested design proposal and was not sized here.'],
 'readouts': [{'label': 'Absorbed Solar Flux (P_sun)', 'value': '30.0 W/m² (R_sol = 97.0%)'},
              {'label': 'Net Sky Cooling Power (P_net, Model)', 'value': '+86.4 W/m² (Noon Sun, Model)'},
              {'label': 'Sub-Ambient Temp Drop (ΔT_sub, Model)', 'value': '−6.2 °C Below Ambient (Model)'},
              {'label': 'Model Check', 'value': 'NET COOLING IN MODEL (P_net > 0)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 07 54 00 / 07 21 00',
                'title': 'Microporous PVDF-HFP Radiative Sky-Cooling Membrane & Bio-PCM Thermal '
                         'Ceiling',
                'body': 'Untested design proposal: a hierarchically porous poly(vinylidene fluoride-co-hexafluoropropylene) cool-roof coating of the kind reported by Mandal et al. (2018, DOI 10.1126/science.aat9513), with assumed R_solar = 0.97 and ε_8-13um = 0.95, paired with 21 °C PCM ceiling cassettes (Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019).',
                'meta': 'References: Raman et al. 2014 (DOI 10.1038/nature13883); Granqvist & Hjortsberg 1981 (DOI 10.1063/1.329270) · Model estimates, not measurements · ASTM E1980 defines solar reflectance index; none was calculated here'},
 'sidenote_1': {'kicker': 'SIDENOTE A.08-A · VISIBLE STRUCTURAL COLOR WITHOUT SOLAR HEATING',
                'body': 'A white roof can glare. Chen et al. (2020, DOI 10.1126/sciadv.aaz5413) report paintable bilayer coatings in which a thin top layer absorbs narrowly for visible color while a scattering underlayer reflects near-infrared sunlight. Because visible absorption adds solar heat, colored roofs may cool less than white ones; this folio models white-limit assumptions only.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.08-B · SPECIFICATION PLATE · CSI 07 54 00 / STEFAN NUMBER',
                'body': 'Illustrative storage estimate: about 7.2 kg/m² of PCM with latent heat L_f = 210 kJ/kg stores 1,512 kJ/m² (420 Wh/m²), assuming about half of an 18 mm panel is PCM and Stefan number Ste = c_p ΔT / L_f = 0.085 (Carslaw & Jaeger 1959; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019). No chiller-demand estimate is computed here.'},
 'skill': {'filename': 'radiative-sky-cooling-stefan-pcm-SKILL.md',
           'name': 'radiative-sky-cooling-stefan-pcm',
           'description': 'AI-agnostic building-physics and photonic-envelope skill for daytime '
                          'radiative sky cooling across the 8-13 um atmospheric window and Stefan '
                          'phase-change thermal storage.',
           'rules': ['Evaluate net radiative cooling flux P_net(T) = epsilon_LWIR * sigma * T^4 - '
                     'P_atm(T_amb) - (1 - R_solar) * I_solar - h_c * (T_amb - T).',
                     'Treat R_solar >= 0.94 across 0.3-2.5 um and epsilon_LWIR >= 0.90 across 8-13 um as this folio\'s own design targets under I_solar = 1000 W/m^2; report P_net and Delta T as model estimates, not measured results.',
                     'Compute Stefan phase-change melting front depth s(t) = 2 * lambda_s * '
                     'sqrt(alpha_th * t) where lambda_s * exp(lambda_s^2) * erf(lambda_s) = Ste / '
                     'sqrt(pi).']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The opening rooftop scene was not sourced and is replaced by what Raman et al. (2014) report: 4.9 °C below ambient and 40.1 W/m². Earlier editions showed a zero-energy PASS verdict and a cold-chain claim for medicines; nothing here was measured and a roof a few degrees below air temperature is not medical cold storage, so both are withdrawn. The −6.2 °C figure now states the combined heat-exchange coefficient it assumes, and walkthrough numbers that did not follow from the formula are corrected.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; arithmetic recomputed from the stated formula.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-02',
                'summary': 'REV 1.0 (Published 2026-11-02): First edition, pairing the daytime radiative cooling result of Raman et al. (DOI 10.1038/nature13883) with a proposed structural-color membrane and Stefan PCM storage.',
                'opus': 'Cross-model check of the model arithmetic only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' wording is withdrawn in REV 1.1: nothing was measured, and −6.2 K does not follow from h_c = 6.9 W/(m^2 K) alone.'}],
 'volume': 4,
 'volume_code': 'VOL. 04',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/nature13883',
           'fetched_on': '2026-11-21',
           'citing_publications': 3807,
           'supporting': 15,
           'mentioning': 2649,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite index entry for Raman et al., Passive radiative cooling below ambient air temperature under direct sunlight (DOI 10.1038/nature13883), checked 2026-11-21: 3,807 citing publications (15 supporting, 2,649 mentioning, 1 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1038/nature13883',
           'fetched_on': '2026-11-21',
           'citing_publications': 3807,
           'supporting': 15,
           'mentioning': 2649,
           'contrasting': 1,
           'retracted': False,
           'summary': 'Scite index entry for Raman et al., Passive radiative cooling below ambient air temperature under direct sunlight (DOI 10.1038/nature13883), checked 2026-11-21: 3,807 citing publications (15 supporting, 2,649 mentioning, 1 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'},
 'act1_title': 'Act I — From Nocturnal Ice Domes to Daytime Radiative Sky-Cooling Roofs',
 'act1_dropcap': 'In 2014, Raman, Anoma, Zhu, Rephaeli, and Fan reported in Nature a multilayer photonic surface that stayed about 4.9 °C below ambient air under direct sunlight exceeding 850 W/m², with no electricity (DOI 10.1038/nature13883). Night-sky radiative cooling is far older: Bahadori documented how Iranian yakhchāl ice-making structures froze water overnight by radiating heat to a clear sky while shaded from daytime sun (1978, DOI 10.1038/scientificamerican0278-144). Cooling in full daylight is harder because midday sunlight delivers about 1,000 W/m² across 0.3–2.5 μm (Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270). This folio explains that spectral energy balance and pairs it with an untested roof design model.',
 'act1_plain_bridge': 'Every warm surface radiates invisible infrared heat, and Earth\'s atmosphere normally absorbs most of it (Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270). Between 8 and 13 μm, however, clear air is partly transparent, creating a sky window toward cold outer space (Catalanotti et al. 1975, DOI 10.1016/0038-092X(75)90062-6). A roof that reflects about 97% of sunlight while emitting strongly in that 8–13 μm band could radiate more heat outward than it absorbs at noon, settling below outdoor air temperature with no compressor (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513).',
 'act1_body': 'Selective radiative cooling at night was analyzed with silicon monoxide and polymer films by Catalanotti et al. (1975, DOI 10.1016/0038-092X(75)90062-6) and Granqvist & Hjortsberg (1981, DOI 10.1063/1.329270). Because midday sun provides about 1,000 W/m² across 0.3–2.5 μm while a room-temperature surface emits approximately 100–150 W/m² through the 8–13 μm sky window, even modest solar absorption prevents daytime sub-ambient cooling (Raman et al. 2014, DOI 10.1038/nature13883). Raman et al. (2014) used seven layers of hafnia and silica on silver to reflect about 97% of sunlight, reaching 4.9 °C below ambient air and 40.1 W/m² cooling power. Zhai et al. (2017, DOI 10.1126/science.aai7899) embedded glass microspheres in a polymer sheet for roll-to-roll manufacture, and Mandal et al. (2018, DOI 10.1126/science.aat9513) reported paintable porous P(VdF-HFP) coatings with solar reflectance near 0.96, emittance near 0.97, and about 6 °C sub-ambient cooling (about 96 W/m²). This folio pairs such a roof (CSI 07 54 00) with proposed 21 °C phase-change ceiling cassettes (Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019); the pairing is an untested conceptual model and does not estimate chiller savings.',
 'act1_stakes': 'Standard white roof paints reflect visible light well, yet still absorb approximately 10–15% of solar energy in the visible and near-infrared, adding about 100–150 W/m² under peak sun and leaving the roof warmer than ambient air (Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513). Most urban cooling relies on vapor-compression chillers powered by the electrical grid, which reject waste heat outdoors; whole-building tools such as EnergyPlus simulate how envelope gains drive those cooling loads (Crawley et al. 2001, DOI 10.1016/S0378-7788(00)00114-6). Passive radiative surfaces may lower roof surface temperature by a few degrees without compressors, though they could only supplement rather than replace mechanical cooling.',
 'pullquote': '"The clear sky can serve as a heat sink in daylight, provided a '
              'building envelope reflects about 97% of sunlight while emitting strongly '
              'across the 8–13 micrometer infrared window."',
 'chronology': [('1975',
                 'Catalanotti et al. analyze selective surfaces emitting in the 8–13 μm sky window (Solar Energy, DOI 10.1016/0038-092X(75)90062-6).'),
                ('1978',
                 'Bahadori documents traditional Iranian passive cooling, including nocturnal radiative yakhchāl ice domes (Scientific American, DOI 10.1038/scientificamerican0278-144).'),
                ('1981',
                 'Granqvist & Hjortsberg formalize radiative cooling across the 8–13 μm atmospheric window (J. Appl. Phys., DOI 10.1063/1.329270).'),
                ('2014',
                 'Raman, Anoma, Zhu, Rephaeli & Fan report daytime sub-ambient radiative cooling under direct sunlight in Nature (DOI 10.1038/nature13883).'),
                ('2017–2018',
                 'Zhai et al. (Science, DOI 10.1126/science.aai7899) and Mandal et al. (Science, DOI 10.1126/science.aat9513) report scalable polymer and porous coatings.')],
 'act2_title': 'Act II — How It Actually Works: Spectral Selectivity (0.3–2.5 um vs. 8–13 um) + '
               'Stefan Phase-Change Storage',
 'act2_analogy': 'A white cotton shirt blocks sunburn yet may trap body heat beneath the cloth. A daytime radiative roof works like a solar mirror paired with an infrared vent through the 8–13 μm atmospheric window (Catalanotti et al. 1975, DOI 10.1016/0038-092X(75)90062-6; Raman et al. 2014, DOI 10.1038/nature13883): it turns away midday sunlight while radiating thermal energy toward space.',
 'act2_plain_primer': 'The model balances two spectral parameters against outdoor heat exchange (Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270). Solar reflectance R_solar across 0.3–2.5 μm must stay high—about 97%—because absorbing even a few percent of 1,000 W/m² sunlight offsets infrared cooling (Raman et al. 2014, DOI 10.1038/nature13883). Long-wave emissivity ε_LWIR in the 8–13 μm sky window sets how effectively the surface could radiate heat upward. Under the stated assumptions, when outgoing infrared exchange exceeds absorbed sunlight, the model roof temperature drops below outdoor air; all readouts here are model estimates, not roof measurements.',
 'distill_diagram': {'analogy_title': 'The Cosmic Thermal Chimney',
                     'analogy_sub': 'Reflects daytime sunlight while venting infrared into deep '
                                    'space',
                     'force_a_title': 'Solar Reflectance Knob (R_sol)',
                     'force_a_sub': 'Blocks 0.3–2.5 μm visible & near-infrared heat gain from noon '
                                    'sun',
                     'force_b_title': 'Sky-Window Emissivity (ε_LWIR)',
                     'force_b_sub': 'Beams 8–13 μm thermal infrared waves straight into 3 K deep '
                                    'space',
                     'threshold_title': 'Sub-Ambient Tipping Point (P_net > 0 W/m²)',
                     'threshold_pass': 'Model roof surface about 6.2 °C below outdoor air, no compressor',
                     'threshold_fail': 'Absorbed solar heat overwhelms emission, heating the '
                                       'building'},
 'act2_intuition': 'Net daytime radiative cooling follows the four-term balance P_net(T) = P_rad(T) − P_atm(T_amb) − P_sun − h_c (T_amb − T) (Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270; Raman et al. 2014, DOI 10.1038/nature13883). Across 0.3–2.5 μm under an assumed I_solar = 1,000 W/m², absorbed solar flux is P_sun = (1 − R_solar) I_solar = 30 W/m² at R_solar = 0.97. Inside 8–13 μm, this folio assigns an illustrative net radiative sky exchange P_rad − P_atm = 116.4 W/m² at air temperature, giving P_net = 116.4 − 30 = +86.4 W/m² (break-even near R_solar = 0.88). Under the stated assumptions, dividing 86.4 W/m² by an assumed combined radiative-plus-convective heat-exchange coefficient of about 13.9 W/(m²·K) gives a model estimate of about 6.2 °C below outdoor air; using a convective coefficient h_c = 6.9 W/(m²·K) without radiative linearization would estimate about 12.5 °C. For comparison, Raman et al. (2014, DOI 10.1038/nature13883) measured about 4.9 °C and Mandal et al. (2018, DOI 10.1126/science.aat9513) reported about 6 °C. A proposed 21 °C PCM ceiling cassette (L_f = 210 kJ/kg, Ste = c_p ΔT / L_f = 0.085) is modeled by the Stefan moving-boundary front s(t) = 2λ_s√(α_th t) (Carslaw & Jaeger 1959; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019).',
 'act2_deepening': 'Solar irradiance (about 1,000 W/m²) is approximately an order of magnitude denser than the 8–13 μm sky-window radiative surplus (about 100–150 W/m²), so each 0.02 drop in R_solar adds 20 W/m² of solar gain and cuts model net cooling by more than one-fifth (Granqvist & Hjortsberg 1981, DOI 10.1063/1.329270; Raman et al. 2014, DOI 10.1038/nature13883). Non-radiative convection h_c (T_amb − T) warms any sub-ambient surface in wind, which is why outdoor experiments routinely employ infrared-transparent wind covers (Catalanotti et al. 1975, DOI 10.1016/0038-092X(75)90062-6; Raman et al. 2014). Porous polymer films avoid silver mirrors by backscattering sunlight from micro/nanopores while emitting via polymer vibrational bonds (Mandal et al. 2018, DOI 10.1126/science.aat9513). In the proposed ceiling buffer, phase-change latent heat could absorb daytime sensible loads without sizing mechanical chillers here (Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019).',
 'walkthrough': ['Experiment 1 (Solar Reflectance Threshold): Drag Solar Reflectance R_solar from 0.88 up to 0.97. In the folio\'s balance, P_net = 116.4 - (1 - R_solar) * 1000, the midday net cooling power rises from about -4 W/m^2 (slight heating) to +86.4 W/m^2.',
                 'Experiment 2 (8–13 um Sky Window Emissivity): Adjust Sky-Window Emissivity epsilon_LWIR from 0.70 to 0.96 and watch the model temperature drop estimate grow; at the default 0.95 it is about 6.2 K below outdoor air.',
                 'Experiment 3 (Photonic Waveband & Stefan PCM Stepper): Step through Stages 1 to '
                 '4 to inspect solar backscattering, 8–13 um infrared emission, '
                 'convective wind coupling, and Stefan PCM latent thermal buffering.'],
 'act4_title': 'Act IV — AI-Designed Photonic Envelopes, Lab Sustainability & Upstream Discovery '
               'Threads',
 'act4_human_ai': 'Inverse optical design could search for coatings that show a chosen architectural color while reflecting near-infrared light and emitting across 8–13 μm, building on bilayer color work by Chen et al. (2020, DOI 10.1126/sciadv.aaz5413); this folio ran no inverse design. Readers could couple spectral boundary-layer airflow simulations in DedalusProject/dedalus (https://github.com/DedalusProject/dedalus, Burns et al. 2020, DOI 10.1103/PhysRevResearch.2.023068) with whole-building thermal simulations in NREL/EnergyPlus (Crawley et al. 2001, DOI 10.1016/S0378-7788(00)00114-6); neither simulation was run here. Citation tallies come from Scite (Nicholson et al. 2021, DOI 10.1162/qss_a_00146).',
 'act4_deepening': 'Three open engineering hurdles govern field adoption beyond laboratory coupons. First, colored bilayer coatings sacrifice part of their solar reflectance to visible absorption, trading cooling power for glare control and aesthetics (Chen et al. 2020, DOI 10.1126/sciadv.aaz5413). Second, although hybrid metamaterials and phase-inversion coatings target roll-to-roll scalability (Zhai et al. 2017, DOI 10.1126/science.aai7899; Mandal et al. 2018, DOI 10.1126/science.aat9513), outdoor ultraviolet exposure, moisture, and atmospheric soot degrade solar reflectance unless coatings resist aging and soiling (Song et al. 2022, DOI 10.1038/s41467-022-32409-7). Third, whole-building coupling with PCM ceilings must be simulated dynamically (Crawley et al. 2001, DOI 10.1016/S0378-7788(00)00114-6; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019) before any municipal energy code could credit passive roof cooling.',
 'cf_bridge': 'This building-physics folio is written for envelope architects, facade physicists, and HVAC engineers (CSI 07 54 00 roofing; ASHRAE Standard 90.1 energy standard). While cooler roof surfaces may modestly reduce envelope heat gain in hot regions with unreliable grids, a surface about 6 °C below ambient air is not refrigeration and cannot hold the 2–8 °C cold-chain range required by medicines. Nothing here is medical or cold-storage guidance.',
 'sources': ['Bahadori, M. N. (1978). Passive Cooling Systems in Iranian Architecture. Scientific American, 238(2), 144–154. DOI: 10.1038/scientificamerican0278-144.',
             'Catalanotti, S., Cuomo, V., Piro, G., Ruggi, D., Silvestrini, V., & Troise, G. (1975). The radiative cooling of selective surfaces. Solar Energy, 17(2), 83–89. DOI: 10.1016/0038-092X(75)90062-6.',
             'Granqvist, C. G., & Hjortsberg, A. (1981). Radiative cooling to low temperatures: General considerations and application to selectively emitting SiO films. Journal of Applied Physics, 52(6), 4205–4220. DOI: 10.1063/1.329270.',
             'Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014). Passive radiative cooling below ambient air temperature under direct sunlight. Nature, 515(7528), 540–544. DOI: 10.1038/nature13883.',
             'Zhai, Y., Ma, Y., David, S. N., Zhao, D., Lou, R., Tan, G., Yang, R., & Yin, X. (2017). Scalable-manufactured randomized glass-polymer hybrid metamaterial for daytime radiative cooling. Science, 355(6329), 1062–1066. DOI: 10.1126/science.aai7899.',
             'Mandal, J., Fu, Y., Overvig, A. C., Jia, M., Sun, K., Shi, N. N., Zhou, H., Xiao, X., Yu, N., & Yang, Y. (2018). Hierarchically porous polymer coatings for highly efficient passive daytime radiative cooling. Science, 362(6412), 315–319. DOI: 10.1126/science.aat9513.',
             'Chen, Y., Mandal, J., Li, W., Smith-Washington, A., Tsai, C., et al. (2020). Colored and paintable bilayer coatings with high solar-infrared reflectance for efficient cooling. Science Advances, 6(17), eaaz5413. DOI: 10.1126/sciadv.aaz5413.',
             'Song, J., Zhang, W., Sun, Z., Pan, M., Tian, F., Li, X., Ye, M., & Deng, X. (2022). Durable radiative cooling against environmental aging. Nature Communications, 13, 4805. DOI: 10.1038/s41467-022-32409-7.',
             'Carslaw, H. S., & Jaeger, J. C. (1959). Conduction of Heat in Solids (2nd ed., Chapter XI: Change of State / Stefan Problem). Oxford University Press.',
             'Kuznik, F., David, D., Johannes, K., & Roux, J.-J. (2011). A review on phase change materials integrated in building walls. Renewable and Sustainable Energy Reviews, 15(1), 379–391. DOI: 10.1016/j.rser.2010.08.019.',
             'Crawley, D. B., Lawrie, L. K., Winkelmann, F. C., Buhl, W. F., Huang, Y. J., et al. (2001). EnergyPlus: creating a new-generation building energy simulation program. Energy and Buildings, 33(4), 319–331. DOI: 10.1016/S0378-7788(00)00114-6.',
             'Burns, K. J., Vasil, G. M., Oishi, J. S., Lecoanet, D., & Brown, B. P. (2020). Dedalus: A flexible framework for numerical simulations with spectral methods (DedalusProject/dedalus, https://github.com/DedalusProject/dedalus). Physical Review Research, 2(2), 023068. DOI: 10.1103/PhysRevResearch.2.023068.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the context of citations and classifies their intent using deep learning (https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: 10.1162/qss_a_00146.',
             'CSI MasterFormat 07 54 00 Thermoplastic Membrane Roofing; ASHRAE Standard 90.1, Energy Standard for Buildings Except Low-Rise Residential Buildings. Named for context; neither sets this folio\'s targets.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Dual-waveband '
        'photonic radiative sky-cooling spectrum showing 97% solar reflection and 95% 8-13 um '
        'atmospheric window emission">\n'
        '            <line x1="55" y1="180" x2="635" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <line x1="55" y1="26" x2="55" y2="180" stroke="currentColor" '
        'stroke-opacity="0.4"/>\n'
        '            <rect x="75" y="34" width="210" height="146" fill="var(--tp-stone)" '
        'stroke="none"/>\n'
        '            <rect x="355" y="34" width="245" height="146" fill="var(--tp-verdigris)" '
        'fill-opacity="0.12" stroke="none"/>\n'
        '            <path d="M 75 178 Q 145 38 225 162 L 285 178" fill="var(--tp-minium-soft)" '
        'stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="4,3"/>\n'
        '            <path id="tp-a08-emissivity-curve" d="M 75 174 L 295 174 L 355 44 L 585 44 L '
        '625 168" fill="none" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <text x="85" y="52" font-size="10.5" font-weight="600" '
        'fill="var(--tp-minium)">Solar Waveband (0.3–2.5 μm)</text>\n'
        '            <text id="tp-a08-rsolar-text" x="85" y="70" font-size="10" '
        'fill="currentColor">Reflectance R_solar = 97.0% (Abs = 3.0%)</text>\n'
        '            <text x="368" y="52" font-size="10.5" font-weight="600" '
        'fill="var(--tp-verdigris)">Atmospheric Sky Window (8–13 μm)</text>\n'
        '            <text id="tp-a08-pnet-text" x="368" y="70" font-size="10" '
        'fill="var(--tp-prussian)">ε_LWIR = 95.0% · Model P_net = +86.4 W/m²</text>\n'
        '            <text x="195" y="202" font-size="10.5" fill="currentColor">Electromagnetic '
        'Wavelength λ (μm) · Model ΔT_sub = −6.2 °C Below Noon Air</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a photonic radiative sky-cooling roof pavilion '
        'beaming 8-13 micrometer infrared thermal waves through the atmosphere into deep space '
        'under midday sunlight would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.08-V (Imagining What It Would Look Like) · Artistic '
            'architectural-physics visualization imagining an AI-designed microporous photonic '
            'roof reflecting midday sunlight while radiating 8–13 μm infrared heat waves directly '
            'into the 3 K sky sink above a Stefan phase-change ceiling.'}

DISPATCH = {'kicker': 'FRONTIER BUILDING PHYSICS DISPATCH · AI PHOTONIC SKY-COOLING & STEFAN PHASE-CHANGE '
           'ENVELOPES',
 'headline': 'How a Roof Can Radiate Building Heat Through the 8–13 μm Sky Window in Daylight: A Design Model',
 'body': 'Raman, Anoma, Zhu, Rephaeli & Fan measured a surface about 4.9 °C below air temperature under direct sunlight (Nature, DOI 10.1038/nature13883), and Mandal et al. reported porous polymer coatings with similar behavior (Science, DOI 10.1126/science.aat9513). Using Granqvist & Hjortsberg\'s 8–13 μm balance (DOI 10.1063/1.329270), this folio models a roof at about 97% solar reflectance and 95% sky-window emissivity (+86.4 W/m², −6.2 °C) paired with a proposed Stefan PCM ceiling (Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019). Model estimates, not measurements.'}

META_3D = ('Photonic Sky-Cooling 8–13 μm Radiative & PCM Envelope',
 'X: Wavelength λ (0.3–20 μm) · Z: Solar Flux · Y: Net Sub-Ambient Radiative Cooling P_net')

ES_TRANSLATION = {'title_es': 'Cubiertas Fotónicas de Enfriamiento Radiativo Diurno al Cielo (Ventana de 8–13 μm) y '
             'Envolventes de Cambio de Fase de Stefan',
 'subtitle_es': 'Modelo de física edilicia que acopla enfriamiento radiativo diurno en la ventana de 8–13 μm '
                '(Raman et al. 2014, DOI 10.1038/nature13883; Mandal et al. 2018, DOI 10.1126/science.aat9513) '
                'con un plafón propuesto de cambio de fase de Stefan (Carslaw y Jaeger 1959; Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019).',
 'why_es': 'Un techo blanco común absorbe suficiente infrarrojo cercano solar para calentarse al sol; una '
           'cubierta selectiva refleja cerca de 97% de la radiación solar y emite calor por la ventana '
           'atmosférica de 8–13 μm hacia el espacio exterior (Catalanotti et al. 1975, DOI 10.1016/0038-092X(75)90062-6; '
           'Raman et al. 2014, DOI 10.1038/nature13883).',
 'plain_es': 'Todos los cuerpos emiten calor en ondas infrarrojas invisibles que la atmósfera suele atrapar '
             '(Granqvist y Hjortsberg 1981, DOI 10.1063/1.329270). Entre 8 y 13 micrómetros existe una ventana '
             'transparente por donde ese calor escapa al espacio frío, principio ya aprovechado en las cúpulas '
             'nocturnas iraníes yakhchāl documentadas por Bahadori (1978, DOI 10.1038/scientificamerican0278-144). '
             'De día, Raman et al. (2014, DOI 10.1038/nature13883) midieron una superficie 4.9 °C por debajo '
             'del aire bajo sol directo, y Mandal et al. (2018, DOI 10.1126/science.aat9513) reportaron '
             'recubrimientos porosos con comportamiento similar; recubrimientos bicapa con color permiten reducir '
             'el deslumbramiento a costa de menor enfriamiento (Chen et al. 2020, DOI 10.1126/sciadv.aaz5413).',
 'deep_es': 'El modelo evalúa el balance radiativo de 8 a 13 μm (Granqvist y Hjortsberg 1981, DOI 10.1063/1.329270): '
            'con 1,000 W/m² de sol y reflectancia R_solar = 0.97, el techo absorbe 30 W/m²; frente a un intercambio '
            'radiativo ilustrativo fijo de 116.4 W/m², la potencia neta es +86.4 W/m² y una caída de 6.2 °C supone '
            'un coeficiente combinado de intercambio de calor de unos 13.9 W/(m²·K). El folio propone acoplar este techo con plafones de cambio de fase de Stefan '
            '(Kuznik et al. 2011, DOI 10.1016/j.rser.2010.08.019) y evaluar cargas térmicas dinámicas en '
            'EnergyPlus (Crawley et al. 2001, DOI 10.1016/S0378-7788(00)00114-6), considerando el envejecimiento '
            'por radiación UV y polvo en campo (Song et al. 2022, DOI 10.1038/s41467-022-32409-7). Son valores '
            'de modelo, no mediciones ni sustituto de refrigeración.'}
