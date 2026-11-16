# Proof-adversarial review: Operational recovery bounds for an expectation-dependent quantum amplifier

**Source SHA-256 (as supplied, not recomputed):** `1f0219515ba8af76fcc077ac2c145aba5b06aea3b4a4494b96fcc3748fe5a419`

**Scope:** I read only the supplied packet. I ran no tools, commands or external lookups. I did not re-inspect Bény–Oreshkov or Watrous; I took them as paraphrased. This is an AI review, not human peer review or formal certification.

**Verdict: GO-WITH-NOTES.** I found no essential mathematical defect. Every constant and identity I attacked survived. The notes below are minor clarifications, separated from optional extensions.

---

## Falsification attempts and outcomes

### 1. Fidelity conventions and the duality import (§2, eqs. (recovery) and (duality))

- **Half-diamond sufficiency.** The target is pure, so f² = ⟨ψ|ω|ψ⟩ ≥ 1 − D(ω, ψ) ≥ 1 − η. This holds.
- **Duality specialization.** If F(RN_V, id) ≥ √(1−η), then max over R′ of F(N̂_V, R′M̂) ≥ √(1−η). R′M̂ ranges over constant channels S_σ. The maximum is attained because states form a compact set and F is continuous, so a σ exists. This holds.
- **Use on pure inputs.** For a pure logical input, the purification is a product state. The entanglement fidelity then reduces to f(N̂_V(ψ), σ), so the min-over-inputs guarantee applies per vector. This holds.
- **Convention.** η is the squared infidelity, and the root-fidelity bound is √(1−η). These are used consistently in Lemma 1 and Theorem 2.

### 2. Lemma 1 (rare-event bound)

- ‖x−y‖² = 2 − 2f ≤ 2 − 2√(1−η) = b². This holds.
- The difference ⟨x,Ox⟩ − ⟨y,Oy⟩ splits as ⟨x−y, OΠx⟩ + ⟨OΠy, x−y⟩. With ‖O‖ ≤ 1, this gives ≤ b(‖Πx‖ + ‖Πy‖) ≤ b(2√w + b). This holds.
- The hypothesis tr(Πρ) ≤ w is needed only for ρ, which is what is stated.
- Edge cases w = 0 and η = 0 hold.
- b ≤ √(2η) holds because 1 − √(1−η) ≤ η on [0,1].

### 3. Exact pullbacks (§3, eqs. (pullP), (pullJ), Π₁)

- **Source projector.** K₁₀†K₁₀ + K₁₁†K₁₁ = γN_S ⊗ (A₀†A₀ + A₁†A₁) = γN_S. This holds.
- **Exchange.** A₁†A₀ = √γ|e⟩⟨g| and A₀†A₁ = √γ|g⟩⟨e|. So K₁₀†K₀₁ = γ|eg⟩⟨ge|, including at γ = 1. T is real symmetric, so the complementary-channel index-ordering convention does not matter. This holds.
- **Single jump.** A₀†A₀ = I − γN gives γ(N_S + N_B − 2γN_SN_B). This holds.
- **Support conditions.** Tr(Π₁ρ_E) ≤ 2γ, T = Π₁TΠ₁ and ‖T‖ = 1. Tr(Π_Sρ_E) = γ⟨N_S⟩ ≤ γ. This holds.

### 4. Theorem 2 constants

- **Source term.** Every expectation γ⟨V†N_SV⟩ lies within 2b√γ + b² of tr(Π_Sσ). The spectral half-diameter is therefore ≤ 2b/√γ + b²/γ. Since P = I − N_S, the same bound holds for P.
- **Exchange term.** With w = 2γ, the bound is 2√2·b/√γ + b²/γ.
- **Trivial caps.** The caps 1/2 and 1 are correct, and midpoint scalars give both minima simultaneously.
- **Dimension independence.** The argument quantifies over all unit code vectors with no dimension factor. This holds.

### 5. Uniform constant 22 and eq. (cost)

- Using b/√γ ≤ √(2r) and b²/γ ≤ 2r:
  - e_P ≤ 2√2·√r + 2r
  - e_J ≤ 4√r + 2r
  - Sum: (4 + 2√2)√r + 4r ≤ (8 + 2√2)√r ≈ 10.83√r < 11√r, using r ≤ 1.
  - The factor two then gives 22.
- **Helstrom step.** P_succ = ½ + D/2 ≥ 2/3 requires D ≥ 1/3.
- **Cost.** 22A√r ≥ 1/3 − 1/4 = 1/12 gives A√r ≥ 1/264.
- **Direction of the asymptotic statement.** Exponentially small r forces exponentially large A. This is stated correctly.

### 6. Residual, p = 0 extension and measurability (Theorem 3 proof)

- **Off-diagonal structure.** J swaps source g ↔ e, so PJP = (I−P)J(I−P) = 0. Then j = 2 Re⟨PΨ, J(I−P)Ψ⟩ ≤ 2√(p(1−p)).
- **Residual norm.** ‖R‖ ≤ |g|(√p·e_J + √(1−p)·e_P) ≤ |g|(e_J + e_P). No lower bound on p is used. This holds.
- **Gradient.** I re-derived the gradient of the degree-2 homogeneous functional (eq. functional). It reproduces eq. (native), including the −pI term.
- **Zero extension.** The operator R(Ψ) is discontinuous at p = 0, because j/√p does not tend to 0 along all directions. However, it is bounded by (3/2)|g| and measurable along a trajectory. The vector R·Ψ is continuous, as the text now states. The zero representative at p = 0 is consistent with the defined vector field.
- **Retained ordinary term.** ωN is retained at p = 0, and E1 is resolved as stated.

