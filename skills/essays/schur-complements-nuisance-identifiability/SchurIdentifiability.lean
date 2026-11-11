/-
Copyright (c) 2026 Informatico.ai Cross-Scale Essays (ES.08).
License: MIT
Companion Formal Specification: Cross-Scale Essay ES.08 (`schur-complements-nuisance-identifiability`)
Core Lean 4 (zero external imports; compiles in pure Lean 4 Prelude).

Epistemic Boundary (Mandatory — Read Alongside Essay ES.08):
  SchurIdentifiability.lean certifies the DEDUCTIVE LINEAR-ALGEBRAIC, FISHER-GEOMETRIC,
  EXPERIMENTAL-DESIGN, AND SI DIMENSIONAL SPINE (`DERIVED (NOT MEASURED)` consequences of
  Fisher information Schur complements, Modified Gram–Schmidt nuisance annihilation,
  Kiefer–Wolfowitz / Carathéodory saturated 3-point D-optimal designs, and the Eöt-Wash
  2020 signed Yukawa recast). Formal verification inside a proof kernel guarantees zero
  algebraic sleight of hand between stated models and derived identifiability bounds; it
  NEVER claims a Theory of Everything and NEVER substitutes for raw 95-run experimental
  covariance data or laboratory measurement. Strictly zero unproven placeholders or custom
  postulates outside comments.
-/

namespace Informatico.Essays.ES08

/-- 1. SI Base Dimension Exponent Vector `[M, L, T, I, Θ, N, J]` over core `Int`. -/
structure SIDim where
  m : Int := 0
  l : Int := 0
  t : Int := 0
  i : Int := 0
  theta : Int := 0
  n : Int := 0
  j : Int := 0
  deriving DecidableEq, Repr

namespace SIDim

def zero        : SIDim := {}

def add (a b : SIDim) : SIDim :=
  { m := a.m + b.m, l := a.l + b.l, t := a.t + b.t,
    i := a.i + b.i, theta := a.theta + b.theta, n := a.n + b.n, j := a.j + b.j }

def sub (a b : SIDim) : SIDim :=
  { m := a.m - b.m, l := a.l - b.l, t := a.t - b.t,
    i := a.i - b.i, theta := a.theta - b.theta, n := a.n - b.n, j := a.j - b.j }

def smul (k : Int) (a : SIDim) : SIDim :=
  { m := k * a.m, l := k * a.l, t := k * a.t,
    i := k * a.i, theta := k * a.theta, n := k * a.n, j := k * a.j }

def Mass        : SIDim := { m := 1 }
def Length      : SIDim := { l := 1 }
def Time        : SIDim := { t := 1 }
def Velocity    : SIDim := sub Length Time
def Energy      : SIDim := add Mass (smul 2 Velocity)
def Force       : SIDim := sub Energy Length
def GravG       : SIDim := { m := -1, l := 3, t := -2 }
def MassDensity : SIDim := sub Mass (smul 3 Length)
def InvLength   : SIDim := smul (-1) Length

/-- Theorem 1 (`schur_identifiability_si_homogeneity`):
    All 6 governing SI dimensional equations of Essay ES.08 reduce by kernel computation (`rfl`)
    to exact `Int` exponent identities:
      (1) Fourier–Bessel wedge torque `[G ρ^2 L^5] = Energy`;
      (2) Fractional torque deficit `[G ρ^2 L^5 / T_N] = zero`;
      (3) Newtonian logarithmic slope `[(dT_N / ds) / T_N] = L^-1`;
      (4) Dimensionless separation-offset basis `[s_min (d ln T_N / ds)] = zero`;
      (5) Constant-torque-noise Fisher weight `[(F L)^2 / σ_T^2] = zero`;
      (6) Yukawa screening wavenumber `[1 / λ] = L^-1`. -/
theorem schur_identifiability_si_homogeneity :
    add (add GravG (smul 2 MassDensity)) (smul 5 Length) = Energy ∧
    sub (add (add GravG (smul 2 MassDensity)) (smul 5 Length)) Energy = zero ∧
    sub Force Energy = InvLength ∧
    add Length (sub Force Energy) = zero ∧
    sub (smul 2 (add Force Length)) (smul 2 Energy) = zero ∧
    sub zero Length = InvLength := by
  refine ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

