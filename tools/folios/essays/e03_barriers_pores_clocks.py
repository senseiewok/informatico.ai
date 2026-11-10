#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Essay ES.03 · Barriers, Pores, and Clocks.

Pure-Python stdlib physics kernel and bilingual (EN / es-MX) long-form essay data
unifying three exact non-equilibrium and continuum-transport laws across scales:

1. Barato & Seifert's Thermodynamic Uncertainty Relation (TUR) on an N-state
   classical Markovian biased ring:
        J = (k_plus - k_minus) / N,
        D_J = (k_plus + k_minus) / (2 N^2),
        A = N * ln(k_plus / k_minus),
        F_tick = Var(N) / <N> = 2 * D_J / J = (1 / N) * coth(A / (2 N)),
        sigma_S / k_B = J * A,
        Q_TUR = (Var(N) / <N>^2) * (Delta_S / k_B) = (A / N) * coth(A / (2 N)) >= 2.
   Physics boundary: Q_TUR >= 2 governs classical Markovian jump dynamics (escapements,
   chemical clocks, ATP-hydrolyzing conformational gating cycles), whereas coherent
   unitary Ramsey precession in optical atomic clocks (T.02 / T.04) is reversible in
   the dark and pays its entropy bill at irreversible readout and optical-pumping reset (T.11).
   Biophysical boundary: CFTR is an ATP-gated ion channel, NOT an active ion pump—ATP
   hydrolysis (~20 k_B T) drives an irreversible conformational gating clock while
   chloride ions flow passively down their electrochemical gradient once open.

2. Brinkman porous-medium momentum balance:
       -grad p + eta * laplacian(u) - (eta / kappa) * u = 0,
   fixing the universal Brinkman screening length ell_B = sqrt(kappa) between viscous
   Stokes shear and Darcy plug drag across sand, lime mortar, cement paste, and hydrogels.

3. Kramers / Eyring thermally activated barrier escape:
       k = k_0 * exp(-Delta_G_dag / (k_B T)),
   where lowering an activation saddle by Delta_Delta_G_dag = 3 k_B T multiplies
   escape or folding flux by exp(3) ≈ 20.09 across optical traps, cement creep, and
   allosterically stabilized protein trusses.
