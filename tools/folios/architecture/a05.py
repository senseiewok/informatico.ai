#!/usr/bin/env python3
"""Folio A.05 (ARCHITECTURE): Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68)."""
from __future__ import annotations

SLUG = 'a05'

PILLAR = 'architecture'

FOLIO = {'folio_id': 'A.05',
 'slug': 'a05',
 'pillar': 'architecture',
 'category_code': 'A',
 'title': 'Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68)',
 'subtitle': "How Wallace Sabine's reverberation law, Carl Eyring's logarithmic absorption, and Manfred Schroeder's "
             'prime-sequence coffers can be used to design rooms where speech is easier to understand.',
 'date_published': '2026-11-01',
 'date_redated': '2026-11-14',
 'current_edition': 'REV 1.2',
 'status_badge': 'REDATED REV 1.2',
 'primary_kernel': 'tools/tectonic_verify.py',
 'colophon': {'identifier': 'A.05 · Architectural Acoustics · CSI 09 84 00',
              'kernels': 'T_60,Eyring = 0.62 s (model) · STI = 0.74 (illustrative)',
              'benchmarks': 'Model values: V = 2,400 m³, S ≈ 1,075 m², α_bar = 0.44 → Eyring 0.62 s, Sabine 0.82 s',
              'bridge': 'Quieter, Clearer Rooms ↔ CF Clinic Conversations (context only)'},
 'sliders': [{'label': 'Mean Acoustic Absorption Coefficient (α_bar)',
              'min': 0.12,
              'max': 0.72,
              'step': 0.02,
              'value': 0.44,
              'unit': 'α_bar = '},
             {'label': 'Schroeder QRD Prime Modulus (p_QRD)',
              'min': 5,
              'max': 23,
              'step': 2,
              'value': 13,
              'unit': 'p = '}],
 'steps': ['Stage 1 (Direct & Early Reflections 0–50 ms): Vault geometry directs early energy to listeners within the '
           'first 50 ms (an illustrative early clarity C_50 = +4.8 dB, not computed here).',
           'Stage 2 (Schroeder Quadratic-Residue Diffusion): Coffered timber wells of depth d_n = (n² mod p)·λ/(2p) '
           'spread reflections across many directions instead of one mirror-like bounce.',
           'Stage 3 (Micro-Perforated Helmholtz Absorption): 0.8 mm perforated timber veneer over mineral wool, with an '
           'assumed mean absorption α_bar = 0.44.',
           'Stage 4 (Eyring Decay): For V = 2,400 m³ and an assumed surface area S ≈ 1,075 m², T_60,Eyring = 0.161 × '
           '2,400 / (−1,075 × ln 0.56) = 0.62 s (Sabine gives 0.82 s). The STI of 0.74 is an illustrative value, not '
           'a measurement.'],
 'readouts': [{'label': 'Eyring Reverberation T_60 (Model)', 'value': '0.62 s (vs 1.85 s illustrative untreated)'},
              {'label': 'Speech Transmission Index (Illustrative)', 'value': '0.74 (folio target ≥ 0.68)'},
              {'label': 'Early Clarity Index C_50 (Illustrative)', 'value': '+4.8 dB'},
              {'label': 'Folio Design Targets (Model)', 'value': 'ILLUSTRATIVE VALUES VS FOLIO TARGETS (NOT MEASURED)'}],
 'sidenote_1': {'kicker': 'SIDENOTE A.05-A · EYRING VS SABINE',
                'body': "In highly absorptive rooms Sabine's formula gives longer reverberation times than Eyring's "
                        "-S·ln(1 - α_bar) form, which is generally the better estimate there (Eyring 1930, DOI "
                        '10.1121/1.1915175). Both rest on a diffuse-field assumption.'},
 'sidenote_2': {'kicker': 'SIDENOTE A.05-B · SPECIFICATION PLATE · CSI 09 84 00',
                'body': 'Design proposal, not a tested product: micro-perforated oak acoustic coffers (0.8 mm apertures '
                        'at 4 mm pitch) with a design target of NRC = 0.85; fire classification under EN 13501-1 would '
                        'need testing.'},
 'skill': {'filename': 'tectonic-acoustics-sabine-eyring-SKILL.md',
           'name': 'tectonic-acoustics-sabine-eyring',
           'description': 'AI-agnostic architectural acoustics skill for Sabine/Eyring reverberation, Schroeder QRD '
                          'coffered vaults, and the IEC 60268-16 Speech Transmission Index (STI).',
           'rules': ['Compute both Sabine T_60 = 0.161 V / A and Eyring T_60 = 0.161 V / (-S ln(1 - alpha_bar)) across '
                     '125 Hz - 4 kHz octave bands.',
                     'Size Schroeder quadratic-residue diffuser wells via d_n = (n^2 mod p) * c / (2 p f_0) to prevent '
                     'focal caustics under curved vaults.',
                     'Use the folio\'s own design targets of STI >= 0.68 and background noise <= NC-28 for consultation '
                     'rooms and civic halls (folio targets, not requirements of a cited standard).']},
 'revisions': [{'edition': 'REV 1.2',
                'date': '2026-11-14',
                'summary': 'REV 1.2 (Redated 2026-11-14): Grounding revision. The Sabine comparison is corrected from '
                           '0.73 s to 0.82 s (it follows from the same room as the Eyring 0.62 s), STI 0.74 and C_50 '
                           '+4.8 dB are labelled illustrative, and claims of ISO 3382 certification, a 40% alarm-fatigue '
                           'effect and protection for CF patients are withdrawn. The Eyring and Schroeder DOIs pointed to '
                           'a one-page supplement item and a different 1975 paper; they now cite DOI 10.1121/1.1915175 and DOI '
                           '10.1121/1.382601. The midnight scene is replaced by a plain account. A later review '
                           'corrected the Speech Transmission Index attribution (IEC 60268-16, not ISO 3382), '
                           'made the NC-28 threshold consistent, softened outcome claims in the plain-language and '
                           'Spanish text, and changed the readout verdict and the Scite record.',
                'opus': 'Review: references checked by DOI in Crossref and the Scite index; Scite literature supports '
                        'that Eyring gives shorter times than Sabine in absorptive rooms.'},
               {'edition': 'REV 1.1',
                'date': '2026-11-02',
                'summary': 'REV 1.1 (Redated 2026-11-02): Added Eyring decay T_60 = 0.62 s and an STI value with '
                           'Schroeder prime QRD diffusion and a portable companion skill.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'and ISO 3382 compliance wording is withdrawn in REV 1.2: nothing was measured.'},
               {'edition': 'REV 1.0',
                'date': '2026-11-01',
                'summary': 'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph on Sabine-Eyring reverberation, '
                           'Schroeder QRD timber vaults, and clinical speech intelligibility.',
                'opus': 'Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier \'verified\' '
                        'wording is withdrawn in REV 1.2.'}],
 'governing_law': 'T_60 = 0.161V / [−S ln(1−α)] · STI = 0.74',
 'volume': 3,
 'volume_code': 'VOL. 03',
 'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1121/1.1915175',
           'fetched_on': '2026-11-08',
           'citing_publications': 146,
           'supporting': 1,
           'mentioning': 31,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Eyring, Reverberation time in dead rooms (DOI 10.1121/1.1915175). The citation counts shown were taken on 2026-11-08 for an earlier record, a one-page 1930 supplement item by Eyring (DOI 10.1121/1.1901884), and have not been refreshed for this DOI. Neither record checks this folio\'s numbers.'}}

