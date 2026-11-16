# Proof-adversarial review: "Operational recovery bounds for an expectation-dependent quantum amplifier"

**Source SHA-256 (as supplied):** `0891e8571c5904555500aed76a8c7814e0835061319bf4243afbe38135c04f58`. I did not hash the file myself, since no commands were permitted. The findings refer to the packet text above.

**Scope.** I read only the supplied material and ran nothing, including the 46-assertion diagnostic. I treat Bény–Oreshkov Theorem 1/Eq. (3) as imported, as the packet paraphrases it; I did not re-inspect it. This is an AI review. It is not human peer review, not formal or Lean certification, and not a novelty clearance.

**Verdict: REVISE (narrow).** The single-pair mathematics survived every falsification attempt below. The essential corrections are hypothesis statements missing from quantified parts of Theorem 3 (E1–E3). None of them breaks the single-pair argument. Once they are fixed, I would expect GO-WITH-NOTES.

---

## Essential corrections

**E1 — MAJOR. Theorem 3: the "simultaneous pairs" clause uses an undefined generator and lacks a hypothesis.**
- **Where:** Theorem 3, sentence after Eq. (gain); "summed over pairs" before Eq. (simple); proof, "parallel generators are charged by the sum of their norms."
- **Missing definition:** §1 defines the native law for one (S,B) pair only.
- **Missing hypothesis:** the theorem assumes Eq. (recovery) "for the finite damping test" without saying which pair is damped. The argument needs, for every pair k and every native time t:
  - a separate guarantee η_k(t) for damping applied to pair k's S_k B_k, with identity elsewhere;
  - η_k/γ_k ≤ r uniformly, for Eq. (simple).
- **Why it matters:** a guarantee for one pair's damping says nothing about another pair's P_k, J_k compressions. As written, the multi-pair claim is not supported.
- **Fix:**
  - Define H = ωN + Σ_k [g_k√p_k J_k + g_k j_k/(2√p_k)(P_k − p_k I)], with each p_k, j_k taken on the complete state.
  - State the per-pair recovery hypothesis.
  - Note that pairs may overlap. Theorem 2 is applied pair by pair, so overlap is harmless.

**E2 — MODERATE. Theorem 3 hypotheses on channel boundaries and records are too informal for the quantified claim.**
- **Where:** §4, first paragraph ("specified retained dilations", "admitted common code"); proof, "Common ordinary channel boundaries contract distance."
- **What the argument needs:**
  1. Each boundary is an input-independent isometry on the complete space, so purity is kept and the nonlinear law stays defined.
  2. All retained records and dilation registers are acted on trivially by P, J, the damping test and the native term.
  3. At the start of each native interval, both complete states lie in range(V(t_k) ⊗ I_R).
- **Wording:** under (1) the boundary preserves distance; "contract" is true but is not the operative fact. If discarding is allowed, the nonlinear law on mixed states is undefined, so discarding must be excluded explicitly.
- **Feed-forward:** classical feed-forward must be modeled coherently. Otherwise "controls independent of the input" fails.

**E3 — MINOR but essential. Regularity and reality conditions are missing from Theorem 3.**
- **Where:** Eq. (native); Theorem 3 hypotheses.
- **Reality:** g(t) and ω must be real. Otherwise H is not Hermitian, and both norm preservation and "½‖[R,ρ]‖₁ ≤ ‖R‖" fail as used.
- **Regularity for variation of constants and the integral:**
  - V should be C¹, or at least absolutely continuous with integrable V̇. Everywhere-differentiable alone does not guarantee an integrable connection −iV†V̇.
  - g should be locally integrable.
  - γ(t) and η(t) should be measurable, or replaced by a measurable upper envelope.
- **Trajectories:** state that "trajectory" means any absolutely continuous solution.

---

## Attempted falsifiers (all survived)

1. **Gradient, Eq. (functional) → Eq. (native).** I differentiated √(⟨P⟩/⟨Ψ,Ψ⟩) with respect to Ψ* at unit norm. The result is (P − p)Ψ/(2√p), which matches the last term exactly.
2. **p = 0 extension.** ‖(P − p)Ψ‖ = √(p(1−p)) and |j| ≤ 2√(p(1−p)), so the singular term is bounded by |g|√p(1−p). The proof's continuity claim is correct.
   - *Stronger, optional:* write x = PΨ and y = J(I−P)Ψ. The term becomes 2Re⟨x,y⟩·x/‖x‖ (positively 1-homogeneous with bounded derivative) plus j√p(I−P)Ψ. So the extended field is locally Lipschitz and trajectories are unique. Stating this removes any well-posedness doubt.
