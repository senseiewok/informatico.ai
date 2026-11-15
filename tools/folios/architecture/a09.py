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
 'subtitle': 'Completing the timber-and-climate thread of Folios A.02, E.04, and A.08: how Stephen '
             "Timoshenko's bilayer curvature formula describes wood bilayers that bend with humidity, the idea behind the motor-free facade skins studied at ICD/ITKE Stuttgart. A design model.",
 'date_published': '2026-11-03',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.1',
 'status_badge': 'HYGROSCOPIC TIMBER · REV 1.1',
 'primary_kernel': 'tools/tectonic_verify.py',
 'governing_law': 'κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 '
                  '18 00',
 'colophon': {'identifier': 'A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00',
              'kernels': 'Timoshenko Bilayer Curvature · Orthotropic Wood Sorption (α_T vs. α_L)',
              'benchmarks': 'Model values: ΔMC = +6.0% · h = 6.0 mm · m = 2 · n = 10.6 ⇒ κ = 1.42 m⁻¹ · δ_tip = 128 mm',
              'bridge': 'Completes A.02/E.04 · Wood Cell-Wall Swelling ↔ P.04 Periciliary '
                        'Brush (Loose Analogy)'},
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
 'steps': ['Stage 1 (Orthotropic Cell-Wall Sorption, Continuing E.04): Below fiber saturation (about 28% MC), the model assumes beech swells tangentially at α_T = 0.32%/%MC and along the grain at only α_L = 0.012%/%MC. Both coefficients are assumed round values.',
           'Stage 2 (Timoshenko Bilayer Formula, DOI 10.1364/JOSA.11.000233): Bonding an active tangential ply h_2 to a passive longitudinal ply h_1 turns the misfit strain Δε = (α_T − α_L)ΔMC = 0.0185 into curvature. With the folio\'s assumed m = h_1/h_2 = 2 and n = E_1/E_2 = 10.6 the geometry factor is 0.46 and κ = 1.42 m⁻¹. Equal plies of equal stiffness (m = n = 1) would give 4.62 m⁻¹.',
           'Stage 3 (Weather-Responsive Facade Petal, Model): A 425 mm cantilever petal moves δ_tip ≈ ½ κ L² = 128 mm at the tip as it dries. The 64.5% free vent area is a fixed illustrative value, not computed from the geometry. Rain-tightness was not assessed.',
           'Stage 4 (Self-Shaping CLT, Continuing A.02): Wood et al. (2020) describe curved cross-laminated timber components for the Urbach Tower that took their shape during drying instead of being milled or pressed to a curve.'],
 'readouts': [{'label': 'Timoshenko Curvature (κ, Model)', 'value': '1.42 m⁻¹ (R = 0.70 m)'},
              {'label': 'Petal Tip Deflection (δ_tip, Model)', 'value': '128.2 mm (at L = 425 mm)'},
              {'label': 'Vent Opening (Illustrative)', 'value': '64.5% Free Area (Illustrative)'},
              {'label': 'Model Check', 'value': 'ACTUATION WITHOUT MOTORS (MODEL)'}],
 'spec_plate': {'division': 'CSI MASTERFORMAT 06 18 00 / EN 1995-1-1',
                'title': 'Programmable Hygroscopic European Beech Bilayer Climate Envelope & '
                         'Self-Shaping CLT',
                'body': 'Design proposal: cross-grained Fagus sylvatica (European beech) bilayer facade elements bonded with a one-component polyurethane structural adhesive, a weather coat, and stainless limit stops. Not a tested product.',
                'meta': 'References: Timoshenko (1925) DOI 10.1364/JOSA.11.000233; Reichert, Menges & Correa (2015) DOI 10.1016/j.cad.2014.02.010 · Model values; no cycle testing was done'},
 'sidenote_1': {'kicker': 'SIDENOTE A.09-A · COMPLETING FOLIO A.02 TIMBER MECHANICS WITH '
                          'TIMOSHENKO (1925)',
                'body': "Timoshenko's dimensionless geometry factor f(m, n) peaks when "
                        'stiffness-weighted layer thicknesses satisfy E_1 h_1² = E_2 h_2², '
                        'maximizing autonomous curvature per unit thickness h.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.09-B · SPECIFICATION PLATE · CSI 06 18 00 (PROGRAMMABLE '
                          'WOOD)',
                'body': 'By choosing grain orientations in each layer, a flat timber panel can be made to curve as it dries. Single-curved components have been built this way (Wood et al. 2020); doubly curved shells made the same way are a proposal here.'},
 'skill': {'filename': 'hygroscopic-timber-timoshenko-bilayer-SKILL.md',
           'name': 'hygroscopic-timber-timoshenko-bilayer',
           'description': 'AI-agnostic architectural and timber-engineering skill for Stephen '
                          'Timoshenko bilayer curvature, orthotropic wood moisture swelling '
                          '(alpha_T vs alpha_L), and zero-energy responsive building skins.',
           'rules': ['Compute differential hygroscopic strain Delta_epsilon = (alpha_T - alpha_L) '
                     '* Delta_MC below the Fiber Saturation Point (MC <= 28%).',
                     'Evaluate Timoshenko curvature kappa = 6 * (1 + m)^2 * Delta_epsilon / (h * '
                     '(3 * (1 + m)^2 + (1 + m*n) * (m^2 + 1/(m*n)))) with m = h_1/h_2 and n = '
                     'E_1/E_2.',
                     'Calculate cantilever aperture tip deflection delta_tip = (1 - cos(kappa * '
                     'L)) / kappa approx 0.5 * kappa * L^2, state the m and n used, and check rolling shear against the timber code that applies; report results as model values.']},
 'revisions': [{'edition': 'REV 1.1',
                'date': '2026-11-14',
                'summary': 'REV 1.1 (Redated 2026-11-14): Grounding revision. The curvature 1.42 m⁻¹ did not follow from the stated formula without the ply ratios, so the assumed m = 2 and n = 10.6 are now stated (equal plies would give 4.62 m⁻¹). The opening scenes about Timoshenko and Menges were not sourced and are replaced by a plain account; beech skins are no longer attributed to the Stuttgart projects. The PASS verdict, the 10,000-cycle claim and the statement that wood swelling obeys the same law as the airway periciliary brush are withdrawn; the last is now called an analogy.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; arithmetic recomputed from the stated formula.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-03',
                'summary': 'REV 1.0 (Published 2026-11-03): First edition, completing Folios A.02, E.04 & A.08 with '
                           "Timoshenko's 1925 bilayer curvature formula (DOI "
                           '10.1364/JOSA.11.000233) and hygroscopic wood skins.',
                'opus': 'Council review of the formula only (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' wording is withdrawn in REV 1.1: the published curvature needed ply ratios that were not stated, and nothing was measured.'}],
 'volume': 5,
 'volume_code': 'VOL. 05',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-08',
           'citing_publications': 2499,
           'supporting': 48,
           'mentioning': 1474,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Timoshenko, Analysis of Bi-Metal Thermostats (DOI 10.1364/JOSA.11.000233), checked 2026-11-08: 2,499 citing publications (48 supporting, 1,474 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'parent_folios': ['A.02', 'E.04', 'A.08'],
 'lineage_mode': 'REFERENCE_COMPLETION · Completes A.02 Timber Gridshells, E.04 Moisture Sorption '
                 '& A.08 Zero-Energy Envelopes',
 'scite': {'doi': '10.1364/JOSA.11.000233',
           'fetched_on': '2026-11-08',
           'citing_publications': 2499,
           'supporting': 48,
           'mentioning': 1474,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Scite index entry for Timoshenko, Analysis of Bi-Metal Thermostats (DOI 10.1364/JOSA.11.000233), checked 2026-11-08: 2,499 citing publications (48 supporting, 1,474 mentioning, 0 contrasting) and no retraction notice. The counts describe that paper, not this folio\'s model.'},
 'act1_title': 'Act I — Completing the Timber & Climate Thread from A.02, E.04 & A.08: Wood That '
               'Breathes and Moves Without Motors',
 'act1_dropcap': 'In 1925 the Ukrainian-born engineer Stephen Timoshenko published Analysis of Bi-Metal Thermostats in the Journal of the Optical Society of America (DOI 10.1364/JOSA.11.000233). It gives the curvature of a strip made of two bonded metals that expand by different amounts when heated. In 1997 Dawson, Vincent and Rocca described in Nature how pine cone scales open as they dry and close when wet, although the tissue is dead: two layers of the scale respond differently to moisture (DOI 10.1038/37745). Reichert, Menges and Correa at the University of Stuttgart later described building skins that use the same effect in wood veneer, so that openings respond to humidity without motors, sensors or wiring (2015, DOI 10.1016/j.cad.2014.02.010). This folio applies Timoshenko\'s formula to a wood bilayer as a design model.',
 'act1_plain_bridge': 'In plain words, think of what happens to a wooden door in your house during '
                      'a humid summer. The door absorbs moisture from the damp air and swells, '
                      'sticking inside its frame. Wood swells because natural plant cells soak up '
                      'water vapor like millions of tiny sponges. However, wood does not swell '
                      'equally in all directions. It expands dramatically across its grain, but '
                      'hardly changes length along the grain. If you take a thin board cut across '
                      'the grain and glue it tightly to a board cut along the grain, a fascinating '
                      'reaction takes place whenever the humidity changes. When the air becomes '
                      'humid, the cross-grain board tries to grow longer while the lengthwise '
                      'board refuses to stretch. Because the two boards are bonded together, the '
                      'whole piece is forced to bend into a curve. By shaping these wooden '
                      'bilayers into facade petals, openings could widen when the air is dry '
                      'and close when it is damp, with no motor.',
 'act1_body': 'Pine cones move without muscles or motors: the layers of a scale swell by different amounts as humidity changes, so the scale bends closed when wet and open when dry (Dawson, Vincent & Rocca 1997, DOI 10.1038/37745). In 1925, '
              'Stephen Timoshenko published a closed-form curvature formula for two-layer strips in the Journal of the Optical Society of America (DOI '
              '10.1364/JOSA.11.000233). Researchers at ICD/ITKE Stuttgart, among them Achim Menges, Steffen Reichert and Dylan Wood, have applied the bilayer idea to wood: in humidity-responsive veneer skins (Reichert, Menges & Correa 2015, DOI 10.1016/j.cad.2014.02.010) and in curved cross-laminated timber for the Urbach Tower that took its shape while drying (Wood et al. 2020). This folio\'s own example is a European beech bilayer: an active ply cut so that it swells along the petal (assumed 0.32 percent per percent change in moisture content) glued to a ply that barely changes length. The beech petal is a design model for this folio; it is not a description of those built projects.',
 'act1_stakes': 'For centuries, carpenters and cabinetmakers treated wood swelling as an '
                'unpredictable flaw to be restrained through heavy framing, metal fasteners, and '
                'moisture-blocking varnishes. Master shipwrights and joiners learned through trial '
                'and error that unseasoned timber twists, warps, and cracks if moisture escapes '
                'unevenly across different grain directions. In twentieth-century construction, '
                'the standard response was to over-engineer steel mechanical systems: motorized '
                'louvers, motorized dampers, and electric actuators wired to electronic humidity '
                'sensors. But motorized kinetic facades have proven notoriously fragile in '
                'real-world buildings. Mechanical linkages jam from wind-borne dust, electric '
                'servo motors burn out after repetitive weather cycles, and electronic sensors '
                'corrode in coastal air. When building owners face mounting maintenance costs, '
                'motorized facade louvers are frequently locked in fixed positions, abandoning '
                'climate responsiveness altogether. The failure of complex mechanical gadgets '
                'highlighted the need for passive, materially embedded movement where the '
                'structure itself serves as sensor, actuator, and weather barrier.',
 'pullquote': '"In hygroscopic timber tectonics, the sensor, the actuator, and the load-bearing '
              'architectural skin are no longer separate mechanical devices—they are the same '
              'piece of wood."',
 'chronology': [('1925',
                 'Stephen Timoshenko publishes the exact analytical curvature theorem for '
                 'bi-material strips in JOSA (DOI 10.1364/JOSA.11.000233).'),
                ('1997',
                 'Dawson, Vincent & Rocca describe how dead pine cone scales open and close through layers that respond differently to moisture (Nature, DOI 10.1038/37745).'),
                ('2015',
                 'Reichert, Menges & Correa publish Meteorosensitive architecture, on humidity-driven wood veneer building skins (DOI 10.1016/j.cad.2014.02.010).'),
                ('2020',
                 'Wood et al. publish the self-shaping curved cross-laminated timber of the Urbach Tower (Fabricate 2020).')],
 'act2_title': 'Act II — How It Actually Works: Timoshenko Bilayer Mechanics + Orthotropic Wood '
               'Swelling',
 'act2_analogy': 'Take two long strips of paper, wet only one strip with a damp sponge, and glue '
                 'them back-to-back. As the wet paper expands, the dry paper stays the same size, '
                 'forcing the glued strip to curl into a tight loop. Conifer pinecones use this '
                 'exact trick, flexing their scales closed during downpours and popping open in '
                 'warm dry air. Programmable timber facades operate on the identical physical '
                 'principle, using natural grain anisotropy instead of mechanical gears.',
 'act2_plain_primer': 'To control this natural wood curling mechanism on a building facade, you '
                      'work with two physical knobs. The first knob represents the change in '
                      'moisture inside the wood as outdoor relative humidity rises or falls with '
                      'the weather. When morning fog rolls into the city, the wood drinks in '
                      'moisture from the air, causing the active tangential layer to swell and '
                      'bending the facade petal tightly against its frame to keep out rain. As the '
                      'midday sun warms and dries the atmosphere, the moisture content drops, '
                      'relaxing the petal and curling it wide open to draw in cooling breezes. The '
                      'second knob sets the total thickness of the bonded wooden bilayer. If you '
                      'choose an ultra-thin wooden veneer, the petal curls rapidly with dramatic '
                      'curvature under the slightest change in humidity. If you increase the '
                      'thickness to several millimeters, the wood bends more slowly but develops '
                      'immense structural force, capable of curling heavy structural roof panels '
                      'into shape.',
 'distill_diagram': {'analogy_title': 'The Pinecone Wet-Paper Curl',
                     'analogy_sub': 'Differential expansion between bonded plies curls the strip '
                                    'with 0 W',
                     'force_a_title': 'Moisture Shift Knob (ΔMC)',
                     'force_a_sub': 'Drives swelling strain differential across tangential '
                                    'cellular grain',
                     'force_b_title': 'Bilayer Thickness Knob (h)',
                     'force_b_sub': 'Governs flexural rigidity and sets the radius of '
                                    'self-actuation',
                     'threshold_title': 'Model Curvature (κ = 1.42 m⁻¹)',
                     'threshold_pass': 'Model: 128 mm tip opening, 64% vent area (illustrative)',
                     'threshold_fail': 'Fiber saturation or delamination if rolling shear exceeds '
                                       'limit'},
 'act2_intuition': "Extending Folio A.02's Eurocode 5 timber mechanics, solid wood operating below "
                   'its Fiber Saturation Point (roughly 28% to 30% moisture content) shows, with the folio\'s assumed coefficients, '
                   'an anisotropy of about 27 to 1 between its tangential swelling coefficient '
                   'alpha_T (approximately 0.0032 per percent moisture shift) and its longitudinal '
                   'grain coefficient alpha_L (barely 0.00012 per percent moisture shift). When an '
                   'active tangential European beech layer of thickness h_2 and elastic modulus '
                   'E_2 is bonded to a passive longitudinal restraint ply of thickness h_1 and '
                   'modulus E_1 with thickness ratio m = h_1 / h_2 and modulus ratio n = E_1 / '
                   'E_2, any shift in ambient moisture Delta_MC produces an internal misfit strain '
                   "Delta_epsilon = (alpha_T - alpha_L) * Delta_MC. By Stephen Timoshenko's "
                   'classical bilayer mechanics, the resulting uniform curvature is kappa = 6 * (1 '
                   '+ m)^2 * Delta_epsilon / (h * (3 * (1 + m)^2 + (1 + m * n) * (m^2 + 1 / (m * '
                   'n)))). At the defaults Delta_MC = 6 percent and h = 6 mm, Delta_epsilon = 0.0185. The folio assumes m = 2 and n = 10.6, which makes the geometry factor 0.46 and kappa = 1.42 per meter; with equal plies of equal stiffness (m = n = 1) the factor is 1.5 and kappa would be 4.62 per meter, so the result depends strongly on the lay-up. For a cantilevered facade petal of length L = 425 mm this curvature gives a '
                   'tip deflection delta_tip of about 0.5 * kappa * L^2 = 128 mm (124 mm with the exact circular-arc expression). These are model values; no petal was built or tested.',
 'act2_deepening': 'The mechanical interaction between moisture shift and bilayer thickness '
                   "reveals an essential engineering trade-off governed by Timoshenko's "
                   'denominator. Because curvature kappa scales inversely with total thickness h, '
                   'doubling the thickness of the wood reduces its curvature by half for any given '
                   'moisture shift. However, the flexural bending rigidity of the composite strip '
                   'scales with the cube of thickness, h^3. This means that while a thin '
                   'three-millimeter veneer curls swiftly under rapid ambient relative humidity '
                   'fluctuations, it possesses minimal resistance against aerodynamic wind '
                   'flutter. Conversely, a thick structural bilayer of ten to twelve millimeters '
                   'requires greater moisture differentials to curl, but generates tremendous '
                   'actuation forces capable of self-shaping massive cross-laminated timber '
                   'plates. Furthermore, interfacial shear stress peaks at the adhesive bond line '
                   'near the free ends: if the differential strain Delta_epsilon expands too '
                   'rapidly without proper moisture conditioning, interfacial rolling shear can '
                   'exceed Eurocode 5 strength limits, necessitating carefully calculated '
                   'fiber-orientation angles.',
 'walkthrough': ['Experiment 1 (Ambient Moisture Content Shift Delta_MC): Drag Wood Moisture '
                 'Content Change Delta_MC from +1.0% up to +12.0%. Watch Timoshenko curvature '
                 'kappa (m^-1) and petal tip opening delta_tip grow linearly in the model.',
                 'Experiment 2 (Bilayer Thickness & Stiffness Tuning h): Adjust Total Bilayer '
                 'Thickness h from 3.0 mm (rapid, high-curvature facade louver) to 14.0 mm '
                 '(structural self-shaping CLT shell panel).',
                 'Experiment 3 (From Pinecone Microfibrils to Zero-Energy Facade): Step through '
                 'Stages 1 to 4 to explore orthotropic cell-wall sorption, Timoshenko neutral-axis '
                 'shear, aperture airflow modulation, and cyclic hysteresis durability.'],
 'act4_title': 'Act IV — Zero-Energy Climate Skins, Archive Continuity & Upstream Biophysical '
               'Threads',
 'act4_human_ai': "Connecting Folio A.02's timber joinery, Folio A.03's solar buoyancy stacks, and "
                  "Folio E.04's psychrometric moisture balance, designers could use "
                  'finite-element hygro-mechanical models to choose grain orientation and '
                  'ply thickness so that an envelope opens as humidity changes. This is a proposal; the folio ran no such model.',
 'act4_deepening': 'Designers could pair finite-element models with optimization or machine-learning tools to plan the curvature of a flat timber panel before it is made: scan the grain, model the anisotropic swelling (FEniCS/dolfinx, DOI 10.1145/3524456, is an open finite-element library a reader could use for this), and search for the lay-up that dries into the target shape. The folio ran none of this. If it worked at scale it could reduce the offcut waste of milling curved parts from solid stock. Open '
                   'research questions remain: How do cyclic '
                   'weathering, micro-crack fatigue, and natural lignocellulosic creep alter the '
                   'long-term curvature response over decades of outdoor exposure? Can '
                   'bio-inspired wax and nano-silicate coatings protect against ultraviolet fiber '
                   'degradation while preserving hygroscopic breathability? Long-term outdoor durability is the main unknown for any moving wood skin.',
 'cf_bridge': 'Written for architects, facade engineers, and mass-timber builders (CSI 06 '
              '18 00 Glued-Laminated Construction, EN 1995-1-1). Loose analogy only: wood cell walls swell as they take up water, and Folio P.04 discusses how the hydration of the airway surface layer changes the height of the periciliary brush. Both are cases of a polymer network taking up water, but the materials and the physics differ, and this folio does not show that the same law governs both. It has no clinical content and nothing here bears on Cystic Fibrosis care.',
 'sources': ['Timoshenko, S. (1925). Analysis of bi-metal thermostats. Journal of the Optical '
             'Society of America, 11(3), 233–255. DOI: 10.1364/JOSA.11.000233.',
             'Reichert, S., Menges, A., & Correa, D. (2015). Meteorosensitive architecture: '
             'Biomimetic building skins based on materially embedded and hygroscopically enabled responsiveness. '
             'Computer-Aided Design, 60, 50–69. DOI: 10.1016/j.cad.2014.02.010.',
             'Dawson, C., Vincent, J. F. V., & Rocca, A.-M. (1997). How pine cones open. Nature, 390(6661), 668. DOI: 10.1038/37745.',
             'Wood, D., Grönquist, P., Bechert, S., Aldinger, L., Riggenbach, D., Lehmann, K., '
             'Rüggeberg, M., Burgert, I., Knippers, J., & Menges, A. (2020). From machine control '
             'to material programming: Self-shaping wood manufacturing of a high performance '
             'curved CLT structure—Urbach Tower. Fabricate 2020, 50–57.',
             'CEN. EN 1995-1-1, Eurocode 5: Design of timber structures, Part 1-1 (first published 2004); CSI MasterFormat '
             '06 18 00 Glued-Laminated Construction. Named for context; neither sets this folio\'s values.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: 10.1145/3524456.',
             'Nicholson, J. M., et al. (2021). scite: A smart citation index that displays the '
             'context of citations and classifies their intent using deep learning '
             '(https://scite.ai). Quantitative Science Studies, 2(3), 882–898. DOI: '
             '10.1162/qss_a_00146.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Timoshenko '
        'hygroscopic cross-laminated timber bilayer curvature and zero-energy facade aperture '
        'response curve">\n'
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
        'fill="currentColor">Timoshenko Beech Bilayer (α_T vs. α_L Grain)</text>\n'
        '            <text id="tp-a09-svg-curv-text" x="55" y="206" font-size="10" '
        'fill="var(--tp-verdigris)">Model: κ = 1.42 m⁻¹ · Tip Opening δ_tip = 128 mm (No Motor)</text>\n'
        '            <line x1="355" y1="24" x2="355" y2="195" stroke="currentColor" '
        'stroke-opacity="0.2"/>\n'
        '            <text x="372" y="26" font-size="10" font-weight="600" '
        'fill="currentColor">Curvature κ(ΔMC, h) &amp; Aperture Free Area</text>\n'
        '            <path id="tp-a09-curv-line" d="M 380 172 L 625 56" fill="none" '
        'stroke="var(--tp-verdigris)" stroke-width="2.8"/>\n'
        '            <circle id="tp-a09-op-dot" cx="502" cy="114" r="6" fill="var(--tp-minium)"/>\n'
        '            <text x="382" y="70" font-size="9.5" fill="var(--tp-verdigris)">Timoshenko '
        'Linear Law κ ∝ (α_T − α_L) ΔMC / h</text>\n'
        '            <text id="tp-a09-vent-text" x="382" y="206" font-size="10" '
        'fill="var(--tp-prussian)">Free-Vent Area: 64.5% Open (Illustrative)</text>\n'
        '          </svg>'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a biomimetic hygroscopic cross-laminated beech '
        'timber facade pavilion opening its curved Timoshenko bilayer petals autonomously in '
        'response to sunlight and humidity would look like (artistic impression, not a measured '
        'structure)',
 'caption': 'Conceptual Vision Plate A.09-V (Imagining What It Would Look Like) · Artistic '
            'architectural visualization (completing Folios A.02, E.04 & A.08) imagining a '
            'zero-energy hygroscopic European beech bilayer skin whose petals curve open and '
            "closed via Stephen Timoshenko's 1925 bimetallic curvature law."}

DISPATCH = {'kicker': 'FRONTIER BIOMIMETIC TIMBER DISPATCH · COMPLETING A.02, E.04 & A.08 · HYGROSCOPIC WOOD '
           'SKINS',
 'headline': "Stephen Timoshenko's 1925 Bilayer Theorem & Cross-Grained Beech Skins Power "
             'Zero-Energy Climate Facades',
 'body': 'Completing the mass-timber and psychrometric threads of Folios A.02, E.04, and A.08, '
         "this folio applies Stephen Timoshenko's bilayer "
         'curvature formula (JOSA DOI 10.1364/JOSA.11.000233) to a wood bilayer whose plies swell very differently with moisture (about 27:1 with the assumed coefficients), the principle behind the meteorosensitive skins described by Reichert, Menges & Correa (DOI 10.1016/j.cad.2014.02.010). Model values, not measurements.'}

META_3D = ('Timoshenko Hygroscopic Beech Bilayer Shell Manifold',
 'X: Spanwise Petal Coordinate · Z: Moisture Shift ΔMC · Y: Timoshenko Curvature κ & Tip Opening')

ES_TRANSLATION = {'title_es': 'Pieles Arquitectónicas Programables de Madera Higroscópica: Curvatura Bicapa de '
             'Timoshenko, Hinchamiento Ortotrópico y Fachadas Climáticas de Energía Cero',
 'subtitle_es': 'Completando los Folios A.02, E.04 y A.08: cómo la fórmula de curvatura bicapa de '
                'Stephen Timoshenko (1925) describe bicapas de madera que se curvan con la humedad, la idea detrás de las pieles de fachada sin motores estudiadas en ICD/ITKE Stuttgart. Un modelo de diseño.',
 'why_es': 'Una piña de pino en la ventana se cierra sola cuando llueve y se abre cuando el aire '
           'está seco porque sus fibras externas e internas se expanden de forma distinta con la '
           'humedad, igual que una tira bimetálica natural.',
 'bridge_es': 'Solo una analogía: las paredes celulares de la madera se hinchan al absorber agua, y el Folio P.04 trata cómo la hidratación de la superficie de la vía aérea cambia la altura del cepillo periciliar. En ambos casos una red de polímeros absorbe agua, pero los materiales y la física son distintos y este folio no demuestra que los rija la misma ley. No tiene contenido clínico ni relación con la atención de la Fibrosis Quística.',
 'plain_es': 'En palabras sencillas, imaginen una fachada de madera que se abre y se cierra sola '
             'con el clima sin tener un solo motor ni gastar electricidad. Piensen en lo que le '
             'ocurre a una puerta de madera en un día muy húmedo: absorbe vapor de agua del aire y '
             'se hincha. La madera se expande mucho a lo ancho de sus fibras, pero casi nada a lo '
             'largo de ellas. Si pegamos dos láminas delgadas de madera con las vetas cruzadas en '
             'direcciones opuestas, cuando el ambiente se vuelve húmedo, una lámina intenta crecer '
             'mientras la otra se resiste. Como están firmemente unidas con pegamento, la única '
             'forma de liberar esa tensión es curvándose, exactamente igual a como una piña de '
             'pino cierra sus escamas bajo la lluvia y las abre cuando sale el sol. Diseñando '
             'estas hojas de madera en las aberturas de un edificio, podrían abrirse solas '
             'para ventilar en días secos y cerrarse cuando el aire está húmedo.',
 'deep_es': 'El modelo usa la fórmula de curvatura bicapa que Stephen Timoshenko publicó en 1925, combinada con la anisotropía '
            'higroscópica de la madera de haya europea. Con los coeficientes supuestos en el folio, por debajo del punto de saturación de la '
            'fibra la expansión tangencial es unas 27 veces mayor que la longitudinal. Un cambio de humedad de 6 por ciento produce una '
            'deformación diferencial de 0.0185, que curva la pieza según los espesores y los módulos elásticos de ambas capas. El folio supone una relación de espesores m = 2 y de módulos n = 10.6, lo que da una curvatura de 1.42 por metro y una apertura de 128 mm en la punta de un pétalo de 425 mm; con capas iguales (m = n = 1) la curvatura sería 4.62 por metro, así que el resultado depende mucho del laminado. Láminas muy delgadas se mueven con rapidez pero resisten poco al viento, mientras que piezas más gruesas se curvan menos y con más fuerza. Los diseñadores podrían usar modelos de elementos finitos para elegir la orientación de las vetas; el folio no corrió ninguno. Son valores de modelo: no se construyó ni se probó ningún pétalo.'}