"""
from __future__ import annotations

import math

CODE = "ES.03"
SLUG = "barriers-pores-clocks"
PLATE_SLUG = "essay03"


# ---------------------------------------------------------------------------
# Part A: Classical Markovian Biased Ring & Thermodynamic Uncertainty Relation
# ---------------------------------------------------------------------------

def coth(x: float) -> float:
    """Hyperbolic cotangent coth(x) = cosh(x) / sinh(x) for x != 0, cancellation-safe near 0."""
    if x == 0.0:
        raise ValueError("coth(0) diverges: equilibrium ring has zero net drift current")
    ax = abs(x)
    if ax < 1.0e-3:
        x2 = x * x
        return (1.0 / x) + (x / 3.0) * (1.0 - (x2 / 15.0) * (1.0 - (2.0 * x2) / 21.0))
    if ax > 20.0:
        return 1.0 if x > 0.0 else -1.0
    return math.cosh(x) / math.sinh(x)


def x_coth_x(x: float) -> float:
    """Cancellation-free evaluation of x * coth(x) >= 1 (with limit 1 at x -> 0)."""
    ax = abs(x)
    if ax < 1.0e-3:
        x2 = x * x
        return 1.0 + (x2 / 3.0) * (1.0 - (x2 / 15.0) * (1.0 - (2.0 * x2) / 21.0))
    if ax > 20.0:
        return ax
    return x * (math.cosh(x) / math.sinh(x))


def _assemble_tur_observables(
    n_states: int,
    k_plus: float,
    k_minus: float,
    delta_k: float,
    affinity: float,
    tau: float,
) -> dict[str, float]:
    n = float(n_states)
    j_curr = delta_k / n
    d_j = (2.0 * k_minus + delta_k) / (2.0 * n * n)
    eps2_tau_from_moments = (2.0 * d_j) / (j_curr * j_curr)
    fano_from_moments = (2.0 * d_j) / j_curr
    x = affinity / (2.0 * n)
    fano_analytic = (1.0 / n) * coth(x)
    rel_var = eps2_tau_from_moments / tau
    sigma_s_kb = j_curr * affinity
    delta_s_kb = sigma_s_kb * tau
    q_tur_from_moments = fano_from_moments * affinity
    q_tur_analytic = 2.0 * x_coth_x(x)
    return {
        "n_states": n,
        "k_plus": k_plus,
        "k_minus": k_minus,
        "tau": tau,
        "affinity_kb": affinity,
        "current_hz": j_curr,
        "diffusion_hz": d_j,
        "eps2_tau": eps2_tau_from_moments,
        "fano_tick": fano_from_moments,
        "fano_tick_analytic": fano_analytic,
        "rel_tick_variance": rel_var,
        "sigma_s_kb_per_s": sigma_s_kb,
        "delta_s_kb": delta_s_kb,
        "q_tur": q_tur_from_moments,
        "q_tur_analytic": q_tur_analytic,
    }


def tur_biased_ring_rates(
    n_states: int,
    k_plus: float,
    k_minus: float,
    tau: float = 1.0,
) -> dict[str, float]:
    """Exact steady-state observables for a homogeneous N-state classical Markovian ring.

    Parameters
    ----------
    n_states : int
        Number of discrete Markov states around the unicyclic ring (N >= 1).
    k_plus : float
        Forward elementary jump rate (s^-1), strictly positive.
    k_minus : float
        Backward elementary jump rate (s^-1), strictly positive and != k_plus for a clock.
    tau : float
        Observation window duration (s), strictly positive.
    """
    if n_states < 1:
        raise ValueError(f"n_states must be >= 1, got {n_states}")
    if k_plus <= 0.0 or k_minus <= 0.0:
        raise ValueError(f"Markov ring rates must be > 0, got k_plus={k_plus}, k_minus={k_minus}")
    if tau <= 0.0:
        raise ValueError(f"tau must be > 0, got {tau}")
    delta_k = k_plus - k_minus
    if math.isclose(delta_k, 0.0, rel_tol=0.0, abs_tol=1e-18):
        raise ValueError("Equilibrium ring (k_plus == k_minus, A == 0) has zero net clock current J = 0")
    rel_step = delta_k / k_minus
    log_ratio = math.log1p(rel_step) if abs(rel_step) < 0.5 else math.log(k_plus / k_minus)
    affinity = float(n_states) * log_ratio
    return _assemble_tur_observables(n_states, k_plus, k_minus, delta_k, affinity, tau)


def tur_from_affinity(
    n_states: int,
    affinity_kb: float,
    k_minus: float = 1.0,
    tau: float = 1.0,
) -> dict[str, float]:
    """Evaluate an N-state biased ring parameterized directly by thermodynamic affinity A / k_B."""
    if n_states < 1:
        raise ValueError(f"n_states must be >= 1, got {n_states}")
    if k_minus <= 0.0 or tau <= 0.0:
        raise ValueError("k_minus and tau must be > 0")
    if affinity_kb == 0.0:
        raise ValueError("Zero affinity (A = 0) yields detailed balance and zero clock current")
    step_aff = affinity_kb / float(n_states)
    delta_k = k_minus * math.expm1(step_aff)
    k_plus = k_minus + delta_k
    return _assemble_tur_observables(n_states, k_plus, k_minus, delta_k, affinity_kb, tau)


def minimum_clock_entropy_kb(rel_tick_variance: float) -> float:
    """Minimum entropy production Delta_S / k_B >= 2 / (Var(N) / <N>^2) for a classical Markovian clock."""
    if rel_tick_variance <= 0.0:
        raise ValueError(f"rel_tick_variance must be > 0, got {rel_tick_variance}")
    return 2.0 / rel_tick_variance


# ---------------------------------------------------------------------------
# Part B: Brinkman Porous Screening & Kramers Barrier Escape
# ---------------------------------------------------------------------------

def brinkman_screening_length(kappa_m2: float, planted_invert: bool = False) -> float:
    """Universal Brinkman viscous-to-Darcy screening length ell_B = sqrt(kappa) in meters."""
    if kappa_m2 <= 0.0:
        raise ValueError(f"Hydraulic permeability kappa_m2 must be > 0, got {kappa_m2}")
    if planted_invert:
        return 1.0 / math.sqrt(kappa_m2)
    return math.sqrt(kappa_m2)


def brinkman_channel_velocity(
    y_m: float,
    half_width_m: float,
    kappa_m2: float,
    eta_pa_s: float,
    grad_p_pa_per_m: float,
) -> float:
    """Exact 1D Brinkman velocity u(y) on y in [-H, H] driven by G = -dp/dx > 0.

    Solves: G + eta * d^2u/dy^2 - (eta / kappa) * u = 0 with no-slip walls u(+-H) = 0:
        u(y) = (G * kappa / eta) * (1 - cosh(y / ell_B) / cosh(H / ell_B)).
    """
    if half_width_m <= 0.0 or kappa_m2 <= 0.0 or eta_pa_s <= 0.0:
        raise ValueError("Channel half-width, permeability, and viscosity must be > 0")
    if abs(y_m) > half_width_m * (1.0 + 1e-12):
        raise ValueError(f"|y_m|={abs(y_m)} exceeds half_width_m={half_width_m}")
    ell_b = brinkman_screening_length(kappa_m2)
    u_darcy = (grad_p_pa_per_m * kappa_m2) / eta_pa_s
    xi_h = half_width_m / ell_b
    xi_y = abs(y_m) / ell_b
    # Avoid overflow at very small ell_B / H (deep Darcy plug regime: xi_h >> 50)
    if xi_h > 60.0:
        ratio = math.exp(xi_y - xi_h) * (1.0 + math.exp(-2.0 * xi_y)) / (1.0 + math.exp(-2.0 * xi_h))
    else:
        ratio = math.cosh(xi_y) / math.cosh(xi_h)
    return u_darcy * (1.0 - ratio)


def brinkman_pde_residual(
    y_m: float,
    half_width_m: float,
    kappa_m2: float,
    eta_pa_s: float,
    grad_p_pa_per_m: float,
) -> float:
    """Dimensionless PDE residual |-dp/dx + eta u''(y) - (eta/kappa) u(y)| / |-dp/dx|."""
    ell_b = brinkman_screening_length(kappa_m2)
    u_val = brinkman_channel_velocity(y_m, half_width_m, kappa_m2, eta_pa_s, grad_p_pa_per_m)
    xi_h = half_width_m / ell_b
    xi_y = abs(y_m) / ell_b
    if xi_h > 60.0:
        cosh_ratio = math.exp(xi_y - xi_h) * (1.0 + math.exp(-2.0 * xi_y)) / (1.0 + math.exp(-2.0 * xi_h))
    else:
        cosh_ratio = math.cosh(xi_y) / math.cosh(xi_h)
    u_yy = -(grad_p_pa_per_m / eta_pa_s) * cosh_ratio
    residual = grad_p_pa_per_m + eta_pa_s * u_yy - (eta_pa_s / kappa_m2) * u_val
    return abs(residual) / abs(grad_p_pa_per_m)


def kramers_escape_rate(k0_hz: float, delta_g_dag_kbt: float) -> float:
    """Arrhenius-Eyring-Kramers barrier escape rate k = k_0 * exp(-Delta_G_dag / (k_B T))."""
    if k0_hz <= 0.0:
        raise ValueError(f"Attempt prefactor k0_hz must be > 0, got {k0_hz}")
    return k0_hz * math.exp(-delta_g_dag_kbt)


def kramers_flux_multiplier(delta_delta_g_dag_kbt: float) -> float:
    """Flux speedup k_rescued / k_initial = exp(Delta_Delta_G_dag / (k_B T)) from lowering a saddle."""
    return math.exp(delta_delta_g_dag_kbt)


# ---------------------------------------------------------------------------
# Essay ES.03 Bilingual Monograph Specification
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": CODE,
    "slug": SLUG,
    "plate_slug": PLATE_SLUG,
    "date": "2026-11-10",
    "seo": (
        "Barriers, Pores, and Autonomous Clocks",
        "How the thermodynamic uncertainty relation, Brinkman porous screening, and Kramers barrier escape govern clocks, stone mortar, and protein pores.",
        "Barreras, Poros y Relojes Autónomos",
        "Cómo la relación de incertidumbre termodinámica, el cribado poroso de Brinkman y el escape de Kramers rigen relojes, morteros y poros proteicos.",
    ),
    "kicker_en": "Cross-Pillar Synthesis · ES.03 · Stochastic Clocks, Porous Screening, and Saddle Escape",
    "kicker_es": "Síntesis Transversal · ES.03 · Relojes Estocásticos, Cribado Poroso y Escape de Silla",
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "title_en": "Barriers, Pores, and Clocks",
    "title_es": "Barreras, Poros y Relojes",
    "standfirst_en": (
        "Every autonomous thermal clock pays an exact entropy price for regular ticks; every fluid crossing a fibrous or mineral "
        "matrix transitions from viscous shear to porous drag at the square root of hydraulic permeability; and every thermally "
        "activated jump over an energy saddle scales exponentially with barrier height. Put those three equations on one sheet "
        "and watch escapements, optical lattice clocks, pumped concrete, limestone mortar, and a 10 nm ATP-gated chloride pore "
        "answer to the same mathematics."
    ),
    "standfirst_es": (
        "Todo reloj térmico autónomo paga un precio exacto de entropía por la regularidad de sus tics; todo fluido que cruza una "
        "matriz fibrosa o mineral pasa del cortante viscoso al arrastre poroso en la raíz cuadrada de la permeabilidad hidráulica; "
        "y todo salto activado térmicamente sobre un punto silla escala exponencialmente con la altura de la barrera. Pon esas "
        "tres ecuaciones en una sola hoja y verás escapes mecánicos, relojes ópticos, concreto bombeado, mortero de cal y un poro "
        "de cloruro de 10 nm compuertado por ATP obedecer la misma matemática."
    ),
    "card_dek_en": (
        "Why regular classical ticks require Q_TUR ≥ 2, where optical Ramsey clocks pay their entropy bill, and how ℓ_B = √κ "
        "and exp(3) = 20.09 link civil mortar to nanoscale pores."
    ),
    "card_dek_es": (
        "Por qué los tics clásicos regulares exigen Q_TUR ≥ 2, dónde pagan su cuenta de entropía los relojes ópticos de Ramsey, y cómo "
        "ℓ_B = √κ y exp(3) = 20.09 enlazan el mortero civil con poros nanométricos."
    ),
    "instrument_kind": "tur_pores",
    "predict": {
        "question_en": (
            "Before inspecting the instrument: can an autonomous classical thermal clock operating via Markovian jumps at room "
            "temperature achieve 1 % tick-timing uncertainty (Var(N) / <N>^2 = 0.0001) while dissipating less than 20,000 k_B "
            "of entropy?"
        ),
        "question_es": (
            "Antes de mirar el instrumento: ¿puede un reloj térmico clásico autónomo que opera mediante saltos markovianos a "
            "temperatura ambiente lograr una incertidumbre de tiempo de 1 % (Var(N) / <N>^2 = 0.0001) disipando menos de "
            "20,000 k_B de entropía?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Yes — adding enough reversible internal gear states lets precision grow without raising entropy dissipation.",
                "es": "Sí — añadir suficientes estados internos reversibles permite aumentar la precisión sin elevar la disipación de entropía.",
            },
            {
                "id": "b",
                "en": "No — Barato and Seifert's bound Q_TUR >= 2 forces Delta_S / k_B >= 2 / 0.0001 = 20,000 regardless of ring size.",
                "es": "No — la cota Q_TUR >= 2 de Barato y Seifert obliga a Delta_S / k_B >= 2 / 0.0001 = 20,000 sin importar el tamaño del anillo.",
            },
        ],
        "answer": "b",
        "explain_en": (
            "For any continuous-time classical Markovian steady state, Q_TUR = (Var(N) / <N>^2) * (Delta_S / k_B) = (A / N) coth(A / (2N)) >= 2. "
            "Adding more states N helps approach the floor 2 at high affinity, cleanly preventing waste, yet never drops below 2: "
            "reaching Var(N) / <N>^2 = 0.0001 (1 % relative error) unconditionally costs at least 2 / 0.0001 = 20,000 k_B of entropy."
        ),
        "explain_es": (
            "Para cualquier estado estacionario markoviano clásico en tiempo continuo, Q_TUR = (Var(N) / <N>^2) * (Delta_S / k_B) = (A / N) coth(A / (2N)) >= 2. "
            "Añadir más estados N acerca el producto al piso 2 a alta afinidad y reduce el desperdicio, pero jamás baja de 2: "
            "alcanzar Var(N) / <N>^2 = 0.0001 (1 % de error relativo) exige sin excepción al menos 2 / 0.0001 = 20,000 k_B de entropía."
        ),
    },
    "sections": [
        {
            "id": "tur-clocks",
            "h2_en": "I · Every Classical Tick Costs Entropy: Barato, Seifert, and the Biased Ring",
            "h2_es": "I · Cada Tic Clásico Cuesta Entropía: Barato, Seifert y el Anillo Sesgado",
            "short_en": "I · Clock Cost",
            "short_es": "I · Costo del Reloj",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "In 1657 Christiaan Huygens hung a brass pendulum beneath a verge escapement in The Hague and confronted "
                        "the quiet paradox at the heart of every autonomous timepiece. Left completely uncoupled from friction, "
                        "falling weights, or wound springs, a harmonic oscillator conserves energy and loses no heat, yet it "
                        "cannot count its own swings against thermal jiggling: every forward excursion is matched by a "
                        "time-reversed twin. To turn an oscillation into an irreversible tick counter that advances strictly "
                        "from 12:00:00 to 12:00:01, each pallet drop must dissipate free energy into a thermal bath. For three "
                        "centuries clockmakers treated that frictional loss as a practical nuisance to be minimized with jeweled "
                        "bearings and deadbeat anchors. Only in 2015 did Andre C. Barato and Udo Seifert prove (DOI "
                        "10.1103/physrevlett.114.158101), building on Seifert's stochastic thermodynamics framework of 2012 "
                        "(DOI 10.1088/0034-4885/75/12/126001), that thermal dissipation is not an engineering blemish at all: "
                        "for every autonomous classical Markovian clock, entropy production sets an unbreakable lower bound on "
                        "timing precision."
                    ),
                    "es": (
                        "En 1657 Christiaan Huygens colgó un péndulo de latón bajo un escape de rueda catalina en La Haya y "
                        "enfrentó la paradoja silenciosa en el corazón de todo reloj autónomo. Si se deja por completo libre de "
                        "fricción, pesas descendentes o resortes tensados, un oscilador armónico conserva la energía y no disipa "
                        "calor, pero no puede contar sus propias oscilaciones frente a la agitación térmica: cada excursión hacia "
                        "adelante tiene una gemela exacta con el tiempo invertido. Para convertir una oscilación en un contador "
                        "irreversible de tics que avance estrictamente de 12:00:00 a 12:00:01, cada caída del áncora debe disipar "
                        "energía libre en un baño térmico. Durante tres siglos los relojeros trataron esa pérdida como una "
                        "imperfección mecánica por minimizar con rubíes y áncoras de reposo. Apenas en 2015 Andre C. Barato y Udo "
                        "Seifert demostraron (DOI 10.1103/physrevlett.114.158101), sobre la termodinámica estocástica formulada "
                        "por Seifert en 2012 (DOI 10.1088/0034-4885/75/12/126001), que esa disipación no es un defecto práctico: "
                        "en todo reloj markoviano clásico autónomo, la producción de entropía impone una cota inferior "
                        "infranqueable a la precisión temporal."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Barato–Seifert Thermodynamic Uncertainty Relation on an N-State Ring",
                    "label_es": "Relación de Incertidumbre Termodinámica de Barato y Seifert en un Anillo de N Estados",
                    "formula": "J = (k_+ - k_-) / N,   D_J = (k_+ + k_-) / (2 N^2),   Q_TUR = (Var(N) / <N>^2) (Delta_S / k_B) = (A / N) coth(A / (2 N)) >= 2",
                    "note_en": (
                        "Exact steady-state precision-dissipation product on a homogeneous N-state biased ring with cycle "
                        "affinity A = N ln(k_+ / k_-) in units of k_B: Q_TUR saturates 2 as A -> 0 and scales as A / N when A >> 2 N."
                    ),
                    "note_es": (
                        "Producto exacto entre varianza y disipación estacionaria en un anillo sesgado homogéneo de N "
                        "estados con afinidad cíclica A = N ln(k_+ / k_-) en unidades de k_B: Q_TUR satura 2 cuando A -> 0 y escala "
                        "como A / N cuando A >> 2 N."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Model any continuous-time classical Markovian tick counter as a ring of N discrete states stepped "
                        "forward at rate k_+ and backward by thermal fluctuations at rate k_-. One full clockwise revolution "
                        "advances the pointer by 1 tick and releases thermodynamic cycle affinity A = N ln(k_+ / k_-) in units "
                        "of Boltzmann's constant k_B, a network identity extended to general open chemical reaction networks by "
                        "Riccardo Rao and Massimiliano Esposito in 2016 (DOI 10.1103/physrevx.6.041064). Because forward and "
                        "backward Poisson jumps are independent, the steady-state drift current is J = (k_+ - k_-) / N and the "
                        "cycle diffusion constant is D_J = (k_+ + k_-) / (2 N^2). Over an observation window tau with <N> = J tau mean ticks, "
                        "the cycle Fano factor satisfies Var(N) / <N> = eps^2 J tau = 2 D_J / J = (1 / N) coth(A / (2 N)), "
                        "while the steady-state entropy production rate is sigma_S / k_B = J A. Multiplying relative variance by "
                        "total dissipated entropy Delta_S / k_B = sigma_S tau / k_B cancels both tau and the bare rate scale, "
                        "leaving Q_TUR = (A / N) coth(A / (2 N)). Because x coth(x) >= 1 for every nonzero real number x = A / (2 N), "
                        "Q_TUR is strictly greater than 2 away from equilibrium and approaches 2 only as A -> 0."
                    ),
                    "es": (
                        "Modelemos cualquier contador clásico markoviano en tiempo continuo como un anillo de N estados discretos "
                        "que avanza con tasa k_+ y retrocede por fluctuaciones térmicas con tasa k_-. Una vuelta completa en "
                        "sentido horario adelanta la aguja en 1 tic y libera una afinidad termodinámica cíclica A = N ln(k_+ / k_-) "
                        "en unidades de la constante de Boltzmann k_B, identidad generalizada a redes químicas abiertas por "
                        "Riccardo Rao y Massimiliano Esposito en 2016 (DOI 10.1103/physrevx.6.041064). Como los saltos de Poisson "
                        "hacia adelante y hacia atrás son independientes, la corriente estacionaria neta es J = (k_+ - k_-) / N y "
                        "la constante de difusión cíclica es D_J = (k_+ + k_-) / (2 N^2). En una ventana tau con <N> = J tau tics medios, "
                        "el factor de Fano por tic cumple Var(N) / <N> = eps^2 J tau = 2 D_J / J = (1 / N) coth(A / (2 N)), "
                        "mientras la tasa estacionaria de producción de entropía vale sigma_S / k_B = J A. Multiplicar la varianza "
                        "relativa por la entropía total disipada Delta_S / k_B = sigma_S tau / k_B cancela tanto tau como la escala "
                        "global de tasas, dejando Q_TUR = (A / N) coth(A / (2 N)). Como x coth(x) >= 1 para todo número real no nulo "
                        "x = A / (2 N), Q_TUR supera estrictamente 2 fuera del equilibrio y solo tiende a 2 cuando A -> 0."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "In Plain Words · Buying Time With Heat",
                    "kicker_es": "En Palabras Sencillas · Comprar Tiempo con Calor",
                    "title_en": "Every 10-fold cut in classical tick jitter demands 100 times more dissipated heat",
                    "title_es": "Reducir 10 veces el temblor de un reloj clásico exige disipar 100 veces más calor",
                    "paras": [
                        (
                            "Think of a turnstile in a crowded subway corridor pushed from both sides by jostling passengers. If "
                            "equal crowds push forward and backward (A = 0), the turnstile clicks wildly in both directions, nets 0 "
                            "turns per minute, and cannot tell you whether 1 minute or 10 minutes have elapsed.",
                            "Imagina un torniquete en un pasillo lleno donde la multitud empuja desde ambos lados. Si la misma "
                            "fuerza empuja hacia adelante y hacia atrás (A = 0), el torniquete gira al azar en ambos sentidos, suma "
                            "0 vueltas netas por minuto y no permite saber si pasó 1 minuto o pasaron 10 minutos.",
                        ),
                        (
                            "To make the counter march reliably forward with at most 1 % timing error (relative variance 0.0001), "
                            "you must bias the flow strongly forward—and Barato and Seifert's inequality proves that cutting "
                            "standard deviation 10-fold (cutting variance 100-fold) forces at least 2 / 0.0001 = 20,000 k_B of heat "
                            "into the surrounding bath.",
                            "Para que el contador avance con un error temporal máximo de 1 % (varianza relativa 0.0001), hay que "
                            "sesgar con fuerza el paso hacia adelante, y la desigualdad de Barato y Seifert demuestra que reducir "
                            "10 veces la desviación estándar (100 veces la varianza) obliga a liberar al menos 2 / 0.0001 = 20,000 k_B "
                            "de calor hacia el baño térmico.",
                        ),
                    ],
                },
            ],
        },
        {
            "id": "unitary-boundary",
            "h2_en": "II · Why Optical Clocks Do Not Burn Entropy in the Dark: Ramsey Precession vs. Pointer Reset",
            "h2_es": "II · Por Qué los Relojes Ópticos No Queman Entropía en la Oscuridad: Precesión de Ramsey frente a Reinicio Puntero",
            "short_en": "II · Optical Boundary",
            "short_es": "II · Frontera Óptica",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "At first glance, modern optical atomic clocks—the instruments that resolved gravitational time dilation "
                        "across 33 cm on T.02 and across a 1 mm strontium-87 cloud in Tobias Bothwell and Jun Ye's 2022 JILA "
                        "experiment at fractional instability near 10^-19 (DOI 10.1038/s41586-021-04349-7)—appear to shatter "
                        "the classical Markovian cost. If an optical clock reaches a fractional timing variance of 10^-36 over "
                        "hours of operation, must its atoms continuously boil off 2 x 10^36 k_B of entropy while precessing in "
                        "ultra-high vacuum? No—and pinpointing exactly why reveals the sharp boundary where Barato and Seifert's "
                        "theorem stops and unitary quantum mechanics takes over."
                    ),
                    "es": (
                        "A primera vista, los relojes atómicos ópticos modernos —los instrumentos que resolvieron la dilatación "
                        "gravitacional del tiempo a 33 cm en T.02 y a través de una nube de estroncio-87 de 1 mm en el "
                        "experimento de 2022 de Tobias Bothwell y Jun Ye en JILA con inestabilidad cercana a 10^-19 (DOI "
                        "10.1038/s41586-021-04349-7)— parecerían romper el costo markoviano clásico. Si un reloj óptico alcanza "
                        "una varianza fraccionaria de 10^-36 tras horas de operación, ¿deben sus átomos hervir continuamente "
                        "2 x 10^36 k_B de entropía mientras precesan en ultraalto vacío? No, y precisar por qué traza con "
                        "nitidez la frontera exacta donde termina el teorema de Barato y Seifert y comienza la mecánica cuántica "
                        "unitaria."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Barato and Seifert's bound Q_TUR >= 2 assumes a continuous-time classical Markovian jump process whose "
                        "off-diagonal quantum coherences vanish at every instant. An optical lattice clock operates on the "
                        "opposite principle. Between the two pi/2 laser pulses of a Ramsey interrogation cycle, each neutral "
                        "87Sr atom sits in a coherent superposition (|g> + exp(-i omega_0 t) |e>) / sqrt(2) evolving under "
                        "the unitary operator U(t) = exp(-i H t / hbar). Unitary evolution preserves von Neumann entropy "
                        "identically: Delta_S = 0 across the entire dark precession window! As long as stray blackbody photons "
                        "and background gas collisions are suppressed, coherent phase accumulation is reversible and non-Markovian, "
                        "so Q_TUR >= 2 simply does not apply to the dark flight between laser pulses."
                    ),
                    "es": (
                        "La cota Q_TUR >= 2 de Barato y Seifert supone un proceso clásico de saltos markovianos en tiempo "
                        "continuo cuyas coherencias cuánticas fuera de la diagonal se anulan en cada instante. Un reloj de red "
                        "óptica trabaja con el principio opuesto. Entre los dos pulsos láser de pi/2 de una secuencia de Ramsey, "
                        "cada átomo neutro de 87Sr permanece en una superposición coherente (|g> + exp(-i omega_0 t) |e>) / sqrt(2) "
                        "que evoluciona bajo el operador unitario U(t) = exp(-i H t / hbar). La evolución unitaria conserva de "
                        "manera idéntica la entropía de von Neumann: ¡Delta_S = 0 durante toda la ventana de precesión en la "
                        "oscuridad! Mientras se supriman fotones térmicos parásitos y colisiones de gas residual, la acumulación "
                        "coherente de fase es reversible y no markoviana, de modo que Q_TUR >= 2 no aplica al vuelo oscuro entre "
                        "pulsos láser."
                    ),
                },
                {
                    "type": "analogy",
                    "kicker_en": "Everyday Analogy · Free Swing vs. Audible Click",
                    "kicker_es": "Analogía Cotidiana · Oscilación Libre frente al Clic Audible",
                    "title_en": "Unitary dark precession glides for 0 entropy; ringing the bell pays the bill",
                    "title_es": "La precesión oscura unitaria se desliza con 0 entropía; sonar la campana paga la cuenta",
                    "paras": [
                        (
                            "Picture an ice skater coasting silently across frictionless ice between 2 painted lines, then "
                            "slapping a brass bell mounted on the rink wall to record each lap. Coasting across the ice corresponds "
                            "to unitary Ramsey phase evolution in the dark (0 entropy generated while coherent); slapping the bell "
                            "and resetting for the next lap corresponds to projective laser fluorescence readout and optical pumping. "
                            "Even a quantum clock cannot produce a shareable classical tick without ringing the bell.",
                            "Imagina a una patinadora deslizándose en silencio sobre hielo sin fricción entre 2 líneas pintadas, "
                            "para luego golpear una campana de bronce en el muro y registrar cada vuelta. El deslizamiento libre "
                            "equivale a la evolución unitaria de fase de Ramsey en la oscuridad (0 entropía generada mientras se "
                            "mantiene coherente); golpear la campana y prepararse para la siguiente vuelta equivale a la lectura por "
                            "fluorescencia láser y al bombeo óptico. Ni siquiera un reloj cuántico puede dejar un tic clásico "
                            "compartible sin hacer sonar la campana.",
                        ),
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Where, then, does an optical clock pay its second-law bill? Exactly at the irreversible measurement and "
                        "reset boundaries analyzed on T.11 through Wojciech Zurek's 2009 Quantum Darwinism framework (DOI "
                        "10.1038/nphys1202). To turn a fragile atomic phase into a macroscopic classical tick that multiple "
                        "engineers and frequency combs can read without disturbing it, a readout laser scatters thousands of "
                        "visible photons (each carrying ~2.7 eV, roughly 105 times room-temperature k_B T = 0.0257 eV at 298 K) "
                        "into the surrounding electromagnetic bath, einselecting a definite pointer state |g> or |e>. Next, "
                        "optical pumping erases that 1-bit outcome back to the pure initial state |g> via spontaneous emission, "
                        "paying far above Landauer's ln(2) ≈ 0.693 k_B floor, while femtosecond optical frequency combs dissipate "
                        "milliwatts (~2.4 x 10^17 k_B per second at 298 K) locking microwave counters to the optical carrier. "
                        "Coherence buys extraordinary phase leverage per cycle; irreversibility still collects its toll the "
                        "instant a phase becomes a recorded tick."
                    ),
                    "es": (
                        "¿Dónde paga entonces su factura de la segunda ley un reloj óptico? Exactamente en las fronteras "
                        "irreversibles de medición y reinicio estudiadas en T.11 mediante el marco del darwinismo cuántico de "
                        "Wojciech Zurek de 2009 (DOI 10.1038/nphys1202). Para convertir una fase atómica frágil en un tic "
                        "clásico macroscópico que varios ingenieros y peines de frecuencia puedan leer sin destruirlo, un láser "
                        "de lectura dispersa miles de fotones visibles (cada uno con ~2.7 eV, cerca de 105 veces k_B T = 0.0257 eV "
                        "a 298 K) hacia el baño electromagnético, seleccionando un estado puntero definido |g> o |e>. Enseguida, "
                        "el bombeo óptico borra ese resultado de 1 bit de vuelta al estado puro |g> por emisión espontánea, "
                        "pagando muy por encima del piso de Landauer de ln(2) ≈ 0.693 k_B, mientras los peines ópticos de "
                        "femtosegundos disipan milivatios (~2.4 x 10^17 k_B por segundo a 298 K) al fijar contadores electrónicos "
                        "a la portadora óptica. La coherencia compra una palanca de fase extraordinaria por ciclo; la "
                        "irreversibilidad cobra su peaje en el instante en que una fase se vuelve un tic registrado."
                    ),
                },
            ],
        },
        {
            "id": "brinkman-pores",
            "h2_en": "III · Viscous Shear Meets Porous Drag: Hendrik Brinkman's Screening Length Across Six Orders of Magnitude",
            "h2_es": "III · El Cortante Viscoso Encuentra el Arrastre Poroso: La Longitud de Cribado de Hendrik Brinkman en Seis Órdenes de Magnitud",
            "short_en": "III · Porous Drag",
            "short_es": "III · Arrastre Poroso",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Leave clockwork for a moment and step onto a civil construction deck where fresh concrete is pumped "
                        "under high pressure through steel pipelines and capillary water migrates into cured limestone masonry. "
                        "Fluid mechanics offers two classic equations that appear to speak different languages: Claude-Louis "
                        "Navier and George Gabriel Stokes's viscous shear balance eta laplacian(u) = grad(p) for open conduits, "
                        "and Henry Darcy's 1856 filtration law u = -(kappa / eta) grad(p) for packed sand beds of hydraulic "
                        "permeability kappa (with dimensions of area, m^2). Because Darcy's law drops second spatial derivatives, "
                        "it cannot satisfy no-slip boundary conditions where a porous bed touches a solid steel pipe wall or an "
                        "open fluid film. In 1949 the Dutch physicist Hendrik C. Brinkman resolved that mismatch in a single "
                        "stroke (DOI 10.1007/bf02120313) by retaining both operators inside one linear momentum equation."
                    ),
                    "es": (
                        "Dejemos por un momento la relojería y subamos a una losa en obra civil donde se bombea concreto fresco "
                        "a alta presión por tuberías de acero y el agua capilar penetra mampostería de piedra caliza curada. La "
                        "mecánica de fluidos ofrece dos ecuaciones clásicas que parecen hablar idiomas distintos: el balance de "
                        "cortante viscoso eta laplacian(u) = grad(p) de Claude-Louis Navier y George Gabriel Stokes para ductos "
                        "abiertos, y la ley de filtración de Henry Darcy de 1856 u = -(kappa / eta) grad(p) para lechos porosos "
                        "con permeabilidad hidráulica kappa (con dimensiones de área, m^2). Como la ley de Darcy omite las "
                        "segundas derivadas espaciales, no puede cumplir la condición de no deslizamiento donde un medio poroso "
                        "toca la pared de acero de un tubo o una película libre. En 1949 el físico neerlandés Hendrik C. Brinkman "
                        "resolvió esa fractura de un solo trazo (DOI 10.1007/bf02120313) al conservar ambos operadores en una "
                        "misma ecuación lineal de momento."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Brinkman Momentum Balance & Universal Screening Length",
                    "label_es": "Balance de Momento de Brinkman y Longitud Universal de Cribado",
                    "formula": "-grad p + eta laplacian(u) - (eta / kappa) u = 0,   ell_B = sqrt(kappa),   u(y) = (G kappa / eta) [1 - cosh(y / ell_B) / cosh(H / ell_B)]",
                    "note_en": (
                        "Brinkman momentum balance, viscosity-independent screening length ell_B = sqrt(kappa), and exact "
                        "channel velocity profile across [-H, H] under pressure gradient G = -dp/dx."
                    ),
                    "note_es": (
                        "Balance de momento de Brinkman, longitud de cribado ell_B = sqrt(kappa) independiente de la viscosidad, "
                        "y perfil exacto de velocidad en un canal [-H, H] bajo gradiente de presión G = -dp/dx."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Compare the two resistive terms in Brinkman's equation: viscous shear scales as eta U / ell^2 while "
                        "Darcy porous drag scales as eta U / kappa. Setting those two stresses equal cancels the fluid viscosity "
                        "eta completely and isolates a purely geometric length scale: the Brinkman screening length "
                        "ell_B = sqrt(kappa). Across a conduit of half-width H, the exact hyperbolic-cosine solution u(y) "
                        "interpolates smoothly between two worlds. When the pore network is wide open (ell_B >> H), Taylor "
                        "expansion of cosh(y / ell_B) recovers classical parabolic Poiseuille shear u(y) = G (H^2 - y^2) / (2 eta). "
                        "When the solid matrix is tight (ell_B << H), velocity flattens into uniform Darcy plug flow "
                        "u_plug = G kappa / eta everywhere except inside a razor-thin boundary skin of thickness ell_B against "
                        "the walls—the exact wall-lubrication physics analyzed for pumped concrete pipelines by Dimitri Feys, "
                        "Geert De Schutter, Kamal H. Khayat, and Ronny Verhoeven in 2016 (DOI 10.1016/j.cemconcomp.2015.11.002) "
                        "and for solute and water transport across hydrated microbial biofilms by Philip S. Stewart in 2003 "
                        "(DOI 10.1128/jb.185.5.1485-1491.2003)."
                    ),
                    "es": (
                        "Comparemos los dos términos resistivos en la ecuación de Brinkman: el cortante viscoso escala como "
                        "eta U / ell^2 mientras el arrastre poroso de Darcy escala como eta U / kappa. Igualar ambos esfuerzos "
                        "cancela por completo la viscosidad del fluido eta y aísla una escala geométrica pura: la longitud de "
                        "cribado de Brinkman ell_B = sqrt(kappa). En un conducto de semiancho H, la solución exacta con coseno "
                        "hiperbólico u(y) interpola sin costuras entre dos regímenes. Cuando la red porosa está muy abierta "
                        "(ell_B >> H), el desarrollo de Taylor de cosh(y / ell_B) recupera el flujo parabólico clásico de "
                        "Poiseuille u(y) = G (H^2 - y^2) / (2 eta). Cuando la matriz sólida es cerrada (ell_B << H), la velocidad "
                        "se aplana en un flujo tapón uniforme de Darcy u_plug = G kappa / eta salvo dentro de una capa límite de "
                        "espesor ell_B pegada a las paredes, exactamente la física de capa lubricante estudiada en tuberías de "
                        "concreto bombeado por Dimitri Feys, Geert De Schutter, Kamal H. Khayat y Ronny Verhoeven en 2016 (DOI "
                        "10.1016/j.cemconcomp.2015.11.002) y en el transporte a través de biopelículas hidratadas por Philip S. "
                        "Stewart en 2003 (DOI 10.1128/jb.185.5.1485-1491.2003)."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.03-1 · Universal Brinkman screening length ell_B = sqrt(kappa) across 5 orders of magnitude in length (10 orders in permeability kappa).",
                    "caption_es": "Tabla ES.03-1 · Longitud universal de cribado de Brinkman ell_B = sqrt(kappa) a lo largo de 5 órdenes de magnitud en longitud (10 órdenes en permeabilidad kappa).",
                    "headers_en": [
                        "Porous Medium",
                        "Permeability kappa (m^2)",
                        "Screening Length ell_B = sqrt(kappa)",
                        "Boundary Skin Regime",
                    ],
                    "headers_es": [
                        "Medio Poroso",
                        "Permeabilidad kappa (m^2)",
                        "Longitud de Cribado ell_B = sqrt(kappa)",
                        "Régimen de Capa Límite",
                    ],
                    "rows": [
                        [
                            ("Pervious drainage concrete & coarse sand", "Concreto permeable de drenaje y arena gruesa"),
                            ("1.0 x 10^-8", "1.0 x 10^-8"),
                            ("100 um (0.10 mm)", "100 um (0.10 mm)"),
                            ("Macroscopic sub-millimeter Stokes shear layer", "Capa macroscópica submilimétrica de cortante de Stokes"),
                        ],
                        [
                            ("Historic lime mortar & porous limestone", "Mortero histórico de cal y piedra caliza porosa"),
                            ("1.0 x 10^-12", "1.0 x 10^-12"),
                            ("1.0 um (1,000 nm)", "1.0 um (1,000 nm)"),
                            ("Micron-scale capillary pore-wall shear skin", "Piel micrométrica de cortante en poros capilares"),
                        ],
                        [
                            ("Hydrated biopolymer brush / hydrogel (open)", "Cepillo / hidrogel biopolimérico hidratado (abierto)"),
                            ("2.5 x 10^-15", "2.5 x 10^-15"),
                            ("50 nm", "50 nm"),
                            ("Mesoscopic polymer-mesh screening around nanoparticles", "Cribado mesoscópico de malla polimérica ante nanopartículas"),
                        ],
                        [
                            ("Compacted dehydrated biopolymer hydrogel", "Hidrogel biopolimérico deshidratado y compactado"),
                            ("1.0 x 10^-16", "1.0 x 10^-16"),
                            ("10 nm", "10 nm"),
                            ("25-fold lower kappa; tight Darcy plug resistance", "kappa 25 veces menor; fuerte resistencia tapón de Darcy"),
                        ],
                        [
                            ("Dense hydrated Portland cement paste (C-S-H)", "Pasta densa de cemento Portland hidratado (C-S-H)"),
                            ("1.0 x 10^-18", "1.0 x 10^-18"),
                            ("1.0 nm", "1.0 nm"),
                            ("Nanometer gel-pore Darcy limit over 99.9 % of section", "Límite de Darcy en poros de gel nanométricos en 99.9 % de la sección"),
                        ],
                    ],
                },
            ],
        },
        {
            "id": "kramers-trusses",
            "h2_en": "IV · Exponential Sensitivity at the Saddle: Kramers Escape in Traps, Cement Creep, and Folding Trusses",
            "h2_es": "IV · Sensibilidad Exponencial en el Punto Silla: Escape de Kramers en Trampas, Fluencia del Cemento y Armaduras Plegables",
            "short_en": "IV · Barrier Escape",
            "short_es": "IV · Escape Térmico",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Our third law governs what happens when a structure—an optically trapped atom, a load-bearing calcium-"
                        "silicate-hydrate sheet in a concrete bridge pier, or a multi-domain macromolecular truss—must cross a "
                        "free-energy saddle Delta_G_dag driven by ambient thermal noise k_B T. In Hendrik Kramers's 1940 "
                        "Langevin escape theory and Henry Eyring's transition-state theory, rare thermal kicks populate the "
                        "barrier crest according to the Boltzmann factor exp(-Delta_G_dag / (k_B T)). Because barrier height "
                        "sits in the exponent rather than the prefactor k_0, tiny linear adjustments in saddle geometry unleash "
                        "dramatic order-of-magnitude shifts in escape and assembly rates."
                    ),
                    "es": (
                        "Nuestra tercera ley gobierna lo que ocurre cuando una estructura —un átomo en una trampa óptica, una "
                        "lámina portante de silicato cálcico hidratado en la pila de un puente de concreto o una armadura "
                        "macromolecular multidominio— debe cruzar un punto silla de energía libre Delta_G_dag impulsada por el "
                        "ruido térmico k_B T. En la teoría de escape de Langevin de Hendrik Kramers de 1940 y la teoría del "
                        "estado de transición de Henry Eyring, los empujones térmicos pueblan la cresta de la barrera según el "
                        "factor de Boltzmann exp(-Delta_G_dag / (k_B T)). Como la altura de la barrera aparece en el exponente y "
                        "no en el prefactor k_0, pequeños ajustes lineales en la geometría del punto silla desatan cambios de "
                        "órdenes de magnitud en el flujo de escape y ensamblaje."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Kramers–Eyring Exponential Barrier Escape Law",
                    "label_es": "Ley Exponencial de Escape de Barrera de Kramers y Eyring",
                    "formula": "k = k_0 exp(-Delta_G_dag / (k_B T)),   k_rescued / k_initial = exp(Delta_Delta_G_dag / (k_B T)),   Delta_Delta_G_dag = 3 k_B T => e^3 ≈ 20.09",
                    "note_en": (
                        "Lowering an activation saddle by Delta_Delta_G_dag = 3 k_B T (7.4 kJ/mol at 298 K, or 7.7 kJ/mol "
                        "at 310 K) multiplies escape or folding flux by exp(3) ≈ 20.09."
                    ),
                    "note_es": (
                        "Reducir una barrera en Delta_Delta_G_dag = 3 k_B T (7.4 kJ/mol a 298 K, o 7.7 kJ/mol a 310 K) "
                        "multiplica el flujo de escape o plegamiento por exp(3) ≈ 20.09."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Put real engineering numbers into that exponential. At room temperature (298 K, where k_B T ≈ 2.48 kJ/mol) "
                        "or physiological temperature (310 K, where k_B T ≈ 2.58 kJ/mol), trimming an activation barrier by just "
                        "Delta_Delta_G_dag = 3 k_B T—roughly 7.4 to 7.7 kJ/mol, the energy of a single modest hydrogen bond or "
                        "local packing contact—multiplies transition flux by e^3 ≈ 20.09. Trimming two independent contacts worth "
                        "6 k_B T multiplies flux by e^6 ≈ 403.43. In atomic metrology (`T.04` and `T.12`), the reverse calculation "
                        "protects coherence: raising an optical lattice trap depth from 10 k_B T to 16 k_B T suppresses thermal "
                        "atom-loss jumps by 403.43-fold. In structural engineering, sustained compressive stress tilts interparticle "
                        "hydration barriers inside cement gel pores, accelerating logarithmic concrete creep by the exact same "
                        "Eyring-Kramers exponential factor."
                    ),
                    "es": (
                        "Pongamos números reales de ingeniería en esa exponencial. A temperatura ambiente (298 K, donde "
                        "k_B T ≈ 2.48 kJ/mol) o a temperatura fisiológica (310 K, donde k_B T ≈ 2.58 kJ/mol), recortar una "
                        "barrera de activación en apenas Delta_Delta_G_dag = 3 k_B T —entre 7.4 y 7.7 kJ/mol, la energía de un "
                        "solo puente de hidrógeno modesto o de un contacto local de empaquetamiento— multiplica el flujo de "
                        "transición por e^3 ≈ 20.09. Recortar dos contactos independientes equivalentes a 6 k_B T multiplica el "
                        "flujo por e^6 ≈ 403.43. En metrología atómica (`T.04` y `T.12`), el cálculo inverso protege la "
                        "coherencia: elevar la profundidad de una trampa de red óptica de 10 k_B T a 16 k_B T reduce las fugas "
                        "térmicas de átomos 403.43 veces. En ingeniería estructural, el esfuerzo compresivo sostenido inclina las "
                        "barreras interpartícula en los poros de gel del cemento, acelerando la fluencia logarítmica del concreto "
                        "con el mismo factor exponencial de Eyring y Kramers."
                    ),
                },
            ],
        },
        {
            "id": "channel-hydrogel-synthesis",
            "h2_en": "V · One Equation Sheet at Nanometer Scale: An ATP-Gated Chloride Channel and a Porous Hydrogel",
            "h2_es": "V · Una Sola Hoja de Ecuaciones a Escala Nanométrica: Un Canal de Cloruro Compuertado por ATP y un Hidrogel Poroso",
            "short_en": "V · Synthesis",
            "short_es": "V · Síntesis",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Now shrink the viewport from 300 mm concrete pipes and 1 mm strontium-87 clouds down to a 10 nm "
                        "epithelial membrane boundary, and watch every equation derived in Sections I through IV lock together "
                        "without changing a single symbol. Embedded in the apical membrane sits CFTR, the sole member of the ABC "
                        "transporter superfamily that evolved into an ion channel—and the biophysical anchor of Cystic Fibrosis "
                        "research. A first-principles thermodynamic distinction is essential here: CFTR is an ATP-gated ion "
                        "channel, NOT an active ion pump. Once its transmembrane pore opens, chloride anions flow passively down "
                        "their electrochemical gradient at roughly 10^7 ions per second without consuming ATP per ion. Why, then, "
                        "does an ion channel burn chemical fuel at all? In 2006 László Csanády, Paola Vergani, David C. Gadsby, "
                        "and Angus C. Nairn answered that question quantitatively from single-channel dwell-time histograms and "
                        "activation enthalpies (DOI 10.1085/jgp.200609558): binding and irreversible hydrolysis of 1 ATP molecule "
                        "(Delta_mu_ATP ≈ 20 k_B T, cycle affinity A = 20) drive an asymmetric, non-equilibrium conformational "
                        "gating clock!"
                    ),
                    "es": (
                        "Reduzcamos ahora la lente desde tuberías de concreto de 300 mm y nubes de estroncio-87 de 1 mm hasta una "
                        "frontera epitelial de 10 nm, y observemos cómo todas las ecuaciones deducidas en las secciones I a IV "
                        "encajan sin cambiar un solo símbolo. Incrustada en la membrana apical se encuentra CFTR, el único "
                        "miembro de la superfamilia de transportadores ABC que evolucionó como canal iónico y el ancla biofísica "
                        "de la investigación en Fibrosis Quística. Aquí resulta indispensable una distinción termodinámica de "
                        "primeros principios: CFTR es un canal iónico compuertado por ATP, NO una bomba activa de iones. Una vez "
                        "abierto su poro transmembranal, los aniones cloruro fluyen pasivamente a favor de su gradiente "
                        "electroquímico a cerca de 10^7 iones por segundo sin consumir ATP por ion. ¿Por qué entonces quema "
                        "combustible químico un canal pasivo? En 2006 László Csanády, Paola Vergani, David C. Gadsby y Angus C. "
                        "Nairn respondieron cuantitativamente mediante histogramas de tiempos de apertura y entalpías de "
                        "activación (DOI 10.1085/jgp.200609558): la unión e hidrólisis irreversible de 1 molécula de ATP "
                        "(Delta_mu_ATP ≈ 20 k_B T, afinidad cíclica A = 20) impulsan un reloj conformacional irreversible fuera "
                        "del equilibrio."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Apply Part A and Part B directly to that 10 nm assembly. First, an equilibrium ligand-gated hinge (A = 0) "
                        "must obey detailed balance: its open-burst durations decay as a memoryless exponential and cannot "
                        "circulate around a directed state cycle. Feeding A = 20 into a 4-state Markovian gating ring gives "
                        "Q_TUR = (20 / 4) coth(20 / 8) ≈ 5.07 >= 2, using ATP free energy to buy peaked, clock-like open-burst "
                        "timing while passive electrodiffusion handles ion throughput. Second, before that channel ever reaches "
                        "the membrane, its five domains must fold across a rugged endoplasmic-reticulum energy landscape; as "
                        "Guido Veit, Gergely L. Lukacs, and colleagues demonstrated in 2020 for allosteric folding rescue in "
                        "Cystic Fibrosis mutants (DOI 10.1172/jci.insight.139983), small-molecule bridges binding distinct "
                        "domain interfaces act as structural gusset plates on a space truss—where lowering a kinetic folding "
                        "saddle by 3 k_B T multiplies productive Kramers escape by e^3 ≈ 20.09. Third, just outside the pore "
                        "mouth sits a hydrated mucin polymer network where ion-driven osmotic water flux maintains pore spacing: "
                        "when mesh permeability drops from kappa = 2.5 x 10^-15 m^2 (ell_B = 50 nm) to 1.0 x 10^-16 m^2 "
                        "(ell_B = 10 nm), Brinkman screening tightens 5-fold in length and 25-fold in Darcy drag. Mechanical "
                        "escapements, optical clocks, civil stone mortars, and nanoscale protein pores do not merely rhyme by "
                        "metaphor; they are governed by one indivisible set of physical bounds."
                    ),
                    "es": (
                        "Apliquemos directamente la Parte A y la Parte B a ese ensamblaje de 10 nm. Primero, una bisagra en "
                        "equilibrio térmico (A = 0) obedece el balance detallado: sus ráfagas de apertura decaen como una "
                        "exponencial sin memoria y no pueden circular en un ciclo dirigido. Inyectar A = 20 en un anillo "
                        "markoviano de compuerta de 4 estados arroja Q_TUR = (20 / 4) coth(20 / 8) ≈ 5.07 >= 2, empleando la "
                        "energía libre del ATP para comprar ráfagas de duración regular tipo reloj mientras la electrodifusión "
                        "pasiva transporta los iones. Segundo, antes de que ese canal llegue a la membrana, sus cinco dominios "
                        "deben plegarse sobre un paisaje energético rugoso; como demostraron Guido Veit, Gergely L. Lukacs y "
                        "colegas en 2020 sobre el rescate alostérico del plegamiento en mutantes asociados con Fibrosis Quística "
                        "(DOI 10.1172/jci.insight.139983), pequeñas moléculas que enlazan interfaces de dominio distantes actúan "
                        "como placas de nudo en una armadura espacial, donde bajar un punto silla cinético en 3 k_B T multiplica "
                        "el escape productivo de Kramers por e^3 ≈ 20.09. Tercero, justo afuera de la boca del poro reposa una "
                        "red polimérica hidratada donde el flujo osmótico mantiene el tamaño de malla: cuando la permeabilidad "
                        "cae de kappa = 2.5 x 10^-15 m^2 (ell_B = 50 nm) a 1.0 x 10^-16 m^2 (ell_B = 10 nm), el cribado de "
                        "Brinkman se estrecha 5 veces en longitud y aumenta 25 veces el arrastre de Darcy. Los escapes mecánicos, "
                        "los relojes ópticos, los morteros civiles y los poros proteicos nanométricos no riman por metáfora; "
                        "obedecen un único conjunto indivisible de cotas físicas."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote ES.03 · Saturation at A -> 0",
            "label_es": "Nota al margen ES.03 · Saturación en A -> 0",
            "en": (
                "Near thermal equilibrium (A << 2 N), expanding coth(x) ≈ 1/x + x/3 gives Q_TUR ≈ 2 + A^2 / (6 N^2), "
                "approaching the universal floor 2 from above at the cost of vanishing net clock speed J -> 0."
            ),
            "es": (
                "Cerca del equilibrio térmico (A << 2 N), desarrollar coth(x) ≈ 1/x + x/3 entrega Q_TUR ≈ 2 + A^2 / (6 N^2), "
                "acercándose desde arriba al piso universal 2 a costa de anular la velocidad neta del reloj J -> 0."
            ),
        },
        {
            "label_en": "Sidenote ES.03 · Quantum Ramsey Boundary",
            "label_es": "Nota al margen ES.03 · Frontera Cuántica de Ramsey",
            "en": (
                "Coherent unitary precession between two pi/2 laser pulses generates 0 entropy in the dark; irreversible "
                "entropy production occurs during fluorescence state readout, photon bath einselection, and optical pumping reset."
            ),
            "es": (
                "La precesión unitaria coherente entre dos pulsos láser de pi/2 genera 0 entropía en la oscuridad; la "
                "producción irreversible de entropía ocurre en la lectura por fluorescencia, la einselección del baño y el bombeo óptico."
            ),
        },
        {
            "label_en": "Sidenote ES.03 · Channel vs. Active Pump",
            "label_es": "Nota al margen ES.03 · Canal frente a Bomba Activa",
            "en": (
                "Active ATPase pumps move ions uphill against an electrochemical gradient (~1–3 ions per ATP). CFTR is an "
                "ATP-gated channel: 1 ATP (~20 k_B T) times the conformational gate while ~10^7 Cl- ions/s flow passively downhill."
            ),
            "es": (
                "Las bombas ATPasa activas empujan iones cuesta arriba contra un gradiente electroquímico (~1–3 iones por ATP). "
                "CFTR es un canal compuertado por ATP: 1 ATP (~20 k_B T) temporiza la compuerta mientras ~10^7 iones Cl-/s fluyen pasivamente."
            ),
        },
        {
            "label_en": "Sidenote ES.03 · Viscosity Cancellation in ell_B",
            "label_es": "Nota al margen ES.03 · Cancelación de Viscosidad en ell_B",
            "en": (
                "Because both Stokes shear (eta laplacian u) and Darcy drag ((eta / kappa) u) are linear in dynamic viscosity "
                "eta, their ratio depends solely on pore geometry: ell_B = sqrt(kappa) has pure dimensions of length."
            ),
            "es": (
                "Como tanto el cortante de Stokes (eta laplacian u) como el arrastre de Darcy ((eta / kappa) u) son lineales en "
                "la viscosidad dinámica eta, su cociente depende solo de la geometría porosa: ell_B = sqrt(kappa) tiene dimensión pura de longitud."
            ),
        },
        {
            "label_en": "Sidenote ES.03 · Kramers 3 k_B T Rule of Thumb",
            "label_es": "Nota al margen ES.03 · Regla de Kramers de 3 k_B T",
            "en": (
                "Every 2.303 k_B T reduction in activation barrier multiplies escape rate by 10; a 3 k_B T allosteric or "
                "mechanical stress tilt yields exp(3) ≈ 20.09-fold higher flux without changing temperature T."
            ),
            "es": (
                "Cada reducción de 2.303 k_B T en la barrera de activación multiplica la tasa de escape por 10; una inclinación "
                "mecánica o alostérica de 3 k_B T produce un flujo exp(3) ≈ 20.09 veces mayor sin cambiar la temperatura T."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES03-BARATO2015",
            "citation": "Barato, A. C., & Seifert, U. (2015). Thermodynamic uncertainty relation for biomolecular processes. Physical Review Letters, 114, 158101.",
            "doi": "10.1103/physrevlett.114.158101",
            "year": 2015,
            "role_en": "Establishes the universal classical Markovian steady-state bound Q_TUR = (Var(N)/<N>^2)(Delta_S/k_B) >= 2.",
            "role_es": "Establece la cota universal estacionaria markoviana clásica Q_TUR = (Var(N)/<N>^2)(Delta_S/k_B) >= 2.",
        },
        {
            "id": "ES03-SEIFERT2012",
            "citation": "Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. Reports on Progress in Physics, 75(12), 126001.",
            "doi": "10.1088/0034-4885/75/12/126001",
            "year": 2012,
            "role_en": "Defines trajectory-level entropy production, cycle affinities, and fluctuation theorems for non-equilibrium rings.",
            "role_es": "Define la producción de entropía por trayectoria, afinidades cíclicas y teoremas de fluctuación fuera del equilibrio.",
        },
        {
            "id": "ES03-RAO2016",
            "citation": "Rao, R., & Esposito, M. (2016). Nonequilibrium thermodynamics of chemical reaction networks: Wisdom from stochastic thermodynamics. Physical Review X, 6, 041064.",
            "doi": "10.1103/physrevx.6.041064",
            "year": 2016,
            "role_en": "Extends cycle affinities and non-equilibrium free-energy dissipation to open chemical reaction networks.",
            "role_es": "Extiende las afinidades cíclicas y la disipación fuera del equilibrio a redes abiertas de reacciones químicas.",
        },
        {
            "id": "ES03-BOTHWELL2022",
            "citation": "Bothwell, T., Kennedy, C. J., Aeppli, A., Kedar, D., Robinson, J. M., Oelker, E., Staron, A., & Ye, J. (2022). Resolving the gravitational redshift across a millimetre-scale atomic sample. Nature, 602, 420–424.",
            "doi": "10.1038/s41586-021-04349-7",
            "year": 2022,
            "role_en": "Demonstrates coherent 87Sr optical clock phase evolution across 1 mm at ~10^-19 fractional stability.",
            "role_es": "Demuestra la evolución coherente de fase en un reloj óptico de 87Sr a través de 1 mm con estabilidad ~10^-19.",
        },
        {
            "id": "ES03-ZUREK2009",
            "citation": "Zurek, W. H. (2009). Quantum Darwinism. Nature Physics, 5, 181–188.",
            "doi": "10.1038/nphys1202",
            "year": 2009,
            "role_en": "Explains how irreversible bath scattering einselects and redundantly records classical pointer states.",
            "role_es": "Explica cómo la dispersión irreversible en el baño selecciona y copia estados puntero clásicos.",
        },
        {
            "id": "ES03-BRINKMAN1949",
            "citation": "Brinkman, H. C. (1949). A calculation of the viscous force exerted by a flowing fluid on a dense swarm of particles. Applied Scientific Research / Flow, Turbulence and Combustion, 1, 27–34.",
            "doi": "10.1007/bf02120313",
            "year": 1949,
            "role_en": "Introduces the Stokes-Darcy momentum equation and viscous screening length ell_B = sqrt(kappa).",
            "role_es": "Introduce la ecuación de momento de Stokes-Darcy y la longitud de cribado viscoso ell_B = sqrt(kappa).",
        },
        {
            "id": "ES03-FEYS2016",
            "citation": "Feys, D., De Schutter, G., Khayat, K. H., & Verhoeven, R. (2016). How do concrete rheology, tribology, flow rate and pipe radius influence pumping pressure? Cement and Concrete Composites, 66, 38–46.",
            "doi": "10.1016/j.cemconcomp.2015.11.002",
            "year": 2016,
            "role_en": "Quantifies wall shear lubrication layers vs. plug core transport in pumped structural concrete pipes.",
            "role_es": "Cuantifica las capas lubricantes de cortante parietal frente al núcleo tapón en tuberías de concreto bombeado.",
        },
        {
            "id": "ES03-STEWART2003",
            "citation": "Stewart, P. S. (2003). Diffusion in biofilms. Journal of Bacteriology, 185(5), 1485–1491.",
            "doi": "10.1128/jb.185.5.1485-1491.2003",
            "year": 2003,
            "role_en": "Characterizes hindered transport and porous-mesh screening across hydrated biopolymer matrices.",
            "role_es": "Caracteriza el transporte impedido y el cribado de malla porosa en matrices biopoliméricas hidratadas.",
        },
        {
            "id": "ES03-CSANADY2006",
            "citation": "Csanády, L., Vergani, P., Gadsby, D. C., & Nairn, A. C. (2006). Thermodynamics of CFTR channel gating: A spreading conformational change initiates an irreversible gating cycle. Journal of General Physiology, 128(5), 523–533.",
            "doi": "10.1085/jgp.200609558",
            "year": 2006,
            "role_en": "Proves CFTR uses ATP hydrolysis to drive an irreversible non-equilibrium gating cycle while Cl- flows passively.",
            "role_es": "Demuestra que CFTR usa la hidrólisis de ATP para impulsar un ciclo irreversible de compuerta con flujo pasivo de Cl-.",
        },
        {
            "id": "ES03-VEIT2020",
            "citation": "Veit, G., Roldan, A., Hancock, M. A., Da Fonte, D. F., Xu, H., Hussein, M., Frenkiel, S., Berthiaume, Y., & Lukacs, G. L. (2020). Allosteric folding correction of F508del and rare CFTR mutants by elexacaftor-tezacaftor-ivacaftor (Trikafta) combination. JCI Insight, 5(18), e139983.",
            "doi": "10.1172/jci.insight.139983",
            "year": 2020,
            "role_en": "Shows cooperative multi-domain allosteric stabilization lowering kinetic folding barriers of misfolded CFTR.",
            "role_es": "Muestra la estabilización alostérica cooperativa multidominio que reduce barreras cinéticas de plegamiento de CFTR.",
        },
    ],
    "skill_path": "skills/essays/barriers-pores-clocks/SKILL.md",
    "verifier_path": "skills/essays/barriers-pores-clocks/verify_essay_barriers_pores_clocks.py",
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any physical law, measurement, or experiment "
        "cited in this essay. The synthesis prose, pure-Python transport/clock kernel, and deterministic verifier were drafted "
        "with AI assistance and audited against the 10 primary sources listed below."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a ninguna ley física, medición "
        "o experimento citado en este ensayo. El texto de síntesis, el núcleo en Python puro y el verificador determinista se "
        "redactaron con asistencia de IA y se auditaron contra las 10 fuentes primarias listadas abajo."
    ),
}
