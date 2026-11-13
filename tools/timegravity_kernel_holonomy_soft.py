#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Infrared gauge-gravity consistency, gravitational-wave memory holonomy, and mixed anomaly kernel (T.13, stdlib only).

T.13  Where Infrared Gravity Meets Gauge Theory:
      1. Weinberg (1964, 1965) Soft Theorems & Higher-Spin Obstruction:
         In relativistic 4-body scattering (1 + 2 -> 3 + 4) with conserved external 4-momenta
         sum_a eta_a p_a^mu = 0 (eta_in = -1, eta_out = +1), longitudinal gauge variation of an emitted
         soft massless boson of helicity s produces a Ward residual:
           - s = 1 (soft photon, eps_mu -> eps_mu + q_mu):
             Delta S^(1) = sum_a eta_a q_a = 0  <=>  charge conservation.
           - s = 2 (soft graviton, eps_{mu nu} -> eps_{mu nu} + q_{(mu} Lambda_{nu)}):
             W^mu = sum_a eta_a kappa_a p_a^mu = 0 for generic conserved 4-momenta
             <=> universal gravitational coupling kappa_a = kappa = sqrt(32 pi G / c^4)
             (Weak Equivalence Principle eta_WEP = 0 from infrared Lorentz invariance).
           - s = 3 (massless higher spin, eps_{mu nu rho} -> eps_{mu nu rho} + q_{(mu} Lambda_{nu rho)}):
             W^{mu nu} = sum_a eta_a g_a p_a^mu p_a^nu = 0 has full column rank 4 across generic
             conserved 4-momenta, forcing g_a = 0 identically (no macroscopic long-range s >= 3 force).
      2. Christodoulou (1991) / Strominger-Zhiboedov (2016) Gravitational-Wave Memory & Arm Holonomy:
         Radiated gravitational-wave energy E_rad at luminosity distance D_L leaves a permanent DC
         transverse-traceless strain step of characteristic scale
           Delta h_char^mem = G E_rad / (c^4 D_L),
         and leading quadrupole inclination profile Delta h_+^mem(iota) = Delta h_char^mem * sin^2(iota)*(17 + cos^2(iota))/24,
         shifting free-falling test-mass / optical-clock proper separation permanently by
           Delta L / L_0 = (1 / 2) Delta h_+^mem.
         Verified by composite 5-point Gauss-Legendre quadrature of dE_rad/dt against the exact hyperbolic-tangent
         antiderivative to < 1e-12 on fiducial GW150914 (E_rad = 3.0 M_sun c^2, D_L = 410 Mpc) and fiducial
         GW250114-class (E_rad = 3.0 M_sun c^2, D_L = 400 Mpc) benchmarks.
      3. Chiral & Mixed Gauge-Gravitational Anomaly Cancellation (Adler 1969; Delbourgo-Salam 1972; Tooby-Smith 2025):
         For one Standard Model left-handed Weyl generation with integer-scaled hypercharges 6Y
         (Q_L: 2 N_c at +1, u_R^c: N_c at -4, d_R^c: N_c at +2, L_L: 2 at -3, e_R^c: 1 at +6):
           - Mixed gravitational-hypercharge trace: Tr[grav^2 (6Y)](N_c) = 2 N_c - 4 N_c + 2 N_c - 6 + 6 = 0.
           - SU(3)_c^2 x U(1)_Y trace: 2 Tr[T_{SU(3)}^2 (6Y)] = 2(+1) + (-4) + (+2) = 0.
           - SU(2)_L^2 x U(1)_Y trace: 2 Tr[T_{SU(2)}^2 (6Y)](N_c) = N_c - 3 = 0  <=>  N_c = 3.
           - Cubic U(1)_Y^3 trace: Tr[(6Y)^3](N_c) = -54 (N_c - 3) = 0  <=>  N_c = 3.
      4. Planted-defect knockout (--planted-defect):
         Perturbing species gravitational coupling kappa_e / kappa_p = 1 + 1e-5 breaks the soft-graviton Ward
         identity ||W^mu|| > 0, and setting quark colour multiplicity N_c = 2 != 3 breaks SU(2)_L^2 U(1)_Y and
         cubic U(1)_Y^3 anomaly cancellation.
