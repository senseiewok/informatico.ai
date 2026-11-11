/-
  Informatico.ai · Track Time & Gravity · Step T.13 (Step 14 of 14)
  Pure Core Lean 4 Prelude Formalization: HolonomySoftAnomaly.lean
  Zero external imports (`0` `import`s) · Zero `sorry` / `admit` / `axiom` · Zero `HPow` (`^`).

  EPISTEMIC SCOPE BOUNDARY (IR / ALGEBRAIC CONSISTENCY vs. OPEN UV QUANTUM GRAVITY):
    What is machine-verified here:
      1. Exact SI dimensional homogeneity (`SIDim`, `Int^3` exponent lattice) of the universal
         gravitational coupling `κ² = 32πG/c⁴`, the Christodoulou / Strominger-Zhiboedov
         gravitational-wave memory strain step `Δh^mem = 2 G E_rad / (c⁴ D_L)`, and the proper
         interferometer / clock-baseline separation shift `ΔL = (1/2) L₀ Δh^mem`.
      2. Weinberg (1964, 1965) infrared soft Ward identities over exact integer-scaled kinematics:
         - Spin `s = 1` soft-photon gauge invariance forces total charge conservation `q₁ + q₂ = q₃ + q₄`.
         - Spin `s = 2` soft-graviton gauge invariance under `p₄ = p₁ + p₂ - p₃` factors identically
           as `(κ₂ - κ₁)(p₁ - p₃)` across all `(κ₁, κ₂, p₁, p₂, p₃ : Int)`, vanishing universally when
           `κ₁ = κ₂` (Weak Equivalence Principle `η = 0`) and forcing `κ₁ = κ₂` for every non-forward
           scattering witness (`p₁ ≠ p₃`).
         - Spin `s = 3` quadratic momentum-tensor Ward residual `Σ_a η_a g p_a²` is non-vanishing for
           conserved non-collinear kinematics unless `g = 0` (higher-spin long-range obstruction).
      3. Exact one-loop chiral and mixed gauge-gravitational anomaly cancellation (`Adler 1969`,
         `Delbourgo & Salam 1972`, `Tooby-Smith 2025` `PhysLean`) for one left-handed Weyl Standard
         Model generation with integer-scaled hypercharges `6Y`:
         `tr_grav_6y Nc = 0`, `tr_su3_6y = 0`, `tr_su2_6y Nc = Nc - 3`, and
         `tr_cubic_6y Nc = -54 * (Nc - 3)`, proving `tr_su2_6y Nc = 0 ↔ Nc = 3` and
         `tr_cubic_6y Nc = 0 ↔ Nc = 3`, plus planted-defect witnesses (`κ_e ≠ κ_p`, `Nc = 2`, and
         omitted `e_R^c`).

    What remains OPEN (NOT proved by infrared Ward identities or anomaly algebra):
      Infrared S-matrix consistency and one-loop anomaly cancellation constrain any low-energy
      effective field theory coupled to gravity, but they do NOT uniquely select or complete
      ultraviolet quantum gravity at the Planck scale `E ~ M_P c²`, nor do they decide tabletop
      superposition vs. objective-collapse dynamics (`73.14 µm` parallel Diósi-Penrose horizon in
      `T.05`/`ES.07`, sub-millimetre Eöt-Wash bounds, or multipartite gravitational entanglement).
-/

/-- Helper square over `Int` avoiding `HPow` (`^ 2`). -/
def sq (x : Int) : Int :=
  x * x

/-- Helper cube over `Int` avoiding `HPow` (`^ 3`). -/
def cube (x : Int) : Int :=
  x * (x * x)

/-- 1. Exact `Int^3` SI Dimensional Homogeneity Lattice `(Mass, Length, Time)`. -/
structure SIDim where
  m : Int
  l : Int
  t : Int
  deriving DecidableEq, Repr

namespace SIDim

def zero : SIDim := { m := 0, l := 0, t := 0 }

def add (a b : SIDim) : SIDim :=
  { m := a.m + b.m, l := a.l + b.l, t := a.t + b.t }

def sub (a b : SIDim) : SIDim :=
  { m := a.m - b.m, l := a.l - b.l, t := a.t - b.t }

def smul (k : Int) (a : SIDim) : SIDim :=
  { m := k * a.m, l := k * a.l, t := k * a.t }