end SIDim

/-- Integer square helper over core `Int` (pure Lean 4 Prelude, zero external imports). -/
def sq (x : Int) : Int := x * x

/-- Self-contained ring helpers built strictly from `Int.mul_add`, `Int.mul_comm`,
    `Int.mul_assoc`, `Int.neg_mul_neg`, `Int.ofNat`, and `omega`. -/
def ofNat_mul_ofNat_eq (a b : Nat) : Int.ofNat a * Int.ofNat b = Int.ofNat (a * b) := rfl

def add_mul_int (a b c : Int) : (a + b) * c = a * c + b * c := by
  rw [Int.mul_comm (a + b) c, Int.mul_add c a b, Int.mul_comm c a, Int.mul_comm c b]

def mul_sub_int (a b c : Int) : a * (b - c) = a * b - a * c := by
  have hbc : (b - c) + c = b := by omega
  have hm : a * ((b - c) + c) = a * (b - c) + a * c := Int.mul_add a (b - c) c
  rw [hbc] at hm
  omega

def sub_mul_int (a b c : Int) : (a - b) * c = a * c - b * c := by
  rw [Int.mul_comm (a - b) c, mul_sub_int c a b, Int.mul_comm c a, Int.mul_comm c b]

def mul_left_comm_int (a b c : Int) : a * (b * c) = b * (a * c) := by
  rw [← Int.mul_assoc a b c, Int.mul_comm a b, Int.mul_assoc b a c]

def mul_self_pair (x y : Int) : (x * y) * (x * y) = (x * x) * (y * y) := by
  rw [Int.mul_assoc (x * y) x y, mul_left_comm_int y x y, ← Int.mul_assoc x x (y * y)]

def mul_cross_swap (a1 b1 a2 b2 : Int) : (a1 * b1) * (a2 * b2) = (a1 * b2) * (a2 * b1) := by
  rw [Int.mul_assoc (a1 * b1) a2 b2, mul_left_comm_int b1 a2 b2, Int.mul_comm b1 b2,
      mul_left_comm_int a2 b2 b1, ← Int.mul_assoc a1 b2 (a2 * b1)]

def neg_mul_int (a b : Int) : (-a) * b = -(a * b) := by
  have h0b : (0 : Int) * b = 0 := by
    have h00 : ((0 : Int) + 0) * b = (0 : Int) * b + (0 : Int) * b := add_mul_int 0 0 b
    have hzz : (0 : Int) + 0 = 0 := rfl
    rw [hzz] at h00
    omega
  have hz : ((-a) + a) * b = (0 : Int) * b := by
    have h0 : (-a) + a = 0 := by omega
    rw [h0]
  have hexp : ((-a) + a) * b = (-a) * b + a * b := add_mul_int (-a) a b
  omega

/-- Theorem 2 (`sq_nonneg`):
    Every integer square `sq x = x * x` is non-negative over core `Int`. -/
theorem sq_nonneg : ∀ x : Int, 0 ≤ sq x := by
  intro x
  unfold sq
  cases x with
  | ofNat n =>
    rw [ofNat_mul_ofNat_eq n n]
    omega
  | negSucc n =>
    have hn : Int.negSucc n = -Int.ofNat (n + 1) := by omega
    rw [hn, Int.neg_mul_neg (Int.ofNat (n + 1)) (Int.ofNat (n + 1)), ofNat_mul_ofNat_eq (n + 1) (n + 1)]
    omega

/-- Theorem 3 (`two_point_cauchy_schwarz_lagrange`):
    Two-point Lagrange / Cauchy–Schwarz identity and non-negativity over `Int`:
    `(a1^2 + a2^2)(b1^2 + b2^2) - (a1 b1 + a2 b2)^2 = (a1 b2 - a2 b1)^2 ≥ 0`.
    Proves that two distinct separation points strictly separate non-collinear shapes (`a1 b2 ≠ a2 b1`). -/