"""
from __future__ import annotations

import json
import math
import sys

from timegravity_kernel import C
from timegravity_kernel_horizon import G_NEWTON, HBAR, M_SUN

PARSEC_M = 3.0856775814913673e16          # m (IAU 2012 exact SI parsec)
MPC_M = 1.0e6 * PARSEC_M                  # m (megaparsec)

# Universal Einstein gravitational coupling kappa = sqrt(32 pi G / c^4) in SI [J^-1/2 m^1/2]
KAPPA_SI = math.sqrt(32.0 * math.pi * G_NEWTON / (C ** 4))

# Fiducial binary-merger memory benchmarks (aligned with T.09 / T.10 ledger conventions)
GW150914_E_RAD_SOLAR = 3.0                # M_sun c^2 radiated energy (LIGO/Virgo 2016 fiducial scale)
GW150914_DL_MPC = 410.0                   # Mpc luminosity distance (LIGO/Virgo 2016 fiducial median)
GW250114_E_RAD_SOLAR = 3.0                # M_sun c^2 fiducial radiated energy for high-SNR O4 benchmark
GW250114_DL_MPC = 400.0                   # Mpc fiducial luminosity distance for GW250114-scale comparison
LIGO_ARM_M = 4000.0                       # m (4 km Fabry-Perot arm baseline)
LISA_ARM_M = 2.5e9                        # m (2.5 million km space-interferometer arm baseline)

# 5-point Gauss-Legendre nodes and weights on [-1, 1]
_GL5_X = (
    -0.9061798459386640,
    -0.5384693101056831,
    0.0,
    0.5384693101056831,
    0.9061798459386640,
)
_GL5_W = (
    0.2369268850561891,
    0.4786286704993665,
    0.5688888888888889,
    0.4786286704993665,
    0.2369268850561891,
)

# Standard Model left-handed Weyl fermion hypercharges scaled by 6 (integer exact)
SM_WEYL_FIELDS_6Y = (
    ("Q_L", "quark_doublet", 2, 1),       # multiplicity = 2 * N_c, 6Y = +1
    ("u_R^c", "up_antiquark", 1, -4),     # multiplicity = 1 * N_c, 6Y = -4
    ("d_R^c", "down_antiquark", 1, 2),    # multiplicity = 1 * N_c, 6Y = +2
    ("L_L", "lepton_doublet", 2, -3),     # multiplicity = 2,       6Y = -3
    ("e_R^c", "positron_singlet", 1, 6),  # multiplicity = 1,       6Y = +6
)


def elastic_2to2_kinematics(
    m1_gev: float = 0.00051099895,
    m2_gev: float = 0.938272088,
    p_cm_gev: float = 2.5,
    theta_rad: float = 0.73,
    phi_rad: float = 0.41,
) -> tuple[list[tuple[float, float, float, float]], tuple[int, int, int, int]]:
    """Construct exact relativistic 2 -> 2 scattering 4-momenta (E, px, py, pz) in GeV.

    Incoming: a = 0 (species 1, eta = -1), a = 1 (species 2, eta = -1).
    Outgoing: a = 2 (species 1, eta = +1), a = 3 (species 2, eta = +1).
    Satisfies sum_a eta_a p_a^mu = 0 to machine precision with rank 3 for {p_0, p_1, p_2}.
    """
    e1 = math.sqrt(m1_gev * m1_gev + p_cm_gev * p_cm_gev)
    e2 = math.sqrt(m2_gev * m2_gev + p_cm_gev * p_cm_gev)
    p1_in = (e1, 0.0, 0.0, p_cm_gev)
    p2_in = (e2, 0.0, 0.0, -p_cm_gev)

    kx = p_cm_gev * math.sin(theta_rad) * math.cos(phi_rad)
    ky = p_cm_gev * math.sin(theta_rad) * math.sin(phi_rad)
    kz = p_cm_gev * math.cos(theta_rad)
    p3_out = (e1, kx, ky, kz)
    p4_out = (e2, -kx, -ky, -kz)
    etas = (-1, -1, +1, +1)
    return [p1_in, p2_in, p3_out, p4_out], etas


def _gram_det(cols: list[list[float]]) -> float:
    """Exact Bareiss/Gaussian determinant of the Gram matrix G_{ij} = cols[i] . cols[j]."""
    k = len(cols)
    mat = [
        [sum(cols[i][m] * cols[j][m] for m in range(len(cols[0]))) for j in range(k)]
        for i in range(k)
    ]
    det = 1.0
    for i in range(k):
        piv = max(range(i, k), key=lambda r: abs(mat[r][i]))
        if abs(mat[piv][i]) < 1e-30:
            return 0.0
        if piv != i:
            mat[i], mat[piv] = mat[piv], mat[i]
            det = -det
        det *= mat[i][i]
        inv = 1.0 / mat[i][i]
        for r in range(i + 1, k):
            fac = mat[r][i] * inv
            for c in range(i, k):
                mat[r][c] -= fac * mat[i][c]
    return det


def soft_ward_identities(
    kappa_ratio_e_over_p: float = 1.0,
    charge_imbalance: float = 0.0,
    spin3_coupling_g: float = 0.0,
) -> dict:
    """Evaluate Weinberg's s = 1, 2, 3 soft gauge Ward residuals on conserved 2 -> 2 kinematics."""
    momenta, etas = elastic_2to2_kinematics()
    e_cm = momenta[0][0] + momenta[1][0]

    # Momentum conservation residual ||sum_a eta_a p_a^mu||
    p_cons_vec = [sum(etas[a] * momenta[a][mu] for a in range(4)) for mu in range(4)]
    p_cons_norm = math.sqrt(sum(x * x for x in p_cons_vec))

    # Spin s = 1 (soft photon): q_1 = -1, q_2 = +1, q_3 = -1 + charge_imbalance, q_4 = +1
    charges = (-1.0, +1.0, -1.0 + charge_imbalance, +1.0)
    ward_s1_charge = sum(etas[a] * charges[a] for a in range(4))

    # Spin s = 2 (soft graviton): species 1 (electron) has kappa_1 = kappa_3 = kappa_ratio, species 2 (proton) = 1.0
    kappas = (kappa_ratio_e_over_p, 1.0, kappa_ratio_e_over_p, 1.0)
    ward_s2_vec = [sum(etas[a] * kappas[a] * momenta[a][mu] for a in range(4)) for mu in range(4)]
    ward_s2_norm = math.sqrt(sum(x * x for x in ward_s2_vec)) / e_cm
    eta_wep_implied = abs(kappa_ratio_e_over_p - 1.0)

    # Linear independence of {p_0, p_1, p_2} in R^4 proves kappa_a = const is unique for s = 2
    gram_det_s2_three_momenta = _gram_det([list(momenta[0]), list(momenta[1]), list(momenta[2])])

    # Spin s = 3 (massless spin-3): 10 symmetric components p_a^mu p_a^nu (0 <= mu <= nu < 4)
    sym_cols: list[list[float]] = []
    for a in range(4):
        p = momenta[a]
        col = [etas[a] * p[mu] * p[nu] for mu in range(4) for nu in range(mu, 4)]
        sym_cols.append(col)
    gram_det_s3_four_tensors = _gram_det(sym_cols)

    # If a hypothetical spin-3 charge g_a = spin3_coupling_g were non-zero (even universal!), W^{mu nu} != 0:
    gs = (spin3_coupling_g, spin3_coupling_g, spin3_coupling_g, spin3_coupling_g)
    ward_s3_sym = [sum(gs[a] * sym_cols[a][idx] for a in range(4)) for idx in range(10)]
    ward_s3_norm = math.sqrt(sum(x * x for x in ward_s3_sym)) / (e_cm * e_cm)
    # Unit-coupling obstruction norm (proves even universal g_a = 1 fails for s = 3!)
    unit_s3_sym = [sum(sym_cols[a][idx] for a in range(4)) for idx in range(10)]
    unit_s3_obstruction_norm = math.sqrt(sum(x * x for x in unit_s3_sym)) / (e_cm * e_cm)

    return {
        "e_cm_gev": e_cm,
        "momentum_conservation_norm_gev": p_cons_norm,
        "s1_charge_ward_residual": ward_s1_charge,
        "s2_kappa_ratio_e_over_p": kappa_ratio_e_over_p,
        "s2_ward_vector_rel_norm": ward_s2_norm,
        "s2_eta_wep_implied": eta_wep_implied,
        "s2_three_momenta_gram_det": gram_det_s2_three_momenta,
        "s3_four_tensor_gram_det": gram_det_s3_four_tensors,
        "s3_ward_tensor_rel_norm": ward_s3_norm,
        "s3_universal_unit_obstruction_norm": unit_s3_obstruction_norm,
    }


