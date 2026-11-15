#!/usr/bin/env python3
"""Verify CC.01 · Mechanics Lab (Golf GTI feature): torque split, lap speeds and quarter-car frequencies.

Standard library only. The verifier reads the page's data (lap table, MODEL inputs) from the content modules, but
computes every result with its own code, then checks the rendered English and Spanish pages against it.

  python skills/classics/cc01/verify_cc01_mechanics.py                       -> exit 0 and PASS
  python skills/classics/cc01/verify_cc01_mechanics.py --planted-defect      -> exit 1 (clutch sends torque the wrong way)
  python skills/classics/cc01/verify_cc01_mechanics.py --planted-defect=open-factor | config | swap-k  -> exit 1

Checks:
  1. Data pin: the lap table and the MODEL inputs hash to the reviewed SHA-256 (a silent edit fails).
  2. Differential: open-axle cap computed two ways (2·min(T/2, grip_in) and the sum of equal halves); torque is
     conserved (road + brake + unused = demand); with equal grip the clutch transfers nothing; the clutch only moves
     torque from the faster (inside) wheel to the slower one; the 1,600 Nm limit binds in a case built to reach it;
     at full demand open < XDS+ < lock.
  3. Laps: speeds recomputed from the time string and from the seconds separately; only rows with a stated
     20,600 m length get a speed.
  4. Quarter car: roots of the characteristic equation found by bisection (not the closed form); wheel hop above body
     bounce; wheel hop falls as unsprung mass rises while body bounce barely moves.
  5. Pages: every torque, km/h and Hz figure printed in the EN and ES lab matches the recomputation.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.classics import cc01 as C  # noqa: E402  (data only)
from folios.classics import cc01_mechanics as M  # noqa: E402  (MODEL inputs only; formulas are re-derived here)

PINNED_SHA256 = "9f1bf87dfd68a9208fb89aae8ca46f3a0dd11fd11ef09c1926751ae06aa58e5b"
PAGES = (ROOT / "src" / "classics" / "golf-gti" / "index.html", ROOT / "src" / "es-mx" / "classics" / "golf-gti" / "index.html")

arg = next((a for a in sys.argv[1:] if a.startswith("--planted-defect")), "")
DEFECT = (arg.split("=", 1)[1] if "=" in arg else "lsd-direction") if arg else ""


def canonical() -> bytes:
    data = {"laps": [list(r) for r in C.LAPS], "diff": M.DIFF_MODEL, "quarter": M.QUARTER_MODEL,
            "config_m": M.CONFIG_LENGTH_M}
    return json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")


# ------------------------------------------------------------------------------------------- independent models ----
def grip(load: float, p: dict) -> float:
    return p["mu"] * load * p["radius_m"]


def split(demand: float, mode: str, p: dict) -> dict:
    g_in, g_out = grip(p["load_in_n"], p), grip(p["load_out_n"], p)
    if mode == "open":
        each = demand / 2 if demand / 2 <= g_in else g_in
        factor = 1 if DEFECT == "open-factor" else 2
        total_a = factor * min(demand / 2, g_in)
        return {"in": each, "out": each, "brake": 0.0, "road": total_a, "road_b": each + each}
    if mode == "xds":
        side = min(demand / 2, g_in + p["brake_max_nm"], g_out)
        brake = side - g_in if side > g_in else 0.0
        return {"in": side - brake, "out": side, "brake": brake, "road": 2 * side - brake}
    # clutch pack: torque flows from the faster wheel (the one that would spin: lower grip) to the slower one
    t_in = min(demand / 2, g_in)
    room = g_out - t_in
    excess = demand - 2 * t_in
    moved = max(0.0, min(excess, p["lock_max_nm"], room))
    if DEFECT == "lsd-direction":
        moved = -moved
    return {"in": t_in, "out": t_in + moved, "brake": 0.0, "road": 2 * t_in + moved, "moved": moved}


def kmh(time_str: str) -> float:
    mins, secs = time_str.split(":")
    return M.CONFIG_LENGTH_M / (int(mins) * 60 + float(secs)) * 3.6


def qc_roots(m_u: float, q: dict) -> tuple[float, float]:
    """Natural frequencies by bisection on det(K - w^2 M) for the two-mass model (independent of the closed form)."""
    m_s, k_s, k_t = q["m_s"], q["k_s"], q["k_t"]
    if DEFECT == "swap-k":
        k_s, k_t = k_t, k_s

    def det(lam: float) -> float:
        return (k_s - m_s * lam) * (k_s + k_t - m_u * lam) - k_s * k_s

    def root(lo: float, hi: float) -> float:
        for _ in range(200):
            mid = (lo + hi) / 2
            if (det(lo) > 0) == (det(mid) > 0):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    split_at = k_s / m_s  # det changes sign once below and once above the body-only frequency
    lam_lo = root(1e-9, split_at)
    lam_hi = root(split_at, 1e7)
    return math.sqrt(lam_lo) / (2 * math.pi), math.sqrt(lam_hi) / (2 * math.pi)


# ------------------------------------------------------------------------------------------------------ checks ----
def main() -> int:
    fails: list[str] = []
    digest = hashlib.sha256(canonical()).hexdigest()
    if digest != PINNED_SHA256:
        fails.append(f"data pin: {digest} != reviewed {PINNED_SHA256}")

    p = dict(M.DIFF_MODEL)
    demand = p["demand_max_nm"]
    res = {m: split(demand, m, p) for m in ("open", "xds", "lock")}
    if abs(res["open"]["road"] - res["open"]["road_b"]) > 1e-9:
        fails.append("open differential: 2·min(T/2, grip_in) disagrees with the sum of equal halves")
    for m, r in res.items():
        unused = demand - r["road"] - r["brake"]
        if unused < -1e-9:
            fails.append(f"{m}: more torque at the road than demanded")
    if not (res["open"]["road"] < res["xds"]["road"] < res["lock"]["road"]):
        fails.append("full demand: expected open < XDS+ < lock")
    if res["lock"]["out"] < res["lock"]["in"]:
        fails.append("clutch pack moved torque toward the faster (spinning) wheel")
    equal = dict(p, load_out_n=p["load_in_n"])
    if abs(split(demand, "lock", equal).get("moved", 0.0)) > 1e-9:
        fails.append("equal grip: the clutch pack should transfer nothing")
    bind = dict(p, load_out_n=20000.0, demand_max_nm=6000.0)
    if abs(split(6000.0, "lock", bind)["moved"] - p["lock_max_nm"]) > 1e-9:
        fails.append("lock limit: 1,600 Nm did not bind in the case built to reach it")

    speeds = {}
    for gen, car, year, ps, ts, secs, driver, tyres, cfg in C.LAPS:
        from_str = kmh(ts)
        from_secs = M.CONFIG_LENGTH_M / secs * 3.6
        if abs(from_str - from_secs) > 1e-6:
            fails.append(f"{car}: time string and seconds disagree")
        if cfg or DEFECT == "config":
            speeds[secs] = from_secs
    if len(speeds) != 4:
        fails.append(f"lap speeds: {len(speeds)} rows got a speed; only the 4 rows with a stated length may")

    q = M.QUARTER_MODEL
    fb0, fh0 = qc_roots(q["m_u_min"], q)
    fb1, fh1 = qc_roots(q["m_u_max"], q)
    if not (fh0 > fb0 and fh1 > fb1):
        fails.append("quarter car: wheel hop must sit above body bounce")
    if not fh1 < fh0:
        fails.append("quarter car: wheel hop must fall as unsprung mass rises")
    if abs(fb1 - fb0) > 0.05 * fb0:
        fails.append("quarter car: body bounce should barely move with unsprung mass")

    fb_start, fh_start = qc_roots(q["m_u_start"], q)
    for page in PAGES:
        if not page.is_file():
            fails.append(f"missing page {page.relative_to(ROOT).as_posix()}")
            continue
        html = page.read_text(encoding="utf-8")
        for mode, r in res.items():
            m = re.search(rf'<tr data-mode="{mode}">(.*?)</tr>', html, re.S)
            if not m:
                fails.append(f"{page.parent.parent.parent.name}: lab row {mode} missing")
                continue
            nums = [int(x.replace(",", "")) for x in re.findall(r">([\d,]+) Nm<", m.group(1))]
            want = [round(r["in"]), round(r["out"]), round(r["brake"]), round(r["road"])]
            if nums != want:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: {mode} row shows {nums}, recomputed {want}")
        shown = {float(s): float(v) for s, v in re.findall(r'data-lap-kmh="([\d.]+)">([\d.]+) km/h<', html)}
        if set(shown) != set(speeds):
            fails.append(f"{page.relative_to(ROOT).as_posix()}: km/h rows {sorted(shown)} != {sorted(speeds)}")
        for secs, v in shown.items():
            if secs in speeds and abs(v - round(speeds[secs], 1)) > 1e-9:
                fails.append(f"{page.relative_to(ROOT).as_posix()}: {v} km/h for {secs} s, recomputed {speeds[secs]:.1f}")
        mb = re.search(r'class="cc-qc-body-hz">([\d.]+) Hz<', html)
        mh = re.search(r'class="cc-qc-hop-hz">([\d.]+) Hz<', html)
        if not (mb and mh) or abs(float(mb.group(1)) - round(fb_start, 2)) > 1e-9 or abs(float(mh.group(1)) - round(fh_start, 1)) > 1e-9:
            fails.append(f"{page.relative_to(ROOT).as_posix()}: quarter-car readout does not match {fb_start:.2f} / {fh_start:.1f} Hz")

    status = "FAIL" if fails else "PASS"
    print(json.dumps({"verifier": "cc01-mechanics", "status": status, "defect": DEFECT or None, "failures": fails,
                      "open_nm": round(res["open"]["road"]), "xds_nm": round(res["xds"]["road"]),
                      "lock_nm": round(res["lock"]["road"]), "wheel_hop_hz": round(fh_start, 2),
                      "body_bounce_hz": round(fb_start, 2)}, ensure_ascii=False))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