LONGFORM_DATA = {'reading_time': '22 MIN READ',
 'word_count': '4,650 WORDS',
 'scite': {'doi': '10.1121/1.1915175',
           'fetched_on': '2026-11-08',
           'citing_publications': 146,
           'supporting': 1,
           'mentioning': 31,
           'contrasting': 0,
           'retracted': False,
           'summary': 'Eyring, Reverberation time in dead rooms (DOI 10.1121/1.1915175). The citation counts shown were taken on 2026-11-08 for an earlier record, a one-page 1930 supplement item by Eyring (DOI 10.1121/1.1901884), and have not been refreshed for this DOI. Neither record checks this folio\'s numbers.'},
 'act1_title': "Act I — Wallace Sabine's Midnight Cushions at Harvard and the Physics of Clear Speech",
 'act1_dropcap': 'In 1895 Harvard asked Wallace Clement Sabine, a young physics instructor, to improve the lecture room '
                 'of the new Fogg Art Museum, where speech was hard to follow because sound lingered too long. Sabine '
                 'measured how long the sound of an organ pipe stayed audible after it stopped, adding and removing '
                 'seat cushions to change the absorption in the room, and worked at night when the city was quieter. '
                 'From those measurements he arrived at the relation between room volume, absorption and reverberation '
                 'time that bears his name; his papers were later collected in his Collected Papers on Acoustics '
                 '(1922).',
 'act1_body': "Sabine's work showed that reverberation time grows with room volume and falls as total absorption grows. In 1930 Carl F. Eyring refined this for highly absorptive rooms, treating the decay as a series of reflections that each lose a fraction of the energy (Journal of the Acoustical Society of America, DOI 10.1121/1.1915175). In 1975 Manfred Schroeder proposed diffusers based on maximum-length sequences (DOI 10.1121/1.380425), and in 1979 he described quadratic-residue diffusers, whose well depths follow n² mod p for a prime p and which spread reflected sound across many directions (JASA, DOI 10.1121/1.382601). ISO 3382-1 describes how to measure room acoustic parameters, and IEC 60268-16 describes the Speech Transmission Index. A reader could model such rooms with a finite-element library such as FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI 10.1145/3524456), or check the quadratic-residue sequence in a proof assistant library such as leanprover-community/mathlib4 (DOI 10.1145/3372885.3373824); this folio did neither, and its reverberation numbers come from the Eyring formula shown.",
 'pullquote': 'Reverberation is not only an aesthetic matter: when sound lingers, one syllable can mask the next '
              'and speech becomes harder to follow.',
 'chronology': [('1895–1900',
                 "Wallace Clement Sabine studies the Fogg lecture room at Harvard and arrives at the reverberation "
                 'relation T_60 = 0.161 V / A; he later advised on Boston Symphony Hall (opened 1900).'),
                ('1930',
                 'Carl F. Eyring publishes a logarithmic reverberation formula for highly absorptive rooms (DOI '
                 '10.1121/1.1915175).'),
                ('1979',
                 'Manfred R. Schroeder describes quadratic-residue diffusers based on prime modular arithmetic (DOI '
                 '10.1121/1.382601).'),
                ('2009',
                 'ISO 3382-1 sets out measurement of room acoustic parameters for performance spaces; the Speech '
                 'Transmission Index itself is defined in IEC 60268-16. The STI >= 0.68 and NC-28 used here are the '
                 "folio's own targets.")],
 'act2_title': 'Act II — How It Actually Works: Eyring Decay + Early-to-Late Energy Ratio C_50',
 'act2_intuition': 'Human speech intelligibility depends on the ratio between early sound arriving within the '
                   '50-millisecond Haas integration window and late reverberant energy that masks consonants. When '
                   "mean surface absorption is high, Sabine's formula gives longer decay times than Carl Eyring's "
                   'logarithmic formulation, T_60 = 0.161 * V / [-S * ln(1 - alpha_bar)], which is generally the '
                   'better estimate there (JASA, DOI 10.1121/1.1915175). Manfred Schroeder showed that ceiling wells '
                   'with depths d_n = (c / [2 f_0 p]) * (n^2 mod p) give reflection phases whose Fourier transform has '
                   'a flat power spectrum, so in theory the reflected energy is spread evenly over the diffraction '
                   'orders within the design band (JASA, DOI 10.1121/1.382601). In this folio\'s model hall, V = 2,400 '
                   'cubic meters, an assumed surface area S of about 1,075 square meters and alpha_bar = 0.44 give '
                   'T_60,Eyring = 0.62 seconds (Sabine gives 0.82 seconds for the same room). The early clarity C_50 = '
                   '+4.8 decibels and STI = 0.74 are illustrative values, not computed or measured, and no '
                   'certification is claimed.',
 'act2_analogy': 'Everyday analogy: Reading text through a greasy, smudged magnifying glass is like trying to listen '
                 'in a reverberant hall. Early sound reflections arriving within fifty milliseconds are like sharp '
                 'reading glasses that bring each letter into focus. But late-arriving echoes are like smeared '
                 'fingerprints on the lens, smudging every consonant into a muddy blur. Diffusive coffered vaults act '
                 'like lens cleaners: they scatter disruptive reflections while keeping every spoken word crisp and '
                 'clear.',
 'walkthrough': ['Experiment 1 (Sabine vs. Eyring Divergence): Compare Sabine T_60 = 0.82 s against Eyring T_60 = 0.62 '
                 's at average absorption alpha_bar = 0.44 in a V = 2,400 m^3 vaulted hall with S of about 1,075 m^2.',
                 'Experiment 2 (Absorption and Prime Modulus): Move the alpha_bar slider to see the Eyring time change, '
                 'and the prime modulus p to change the quadratic-residue well pattern.',
                 'Experiment 3 (Speech Transmission Index): The STI shown is an illustrative mapping from T_60, not a '
                 "measurement; compare it with the folio's own target of 0.68."],
 'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification Bridge',
 'act4_human_ai': 'A designer, with or without an AI assistant, could use acoustic ray-tracing and wave solvers, for '
                  'example built on a finite-element library such as FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, '
                  'DOI 10.1145/3524456), to shape timber coffers so seats receive more even early reflections, and could '
                  'check the quadratic-residue sequence in a proof library such as leanprover-community/mathlib4 (DOI '
                  '10.1145/3372885.3373824). Any real hall would then be measured to ISO 3382-1. This folio names those '
                  'tools as options; it did not run them.',
 'cf_bridge': 'A modest bridge. In Cystic Fibrosis clinics, patients and clinicians may talk through masks and '
              'over equipment noise, and noisy, reverberant rooms make speech harder to follow for anyone. Measured '
              'hospital noise levels have been reported well above World Health Organization guideline values '
              '(Busch-Vishniac et al. 2005, DOI 10.1121/1.2118327). This folio is a room-acoustics study: it reports no clinical outcome and is not medical advice; '
              'people with CF should follow their care team.',
 'sources': ['Sabine, W. C. (1922). Collected Papers on Acoustics. Harvard University Press.',
             'Eyring, C. F. (1930). Reverberation time in "dead" rooms. Journal of the Acoustical Society of America, '
             '1(2A), 217–241. DOI: 10.1121/1.1915175.',
             'Schroeder, M. R. (1975). Diffuse sound reflection by maximum-length sequences. Journal of the Acoustical '
             'Society of America, 57(1), 149–150. DOI: 10.1121/1.380425.',
             'Schroeder, M. R. (1979). Binaural dissimilarity and optimum ceilings for concert halls: More lateral '
             'sound diffusion. Journal of the Acoustical Society of America, 65(4), 958–963. DOI: 10.1121/1.382601.',
             'ISO 3382-1:2009. Acoustics — Measurement of room acoustic parameters — Part 1: Performance spaces. IEC '
             '60268-16: Sound system equipment — Objective rating of speech intelligibility by speech transmission '
             'index. FGI Guidelines for Design and Construction of Hospitals (named as context; no threshold here is '
             'taken from them).',
             'Busch-Vishniac, I. J., West, J. E., Barnhill, C., Hunter, T., Orellana, D., & Chivukula, R. (2005). Noise '
             'levels in Johns Hopkins Hospital. Journal of the Acoustical Society of America, 118(6), 3629–3645. DOI: '
             '10.1121/1.2118327.',
             'The mathlib Community (2020). The Lean mathematical library. Proceedings of the 9th ACM SIGPLAN '
             'International Conference on Certified Programs and Proofs, 367–381. DOI: 10.1145/3372885.3373824.',
             'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of Arbitrary Order '
             'Finite Element Degree-of-Freedom Maps on Polygonal and Polyhedral Cell Meshes (FEniCS/dolfinx, '
             'https://github.com/FEniCS/dolfinx). ACM Transactions on Mathematical Software, 48(2), 18:1–18:23. DOI: '
             '10.1145/3524456.'],
 'svg': '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Sabine vs Eyring reverberation decay '
        'and Schroeder coffered vault STI=0.74">\n'
        '            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" stroke-opacity="0.4"/>\n'
        '            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" stroke-opacity="0.4"/>\n'
        '            <path d="M 60 35 L 560 182" fill="none" stroke="var(--tp-minium)" stroke-width="2" '
        'stroke-dasharray="5,4"/>\n'
        '            <path d="M 60 35 L 365 182" fill="none" stroke="var(--tp-verdigris)" stroke-width="3"/>\n'
        '            <rect x="60" y="35" width="95" height="150" fill="var(--tp-prussian)" fill-opacity="0.12"/>\n'
        '            <text x="68" y="55" font-size="11" fill="var(--tp-prussian)">Early (0–50 ms)</text>\n'
        '            <text x="68" y="72" font-size="11" fill="var(--tp-prussian)">C_50 = +4.8 dB (illus.)</text>\n'
        '            <text x="330" y="135" font-size="11" fill="var(--tp-verdigris)">Model Vault: T_60 = '
        '0.62 s · STI 0.74 (illus.)</text>\n'
        '            <text x="415" y="102" font-size="11" fill="var(--tp-minium)">Illustrative Plaster Hall: T_60 = 1.85 '
        's</text>\n'
        '            <text x="235" y="204" font-size="11" fill="currentColor">Impulse Decay Time t (ms) · -60 dB '
        'Threshold (CSI 09 84 00)</text>\n'
        '          </svg>',
 'history_lead': 'In 1895 Harvard asked Wallace Clement Sabine, a young physics instructor, to improve the lecture room '
                 'of the new Fogg Art Museum, where speech was hard to follow because sound lingered too long. Sabine '
                 'measured how long the sound of an organ pipe stayed audible after it stopped, adding and removing '
                 'seat cushions to change the absorption in the room, and worked at night when the city was quieter. '
                 'From those measurements he arrived at the relation between room volume, absorption and reverberation '
                 'time that bears his name; his papers were later collected in his Collected Papers on Acoustics '
                 '(1922).',
 'act1_plain_bridge': 'We have all experienced how unpleasant it is to talk inside a bare tiled bathroom or a noisy '
                      'cafeteria. When you speak, your voice bounces wildly off hard walls, creating echoes that '
                      'linger and collide with the very next word you say. Listening in a room with too much echo is '
                      'like reading a book where every line of print has been stamped twice, blurring the letters '
                      'together. In hospitals, school classrooms, and lecture auditoriums, excessive echo is tiring '
                      'and makes simple conversations difficult to follow. Good acoustic '
                      'design acts like a pair of reading glasses for your ears. By sculpting ceiling surfaces with '
                      'specialized wooden grooves and hidden sound-absorbing padding, architects catch and tame those '
                      'wandering sound waves. The aim is a room where the voice of a doctor, teacher, or friend is '
                      'easier to follow. This folio models reverberation time only and does not measure how well anyone understands speech.',
 'history_body': "Sabine's work showed that reverberation time grows with room volume and falls as total absorption grows. In 1930 Carl F. Eyring refined this for highly absorptive rooms, treating the decay as a series of reflections that each lose a fraction of the energy (Journal of the Acoustical Society of America, DOI 10.1121/1.1915175). In 1975 Manfred Schroeder proposed diffusers based on maximum-length sequences (DOI 10.1121/1.380425), and in 1979 he described quadratic-residue diffusers, whose well depths follow n² mod p for a prime p and which spread reflected sound across many directions (JASA, DOI 10.1121/1.382601). ISO 3382-1 describes how to measure room acoustic parameters, and IEC 60268-16 describes the Speech Transmission Index. A reader could model such rooms with a finite-element library such as FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI 10.1145/3524456), or check the quadratic-residue sequence in a proof assistant library such as leanprover-community/mathlib4 (DOI 10.1145/3372885.3373824); this folio did neither, and its reverberation numbers come from the Eyring formula shown.",
 'act1_stakes': 'Historically, master builders relied on ornate classical plaster moldings, heavy velvet draperies, '
                'and deeply coffered basilican ceilings to temper acoustic reverberation without understanding the '
                'underlying physics. However, when twentieth-century modernism stripped away ornamental surfaces in '
                'favor of vast expanses of smooth bare plaster, polished terrazzo, and monolithic glass, public spaces '
                'could become hard to speak in. When reverberation is long in a consultation room or lecture hall, '
                'the vowel sounds of one syllable overlap and mask the quieter consonant sounds of the next. Conversely, covering an entire room with '
                'generic porous foam creates a dead, oppressive acoustic vacuum that feels claustrophobic and '
                'unnatural. Acoustic engineering must achieve a delicate equilibrium: absorbing excess sound energy '
                'while scattering early reflections to preserve vocal warmth.',
 'act2_plain_primer': 'In the interactive laboratory below, you control two primary knobs that calibrate the acoustic '
                      'clarity of a vaulted civic hall. The first knob adjusts the average absorption coefficient of '
                      'the interior surfaces. When this slider sits at low values, sound bounces repeatedly off hard '
                      'walls, creating a long, echoing tail that drowns out spoken consonants. As you slide it higher '
                      'by introducing micro-perforated wood paneling backed by acoustic insulation, sound energy is '
                      'absorbed more rapidly, shortening the reverberation time. '
                      'The second knob sets the mathematical prime number that governs the depth pattern of the wooden '
                      'ceiling coffers. Increasing this prime modulus creates a richer, more diverse sequence of well '
                      'depths across the vault. In theory, this sequence spreads reflected sound evenly over the diffraction '
                      'orders in the design band, like a prism splitting light; the folio does not measure how well a real '
                      'room would do this.',
 'distill_diagram': {'analogy_title': 'Early Acoustic Clarity vs Echo Blur',
                     'analogy_sub': 'Early reflections sharpen speech; late reverberation smears words',
                     'force_a_title': 'Mean Absorption (α_bar)',
                     'force_a_sub': 'Lined timber cavities soak up late decay energy, lowering T_60',
                     'force_b_title': 'Schroeder Prime Modulus (p)',
                     'force_b_sub': 'Number-theoretic wells scatter sound waves across wide angles',
                     'threshold_title': 'Speech Transmission Index (STI >= 0.68, folio target)',
                     'threshold_pass': 'Folio targets: STI >= 0.68 and NC-28; consonants easier to follow',
                     'threshold_fail': 'Echoes mask consonants; speech smeared'},
 'intuition_lead': 'Human speech intelligibility depends on the ratio between early sound arriving within the '
                   '50-millisecond Haas integration window and late reverberant energy that masks consonants. When '
                   "mean surface absorption is high, Sabine's formula gives longer decay times than Carl Eyring's "
                   'logarithmic formulation, T_60 = 0.161 * V / [-S * ln(1 - alpha_bar)], which is generally the '
                   'better estimate there (JASA, DOI 10.1121/1.1915175). Manfred Schroeder showed that ceiling wells '
                   'with depths d_n = (c / [2 f_0 p]) * (n^2 mod p) give reflection phases whose Fourier transform has '
                   'a flat power spectrum, so in theory the reflected energy is spread evenly over the diffraction '
                   'orders within the design band (JASA, DOI 10.1121/1.382601). In this folio\'s model hall, V = 2,400 '
                   'cubic meters, an assumed surface area S of about 1,075 square meters and alpha_bar = 0.44 give '
                   'T_60,Eyring = 0.62 seconds (Sabine gives 0.82 seconds for the same room). The early clarity C_50 = '
                   '+4.8 decibels and STI = 0.74 are illustrative values, not computed or measured, and no '
                   'certification is claimed.',
 'act2_deepening': 'The physical interplay between boundary absorption and number-theoretic diffusion reveals why '
                   "high-performance acoustic architecture cannot rely on absorption alone. In Eyring's logarithmic "
                   'denominator, as average absorption alpha_bar approaches unity, the decay time asymptotically '
                   "plunges toward zero. Conversely, Schroeder's quadratic residue "
                   'diffuser operates as an energy-conserving phase grating: it does not destroy acoustic energy, but '
                   'redistributes specular reflections into a diffuse, enveloping sound field across design frequency '
                   'band [f_0, (p - 1) f_0]. Selecting a higher prime modulus p raises the upper edge (p - 1) f_0 of that band '
                   'and gives more distinct well depths per period. The folio pairs the diffusers with micro-perforated '
                   'timber veneers over mineral wool, whose sub-millimeter apertures act as Helmholtz-type resonators; the '
                   'mean absorption alpha_bar = 0.44 is an assumed value, and no speech benefit is measured here.',
 'act4_deepening': 'A proposal for practice: instead of running ray-tracing only after the room geometry is frozen, '
                   'wave solvers could be built into parametric modeling tools, so that as a designer adjusts vault '
                   'curvature, an assistant estimates speech transmission at many virtual listener positions and '
                   'suggests well depths. Any such estimate would still need measurement in the finished room. At the material scale, a proposal: robotic laser-drilling systems could modulate '
                   'micro-perforation density across timber veneers to target specific room resonant modes. The open '
                   'frontier question explores active metamaterial surfaces: can electro-pneumatic or piezoelectric '
                   'ceiling coffers dynamically adjust their cavity depth in real time, shifting room acoustics from a '
                   'crisp 0.5-second lecture hall into a lush 1.8-second choral sanctuary at the touch of a button, '
                   'creating completely adaptive acoustic environments for future civic halls?'}