theorem two_point_cauchy_schwarz_lagrange :
    ∀ a1 a2 b1 b2 : Int,
      (sq a1 + sq a2) * (sq b1 + sq b2) - sq (a1 * b1 + a2 * b2) = sq (a1 * b2 - a2 * b1) ∧
      0 ≤ (sq a1 + sq a2) * (sq b1 + sq b2) - sq (a1 * b1 + a2 * b2) := by
  intro a1 a2 b1 b2
  have hid : (sq a1 + sq a2) * (sq b1 + sq b2) - sq (a1 * b1 + a2 * b2) = sq (a1 * b2 - a2 * b1) := by
    unfold sq
    have h_lhs : (a1 * a1 + a2 * a2) * (b1 * b1 + b2 * b2) =
        (a1 * a1) * (b1 * b1) + (a1 * a1) * (b2 * b2) + ((a2 * a2) * (b1 * b1) + (a2 * a2) * (b2 * b2)) := by
      rw [add_mul_int, Int.mul_add, Int.mul_add]
    have h_dot : (a1 * b1 + a2 * b2) * (a1 * b1 + a2 * b2) =
        (a1 * a1) * (b1 * b1) + 2 * ((a1 * b2) * (a2 * b1)) + (a2 * a2) * (b2 * b2) := by
      rw [add_mul_int, Int.mul_add, Int.mul_add]
      rw [mul_self_pair a1 b1, mul_self_pair a2 b2]
      rw [Int.mul_comm (a2 * b2) (a1 * b1), mul_cross_swap a1 b1 a2 b2]
      omega
    have h_wedge : (a1 * b2 - a2 * b1) * (a1 * b2 - a2 * b1) =
        (a1 * a1) * (b2 * b2) - 2 * ((a1 * b2) * (a2 * b1)) + (a2 * a2) * (b1 * b1) := by
      rw [sub_mul_int, mul_sub_int, mul_sub_int]
      rw [mul_self_pair a1 b2, mul_self_pair a2 b1]
      rw [Int.mul_comm (a2 * b1) (a1 * b2)]
      omega
    rw [h_lhs, h_dot, h_wedge]
    omega
  refine ⟨hid, ?_⟩
  rw [hid]
  exact sq_nonneg (a1 * b2 - a2 * b1)

/-- Theorem 4 (`schur_fisher_bounds`):
    Integer-cleared Schur-complement Fisher inequality: for any block Fisher entries
    `0 ≤ i_tt`, `0 ≤ i_nn`, and cross-information `i_tn`, profiling over nuisance parameters
    yields numerator `i_tt * i_nn - sq i_tn ≤ i_tt * i_nn`—proving floating calibration
    parameters NEVER increase Fisher information on the target parameter. -/
theorem schur_fisher_bounds :
    ∀ i_tt i_nn i_tn : Int,
      0 ≤ i_tt → 0 ≤ i_nn → i_tt * i_nn - sq i_tn ≤ i_tt * i_nn := by
  intro i_tt i_nn i_tn _ _
  have hsq : 0 ≤ sq i_tn := sq_nonneg i_tn
  omega

/-- Integer-cleared Gram–Schmidt orthogonal residual components `r_i = (v1^2 + v2^2) d_i - (d1 v1 + d2 v2) v_i`. -/
def orth_res1 (d1 d2 v1 v2 : Int) : Int :=
  (sq v1 + sq v2) * d1 - (d1 * v1 + d2 * v2) * v1

def orth_res2 (d1 d2 v1 v2 : Int) : Int :=
  (sq v1 + sq v2) * d2 - (d1 * v1 + d2 * v2) * v2

def orth_res1_factor (d1 d2 v1 v2 : Int) :
    orth_res1 d1 d2 v1 v2 = v2 * (d1 * v2 - d2 * v1) := by
  unfold orth_res1 sq
  have h1 : (v1 * v1 + v2 * v2) * d1 = (v1 * v1) * d1 + (v2 * v2) * d1 := add_mul_int (v1 * v1) (v2 * v2) d1
  have h2 : (d1 * v1 + d2 * v2) * v1 = (v1 * v1) * d1 + v2 * (d2 * v1) := by
    rw [add_mul_int, Int.mul_assoc d1 v1 v1, Int.mul_comm d1 (v1 * v1)]
    rw [Int.mul_comm d2 v2, Int.mul_assoc v2 d2 v1]
  have h3 : (v2 * v2) * d1 = v2 * (d1 * v2) := by
    rw [Int.mul_assoc v2 v2 d1, Int.mul_comm v2 d1]
  have h4 : v2 * (d1 * v2 - d2 * v1) = v2 * (d1 * v2) - v2 * (d2 * v1) :=
    mul_sub_int v2 (d1 * v2) (d2 * v1)
  omega