3. **Kraus pullbacks, Eqs. (pullP), (pullJ), Π₁.**
   - Σ K_a†K_a over the Π_S labels gives A₁†A₁ ⊗ I = γN_S.
   - A₁†A₀ = √γ|e⟩⟨g| and A₀†A₁ = √γ|g⟩⟨e|, so K₁₀†K₀₁ = γ|eg⟩⟨ge|, valid at γ = 1.
   - A₀†A₀ = I − γN gives γ(N_S + N_B − 2γN_SN_B) for Π₁. Its maximum eigenvalue is γ·max(1, 2−2γ) ≤ 2γ.
   - T and Π_S are real and symmetric, so the |a⟩⟨b| ordering convention of the complement is irrelevant.
4. **Lemma 1.**
   - Uhlmann with a phase choice gives ‖x − y‖² = 2 − 2f ≤ b².
   - Writing O = ΠOΠ, the split ⟨x−y, OΠx⟩ + ⟨OΠy, x−y⟩ gives b(2√w + b).
   - b ≤ √(2η) because √(1−η) ≥ 1 − η.
   - The w = 0 and η = 0 cases hold.
5. **Theorem 2.**
   - Fidelity on the environment marginal follows directly for pure logical inputs.
   - σ is input-independent, which is the crucial point supplied by the duality.
   - Dividing by γ confines the numerical range of V†N_SV to [s/γ ± ε], which yields the operator-norm bound.
   - The P defect equals the N_S defect.
   - The midpoint scalar is optimal and serves both caps simultaneously.
   - Sanity cases:
     - V|j⟩ = |eg⟩|j⟩: η = 0 and both compressions are scalar.
     - V|0⟩ = |eg⟩, V|1⟩ = |ge⟩: defect 1 and η = γ/2, so the uncapped e_J ≈ 2 ≥ 1, which is consistent.
6. **Duality convention.** Max and min commute with the monotone map f ↦ f². If Bény–Oreshkov's equality holds for root fidelity, it holds identically for squared fidelity. The √(1−η) transfer is therefore convention-robust, provided the same fidelity appears on both sides with the minimum over purified inputs.
   - The half-diamond sufficiency claim is correct: Tr ψ(ψ − ω) ≤ D for pure ψ.
   - Tensoring V with passive references does not change F, because the minimum ranges over purified inputs.
7. **Constants in Theorem 3.**
   - The uncapped integrand is e_P + e_J ≤ (2+2√2)√(2r) + 4r = (4+2√2)√r + 4r ≤ (8+2√2)√r ≈ 10.83√r for r ≤ 1. Hence 22.
   - Eq. (cost): ½ + D/2 ≥ ⅔ gives D ≥ ⅓, and (⅓ − ¼)/22 = 1/264.
   - The variation-of-constants step is correct: state-dependent scalars drop out of the commutator, and R is evaluated on the actual trajectory.
8. **Section 5 example.**
   - V is an isometry and V†PV = diag(1−a−d, 1−a+d), so the defect is exactly d.
   - Only K₀₀ and K₁₀ act. Their branch norms are √(1−γn_j) and √(γn_j), and the four directions are orthogonal.
   - The off-diagonal multiplier is λ, since (1−γn₀)(1−γn₁) = (1−γa)² − γ²d².
   - λ ≤ 1 by Cauchy–Schwarz, and the radicand is positive because γn₀ < 1.
   - The dephasing worst case is η_rec = (1−λ)/2.
   - Eq. (scaling): expanding to second order gives γd²/4·[γ/(1−γa) + 1/a] = γd²/(4a(1−γa)), which matches.
   - *Optimal-recovery remark:* the claim holds without assuming the replacement bound φ is monotone. If φ(x) = o(√x), then sup over x ≤ X of φ(x) = o(√X). One line saying so would close the gap the current wording ("no larger than") leaves.

---

## Optional exposition

- **O1.** Abstract: "recovery-to-compression exponent" should read "recovery-to-**source**-compression exponent". Section 5 witnesses only the P defect, not e_J. CLAIMS C7 already scopes it correctly.
- **O2.** Cite "Bény–Oreshkov Theorem 1, Eq. (3)" in §2. State that the maximum over R′ is attained and that the minimum ranges over purified inputs.
- **O3.** Notation clashes:
  - the scalar *a* (Theorems 2–3) versus the code parameter *a* (§5);
  - *j* as the expectation ⟨J⟩ versus the logical index.
- **O4.** The Section 5 remainder appears to be γ·O(d⁴) uniformly in γ. If verified, the family also shows the 1/γ normalization is necessary, not just the exponent at fixed γ. I have not fully verified this; state it only with a proof.
- **O5.** In Theorem 2's statement, say explicitly that the test damps the stated S,B pair with γ ∈ (0,1] and acts as the identity on other registers. This currently appears only in the preceding text.

---

## Non-findings and scope

- The diagnostic (46 assertions, maximum dimension 16, exit 0) was not run or inspected. Its results are neither confirmed nor relied upon.
- The manuscript's disclaimers are consistent with what is proved: no dynamical tightness, no excursion theorem, no physical realization, no BPP/BQP claim.
- I make no novelty or priority judgment.
