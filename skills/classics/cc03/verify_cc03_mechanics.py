#!/usr/bin/env python3
"""Verify CC.03 · Mechanics Lab (MINI -> F56 JCW feature): load transfer, brake rotor thermal rise, Indy speeds & NA/EU unit conversion.

Standard library only. Reads ONLY data tables and MODEL parameters from cc03 / cc03_mechanics, re-derives every
result independently, cross-checks algebraic identities and time-domain numerical integration, checks the rendered
English and Spanish pages, and fails on five computational planted defects.

  python skills/classics/cc03/verify_cc03_mechanics.py
  python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect
  python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect=single-disc
  python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect=config
  python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect=unit-kmh
  python skills/classics/cc03/verify_cc03_mechanics.py --planted-defect=hp-ps
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc03 as C  # noqa: E402  (data only)
from folios.classics import cc03_mechanics as M  # noqa: E402  (MODEL inputs only; physics re-derived here)

PINNED_SHA256 = "1fe82316fc2e1f5164fb50eb958fbdcbc6422da35502eff48058a5a686bc9502"
PAGES = (
    ROOT / "src" / "classics" / "mini-jcw" / "index.html",
    ROOT / "src" / "es-mx" / "classics" / "mini-jcw" / "index.html",
)

arg = next((a for a in sys.argv[1:] if a.startswith("--planted-defect")), "")
DEFECT = (arg.split("=", 1)[1] if "=" in arg else "load-sign") if arg else ""


def canonical() -> bytes:
    data = {
        "laps": [list(r) for r in C.LAPS],
        "load": M.LOAD_MODEL,
        "brake": M.BRAKE_MODEL,
        "indy_miles": M.INDY_MILES,
        "power_units": M.POWER_UNIT_MODEL,
    }
    return json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")


# -------------------------------------------------------------------------------------- independent physics ----
def fy_wheel(fz: float, lm: dict) -> float:
    sign = 1.0 if DEFECT == "load-sign" else -1.0
    return fz * (lm["mu_0"] + sign * lm["k_load"] * fz)


def recompute_load(ay_g: float, key: str, lm: dict) -> dict:
    _en, _es, h_cg, trk = lm["geometries"][key]
    fz0 = 0.5 * lm["m_axle_kg"] * lm["g"]
    dfz_raw = lm["m_axle_kg"] * lm["g"] * ay_g * h_cg / trk
    dfz = min(dfz_raw, fz0)
    fz_in = fz0 - dfz
    fz_out = fz0 + dfz
    fy_in = fy_wheel(fz_in, lm)
    fy_out = fy_wheel(fz_out, lm)
    fy_total = fy_in + fy_out
    fy_flat = 2.0 * fy_wheel(fz0, lm)
    loss = fy_flat - fy_total
    return {
        "dfz": dfz,
        "fz_in": fz_in,
        "fz_out": fz_out,
        "fy_total": fy_total,
        "loss": loss,
        "slope_out": lm["mu_0"] - 2.0 * lm["k_load"] * fz_out,
    }


def recompute_brake_numerical(v1_kmh: float, rotor_key: str, bm: dict) -> dict:
    """Independent time-domain numerical integration of constant-deceleration braking power P(t) = F * v(t)."""
    _en, _es, m_disc = bm["rotors"][rotor_key]
    scale = 1.0 if DEFECT == "unit-kmh" else (1.0 / 3.6)
    v1_ms = v1_kmh * scale
    v2_ms = bm["v2_kmh"] * scale
    steps = 1000
    # Over dimensionless braking time tau in [0, 1], uniform deceleration v(tau) = v1 - (v1 - v2)*tau,
    # total mechanical work = integral_0^1 m * (v1 - v2) * v(tau) dtau via trapezoidal quadrature.
    dv = v1_ms - v2_ms
    work_j = 0.0
    dtau = 1.0 / steps
    for i in range(steps):
        va = v1_ms - dv * (i * dtau)
        vb = v1_ms - dv * ((i + 1) * dtau)
        work_j += 0.5 * bm["m_car_kg"] * dv * (va + vb) * dtau
    e_front_j = bm["front_share"] * work_j
    e_disc_j = e_front_j if DEFECT == "single-disc" else (e_front_j / 2.0)
    dt_c = e_disc_j / (m_disc * bm["cp_j_kgk"])
    return {
        "m_disc": m_disc,
        "work_j": work_j,
        "e_disc_kj": e_disc_j / 1000.0,
        "dt_c": dt_c,
        "t_peak_c": bm["t_amb_c"] + dt_c,
    }


def parse_lap_secs(ts: str) -> float:
    mins, sec = ts.split(":")
    return int(mins) * 60.0 + float(sec)


# -------------------------------------------------------------------------------------------------- checks ----
def main() -> int:
    fails: list[str] = []
    digest = hashlib.sha256(canonical()).hexdigest()
    if digest != PINNED_SHA256:
        fails.append(f"data pin: {digest} != reviewed {PINNED_SHA256}")

    lm = dict(M.LOAD_MODEL)
    ay = lm["ay_start_g"]
    load_res = {k: recompute_load(ay, k, lm) for k in ("tall", "f56", "kart")}
    for k, r in load_res.items():
        if r["fz_in"] <= 0.0:
            fails.append(f"load[{k}]: inside wheel lifted (fz_in={r['fz_in']:.1f} N)")
        if r["slope_out"] <= 0.0:
            fails.append(f"load[{k}]: outside wheel passed tire peak parabola (slope={r['slope_out']:.3f})")
        analytic_loss = 2.0 * lm["k_load"] * (r["dfz"] ** 2)
        if abs(r["loss"] - analytic_loss) > 1e-6:
            fails.append(f"load[{k}]: grip loss {r['loss']:.4f} != algebraic 2*k*(dfz)^2 {analytic_loss:.4f}")
    if not (load_res["tall"]["loss"] > load_res["f56"]["loss"] > load_res["kart"]["loss"] > 0.0):
        fails.append("load: expected positive decreasing grip loss tall > f56 > kart")

    bm = dict(M.BRAKE_MODEL)
    v1 = bm["v1_start_kmh"]
    true_ke_j = 0.5 * bm["m_car_kg"] * ((v1 / 3.6) ** 2 - (bm["v2_kmh"] / 3.6) ** 2)
    brake_res = {k: recompute_brake_numerical(v1, k, bm) for k in ("small", "mid", "brembo")}
    for k, r in brake_res.items():
        if abs(r["work_j"] - true_ke_j) > 1e-2:
            fails.append(f"brake[{k}]: kinetic energy {r['work_j']:.1f} J != SI 1/2 m dv^2 {true_ke_j:.1f} J")
        expected_disc_kj = 0.5 * bm["front_share"] * true_ke_j / 1000.0
        if abs(r["e_disc_kj"] - expected_disc_kj) > 1e-3:
            fails.append(f"brake[{k}]: per-disc energy {r['e_disc_kj']:.2f} kJ != {expected_disc_kj:.2f} kJ")
    if not (brake_res["small"]["dt_c"] > brake_res["mid"]["dt_c"] > brake_res["brembo"]["dt_c"] > 0.0):
        fails.append("brake: expected dt_small > dt_mid > dt_brembo > 0")

    indy_m = M.INDY_MILES * 1609.344
    speeds: dict[str, tuple[float, float]] = {}
    for rid, _era, car, _year, ts, secs, _drv, listed_mph, cfg, _sk in C.LAPS:
        parsed = parse_lap_secs(ts)
        if abs(parsed - secs) > 1e-6:
            fails.append(f"laps[{rid}]: string {ts} != {secs}")
        if cfg or DEFECT == "config":
            kmh_v = indy_m / parsed * 3.6
            mph_v = M.INDY_MILES / (parsed / 3600.0)
            speeds[rid] = (kmh_v, mph_v)
            if listed_mph != "not stated":
                listed_val = float(listed_mph.split()[0])
                if abs(mph_v - listed_val) > 0.02:
                    fails.append(f"laps[{rid}]: derived {mph_v:.2f} mph vs table {listed_val:.2f} mph (>0.02)")
    if len(speeds) != 4:
        fails.append(f"laps: {len(speeds)} rows got derived speeds; exactly 4 rows state 1.208 mi")

    pm = dict(M.POWER_UNIT_MODEL)
    hp_div = pm["watts_per_ps_metric"] if DEFECT == "hp-ps" else pm["watts_per_hp_sae"]
    ps_div = pm["watts_per_hp_sae"] if DEFECT == "hp-ps" else pm["watts_per_ps_metric"]
    watts = pm["kw"] * 1000.0
    hp_sae = watts / hp_div
    ps_metric = watts / ps_div
    lbft_f56 = pm["nm_f56"] / pm["nm_per_lbft"]
    lbft_f66 = pm["nm_f66"] / pm["nm_per_lbft"]
    if not (227.5 < hp_sae < 228.5 and 230.5 < ps_metric < 231.8 and ps_metric > hp_sae):
        fails.append(f"power: expected hp_SAE ~227.97 < PS_metric ~231.14 (got {hp_sae:.2f}, {ps_metric:.2f})")
    if abs(round(lbft_f56) - 236) > 0 or abs(round(lbft_f66) - 280) > 0:
        fails.append(f"torque: expected 320->236 lb-ft and 380->280 lb-ft (got {lbft_f56:.2f}, {lbft_f66:.2f})")

    for page in PAGES:
        if not page.is_file():
            fails.append(f"missing page {page.relative_to(ROOT).as_posix()}")
            continue
        html = page.read_text(encoding="utf-8")
        for mode, r in load_res.items():
            m = re.search(rf'<tr data-load-mode="{mode}">(.*?)</tr>', html, re.S)
            if not m:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: load row {mode} missing")
                continue
            nums = [int(x.replace(",", "")) for x in re.findall(r">([\d,]+) N<", m.group(1))]
            want = [round(r["dfz"]), round(r["fz_in"]), round(r["fz_out"]), round(r["fy_total"]), round(r["loss"])]
            if nums != want:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: load[{mode}] {nums} != {want}")
        for mode, r in brake_res.items():
            m = re.search(rf'<tr data-brake-mode="{mode}">(.*?)</tr>', html, re.S)
            if not m:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: brake row {mode} missing")
                continue
            m_kj = re.search(r">([\d.]+) kJ<", m.group(1))
            m_temps = re.findall(r">\+?([\d.]+) °C<", m.group(1))
            if not m_kj or len(m_temps) != 2:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: brake[{mode}] numbers missing")
                continue
            if abs(float(m_kj.group(1)) - round(r["e_disc_kj"], 1)) > 1e-6 or \
               abs(float(m_temps[0]) - round(r["dt_c"], 1)) > 1e-6 or \
               abs(float(m_temps[1]) - round(r["t_peak_c"], 1)) > 1e-6:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: brake[{mode}] mismatch")
        shown_kmh = dict(re.findall(r'data-lap-kmh="([^"]+)">([\d.]+) km/h<', html))
        shown_mph = dict(re.findall(r'data-lap-mph="([^"]+)">([\d.]+) mph<', html))
        if set(shown_kmh) != set(speeds) or set(shown_mph) != set(speeds):
            fails.append(f"{page.relative_to(ROOT).as_posix()}: lap rows {sorted(shown_kmh)} != {sorted(speeds)}")
        for rid, (kmh_v, mph_v) in speeds.items():
            if rid in shown_kmh and abs(float(shown_kmh[rid]) - round(kmh_v, 1)) > 1e-6:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: {rid} km/h mismatch")
            if rid in shown_mph and abs(float(shown_mph[rid]) - round(mph_v, 2)) > 1e-6:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: {rid} mph mismatch")
        m_hp = re.search(r'data-unit-hp="([^"]+)"', html)
        m_ps = re.search(r'data-unit-ps="([^"]+)"', html)
        m_t56 = re.search(r'data-unit-lbft-f56="([^"]+)"', html)
        m_t66 = re.search(r'data-unit-lbft-f66="([^"]+)"', html)
        if not (m_hp and m_ps and m_t56 and m_t66):
            fails.append(f"{page.relative_to(ROOT).as_posix()}: NA vs MX/EU unit cells missing")
        else:
            if abs(float(m_hp.group(1)) - round(hp_sae, 2)) > 1e-2 or abs(float(m_ps.group(1)) - round(ps_metric, 2)) > 1e-2:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: hp/PS mismatch ({m_hp.group(1)}, {m_ps.group(1)})")
            if abs(float(m_t56.group(1)) - round(lbft_f56, 1)) > 0.2 or abs(float(m_t66.group(1)) - round(lbft_f66, 1)) > 0.2:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: lb-ft mismatch ({m_t56.group(1)}, {m_t66.group(1)})")

    status = "FAIL" if fails else "PASS"
    print(json.dumps({
        "verifier": "cc03-mechanics",
        "status": status,
        "defect": DEFECT or None,
        "failures": fails,
        "loss_tall_n": round(load_res["tall"]["loss"]),
        "loss_f56_n": round(load_res["f56"]["loss"]),
        "loss_kart_n": round(load_res["kart"]["loss"]),
        "dt_small_c": round(brake_res["small"]["dt_c"], 1),
        "dt_brembo_c": round(brake_res["brembo"]["dt_c"], 1),
        "hp_sae": round(hp_sae, 2),
        "ps_metric": round(ps_metric, 2),
    }, ensure_ascii=False))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