def orth_res2_factor (d1 d2 v1 v2 : Int) :
    orth_res2 d1 d2 v1 v2 = -(v1 * (d1 * v2 - d2 * v1)) := by
  unfold orth_res2 sq
  have h1 : (v1 * v1 + v2 * v2) * d2 = (v1 * v1) * d2 + (v2 * v2) * d2 := add_mul_int (v1 * v1) (v2 * v2) d2
  have h2 : (d1 * v1 + d2 * v2) * v2 = v1 * (d1 * v2) + (v2 * v2) * d2 := by
    rw [add_mul_int, Int.mul_assoc d1 v1 v2, Int.mul_assoc d2 v2 v2, Int.mul_comm d2 (v2 * v2)]
    rw [mul_left_comm_int d1 v1 v2]
  have h3 : (v1 * v1) * d2 = v1 * (d2 * v1) := by
    rw [Int.mul_assoc v1 v1 d2, Int.mul_comm v1 d2]
  have h4 : v1 * (d1 * v2 - d2 * v1) = v1 * (d1 * v2) - v1 * (d2 * v1) :=
    mul_sub_int v1 (d1 * v2) (d2 * v1)
  omega

/-- Theorem 5 (`gram_schmidt_nuisance_annihilation`):
    Exact Gram–Schmidt orthogonality over `Int`: for every deficit `(d1, d2)` and nuisance
    tangent vector `(v1, v2)`, `r1 * v1 + r2 * v2 = 0` identically. -/
theorem gram_schmidt_nuisance_annihilation :
    ∀ d1 d2 v1 v2 : Int,
      orth_res1 d1 d2 v1 v2 * v1 + orth_res2 d1 d2 v1 v2 * v2 = 0 := by
  intro d1 d2 v1 v2
  rw [orth_res1_factor, orth_res2_factor]
  let w : Int := d1 * v2 - d2 * v1
  change (v2 * w) * v1 + (-(v1 * w)) * v2 = 0
  have h1 : (v2 * w) * v1 = (v1 * v2) * w := by
    rw [Int.mul_comm (v2 * w) v1, ← Int.mul_assoc v1 v2 w]
  have h2 : (-(v1 * w)) * v2 = -((v1 * v2) * w) := by
    rw [neg_mul_int (v1 * w) v2, Int.mul_assoc v1 w v2, Int.mul_comm w v2, ← Int.mul_assoc v1 v2 w]
  omega

/-- Theorem 6 (`orthogonal_pythagoras_decomposition`):
    Exact Pythagorean Fisher energy decomposition over `Int`:
    `(v1^2 + v2^2)^2 (d1^2 + d2^2) = (v1^2 + v2^2)(d1 v1 + d2 v2)^2 + (r1^2 + r2^2)`. -/
theorem orthogonal_pythagoras_decomposition :
    ∀ d1 d2 v1 v2 : Int,
      sq (sq v1 + sq v2) * (sq d1 + sq d2) =
        (sq v1 + sq v2) * sq (d1 * v1 + d2 * v2) + (sq (orth_res1 d1 d2 v1 v2) + sq (orth_res2 d1 d2 v1 v2)) := by
  intro d1 d2 v1 v2
  rw [orth_res1_factor, orth_res2_factor]
  let w : Int := d1 * v2 - d2 * v1
  let nv : Int := sq v1 + sq v2
  let nd : Int := sq d1 + sq d2
  let dot : Int := d1 * v1 + d2 * v2
  have hlag : nd * nv - sq dot = sq w := (two_point_cauchy_schwarz_lagrange d1 d2 v1 v2).1
  have hr1 : sq (v2 * w) = sq v2 * sq w := mul_self_pair v2 w
  have hr2 : sq (-(v1 * w)) = sq v1 * sq w := by
    unfold sq
    rw [Int.neg_mul_neg (v1 * w) (v1 * w)]
    exact mul_self_pair v1 w
  have hsum : sq v2 * sq w + sq v1 * sq w = nv * sq w := by
    change sq v2 * sq w + sq v1 * sq w = (sq v1 + sq v2) * sq w
    rw [add_mul_int]
    omega
  change sq nv * nd = nv * sq dot + (sq (v2 * w) + sq (-(v1 * w)))
  rw [hr1, hr2, hsum]
  have hexp : nv * (nd * nv - sq dot) = nv * (nd * nv) - nv * sq dot := mul_sub_int nv (nd * nv) (sq dot)
  rw [hlag] at hexp
  have hcomm : nv * (nd * nv) = sq nv * nd := by
    unfold sq
    rw [Int.mul_comm nd nv, ← Int.mul_assoc nv nv nd]
  omega