def Mass     : SIDim := { m := 1,  l := 0,  t := 0 }
def Length   : SIDim := { m := 0,  l := 1,  t := 0 }
def Time     : SIDim := { m := 0,  l := 0,  t := 1 }
def Velocity : SIDim := { m := 0,  l := 1,  t := -1 }
def Energy   : SIDim := { m := 1,  l := 2,  t := -2 }
def Action   : SIDim := { m := 1,  l := 2,  t := -1 }
def GravG    : SIDim := { m := -1, l := 3,  t := -2 }
def KappaSq  : SIDim := sub GravG (smul 4 Velocity)

/-- Theorem 1 (`t13_si_homogeneity`):
    Kernel-verified (`rfl`) SI dimensional homogeneity of:
      (1) Universal squared Einstein coupling `[G / c⁴] = M⁻¹ L⁻¹ T²`;
      (2) Memory strain step `[2 G E_rad / (c⁴ D_L)] = zero` (dimensionless strain);
      (3) Proper baseline memory shift `[(1/2) L₀ Δh^mem] = Length`;
      (4) Squared Planck length `[ħ G / c³] = L²`. -/
theorem t13_si_homogeneity :
    KappaSq = { m := -1, l := -1, t := 2 } ∧
    sub (add GravG Energy) (add (smul 4 Velocity) Length) = zero ∧
    add Length (sub (add GravG Energy) (add (smul 4 Velocity) Length)) = Length ∧
    sub (add Action GravG) (smul 3 Velocity) = smul 2 Length := by
  refine ⟨rfl, rfl, rfl, rfl⟩

end SIDim

/-- 2. Weinberg (1964, 1965) Soft-Photon (`s = 1`), Soft-Graviton (`s = 2`), and Higher-Spin (`s = 3`)
    Longitudinal Gauge Ward Residuals on Conserved `2 → 2` Scattering (`p₄ = p₁ + p₂ - p₃`). -/
def softPhotonWard (q1 q2 q3 q4 : Int) : Int :=
  -q1 - q2 + q3 + q4

/-- Theorem 2 (`weinberg_soft_photon_charge_conservation`):
    Spin `s = 1` soft gauge invariance (`softPhotonWard = 0`) is equivalent to exact additive
    charge conservation `q1 + q2 = q3 + q4`. -/
theorem weinberg_soft_photon_charge_conservation :
    ∀ q1 q2 q3 q4 : Int, softPhotonWard q1 q2 q3 q4 = 0 ↔ q1 + q2 = q3 + q4 := by
  intro q1 q2 q3 q4
  unfold softPhotonWard
  omega

/-- Spin `s = 2` soft-graviton Ward residual for elastic `2 → 2` scattering of species 1 (coupling `k1`,
    incoming momentum `p1`, outgoing `p3`) and species 2 (coupling `k2`, incoming `p2`, outgoing
    `p4 = (p1 + p2) + (-p3)` by exact momentum conservation). -/
def softGravitonWard (k1 k2 p1 p2 p3 : Int) : Int :=
  -(k1 * p1) - (k2 * p2) + (k1 * p3) + k2 * ((p1 + p2) + (-p3))

/-- Theorem 3 (`weinberg_soft_graviton_ward_factorization`):
    Across all integers `(k1, k2, p1, p2, p3)`, the conserved `2 → 2` soft-graviton Ward residual
    factors identically into `(k2 - k1) * (p1 - p3)`. -/
theorem weinberg_soft_graviton_ward_factorization :
    ∀ k1 k2 p1 p2 p3 : Int,
      softGravitonWard k1 k2 p1 p2 p3 = (k2 + (-k1)) * (p1 + (-p3)) := by
  intro k1 k2 p1 p2 p3
  unfold softGravitonWard
  have hL : k2 * ((p1 + p2) + (-p3)) = (k2 * p1 + k2 * p2) + -(k2 * p3) := by
    rw [Int.mul_add k2 (p1 + p2) (-p3), Int.mul_add k2 p1 p2, Int.mul_neg k2 p3]
  have hR : (k2 + (-k1)) * (p1 + (-p3)) = (k2 * p1 + -(k2 * p3)) + -(k1 * p1 + -(k1 * p3)) := by
    rw [Int.add_mul k2 (-k1) (p1 + (-p3)),
        Int.mul_add k2 p1 (-p3), Int.mul_neg k2 p3,
        Int.neg_mul k1 (p1 + (-p3)), Int.mul_add k1 p1 (-p3), Int.mul_neg k1 p3]
  rw [hL, hR]
  omega

/-- Theorem 4 (`weinberg_universal_coupling_vanishes`):
    Universal gravitational coupling `k1 = k2 = k` (`η_WEP = 0`) satisfies the soft-graviton Ward
    identity identically for all momenta `(p1, p2, p3 : Int)`. -/