### 7. Moving code, variation of constants and boundaries

- **Exact compression.** If Ψ = VΦ, then iΦ̇ = V†HVΦ − iV†V̇Φ, given that the trajectory stays in the code. −iV†V̇ is Hermitian because V†V = I. This holds.
- **Scalar terms.** Every scalar term, including the state-dependent ones such as g·j·a/(2√p) and −p, contributes only phase. These are correctly dropped.
- **Commutator bound.** ½‖[R,ρ]‖₁ ≤ ‖R‖. Combined with Duhamel on an absolutely continuous ρ and the triangle inequality across the two inputs, this gives the factor 2·∫|g|(e_P + e_J). The argument does not assume nonlinear contractivity.
- **Boundaries.** Input-independent isometries retaining all records preserve D. The final readout contracts it. Restarting the comparison per interval and summing is valid.
- **Multi-pair case.** Summing per-pair residual norms by the triangle inequality is valid for overlapping, non-commuting pairs, given each pair's separate damping guarantee on the common code.
- **Attempted falsifier.** I tried a record discarded mid-run, which would let separately evolved branches have different p. This is excluded by the stated hypotheses, and I found no remaining loophole.

### 8. Finite code, decoder and exponent (§5)

- **Isometry and defect.** V is an isometry. V†PV = diag(1−a−d, 1−a+d), so the defect is exactly d.
- **Kraus action.** K₀₀V|j⟩ has norm² = 1 − γn_j. K₁₀V|j⟩ = √(γn_j)|gg⟩|j,1⟩. K₀₁ and K₁₁ annihilate the code.
- **Orthogonality.** The four normalized directions are orthogonal, as claimed.
- **Dephasing multiplier.** The off-diagonal multiplier is √((1−γn₀)(1−γn₁)) + γ√(n₀n₁), which equals λ in eq. (lambda).
  - λ ∈ [0,1] by Cauchy–Schwarz.
  - The worst-case infidelity is exactly (1−λ)/2, attained at ⟨Z⟩ = 0.
- **Taylor expansion.** 1 − λ = (γd²/2)[γ/(1−γa) + 1/a] + O(d⁴) = γd²/(2a(1−γa)) + O(d⁴). This confirms eq. (scaling). The condition 1 − γa > 0 holds because a < 1 and γ ≤ 1.
- **Consistency with Theorem 2.** The leading term 2√(η/γ) = d/√(a(1−γa)) ≥ d, so the witness does not contradict Theorem 2.
- **Optimal-recovery remark.** Substituting the optimal recovery error is correctly argued, because η* ≤ η_rec only strengthens the conclusion.
- **Non-invariance.** It is correctly disclosed that J leaves the code.

---

## Findings

### Essential
None.

### Minor (clarifications; no change to any result)

- **M1 — §2, after eq. (duality).** "Some environment state σ satisfies" relies on attainment of the maximum over R′. This is trivial by compactness in finite dimension. A short clause would close it.
- **M2 — §5, eq. (scaling) and the following paragraph.** The necessity claim is made at fixed γ, with d → 0. It therefore establishes necessity of the exponent ½ in η. It does not by itself establish necessity of the 1/√γ normalization. The text says "for fixed a, γ", which is accurate. However, the phrase "the scale √(η/γ)" could be read as covering γ-dependence.
  - Spot check: for d fixed and γ → 0, η/γ → (a − √(a²−d²))/2 ≈ d²/(4a). This is consistent with Θ(√(η/γ)) scaling, but it is not stated or claimed.
  - Either keep "exponent in η" explicitly, or add one sentence.
- **M3 — README display.** The README uses D_in, while the manuscript uses d₀. It also writes r ≥ sup_t η/γ, while Theorem 3 quantifies "every active pair and time". This is harmless, but the README should match the theorem.

### Optional exposition (not required)
- The Theorem 3 proof could state the identity iΦ̇ = V†HVΦ − iV†V̇Φ explicitly instead of naming its terms.
- In the proof of Theorem 2, "half the spectral diameter ≤ obtained bound" could note that the obtained bound is a radius about tr(Π_Sσ)/γ.

### Out of scope (correctly disclaimed; not defects)
These are all explicitly excluded by the manuscript:
- tightness of the dynamical bound or of the constant 22
- unprotected excursions
- restricted-state recovery
- physical realization
- general well-posedness or Lipschitz properties
- derivation of η(Δt)

The finite diagnostic is correctly described as checking substitutions only.

---

**Verdict: GO-WITH-NOTES.** No missing hypothesis or failing constant was found in the operational recovery-to-compression theorem, Lemma 1, the pullbacks, the p = 0 extension, the moving-code and boundary comparison, or the finite witness and its exponent. M1–M3 are wording-level only.