PLATE_CAPTION = {'alt': 'Conceptual visualization imagining what a timber and limestone coffered vault sculpted with Manfred Schroeder '
        'prime-sequence acoustic diffuser wells would look like (artistic impression, not a measured structure)',
 'caption': 'Conceptual Vision Plate A.05-V (Imagining What It Would Look Like) · Artistic interior visualization '
            "imagining a limestone and oak coffered ceiling sculpted to Manfred Schroeder's prime-sequence quadratic "
            'residue depths.'}

DISPATCH = {'kicker': 'FRONTIER ACOUSTICS DISPATCH · NUMBER-THEORETIC SCHROEDER DIFFUSERS & ROOM-ACOUSTIC MODELLING',
 'headline': 'Prime-Sequence Quadratic Residue Coffered Vaults: A Reverberation Model for Clearer Speech',
 'body': "Combining Carl Eyring's logarithmic reverberation law (JASA DOI 10.1121/1.1915175) with Manfred Schroeder's "
         'prime-sequence quadratic residue diffusers (JASA DOI 10.1121/1.382601), this folio models a 2,400 m³ vault '
         'with T_60 = 0.62 s and shows an illustrative Speech Transmission Index of 0.74. It measured no room and '
         'makes no health claim.'}

META_3D = ('Schroeder Prime-Sequence (p=17) Acoustic Diffuser',
 'X: Quadratic Residue Well Index n · Z: Concert Vault Span · Y: Phase-Grating Well Depth d_n')

