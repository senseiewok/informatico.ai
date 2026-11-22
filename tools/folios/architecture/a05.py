#!/usr/bin/env python3
"""Folio A.05 (ARCHITECTURE): Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68)."""
from __future__ import annotations

SLUG = 'a05'

PILLAR = 'architecture'

_SCITE_RECORD = {
    'doi': '10.1121/1.1915175',
    'fetched_on': '2026-11-21',
    'citing_publications': 217,
    'supporting': 4,
    'mentioning': 84,
    'contrasting': 0,
    'retracted': False,
    'summary': (
        'Scite index entry for Eyring, Reverberation Time in "Dead" Rooms (DOI 10.1121/1.1915175), '
        'checked 2026-11-21: 217 citing publications (4 supporting, 84 mentioning, 0 contrasting) '
        "and no retraction notice. Does not check this folio's numbers."
    ),
}

FOLIO = {
    'folio_id': 'A.05',
    'slug': 'a05',
    'pillar': 'architecture',
    'category_code': 'A',
    'title': 'Acoustic Sabin–Eyring Reverberation, Diffusive Coffered Vaults, and Speech Intelligibility (STI ≥ 0.68)',
    'subtitle': (
        "How Wallace Sabine's reverberation law, Carl Eyring's logarithmic absorption, and Manfred Schroeder's "
        'prime-sequence coffers can be used to design rooms where speech is easier to understand.'
    ),
    'date_published': '2026-11-01',
    'date_redated': '2026-11-14',
    'current_edition': 'REV 1.2',
    'status_badge': 'REDATED REV 1.2',
    'primary_kernel': 'tools/tectonic_verify.py',
    'colophon': {
        'identifier': 'A.05 · Architectural Acoustics · CSI 09 84 00',
        'kernels': 'T_60,Eyring = 0.62 s (model) · STI = 0.74 (illustrative)',
        'benchmarks': 'Model values: V = 2,400 m³, S ≈ 1,075 m², α_bar = 0.44 → Eyring 0.62 s, Sabine 0.82 s',
        'bridge': 'Quieter, Clearer Rooms',
    },
    'sliders': [
        {
            'label': 'Mean Acoustic Absorption Coefficient (α_bar)',
            'min': 0.12,
            'max': 0.72,
            'step': 0.02,
            'value': 0.44,
            'unit': 'α_bar = ',
        },
        {
            'label': 'Schroeder QRD Prime Modulus (p_QRD)',
            'min': 5,
            'max': 23,
            'step': 2,
            'value': 13,
            'unit': 'p = ',
        },
    ],
    'steps': [
        'Stage 1 (Early Window, Bradley 1986, DOI 10.1121/1.393907): Sound within 50 ms aids speech; '
        'C_50 = +4.8 dB is an illustrative estimate.',
        'Stage 2 (Schroeder Diffusion, DOI 10.1121/1.382601): For prime p and design wavelength λ_0 = c/f_0, '
        'well depths d_n = (n² mod p)·λ_0/(2p) scatter reflections.',
        'Stage 3 (Perforated Veneer, cf. Maa 1998, DOI 10.1121/1.423870): Maa models fiber-free air-cavity '
        'panels; this untested sketch backs 0.8 mm oak veneer with wool (assumed α_bar = 0.44).',
        'Stage 4 (Eyring Decay, DOI 10.1121/1.1915175): For V = 2,400 m³ and S ≈ 1,075 m², Eyring gives 0.62 s '
        '(Sabine 0.82 s); STI = 0.74 is a linear estimate, not an MTF value (DOI 10.1121/1.384464).',
    ],
    'readouts': [
        {'label': 'Eyring Reverberation T_60 (Model)', 'value': '0.62 s (vs 1.85 s illustrative untreated)'},
        {'label': 'Speech Transmission Index (Illustrative)', 'value': '0.74 (folio target ≥ 0.68)'},
        {'label': 'Early Clarity Index C_50 (Illustrative)', 'value': '+4.8 dB'},
        {'label': 'Folio Design Targets (Model)', 'value': 'ILLUSTRATIVE VALUES VS FOLIO TARGETS (NOT MEASURED)'},
    ],
    'sidenote_1': {
        'kicker': 'SIDENOTE A.05-A · EYRING VS SABINE',
        'body': (
            "In absorptive rooms Sabine's formula predicts longer decay than Eyring's "
            '-S·ln(1 - α_bar) estimate (Eyring 1930, DOI 10.1121/1.1915175) under stated assumptions.'
        ),
    },
    'sidenote_2': {
        'kicker': 'SIDENOTE A.05-B · SPECIFICATION PLATE · CSI 09 84 00',
        'body': (
            'Untested design proposal: 0.8 mm perforated oak coffers at 4 mm pitch over mineral wool '
            '(cf. Maa 1998, DOI 10.1121/1.423870), targeting about NRC = 0.85; EN 13501-1 fire rating not yet tested.'
        ),
    },
    'skill': {
        'filename': 'tectonic-acoustics-sabine-eyring-SKILL.md',
        'name': 'tectonic-acoustics-sabine-eyring',
        'description': (
            'AI-agnostic architectural acoustics skill for Sabine/Eyring reverberation, Schroeder QRD '
            'coffered vaults, and the IEC 60268-16 Speech Transmission Index (STI).'
        ),
        'rules': [
            'Estimate SI-unit Sabine T_60 = 0.161 V / A and Eyring logarithmic decay '
            'T_60 = 0.161 V / (-S ln(1 - alpha_bar)) (after Eyring 1930, DOI 10.1121/1.1915175) for volume V and area S.',
            'Size Schroeder diffuser wells for prime p via d_n = (n^2 mod p) * c / (2 p f_0) '
            'under curved vaults (Schroeder 1979, DOI 10.1121/1.382601).',
            "Apply the folio's own targets of STI >= 0.68 and noise <= NC-28 as model caveats, "
            'not requirements of IEC 60268-16 or ISO 3382-1.',
        ],
    },
    'revisions': [
        {
            'edition': 'REV 1.2',
            'date': '2026-11-14',
            'summary': (
                'REV 1.2 (Redated 2026-11-14): Grounding revision. Sabine is corrected from 0.73 s to 0.82 s '
                '(same room as Eyring 0.62 s), STI 0.74 and C_50 +4.8 dB are labeled illustrative estimates, '
                'and earlier ISO 3382 rating and alarm-fatigue claims are withdrawn. Eyring and the 1979 QRD '
                'diffuser now cite DOI 10.1121/1.1915175 and DOI 10.1121/1.382601, STI cites IEC 60268-16, '
                'NC-28 is aligned, and the readout verdict and Scite note are updated.'
            ),
            'opus': (
                'Review: references checked by DOI in Crossref and the Scite index; Scite literature suggests '
                'that Eyring estimates shorter decay than Sabine in absorptive rooms.'
            ),
        },
        {
            'edition': 'REV 1.1',
            'date': '2026-11-02',
            'summary': (
                'REV 1.1 (Redated 2026-11-02): Added Eyring decay T_60 = 0.62 s and an STI value with '
                'Schroeder prime QRD diffusion and a portable companion skill.'
            ),
            'opus': (
                "Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier 'verified' "
                'and ISO 3382 compliance wording is withdrawn in REV 1.2: nothing was measured.'
            ),
        },
        {
            'edition': 'REV 1.0',
            'date': '2026-11-01',
            'summary': (
                'REV 1.0 (Published 2026-11-01): Initial 5-Act monograph on Sabine-Eyring reverberation, '
                'Schroeder QRD timber vaults, and clinical speech intelligibility.'
            ),
            'opus': (
                "Council review of the model text (Gemini 4 Argon + Qwen 3.8 27B). Its earlier 'verified' "
                'wording is withdrawn in REV 1.2.'
            ),
        },
    ],
    'governing_law': 'T_60 = 0.161V / [−S ln(1−α)] · STI = 0.74',
    'volume': 3,
    'volume_code': 'VOL. 03',
    'reading_time': '22 MIN READ',
    'word_count': '4,650 WORDS',
    'scite': _SCITE_RECORD,
}

