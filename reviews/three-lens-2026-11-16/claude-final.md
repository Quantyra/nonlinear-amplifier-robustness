**Source SHA-256 (as supplied, not recomputed):** `07d0f17d9bc09aae4f713cb988e51363812f37e8030963513ecf022000819b46`

**Scope:** I read only the material in your message and used no tools. The Beny–Oreshkov Theorem 1 is checked only against your paraphrase, not the primary source. This is an AI review. It is not human peer review, not kernel or Lean acceptance, and not a novelty clearance.

## Verdict: **GO-WITH-NOTES**

I found no falsifier for any quantified claim. Every constant re-derives. The residual items are one essential wording correction (E1) and optional exposition.

## Essential correction

**E1 (Minor, wording affects correctness). Theorem 3 proof, paragraph after eq. `eq:bounded`: "At p=0 the native vector field is zero by its stated extension."**
- Section 1 sets only the *nonlinear* vector field to zero at p=0. The "native law" `eq:native` also contains ωN.
- If the whole native field vanished at p=0, the ωN term would drop out on p=0 time sets for one input but not the other.
- The propagator built from ωV†NV would then not be common to both inputs, and the variation-of-constants comparison would fail.
- Fix: write "the native *nonlinear* vector field (the g-dependent terms) is zero; ωNΨ is retained." The same applies to "its density-operator contribution."

## Optional exposition

- **O1, Lemma 1 proof.** Uhlmann gives |⟨x,y⟩| = f. State that the phase of y is chosen so ⟨x,y⟩ = f ≥ 0. That gives ‖x−y‖² = 2−2f ≤ b².
- **O2, Section 2 / eq. `eq:duality`.** State explicitly that the duality is applied to the 4-dimensional Kraus-labelled complement used in Section 3. Equality holds for any Stinespring complement, since the R′ maximization absorbs the isometric freedom, but the text only fixes the labelling later.
- **O3, Theorem 3 proof.** Measurability of t ↦ R_Ψ(t) is not stated. It holds because V is C¹, the eigenvalue midpoints a(t), c(t) are continuous, p and j are continuous along an absolutely continuous Ψ, and ‖R‖ ≤ 1.5|g| makes it integrable. One sentence would close this.
- **O4, Section 5, eq. `eq:scaling`.** The remainder is in fact uniform in γ ∈ (0,1]:
  - η_rec/γ = d²/[4a(1−γa)] + O(d⁴), with the O(d⁴) depending only on a, using 1−γa ≥ 1−a.
  - So the family shows necessity of the √(η/γ) scale uniformly, including as γ→0, not just the √η exponent at fixed γ.
  - The current fixed-(a,γ) statement is correct as written. This would only strengthen it.
- **O5, after eq. `eq:cost`.** "Needs exponentially large coupling-time" follows from A√r ≥ 1/264 alone. The polynomial strength bound is what converts it into exponential *duration*. Say "duration" there.
- **O6, README.** It uses D_in where the manuscript uses d₀.

## Attempted falsifiers (all failed)

**Functional and gradient (eq. `eq:native` vs `eq:functional`).**
- ∂/∂Ψ* of √(⟨P⟩/⟨Ψ,Ψ⟩) at a normalized state is (PΨ − pΨ)/(2√p).
- Multiplying by g·j gives the last term exactly. ✓

**Fidelity conventions.**
- η is squared-root-fidelity infidelity throughout.
- The half-diamond sufficiency holds: for the projector Q = I − ψ, tr(Qρ′) = tr(Q(ρ′−ψ)) ≤ ½‖ρ′−ψ‖₁. ✓
- For pure logical inputs ψ⊗|0⟩, the channel-fidelity minimum controls f(N̂(ψ), σ). ✓
- For M = id, the complement is the trace, so R′∘M̂ is a constant state σ. ✓

**Lemma 1.**
- The bound splits as ⟨x−y, O x⟩ + ⟨y, O(x−y)⟩, with O = ΠOΠ.
- This gives b‖Πx‖ + b‖Πy‖ ≤ b(2√w + b).
- 1 − √(1−η) ≤ η follows from √(1−η) ≥ 1−η.
- The cases w = 0 and η = 0 are covered. ✓