def memory_inclination_factor(iota_rad: float) -> float:
    """Leading quadrupole DC memory angular factor Phi(iota) = sin^2(iota) * (17 + cos^2(iota)) / 24."""
    s = math.sin(iota_rad)
    c = math.cos(iota_rad)
    return (s * s) * (17.0 + c * c) / 24.0


def memory_strain_step(
    e_rad_solar: float = GW150914_E_RAD_SOLAR,
    d_l_mpc: float = GW150914_DL_MPC,
    iota_rad: float = math.pi / 2.0,
    arm_length_m: float = LIGO_ARM_M,
) -> dict:
    """Compute Christodoulou / Strominger-Zhiboedov gravitational-wave memory strain and arm shift."""
    e_rad_j = e_rad_solar * M_SUN * (C ** 2)
    d_l_m = d_l_mpc * MPC_M
    # Characteristic infrared memory scale: Delta h_char = G E_rad / (c^4 D_L)
    # Favata 2009 (ApJL 696, L159), Eq. (5), with the l = m = 2 energy flux: Delta h_+ = dh_char * sin^2(i) (17 + cos^2(i)) / 24
    dh_char = G_NEWTON * e_rad_j / ((C ** 4) * d_l_m)
    phi_inc = memory_inclination_factor(iota_rad)
    dh_plus_inclined = dh_char * phi_inc

    # Proper separation step Delta L = (1/2) L_0 Delta h
    dl_char_m = 0.5 * arm_length_m * dh_char
    dl_inclined_m = 0.5 * arm_length_m * dh_plus_inclined

    return {
        "e_rad_solar": e_rad_solar,
        "e_rad_j": e_rad_j,
        "d_l_mpc": d_l_mpc,
        "d_l_m": d_l_m,
        "iota_rad": iota_rad,
        "inclination_factor": phi_inc,
        "arm_length_m": arm_length_m,
        "delta_h_char": dh_char,
        "delta_h_plus_inclined": dh_plus_inclined,
        "delta_l_char_m": dl_char_m,
        "delta_l_inclined_m": dl_inclined_m,
    }