LONGFORM_DATA = {
    'reading_time': '22 MIN READ',
    'word_count': '4,650 WORDS',
    'scite': _SCITE_RECORD,
    'act1_title': "Act I — Wallace Sabine's Midnight Cushions at Harvard and the Physics of Clear Speech",
    'act1_dropcap': (
        'Harvard University opened its Fogg Art Museum in 1895 with a semicircular lecture hall where professors '
        'at the lectern could scarcely make a sentence understood. Spoken words hung in the plaster room '
        'for about five and a half seconds, blurring each syllable into the next. Harvard asked Wallace Clement '
        'Sabine, a twenty-seven-year-old physics instructor, to find a remedy. Working after midnight once '
        'Cambridge streetcars fell quiet, Sabine sounded an organ pipe, shut off the wind, and timed the fading '
        'tone with a chronograph. Night after night his assistants carried hundreds of hair-stuffed seat cushions '
        'across from Sanders Theater and placed them on the seats and aisles. More cushions meant a shorter echo, '
        "tracing a clean inverse curve. Sabine's cushion experiments linked room volume, surface absorption, and "
        'decay time, a foundation later gathered in his 1922 Collected Papers on Acoustics.'
    ),
    'act1_plain_bridge': (
        'Anyone who has tried to talk inside a tiled bathroom or a crowded cafeteria knows how tiring lingering '
        "sound can be. Hard walls, ceilings, and floors bounce a speaker's voice back and forth across the room. "
        'Strong vowels keep ringing in the air and may cover up the quiet consonants of the next word. In busy '
        'hospital wards, classrooms, and civic halls, both lingering echo and steady background noise could make '
        'ordinary conversation hard to follow. Architects calm a room in two ways at once. Porous linings soak up '
        'excess sound energy so echoes die out sooner, while stepped wooden ceiling recesses scatter reflections '
        'instead of focusing sharp echoes. This essay estimates reverberation decay from average absorption and '
        'maps that decay to illustrative clarity estimates. It evaluates model formulas only and does not measure '
        'how well any person hears speech in a built room.'
    ),
    'act1_body': (
        'Sabine showed that reverberation grows with volume and falls with absorption. In 1930 Carl F. Eyring '
        'refined that estimate for absorptive rooms via discrete energy-loss reflections (DOI 10.1121/1.1915175). '
        'Manfred Schroeder proposed maximum-length-sequence diffusers in 1975 (DOI 10.1121/1.380425) and prime '
        'quadratic-residue wells in 1979 (DOI 10.1121/1.382601). Herman Steeneken and Tammo Houtgast defined the '
        'Speech Transmission Index in 1980 (DOI 10.1121/1.384464), standardized in IEC 60268-16 beside ISO 3382-1. '
        'A reader could simulate room waves with FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI '
        '10.1145/3524456) or check residues in leanprover-community/mathlib4 (DOI 10.1145/3372885.3373824); '
        'neither simulation was run here.'
    ),
    'act1_stakes': (
        'Hard plaster, glass, and terrazzo leave rooms reflective, while elevated ward noise measured at Johns '
        'Hopkins Hospital by Busch-Vishniac et al. (2005, DOI 10.1121/1.2118327) may add masking. Bradley (1986, '
        'DOI 10.1121/1.393907; DOI 10.1121/1.393908) found that room speech scores track both fifty-millisecond '
        'early-to-late ratios and signal-to-noise ratio. Heavy foam everywhere might deaden speech, whereas bare '
        'vaults focus echoes; pairing absorption with scattering aims to balance decay and early support.'
    ),
    'pullquote': (
        'Reverberation is not only an aesthetic matter: when sound lingers, one syllable can mask the next '
        'and speech becomes harder to follow.'
    ),
    'chronology': [
        (
            '1895–1900',
            'Wallace Clement Sabine measures the Fogg lecture room at Harvard, formulates his inverse '
            'reverberation law, and advises on Boston Symphony Hall (Sabine 1922).',
        ),
        (
            '1930',
            'Carl F. Eyring derives a logarithmic reverberation formula for absorptive rooms '
            '(DOI 10.1121/1.1915175).',
        ),
        (
            '1979–1980',
            'Manfred R. Schroeder proposes prime quadratic-residue ceilings (DOI 10.1121/1.382601); '
            'Steeneken and Houtgast formulate the Speech Transmission Index (DOI 10.1121/1.384464).',
        ),
        (
            '1986–2009',
            'John S. Bradley relates early-to-late ratios and noise to speech intelligibility '
            '(DOI 10.1121/1.393907), preceding ISO 3382-1 and IEC 60268-16.',
        ),
    ],
    'act2_title': 'Act II — How It Actually Works: Eyring Decay + Early-to-Late Energy Ratio C_50',
    'act2_analogy': (
        'Everyday analogy: Listening in an echoey hall feels like reading fine print through a smudged magnifying '
        'glass. Early reflections arriving right after the direct voice sharpen each syllable like a clean lens. '
        'Late echoes smear consonants together. Coffered diffusers and porous linings may clear part of that blur. '
        'The lens comparison stops where room acoustics begins, because sound unfolds over time and background '
        'noise might still mask speech after echoes fade.'
    ),
    'act2_plain_primer': (
        'Two controls drive the interactive model below. Mean Acoustic Absorption Coefficient sets the average '
        'fraction of sound energy absorbed per bounce. At low values, sound lingers off hard walls. Raising '
        'absorption shortens estimated decay time and shifts two linear clarity estimates (with the speech index '
        'clamped at its ends), which are not verified room scores. Schroeder QRD Prime Modulus steps across odd '
        'values from five to twenty-three around prime choices such as thirteen. Moving this second slider updates '
        'the modulus label and scales the three-dimensional relief over a fixed seven-well cycle, without changing '
        'decay time.'
    ),
    'distill_diagram': {
        'analogy_title': 'Early Acoustic Clarity vs Echo Blur',
        'analogy_sub': 'Early reflections sharpen speech; late reverberation smears words',
        'force_a_title': 'Mean Absorption (α_bar)',
        'force_a_sub': 'Lined timber cavities soak up late decay energy, lowering T_60',
        'force_b_title': 'Schroeder Prime Modulus (p)',
        'force_b_sub': 'Number-theoretic wells scatter sound waves across wide angles',
        'threshold_title': 'Speech Transmission Index (STI >= 0.68, folio target)',
        'threshold_pass': 'Folio targets: STI >= 0.68 and NC-28; consonants easier to follow',
        'threshold_fail': 'Echoes mask consonants; speech smeared',
    },
    'act2_intuition': (
        'Bradley (1986, DOI 10.1121/1.393907) reported that speech intelligibility tracks signal-to-noise ratio '
        'and the fifty-millisecond early-to-late ratio C_50. At high absorption, Eyring estimates shorter decay '
        'than Sabine via T_60 = 0.161 * V / [-S * ln(1 - alpha_bar)] (DOI 10.1121/1.1915175). For prime p, '
        'Schroeder depths d_n = (c / [2 f_0 p]) * (n^2 mod p) give a flat discrete Fourier power spectrum in the '
        'design band (DOI 10.1121/1.382601). Under stated assumptions (V = 2,400 m³, about S ≈ 1,075 m², '
        'alpha_bar = 0.44), Eyring gives 0.62 s and Sabine 0.82 s. In the widget, STI (0.74) and C_50 (+4.8 dB) '
        'are linear T_60 estimates, not Steeneken–Houtgast MTF values (DOI 10.1121/1.384464).'
    ),
    'act2_deepening': (
        "As alpha_bar nears one in Eyring's denominator, estimated decay drops toward zero (DOI 10.1121/1.1915175). "
        'A Schroeder diffuser instead acts as a phase grating over [f_0, (p - 1) f_0] for prime p, spreading '
        'reflections across angles (DOI 10.1121/1.382601). Dah-You Maa (1998, DOI 10.1121/1.423870) analyzed '
        'fiber-free micro-perforated panels over air cavities; this untested sketch pairs 0.8 mm perforated veneer '
        'with mineral wool at approximately alpha_bar = 0.44.'
    ),
    'walkthrough': [
        'Experiment 1 (Sabine vs. Eyring): At alpha_bar = 0.44 (V = 2,400 m³, about S ≈ 1,075 m²), compare '
        'Eyring T_60 = 0.62 s with Sabine T_60 = 0.82 s.',
        'Experiment 2 (Absorption vs. Modulus): Move alpha_bar to update Eyring T_60 and linear STI/C_50 '
        'estimates; move p_QRD (odd steps 5–23, prime choices 5, 7, 11, 13, 17, 19, 23) to scale the 3D relief '
        'and label without altering T_60.',
        "Experiment 3 (Folio Caveat): Compare the STI estimate with the folio's 0.68 target; real rooms also "
        'depend on noise (Bradley 1986, DOI 10.1121/1.393908).',
    ],
    'act4_title': 'Act IV — Human + AI Co-Design & the Structural & Civil Engineering Specification Bridge',
    'act4_human_ai': (
        'A designer could simulate room waves in FEniCS/dolfinx (https://github.com/FEniCS/dolfinx, DOI '
        '10.1145/3524456) and check residue sequences in leanprover-community/mathlib4 (DOI '
        '10.1145/3372885.3373824) before ISO 3382-1 field testing. Neither simulation was run here.'
    ),
    'act4_deepening': (
        'Zhu et al. (2017, DOI 10.1103/PhysRevX.7.021034) reported a passive planar metasurface Schroeder diffuser '
        'about one-twentieth of a wavelength thick. An untested question asks whether motorized coffers could '
        'shift a room between about 0.5 s for speech and 1.8 s for music, which is not verified here.'
    ),
    'sources': [
        'Sabine, W. C. (1922). Collected Papers on Acoustics. Harvard University Press.',
        'Eyring, C. F. (1930). Reverberation time in "dead" rooms. J. Acoust. Soc. Am., 1(2A), 217–241. '
        'DOI: 10.1121/1.1915175.',
        'Schroeder, M. R. (1975). Diffuse sound reflection by maximum-length sequences. J. Acoust. Soc. Am., '
        '57(1), 149–150. DOI: 10.1121/1.380425.',
        'Schroeder, M. R. (1979). Binaural dissimilarity and optimum ceilings for concert halls: More lateral '
        'sound diffusion. J. Acoust. Soc. Am., 65(4), 958–963. DOI: 10.1121/1.382601.',
        'Steeneken, H. J. M., & Houtgast, T. (1980). A physical method for measuring speech-transmission quality. '
        'J. Acoust. Soc. Am., 67(1), 318–326. DOI: 10.1121/1.384464.',
        'Bradley, J. S. (1986). Predictors of speech intelligibility in rooms. J. Acoust. Soc. Am., 80(3), '
        '837–845. DOI: 10.1121/1.393907.',
        'Bradley, J. S. (1986). Speech intelligibility studies in classrooms. J. Acoust. Soc. Am., 80(3), '
        '846–854. DOI: 10.1121/1.393908.',
        'Maa, D.-Y. (1998). Potential of microperforated panel absorber. J. Acoust. Soc. Am., 104(5), '
        '2861–2866. DOI: 10.1121/1.423870.',
        'Busch-Vishniac, I. J., et al. (2005). Noise levels in Johns Hopkins Hospital. J. Acoust. Soc. Am., '
        '118(6), 3629–3645. DOI: 10.1121/1.2118327.',
        'Zhu, Y., Fan, X., Liang, B., Cheng, J., & Jing, Y. (2017). Ultrathin acoustic metasurface-based '
        'Schroeder diffuser. Phys. Rev. X, 7(2), 021034. DOI: 10.1103/PhysRevX.7.021034.',
        'ISO 3382-1:2009 & IEC 60268-16; FGI Hospital Guidelines named as context only (STI >= 0.68 and NC-28 '
        'are folio targets).',
        'The mathlib Community (2020). The Lean mathematical library. Proc. CPP, 367–381. '
        'DOI: 10.1145/3372885.3373824.',
        'Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). DOF maps on polyhedral meshes '
        '(FEniCS/dolfinx, https://github.com/FEniCS/dolfinx). ACM Trans. Math. Softw., 48(2), 18:1–18:23. '
        'DOI: 10.1145/3524456.',
    ],
    'svg': (
        '<svg class="tp-svg-stage" viewBox="0 0 680 220" role="img" aria-label="Sabine vs Eyring reverberation decay '
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
        '          </svg>'
    ),
}

