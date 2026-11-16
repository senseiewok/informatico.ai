---
name: classics-cc03-mini-jcw-mechanics
description: Rebuild and verify the CC.03 Mechanics Lab (MINI to F56 John Cooper Works Hot Chili on informatico.ai) - steady-state axle lateral load transfer and tire load sensitivity, adiabatic single-stop front brake rotor temperature rise, Brands Hatch Indy (1.208 miles) lap speeds, and US SAE vs. Mexico/EU metric power-unit conversion - using a standard-library Python verifier that checks the published English and Spanish pages and fails under five planted physics defects.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Wheels at the Corners · Mechanics Lab (CC.03)

> **Boundary (`EN`):** Education, not buying, tuning or track-driving advice. Any input that is not a sourced figure is a MODEL value, chosen to show the mechanism, and is not a measurement of any MINI. BMW/MINI statements are attributed to BMW Group and MINI USA; the peer-reviewed papers explain mechanics in general and did not test a Mini. Not affiliated with or endorsed by BMW AG, MINI or John Cooper Works.
>
> **Límite (`ES-MX`):** Educación, no consejo de compra, modificación ni manejo en pista. Toda entrada que no sea una cifra con fuente es un valor de MODELO, elegido para mostrar el mecanismo, y no es una medición de ningún MINI. Las declaraciones de BMW/MINI se atribuyen a BMW Group y MINI USA; los artículos revisados por pares explican mecánica general y no probaron un Mini. Sin afiliación ni respaldo de BMW AG, MINI ni John Cooper Works.

## 1. Page and files
- **Page**: https://informatico.ai/classics/mini-jcw/#part-5 (Spanish: https://informatico.ai/es-mx/classics/mini-jcw/#part-5)
- **Models**: `tools/folios/classics/cc03_mechanics.py` (used by the page builder)
- **Content and data**: `tools/folios/classics/cc03.py` (Brands Hatch Indy table, North American vs. EU/Mexico specs, sources, copy)
- **Builder**: `python tools/build_mini_jcw.py`
- **Verifier**: `python skills/classics/cc03/verify_cc03_mechanics.py`
- **Knockouts** (each must exit non-zero):
  - `--planted-defect` (`load-sign`): flips the tire load-sensitivity sign in `F_y(F_z)`
  - `--planted-defect=single-disc`: drops the two-front-rotor factor `/ 2` in brake energy split
  - `--planted-defect=config`: borrows `1.208 mi` onto MINI CHALLENGE rows where distance is blank
  - `--planted-defect=unit-kmh`: omits the `1 / 3.6` conversion from `km/h` to `m/s`
  - `--planted-defect=hp-ps`: swaps SAE mechanical hp (`745.7 W`) and DIN metric PS (`735.5 W`) conversion divisors

## 2. Equations
- **Axle lateral load transfer**: `ΔF_z = m_axle · g · a_y · h_cg / t_track`
- **Sub-linear peak tire force & grip loss**: `F_y(F_z) = F_z · (μ₀ − k · F_z)`, `ΔF_y,loss = 2 · k · (ΔF_z)²` (before inside-wheel lift and on the rising branch `F_z,out < μ₀ / (2k)`)
- **Single-stop adiabatic rotor temperature rise**: `E_disc = ½ · f_front · (½ · m_car · (v₁² − v₂²))`, `ΔT = E_disc / (m_disc · c_p)`
- **Brands Hatch Indy average speed**: `L = 1.208 mi × 1,609.344 m/mi = 1,944.087552 m`, `v̄ = L ÷ t_lap` (only where the source table states `1.208 mi`)
- **NA vs. MX/EU shaft power & torque equivalence**: `hp_SAE = (1,000 · kW) / 745.699872`, `PS_metric = (1,000 · kW) / 735.49875`, `lb-ft = N·m / 1.3558179483314004`

## 3. Sources
| What | Source |
| --- | --- |
| Front-to-total anti-roll moment & lateral load transfer control | Ricco et al. 2020, IEEE Trans. Veh. Technol. 69(2) · https://doi.org/10.1109/tvt.2019.2955902 |
| Disc brake transient thermal distribution & convective cooling | Adamowicz & Grzes 2011, Applied Thermal Engineering 31(14–15) · https://doi.org/10.1016/j.applthermaleng.2011.05.016 |
| Twin-scroll turbine exhaust-pulse modeling | Chiong et al. 2016, Energy 115 · https://doi.org/10.1016/j.energy.2016.09.041 |
| Brake-based torque vectoring | Kakalis et al. 2008, SAE Int. J. Passeng. Cars · https://doi.org/10.4271/2008-01-0596 |
| Downsized turbo & supercharged spark-ignition reviews | Hu et al. 2016 · https://doi.org/10.1177/1468087415599866 ; Hu et al. 2017 · https://doi.org/10.1177/0954407016636971 |
| Brands Hatch Indy `1.208 mi` lap records & MINI CHALLENGE UK times | Mini 7 Racing Club (`mini7.co.uk/lap-records`); MINI CHALLENGE Stats (`minichallengestats.co.uk`) |
| US SAE `228 hp` / `280 lb-ft` vs. metric `231 PS` / `380 Nm` & FMVSS 108 | MINI USA (`miniusa.com/model/john-cooper-works.html`); BMW Group (`newsroom.bmwgroup.com`); Wikipedia `Horsepower` & `FMVSS 108` |

## 4. Check it yourself
Change one MODEL input in `cc03_mechanics.py`, rebuild with `python tools/build_mini_jcw.py`, update `PINNED_SHA256` after reviewing the diff, and run `verify_cc03_mechanics.py` plus every `--planted-defect` variant.
