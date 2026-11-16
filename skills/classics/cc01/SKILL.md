---
name: classics-cc01-golf-gti-mechanics
description: Rebuild and verify the CC.01 Mechanics Lab (Golf GTI feature on informatico.ai) - front-axle torque split for an open differential, a brake-based XDS+ and a clutch-pack lock, lap times as average speeds where the track length is stated, and the quarter-car body-bounce and wheel-hop frequencies - using a standard-library Python verifier that checks the published English and Spanish pages and fails under planted defects.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# One Brief, Eight Answers · Mechanics Lab (CC.01)

> **Boundary (`EN`):** Education, not buying, tuning or driving advice. Any input that is not a sourced figure is a MODEL value, chosen to show the mechanism, and is not a measurement of any Golf. Volkswagen statements are attributed to Volkswagen; the papers explain mechanisms in general and did not test these cars. Not affiliated with or endorsed by Volkswagen AG.
>
> **Límite (`ES-MX`):** Educación, no consejo de compra, de modificación ni de manejo. Toda entrada que no sea una cifra con fuente es un valor de MODELO, elegido para mostrar el mecanismo, y no es una medición de ningún Golf. Las declaraciones de Volkswagen se atribuyen a Volkswagen; los artículos explican mecanismos en general y no probaron estos autos. Sin afiliación ni respaldo de Volkswagen AG.

## 1. Page and files
- **Page**: https://informatico.ai/classics/golf-gti/#part-6 (Spanish: https://informatico.ai/es-mx/classics/golf-gti/#part-6)
- **Models**: `tools/folios/classics/cc01_mechanics.py` (diff split, lap average speed, quarter-car eigenfrequencies, plus Model 4 `corner_load_and_yaw` & Model 5 `dct_shift_kinematics` used by the page builder)
- **Content and data**: `tools/folios/classics/cc01.py` (lap table, sources, copy)
- **Builder**: `python tools/build_cult_classics.py`
- **Verifier**: `python skills/classics/cc01/verify_cc01_mechanics.py`
- **Knockouts** (each must exit non-zero):
  - `--planted-defect`: the clutch pack sends torque to the faster wheel
  - `--planted-defect=open-factor`: the open-axle cap loses its factor of 2
  - `--planted-defect=config`: older lap rows borrow a track length the source does not state
  - `--planted-defect=swap-k`: suspension and tyre rates are swapped

## 2. Equations
- **Grip limit of one wheel**: `T_grip = μ · N · r`
- **Open differential** (each wheel gets half the axle torque): `T_road = 2 · min(T/2, T_grip,in)`
- **Brake on the inside wheel** (XDS+): side torque `S = min(T/2, T_grip,in + T_brake, T_grip,out)`, brake `= max(0, S − T_grip,in)`
- **Clutch-pack lock** (torque only from the faster wheel to the slower): `T_out = T_in + min(T − 2·T_in, 1,600 Nm, T_grip,out − T_in)`
- **Average lap speed**: `v̄ = 20,600 m ÷ t_lap`, only for rows where the source states that length
- **Quarter car**: `m_s·m_u·ω⁴ − (m_s(k_s + k_t) + m_u·k_s)·ω² + k_s·k_t = 0`, `f = ω / 2π`
- **Corner load transfer & direct yaw moment (Model 4)**: `ΔF_z = a_y · (ΔF_z,ref / a_y,ref)`, `M_z = ((T_out − T_in) / r_w) · (b_f / 2)`
- **Coaxial DCT upshift handover (Model 5)**: `Δω = Δrpm · (2π / 60)`, `E_slip = 0.5 · T_in · |Δω| · t_overlap`

## 3. Sources
| What | Source |
| --- | --- |
| Open differential gives each wheel half the torque | Scamarcio et al. 2023, IEEE Trans. Veh. Technol. 72(6) · https://doi.org/10.1109/tvt.2022.3143497 |
| Clutch-type differential moves torque only from the faster to the slower wheel; brakes can create a yaw moment with a free differential | Kakalis et al. 2008, SAE · https://doi.org/10.4271/2008-01-0596 |
| 1,600 Nm locking torque, multi-plate construction (Mk7 GTI Performance) | Volkswagen Newsroom, 2013 running-gear page |
| sport auto Nordschleife times and the 20,600 m configuration | Wikipedia, List of Nürburgring Nordschleife lap times (rows citing sport auto) |
| Quarter car: bounce and wheel-hop modes; unsprung mass mainly moves wheel hop | Micromachines 17(10) 1111, 2026 · https://doi.org/10.3390/mi17101111 |
| Less wheel hop, better road holding | Ahmadian & Pare 2000 · https://doi.org/10.1106/mr3w-5d8w-0lpl-wguq ; Woo & Shin 2021 · https://doi.org/10.3390/app11198912 |

## 4. How to use this with any AI
Ask it to change one MODEL input in `cc01_mechanics.py`, rebuild the page, update the data pin in the verifier after review, and run the verifier and every knockout. A change that passes without a new pin was not reviewed.