PLATE_CAPTION = {
    'alt': (
        'Conceptual visualization imagining what a timber and limestone coffered vault sculpted with Manfred Schroeder '
        'prime-sequence acoustic diffuser wells would look like (artistic impression, not a measured structure)'
    ),
    'caption': (
        'Conceptual Vision Plate A.05-V (Imagining What It Would Look Like) · Artistic interior visualization '
        "imagining a limestone and oak coffered ceiling sculpted to Manfred Schroeder's prime-sequence quadratic "
        'residue depths.'
    ),
}

DISPATCH = {
    'kicker': 'FRONTIER ACOUSTICS DISPATCH · NUMBER-THEORETIC SCHROEDER DIFFUSERS & ROOM-ACOUSTIC MODELING',
    'headline': 'Prime-Sequence Quadratic Residue Coffered Vaults: A Reverberation Model for Clearer Speech',
    'body': (
        "Pairing Eyring's reverberation formula (DOI 10.1121/1.1915175) with Schroeder diffuser geometry "
        '(DOI 10.1121/1.382601), this folio models a 2,400 m³ vault with estimated T_60 = 0.62 s and a clamped '
        'linear STI estimate of 0.74, beside frontier metasurface diffusers (Zhu et al. 2017, DOI '
        '10.1103/PhysRevX.7.021034). It measured no room and makes no health claim.'
    ),
}