ES_TRANSLATION = {'title_es': 'Reverberación Acústica de Sabin–Eyring, Bóvedas Difusoras de Residuo Cuadrático y Claridad del Habla '
             '(STI ≥ 0.68)',
 'subtitle_es': 'Cómo la ley de reverberación de Wallace Sabine, la absorción logarítmica de Carl Eyring y los '
                'casetones de números primos de Manfred Schroeder sirven para diseñar salas donde la voz se entiende '
                'mejor.',
 'why_es': 'Escuchar en una sala con eco es como leer un texto borroso: las reflexiones tempranas (0–50 ms) enfocan '
           'cada sílaba, mientras que las reverberaciones tardías la vuelven ininteligible.',
 'bridge_es': 'En las clínicas de Fibrosis Quística, pacientes y personal pueden hablar a través de cubrebocas y con ruido '
              'de equipos, y las salas ruidosas y reverberantes dificultan entender el habla a cualquier persona. Se han '
              'reportado niveles de ruido hospitalario muy por encima de los valores guía de la Organización Mundial de la '
              'Salud (Busch-Vishniac et al. 2005, DOI 10.1121/1.2118327). Esta ficha es un estudio de acústica, no reporta '
              'resultados clínicos y no es consejo médico; las personas con Fibrosis Quística deben seguir las '
              'indicaciones de su equipo de atención.',
 'plain_es': 'Todos hemos experimentado lo incómodo que resulta conversar dentro de una habitación vacía con azulejos '
             'o en una cafetería ruidosa. Cuando hablamos, la voz rebota una y otra vez en las superficies duras, '
             'generando un eco molesto que se encalla y borra las palabras que siguen. Escuchar en un salón con '
             'demasiada reverberación es como leer un libro donde cada renglón ha sido impreso dos veces, volviendo '
             'las letras borrosas e incomprensibles. En hospitales, aulas y auditorios, el exceso '
             'de eco cansa y dificulta seguir conversaciones sencillas. Un buen diseño '
             'acústico funciona como unos anteojos de lectura para nuestros oídos. Al esculpir los techos con ranuras '
             'especiales de madera y colocar relleno absorbente oculto, los arquitectos buscan atrapar '
             'y domar esas ondas sonoras errantes. El objetivo es una sala donde la voz de un médico, profesor o amigo sea más '
             'fácil de seguir. Este folio modela solo el tiempo de reverberación y no mide qué tan bien entiende nadie el habla.',
 'deep_es': 'El diseño acústico de una sala abovedada depende del equilibrio preciso entre dos variables: el '
            'coeficiente de absorción promedio y la difusión por residuos cuadráticos de Schroeder. La fórmula de Carl '
            'Eyring en general estima mejor que la de Sabine el tiempo de reverberación en recintos con alta absorción. En la sala '
            'modelo de esta ficha (2,400 m³, unos 1,075 m² de superficie y absorción media de 0.44), Eyring da 0.62 s '
            'y Sabine 0.82 s. '
            'Paralelamente, los casetones de madera basados en números primos reflejan las ondas sonoras en múltiples '
            'direcciones; en teoría, la energía reflejada se reparte con la misma intensidad entre los órdenes de '
            'difracción dentro de la banda de diseño. Un proyectista podría modelar estas superficies con simulaciones en computadora y después '
            'medir la sala terminada según ISO 3382-1. El Índice de Transmisión del Habla de 0.74 que muestra la ficha '
            'es ilustrativo, y la meta de 0.68 es propia de la ficha, no de una norma.'}
