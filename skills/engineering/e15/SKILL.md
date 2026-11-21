---
name: bazant-size-effect
description: AI-agnostic civil structural fracture skill for Bazant Type II Size Effect Law, Hillerborg fictitious crack length l_ch, and Bazant-Kazemi extraction of fracture energy G_f and process-zone length c_f.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Quasi-Brittle Concrete Fracture, Bažant Size Effect Law & Hillerborg Process-Zone Scaling (Folio E.15)

A plain-text companion to the essay at https://informatico.ai/engineering/e15/ (`E.15 · Bažant Size Effect & Concrete Fracture · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`σ_N(D) = B f'_t / √(1 + D / D_0) · β_B = D / D_0 · G_f = (B f'_t)² D_0 g(α_0) / E' · c_f = D_0 g(α_0) / g'(α_0)`

## Rules the essay derives
1. Enforce strictly positive finite parameters D, D_0, B*f_t, E', f_t, g(alpha_0), and g'(alpha_0) inside geometrically similar notched Type II members (alpha_0 = a_0 / D > 0).
2. Compute nominal strength via Bazant Type II Size Effect Law sigma_N = B*f_t / sqrt(1 + D/D_0) with brittleness number beta_B = D / D_0 and log-log slope s = -beta_B / (2*(1 + beta_B)), avoiding scale-invariant plastic extrapolation.
3. Check unit identity (MPa^2 * mm / GPa = N/m) when evaluating initial Mode I fracture energy G_f = (B*f_t)^2 * D_0 * g(alpha_0) / E', effective FPZ length c_f = D_0 * g(alpha_0) / g'(alpha_0), and Hillerborg characteristic length l_ch = E' * G_f / f_t^2 (mm).
4. Frame Type II size-effect scaling as a Tier T1-T2 structural screening hypothesis that stops at unnotched Type I beams, stirrup-confined or fiber-reinforced shear members, and code design checks.

## How it works, in four stages
- Stage 1 (From Griffith LEFM to Hillerborg's Fictitious Crack Zone): Griffith (1921, DOI 10.1098/rsta.1921.0006) showed that a sharp crack in a brittle solid grows when stored elastic energy release matches surface energy, scaling nominal strength as D^(−1/2). Concrete is not ideally brittle: ahead of a visible notch, microcracking and aggregate bridging form a finite Fracture Process Zone (FPZ). Hillerborg, Modéer, and Petersson (1976, DOI 10.1016/0008-8846(76)90007-7) modeled this softening zone via tensile strength f'_t, initial fracture energy G_f, and characteristic length l_ch = E' G_f / (f'_t)^2 (424.5 mm at E' = 34.0 GPa, f'_t = 3.20 MPa, G_f = 127.84 N/m).
- Stage 2 (Bažant Type II Size Effect Law & Brittleness Number β_B): For geometrically similar notched members (notch ratio α_0 = a_0 / D > 0), Bažant (1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) matched plastic yield at small D against LEFM at large D via σ_N(D) = B f'_t / √(1 + β_B), with brittleness number β_B = D / D_0. Using illustrative calibration B f'_t = 4.20 MPa and D_0 = 220.0 mm, a 100 mm laboratory beam reaches σ_N = 3.482 MPa (82.9% of B f'_t, β_B = 0.455), while a 400 mm beam drops to 2.502 MPa (59.6%, β_B = 1.818) and log–log slope s = −β_B / [2(1 + β_B)] steepens from −0.156 to −0.323.
- Stage 3 (Bažant–Kazemi Regression for G_f and Process-Zone Length c_f): Bažant and Kazemi (1990, DOI 10.1007/BF00047063) inverted the size-effect curve into a linear relation Y = 1 / σ_N^2 = C D + A, where G_f = (B f'_t)^2 D_0 g(α_0) / E' and effective FPZ length c_f = D_0 g(α_0) / g'(α_0). With LEFM geometry factors g(α_0) = 1.12 and g'(α_0) = 3.80 at D_0 = 220.0 mm, the model yields G_f = 127.84 N/m and c_f = 64.84 mm. Doubling D_0 to 440.0 mm (a tougher aggregate mix at fixed B f'_t) raises G_f to 255.68 N/m, c_f to 129.68 mm, and 400 mm beam nominal strength to 3.040 MPa.
- Stage 4 (Open Hypothesis, Tier T1–T2, and Falsification Condition): Hypothesis (Tier T1–T2): in geometrically similar notched concrete beams without distributed shear reinforcement, nominal failure stress declines along σ_N = B f'_t (1 + D / D_0)^(−1/2) toward Griffith D^(−1/2) scaling as structural depth grows; at D = 2000 mm (D_0 = 220 mm, β_B = 9.091), modeled σ_N falls to 1.322 MPa (31.5%, slope −0.450), whereas ignoring (1 + D / D_0) overpredicts capacity by 3.177× at 4.20 MPa. This Type II hypothesis is falsified in unnotched Type I beams governed by Weibull boundary-layer strength (Bažant & Yu 2009, DOI 10.1061/(ASCE)0733-9399(2009)135:2(78)), in heavily stirrup-confined or steel-fiber members that arrest localization, or where aggregate size d_a is comparable to D.

## Reference values stated in the essay
- **Brittleness & Fracture Energy**: `β_B = 1.818 · G_f = 127.84 N/m (model)`
- **Nominal Strength & Retention**: `σ_N = 2.502 MPa (59.6% of B f'_t, model)`
- **Log–Log Slope & FPZ Length**: `s = −0.323 · c_f = 64.84 mm (model)`
- **Size-Effect Fracture Regime**: `QUASI-BRITTLE TRANSITION (0.15 < β_B <= 10, model)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/engineering/e15/verify_e15_bazant_size_effect.py
python skills/engineering/e15/verify_e15_bazant_size_effect.py --planted-defect
```

## Primary source
- https://doi.org/10.1061/(ASCE)0733-9399(1984)110:4(518) (Scite report: https://scite.ai/reports/10.1061/(ASCE)0733-9399(1984)110:4(518))
- What the essay compares against: Model values (notched beam D = 400.0 mm, D_0 = 220.0 mm): β_B = 1.818 · σ_N = 2.502 MPa (59.6% of B f'_t) · s = −0.323 · G_f = 127.84 N/m · c_f = 64.84 mm (drops to σ_N = 1.322 MPa at D = 2000 mm)

## Recent research context
- **Bažant Size Effect Law, Hillerborg Process Zones & Deep Concrete Girder Scaling**: Why do small notched concrete test beams sustain higher nominal stress than two-meter bridge girders of the same batch? Coupling Hillerborg's fictitious crack model (1976) with Bažant's Type II Size Effect Law (1984, DOI 10.1061/(ASCE)0733-9399(1984)110:4(518)) tracks the shift from 3.482 MPa at D = 100 mm to 1.322 MPa at D = 2,000 mm (D_0 = 220 mm, G_f = 127.84 N/m).