META_3D = (
    'Schroeder Quadratic-Residue (Default p=13) Acoustic Diffuser',
    'X: Quadratic Residue Well Index n · Z: Concert Vault Span · Y: Phase-Grating Well Depth d_n',
)

ES_TRANSLATION = {
    'title_es': (
        'Reverberación Acústica de Sabin–Eyring, Bóvedas Difusoras de Residuo Cuadrático y Claridad del Habla '
        '(STI ≥ 0.68)'
    ),
    'subtitle_es': (
        'Cómo la ley de reverberación de Wallace Sabine, la absorción logarítmica de Carl Eyring y los '
        'casetones de números primos de Manfred Schroeder sirven para diseñar salas donde la voz se entiende '
        'mejor.'
    ),
    'why_es': (
        'Escuchar en una sala con eco es como leer con lentes empañados: los reflejos tempranos enfocan cada '
        'sílaba y los tardíos la vuelven borrosa, aunque el ruido de fondo también limita el habla.'
    ),
    'plain_es': (
        'Conversar en un baño con azulejos o en una cafetería llena cansa pronto cuando el sonido tarda en '
        'apagarse. Los muros, pisos y techos duros hacen rebotar la voz por todo el salón. Las vocales fuertes '
        'siguen sonando y tapan las consonantes suaves que siguen. En hospitales, aulas y salas públicas, el eco '
        'largo y el ruido de fondo dificultan seguir una plática sencilla. La arquitectura acústica serena un '
        'recinto por dos vías. Los revestimientos porosos absorben energía para acortar el eco, mientras los '
        'casetones de madera dispersan los reflejos. Este ensayo calcula la caída según la absorción media y '
        'muestra estimaciones ilustrativas de claridad. Solo evalúa fórmulas y no mide cuánto entiende nadie en '
        'una sala real.'
    ),
    'deep_es': (
        'En la sala modelo (2,400 m³, unos 1,075 m² y absorción media de 0.44), Eyring (DOI 10.1121/1.1915175) da '
        '0.62 s frente a 0.82 s de Sabine, junto a difusores de Schroeder (DOI 10.1121/1.382601). El primer '
        'control recalcula T_60 y estimaciones lineales ilustrativas de STI y C_50, distintas de Steeneken y '
        'Houtgast (DOI 10.1121/1.384464) y Bradley (DOI 10.1121/1.393907). El segundo control cambia la etiqueta '
        'del módulo impar (5 a 23, inicial 13) y la escala 3D sin alterar T_60. Un proyectista podría simular '
        'ondas en computadora y medir según ISO 3382-1; la meta 0.68 es propia de la ficha.'
    ),
}