theorem weinberg_universal_coupling_vanishes :
    ∀ k p1 p2 p3 : Int, softGravitonWard k k p1 p2 p3 = 0 := by
  intro k p1 p2 p3
  rw [weinberg_soft_graviton_ward_factorization k k p1 p2 p3]
  have hz : k + (-k) = 0 := by omega
  rw [hz, Int.zero_mul]

/-- Linear-momentum-conserving witness `(p1, p2, p3, p4) = (5, 7, 2, 10)` with non-zero momentum
    transfer `p1 - p3 = 3 ≠ 0`. -/
def softGravitonWitness (k1 k2 : Int) : Int :=
  (-5) * k1 - 7 * k2 + 2 * k1 + 10 * k2

/-- Theorem 5 (`weinberg_wep_forced_on_nonforward_kinematics`):
    On conserved non-forward scattering kinematics `(5, 7) → (2, 10)`, `softGravitonWard k1 k2 5 7 2`
    equals `3 * (k2 - k1)` and vanishes if and only if `k1 = k2` (Weak Equivalence Principle). -/
theorem weinberg_wep_forced_on_nonforward_kinematics :
    (∀ k1 k2 : Int, softGravitonWard k1 k2 5 7 2 = 3 * (k2 - k1)) ∧
    (∀ k1 k2 : Int, softGravitonWard k1 k2 5 7 2 = 0 ↔ k1 = k2) := by
  constructor
  · intro k1 k2
    rw [weinberg_soft_graviton_ward_factorization k1 k2 5 7 2]
    have hp : (5 : Int) + (-(2 : Int)) = 3 := rfl
    rw [hp, Int.mul_comm (k2 + (-k1)) 3]
    omega
  · intro k1 k2
    rw [weinberg_soft_graviton_ward_factorization k1 k2 5 7 2]
    have hp : (5 : Int) + (-(2 : Int)) = 3 := rfl
    rw [hp, Int.mul_comm (k2 + (-k1)) 3]
    omega

/-- Spin `s = 3` quadratic momentum Ward residual on conserved kinematics `(5, 7) → (2, 10)`
    even when all external legs share a universal spin-3 coupling `g`. -/
def spin3UniversalWard (g : Int) : Int :=
  (-(sq 5)) * g + (-(sq 7)) * g + (sq 2) * g + (sq 10) * g

/-- Theorem 6 (`weinberg_spin3_obstruction`):
    For conserved kinematics `5 + 7 = 2 + 10`, the quadratic `s = 3` symmetric Ward residual equals
    `30 * g` and vanishes if and only if `g = 0` (forbidding macroscopic long-range `s ≥ 3` forces). -/
theorem weinberg_spin3_obstruction :
    (∀ g : Int, spin3UniversalWard g = 30 * g) ∧
    (∀ g : Int, spin3UniversalWard g = 0 ↔ g = 0) := by
  have hs5 : -(sq 5) = -25 := rfl
  have hs7 : -(sq 7) = -49 := rfl
  have hs2 : sq 2 = 4 := rfl
  have hs10 : sq 10 = 100 := rfl
  constructor
  · intro g
    unfold spin3UniversalWard
    rw [hs5, hs7, hs2, hs10]
    omega
  · intro g
    unfold spin3UniversalWard
    rw [hs5, hs7, hs2, hs10]
    omega

/-- 3. Standard Model Chiral & Mixed Gauge-Gravitational Anomaly Traces (`6Y` integer scaling).
    One left-handed Weyl generation parameterized by colour multiplicity `Nc`:
      `Q_L`:   `2 * Nc` components at `6Y = +1`
      `u_R^c`: `1 * Nc` components at `6Y = -4`
      `d_R^c`: `1 * Nc` components at `6Y = +2`
      `L_L`:   `2`      components at `6Y = -3`
      `e_R^c`: `1`      component  at `6Y = +6` -/
def tr_grav_6y (Nc : Int) : Int :=
  (2 * 1) * Nc + (-4) * Nc + 2 * Nc + 2 * (-3) + 1 * 6

def tr_su3_6y : Int :=
  2 * 1 + 1 * (-4) + 1 * 2

def tr_su2_6y (Nc : Int) : Int :=
  1 * Nc + 1 * (-3)

def tr_cubic_6y (Nc : Int) : Int :=
  (2 * cube 1) * Nc + (cube (-4)) * Nc + (cube 2) * Nc + 2 * cube (-3) + 1 * cube 6