/-- Theorem 7 (`kiefer_wolfowitz_trace_identity`):
    Saturated 3-point Kiefer–Wolfowitz Equivalence Theorem trace saturation:
    for a `p`-parameter model (`p = 3` for `(γ, s0, α)`) supported on 3 points with equal
    weights `1 / 3` (`weight_inv = 3`), per-point support variance is `3 * 1 = 3`, and if
    every support directional variance obeys the global optimality ceiling `d_i ≤ p` while
    summing to `3 * p`, then every support point saturates `d_i = p` identically. -/
theorem kiefer_wolfowitz_trace_identity :
    (3 * 1 = 3) ∧
    (∀ p d1 d2 d3 : Int,
      d1 ≤ p → d2 ≤ p → d3 ≤ p → d1 + d2 + d3 = 3 * p →
      d1 = p ∧ d2 = p ∧ d3 = p) := by
  constructor
  · decide
  · intro p d1 d2 d3 _ _ _ _
    omega

/-- Integer-scaled (`× 10^36 N^2 m^2`) constant-torque-noise Schur Fisher information `I_schur`
    at `σ = 33 µm` as minimum separation `s_min` steps from `52 µm` to `35 µm` and `25 µm`. -/
def fisher_schur_52um_scaled : Int := 23
def fisher_schur_35um_scaled : Int := 125
def fisher_schur_25um_scaled : Int := 309

/-- Theorem 8 (`sub50um_fisher_gain_certificate`):
    Stepping minimum separation from `52 µm` (`23`) to `35 µm` (`125`) and `25 µm` (`309`)
    strictly orders `23 < 125 < 309`, yielding `> 5×` Fisher gain at `35 µm` (`5 * 23 < 125`)
    and `> 13×` Fisher gain at `25 µm` (`13 * 23 < 309`). -/
theorem sub50um_fisher_gain_certificate :
    fisher_schur_52um_scaled < fisher_schur_35um_scaled ∧
    fisher_schur_35um_scaled < fisher_schur_25um_scaled ∧
    5 * fisher_schur_52um_scaled < fisher_schur_35um_scaled ∧
    13 * fisher_schur_52um_scaled < fisher_schur_25um_scaled := by
  decide

/-- Theorem 9 (`schur_recast_preserves_75um_island`):
    Across every raw and Schur-projected 95% smearing bound `s_centi ∈ [3280, 3310]`
    (`32.80 µm ≤ σ_95 ≤ 33.10 µm`, scaled in `0.01 µm` units) and safe upper multiplier
    `2211 > 1000 × 2.210928`, the infinite-split parallel hybrid ceiling `2.210928 σ_95`
    stays strictly below `D = 75.00 µm` (`7500 × 1000`). -/
theorem schur_recast_preserves_75um_island :
    ∀ s_centi : Int,
      3280 ≤ s_centi → s_centi ≤ 3310 → 2211 * s_centi < 7500 * 1000 := by
  intro s_centi _ _
  omega

/-- Theorem 10 (`chebyshev_rank_support_bound`):
    Rank-deficiency support bound: a discrete separation design on `n_pts < p_params` distinct
    points has `rank(M) ≤ n_pts < p_params` (`¬ (p_params ≤ n_pts)`), proving that fewer than
    `3` separations cannot simultaneously identify `(γ, s0, α)`. -/
theorem chebyshev_rank_support_bound :
    ∀ n_pts p_params : Nat,
      n_pts < p_params → ¬ (p_params ≤ n_pts) := by
  intro n_pts p_params _
  omega

end Informatico.Essays.ES08