def memory_flux_quadrature_check(
    e_rad_solar: float = GW150914_E_RAD_SOLAR,
    d_l_mpc: float = GW150914_DL_MPC,
    tau_merger_s: float = 0.005,
    n_panels: int = 400,
) -> dict:
    """Double-entry check: integrate d(Delta h)/dt = (2G / c^4 D_L) dE_rad/dt via 5-point Gauss-Legendre.

    Uses smooth burst flux profile dE_rad/dt = E_rad / (2 tau_m cosh^2(t / tau_m)) over [-22 tau_m, +22 tau_m],
    where sech^2(22) < 3.2e-19, and compares against closed-form step Delta h_char * (tanh(T/tau_m) - tanh(-T_max/tau_m))/2.
    """
    step_info = memory_strain_step(e_rad_solar=e_rad_solar, d_l_mpc=d_l_mpc, iota_rad=math.pi / 2.0)
    dh_char = step_info["delta_h_char"]
    t_max = 22.0 * tau_merger_s
    panel_w = (2.0 * t_max) / n_panels

    total = 0.0
    for k in range(n_panels):
        a = -t_max + k * panel_w
        b = a + panel_w
        mid = 0.5 * (a + b)
        half = 0.5 * (b - a)
        acc = 0.0
        for x_i, w_i in zip(_GL5_X, _GL5_W):
            u = (mid + half * x_i) / tau_merger_s
            # sech^2(u) = 4 / (exp(u) + exp(-u))^2 avoids overflow
            eu = math.exp(-abs(u))
            sech2 = 4.0 * (eu * eu) / ((1.0 + eu * eu) ** 2)
            rate = dh_char * sech2 / (2.0 * tau_merger_s)
            acc += w_i * rate
        total += half * acc

    exact_window = 0.5 * dh_char * (math.tanh(22.0) - math.tanh(-22.0))
    rel_err_window = abs(total - exact_window) / dh_char
    rel_err_asymptotic = abs(total - dh_char) / dh_char
    return {
        "dh_quadrature": total,
        "dh_closed_form": dh_char,
        "quadrature_rel_err": rel_err_asymptotic,
        "quadrature_window_rel_err": rel_err_window,
    }