/-- Theorem 7 (`tr_grav_6y_vanishes`):
    The Delbourgo-Salam mixed gravitational-hypercharge triangle `Tr[grav² · (6Y)]` vanishes
    identically when quark and lepton Weyl sectors both carry their Standard Model hypercharges. -/
theorem tr_grav_6y_vanishes :
    ∀ Nc : Int, tr_grav_6y Nc = 0 := by
  intro Nc
  unfold tr_grav_6y
  have hq1 : (2 : Int) * 1 = 2 := rfl
  have hl : (2 : Int) * (-3) + 1 * 6 = 0 := rfl
  rw [hq1]
  omega

/-- Theorem 8 (`tr_su3_6y_vanishes`):
    The `SU(3)_c² × U(1)_Y` chiral anomaly trace vanishes (`2(+1) + (-4) + (+2) = 0`). -/
theorem tr_su3_6y_vanishes :
    tr_su3_6y = 0 :=
  rfl

/-- Theorem 9 (`nc_forced_su2`):
    The `SU(2)_L² × U(1)_Y` chiral anomaly trace `tr_su2_6y Nc = Nc - 3` vanishes if and only if
    quark colour multiplicity is `Nc = 3`. -/
theorem nc_forced_su2 :
    ∀ Nc : Int, tr_su2_6y Nc = 0 ↔ Nc = 3 := by
  intro Nc
  unfold tr_su2_6y
  omega

/-- Theorem 10 (`nc_forced_cubic`):
    The cubic `U(1)_Y³` chiral anomaly trace reduces to `-54 * (Nc - 3)` and vanishes if and only
    if quark colour multiplicity is `Nc = 3`. -/
theorem nc_forced_cubic :
    (∀ Nc : Int, tr_cubic_6y Nc = -54 * (Nc - 3)) ∧
    (∀ Nc : Int, tr_cubic_6y Nc = 0 ↔ Nc = 3) := by
  have hc1 : 2 * cube 1 = 2 := rfl
  have hc2 : cube (-4) = -64 := rfl
  have hc3 : cube 2 = 8 := rfl
  have hc4 : 2 * cube (-3) = -54 := rfl
  have hc5 : 1 * cube 6 = 216 := rfl
  constructor
  · intro Nc
    unfold tr_cubic_6y
    rw [hc1, hc2, hc3, hc4, hc5]
    omega
  · intro Nc
    unfold tr_cubic_6y
    rw [hc1, hc2, hc3, hc4, hc5]
    omega

/-- Theorem 11 (`sm_gauge_gravity_anomaly_bridge`):
    Joint cancellation of all four gauge and mixed gravitational anomalies holds if and only if
    `Nc = 3`. -/
theorem sm_gauge_gravity_anomaly_bridge :
    ∀ Nc : Int,
      (tr_grav_6y Nc = 0 ∧ tr_su3_6y = 0 ∧ tr_su2_6y Nc = 0 ∧ tr_cubic_6y Nc = 0) ↔ Nc = 3 := by
  intro Nc
  rw [nc_forced_su2 Nc, (nc_forced_cubic).2 Nc]
  have hg : tr_grav_6y Nc = 0 := tr_grav_6y_vanishes Nc
  have hs3 : tr_su3_6y = 0 := tr_su3_6y_vanishes
  omega

/-- Theorem 12 (`planted_defect_knockout_witnesses`):
    Deterministic knockout witnesses matching `verify_t13_holonomy_soft.py --planted-defect`:
      (1) Perturbing species couplings (`k1 = 100001 ≠ k2 = 100000`, `1 + 10⁻⁵`) breaks the
          soft-graviton Ward identity (`softGravitonWard = -3 ≠ 0`);
      (2) Setting `Nc = 2 ≠ 3` breaks `SU(2)_L² U(1)_Y` (`-1 ≠ 0`) and `U(1)_Y³` (`54 ≠ 0`);
      (3) Omitting `e_R^c` breaks mixed gravitational-hypercharge cancellation (`-6 ≠ 0`). -/
theorem planted_defect_knockout_witnesses :
    softGravitonWard 100001 100000 5 7 2 = -3 ∧
    tr_su2_6y 2 = -1 ∧
    tr_cubic_6y 2 = 54 ∧
    (2 * 3 * 1 + 3 * (-4) + 3 * 2 + 2 * (-3) : Int) = -6 := by
  refine ⟨?_, rfl, rfl, rfl⟩
  rw [weinberg_soft_graviton_ward_factorization 100001 100000 5 7 2]
  rfl