**Pullbacks (eqs. `eq:pullP`, `eq:pullJ`, and Π₁).**
- K₁₀†K₁₀ + K₁₁†K₁₁ = γ|e⟩⟨e| ⊗ I. ✓
- K₁₀†K₀₁ = (√γ|e⟩⟨g|) ⊗ (√γ|g⟩⟨e|) = γ|eg⟩⟨ge|, valid at γ = 1. ✓
- A₀†A₀ = I − γN gives γ(N_S + N_B − 2γN_SN_B). Its maximum eigenvalue is γ·max(1, 2−2γ) ≤ 2γ. ✓
- T = Π₁TΠ₁ and ‖T‖ = 1. ✓

**Theorem 2.**
- Dividing (2b√γ + b²) by γ, and (2b√(2γ) + b²) by γ, gives the stated e_P and e_J.
- The P bound transfers from N_S via V†PV = I − V†N_SV.
- The midpoint scalar is optimal, and the caps 1/2 and 1 are correct. ✓

**Generator and p=0.**
- |j| ≤ 2√(p(1−p)) holds because J = PJ(I−P) + h.c. Then ‖R‖ ≤ |g|(√p·e_J + √(1−p)·e_P). ✓
- The nonlinear vector norm is ≤ |g|(√p + √p + p). It is continuous at p=0, though not Lipschitz. The manuscript correctly conditions on solutions rather than claiming well-posedness. ✓

**Moving code.**
- From Ψ = Vφ: φ̇ = −iV†HVφ − V†V̇φ, and −iV†V̇ is Hermitian because V†V = I.
- The state-dependent scalar parts are phases and drop out of the density-operator commutator. ✓
- ½‖[R,ρ]‖₁ ≤ ‖R‖ gives an increment of ∫‖R‖ per input. The triangle inequality gives the factor 2. ✓
- Boundaries: an isometric Stinespring dilation with retained records preserves D; the final channel contracts it. Discarding a record before native evolution would make Ψ mixed and the generator undefined, and the hypothesis correctly forbids it. ✓

**Multi-pair.**
- The scalar parts of each summand are removed separately and the residual norms add.
- The bound |j_k| ≤ 2√(p_k(1−p_k)) needs only P_kJ_kP_k = 0. Overlap between pairs is irrelevant. ✓

**Constants.**
- e_P ≤ 2√2·√r + 2r and e_J ≤ 4√r + 2r.
- With r ≤ √r, the sum is ≤ (8 + 2√2)√r ≈ 10.83√r < 11√r, giving the factor 22.
- 1/3 ≤ 1/4 + 22A√r gives A√r ≥ 1/264. (For r > 1 the caps give A ≥ 1/36 anyway.) ✓

**Section 5 code and decoder.**
- V is an isometry, V†PV = diag(1−a−d, 1−a+d), and the defect is d.
- K₀₁ and K₁₁ annihilate the code. The branch norms are √(1−γn_j) and √(γn_j).
- The four directions are orthonormal.
- λ = √((1−γn₀)(1−γn₁)) + γ√(n₀n₁), which equals eq. `eq:lambda`, with 0 ≤ λ ≤ 1.
- F² = 1 − η_rec + η_rec⟨Z⟩², with worst case η_rec.
- The Taylor coefficient is (γd²/2)[γ/(1−γa) + 1/a]/2 = γd²/[4a(1−γa)]. ✓
- Consistency with Theorem 2: 2√(η/γ) ≈ d/√(a(1−γa)) ≥ d. No contradiction. ✓
- Substituting the optimal recovery error is sound: η* ≤ η_rec, and η* > 0 because d > 0 together with Theorem 2. ✓

## Not checked

- The primary text of Beny–Oreshkov Theorem 1, including its root-fidelity convention and its complement-choice statement.
- Watrous Theorem 3.22 itself.
- Diagnostic receipts and build receipts.
- Novelty or priority.