def anomaly_traces_6y(n_c: int = 3, include_right_electron: bool = True) -> dict:
    """Exact integer chiral and mixed gauge-gravitational anomaly traces for one SM Weyl generation."""
    # Q_L: 2 * N_c * (+1); u_R^c: N_c * (-4); d_R^c: N_c * (+2); L_L: 2 * (-3); e_R^c: 1 * (+6)
    e_mult = 1 if include_right_electron else 0

    tr_grav = 2 * n_c * 1 + n_c * (-4) + n_c * 2 + 2 * (-3) + e_mult * 6
    tr_su3 = 2 * 1 + 1 * (-4) + 1 * 2
    tr_su2 = n_c * 1 + 1 * (-3)
    tr_cubic = (
        2 * n_c * (1 ** 3)
        + n_c * ((-4) ** 3)
        + n_c * (2 ** 3)
        + 2 * ((-3) ** 3)
        + e_mult * (6 ** 3)
    )
    all_zero = (tr_grav == 0) and (tr_su3 == 0) and (tr_su2 == 0) and (tr_cubic == 0)
    return {
        "n_c": int(n_c),
        "include_right_electron": bool(include_right_electron),
        "tr_grav_6y": int(tr_grav),
        "tr_su3_sq_6y": int(tr_su3),
        "tr_su2_sq_6y": int(tr_su2),
        "tr_u1_cubic_6y": int(tr_cubic),
        "all_anomalies_cancel": bool(all_zero),
    }


def anomaly_nc_scan(nc_values: tuple[int, ...] = (1, 2, 3, 4, 5)) -> list[dict]:
    """Scan quark colour multiplicity N_c across positive integers to demonstrate N_c = 3 uniqueness."""
    return [anomaly_traces_6y(n_c=nc, include_right_electron=True) for nc in nc_values]


def build_reference(planted_defect: bool = False) -> dict:
    """Build complete T.13 reference payload for make_t13.py and verify_t13_holonomy_soft.py."""
    kappa_ratio = 1.0 + 1.0e-5 if planted_defect else 1.0
    n_c = 2 if planted_defect else 3

    soft = soft_ward_identities(kappa_ratio_e_over_p=kappa_ratio, charge_imbalance=0.0, spin3_coupling_g=0.0)
    gw150914 = memory_strain_step(
        e_rad_solar=GW150914_E_RAD_SOLAR,
        d_l_mpc=GW150914_DL_MPC,
        iota_rad=math.pi / 2.0,
        arm_length_m=LIGO_ARM_M,
    )
    gw250114_fid = memory_strain_step(
        e_rad_solar=GW250114_E_RAD_SOLAR,
        d_l_mpc=GW250114_DL_MPC,
        iota_rad=math.pi / 2.0,
        arm_length_m=LIGO_ARM_M,
    )
    lisa_fid = memory_strain_step(
        e_rad_solar=GW150914_E_RAD_SOLAR,
        d_l_mpc=GW150914_DL_MPC,
        iota_rad=math.pi / 2.0,
        arm_length_m=LISA_ARM_M,
    )
    quad = memory_flux_quadrature_check(
        e_rad_solar=GW150914_E_RAD_SOLAR,
        d_l_mpc=GW150914_DL_MPC,
    )
    anom = anomaly_traces_6y(n_c=n_c, include_right_electron=True)
    anom_no_er = anomaly_traces_6y(n_c=3, include_right_electron=False)
    nc_table = anomaly_nc_scan((1, 2, 3, 4, 5))

    return {
        "step": "T.13",
        "planted_defect": bool(planted_defect),
        "constants": {
            "c_m_s": C,
            "g_si": G_NEWTON,
            "hbar_j_s": HBAR,
            "m_sun_kg": M_SUN,
            "mpc_m": MPC_M,
            "kappa_si": KAPPA_SI,
        },
        "soft_theorems": soft,
        "memory_benchmarks": {
            "gw150914_fiducial": gw150914,
            "gw250114_fiducial": gw250114_fid,
            "gw150914_on_lisa_arm": lisa_fid,
            "flux_quadrature": quad,
        },
        "anomaly_cancellation": {
            "active_generation": anom,
            "without_right_electron_knockout": anom_no_er,
            "nc_scan": nc_table,
        },
    }


if __name__ == "__main__":
    defect = "--planted-defect" in sys.argv[1:]
    print(json.dumps(build_reference(planted_defect=defect), indent=2, sort_keys=True))
