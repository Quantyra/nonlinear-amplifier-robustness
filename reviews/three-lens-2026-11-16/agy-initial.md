# Independent Review Report: Non-Claims and Attribution Lens

**Source SHA-256:** `0891e8571c5904555500aed76a8c7814e0835061319bf4243afbe38135c04f58`  
**Review Target:** `manuscript/main.tex`, `README.md`, `CLAIMS.md`, `SOURCES.md`, `.zenodo.json`, `CITATION.cff`  
**Review Scope:** Non-claims, attribution boundaries, imported machinery separation, coherence of scoped contribution, and verification of operational constraints.

---

## 1. Executive Summary & Disposition

- **Disposition:** **GO-WITH-NOTES**
- **Coherence Assessment:** The manuscript candidate presents a coherent, mathematically scoped technical contribution. It does not merely restate existing approximate quantum error correction (AQEC) duality or linear metrology principles. Instead, it constructs an operational bridge from worst-case entanglement recovery under a finite two-qubit amplitude-damping benchmark to concrete compression defect bounds on a hypothetical nonlinear generator, establishing a whole-trajectory distinguishability bound under a strict common-invariant-code assumption.
- **Attribution Boundary:** Prior theorems (Bény–Oreshkov duality, Watrous purification/fidelity relations, Zhou et al. metrology principles, Childs–Young nonlinear discrimination) are explicitly demarcated and cited. No novel channel duality, linear-metrology sufficiency, or computational complexity advance is claimed.
- **Negative Disclaimers & Non-Claims:** The text, README, and claim maps consistently and repeatedly disclaim:
  1. Physical realization, causal completion, or energy apparatus for the nonlinear primitive.
  2. Sharpness or optimality of the whole-trajectory dynamical gain bound ($22 A \sqrt{r}$).
  3. General/unrestricted nonlinear fault-tolerance impossibility.
  4. Excursion dynamics outside a common invariant moving code.
  5. Any alteration to BPP vs. BQP.
  6. Human peer review, formal kernel certification, or archival publication status.

---

## 2. Distinction of Imported Machinery vs. New Application

| Imported Result / Principle | Primary Source Attribution | Role in Candidate | Candidate's New Contribution |
| :--- | :--- | :--- | :--- |
| **Approximate QEC Duality** | C. Bény & O. Oreshkov, *PRL* **104**, 120501 (2010); arXiv:0907.5391v4 [Theorem 1, Eq. (3)] | Specializes identity-target duality to obtain an environment state $\sigma$ with root fidelity $F(\widehat{\mathcal{N}}_V, \mathcal{S}_\sigma) \ge \sqrt{1-\eta}$. Applied strictly to linear native-off damping benchmark. | Exact finite complementary pullbacks $\widehat{\mathcal{N}}_V^*(\Pi_S) = \gamma V^\dagger N_S V$ and $\widehat{\mathcal{N}}_V^*(T) = \gamma V^\dagger J V$ for two-qubit amplitude damping with noiseless spectators. |
| **Purification & Fidelity Relations** | J. Watrous, *The Theory of Quantum Information* (2018) [Chapter 3, Thm 3.22] | Standard tools relating root fidelity to maximal purification overlap. | **Lemma 1 (Rare-event observable bound):** Refines plain trace-distance estimates ($b/\gamma$) to $2b\sqrt{w}/\gamma + b^2/\gamma$, yielding scale $\sqrt{\eta/\gamma} + \eta/\gamma$ when environment jump probability is $O(\gamma)$. |
| **Signal vs. Noise-Span Principle** | S. Zhou et al., *Nat. Commun.* **9**, 78 (2018); S. Zhou & L. Jiang, *PRResearch* **2**, 013235 (2020) | Baseline organizing concept that signal operators overlapping noise operators cannot be error-corrected. | Generator integration for a **state-dependent nonlinear vector field**, handling the gradient correction term and removing the need for a strictly positive lower bound on population $p$. |
| **Ideal Nonlinear State Discrimination** | A. M. Childs & J. Young, *PRA* **93**, 022314 (2016) | Conceptual baseline for fast state discrimination under uncorrected nonlinear QM. | Counterexample code and isometric recovery (Section 5) demonstrating that the $\sqrt{\eta/\gamma}$ scaling is strictly necessary for the recovery-to-compression bridge. |

---

## 3. Audit of Claims, Proofs, and Structural Constraints

### 3.1 Strict Common Invariant-Code Premise
- **Locations:** `manuscript/main.tex` lines 58–59, 147–148; `CLAIMS.md` Claim C4; `README.md` lines 249, 268.
- **Verification:** The dynamical integration in Theorem 3 ($D_{\mathrm{out}} \le \min\{1, d_0 + 22 A \sqrt{r}\}$) explicitly premises that both compared clean trajectories remain in the range of a common differentiable isometry $V(t)$. The text explicitly cautions that this does not model arbitrary excursion dynamics, syndrome-conditioned state-dependent recovery, or simultaneous continuous noisy nonlinear flows. This matches the required protocol constraint.

### 3.2 Hypothetical Primitive & Boundary Cancellation
- **Locations:** `manuscript/main.tex` lines 46–56, 163–170; `CLAIMS.md` Claim D1.
- **Verification:** The native Hamiltonian includes the gradient correction term $\frac{g(t)j}{2\sqrt{p}}(P - pI)$ required by the homogeneous functional $\mathcal{E}(\Psi)$. In the proof of Theorem 3, the residual operator $R_\Psi = g\sqrt{p} E_J + \frac{gj}{2\sqrt{p}} E_P$ exhibits an apparent singularity as $p \to 0$. However, because $P J P = (I-P) J (I-P) = 0$, the manuscript establishes $|j| \le 2\sqrt{p(1-p)}$, ensuring $\frac{|j|}{2\sqrt{p}} \le \sqrt{1-p} \le 1$. Hence $\|R_\Psi\| \le |g|(e_J + e_P)$ holds uniformly without dividing by any minimum population threshold.

### 3.3 Non-Attainment of Dynamical Sharpness
- **Locations:** `manuscript/main.tex` lines 194, 221–222; `CLAIMS.md` Claim C7; `README.md` lines 255–256.
- **Verification:** Section 5 constructs a 1-qubit code in a 4-dimensional ancilla space with isometric recovery showing $\eta_{\mathrm{rec}} = \frac{\gamma d^2}{4a(1-\gamma a)} + O(d^4)$, proving the necessity of the square-root exponent for the *recovery-to-source-compression* step. Crucially, the manuscript explicitly notes in line 221 that the exchange operator $J$ maps the code space to states with detector excitation outside the code, thus violating the invariance premise of Theorem 3. The candidate does not claim to establish dynamical sharpness or implement a protected nonlinear amplifier.

### 3.4 Review, Formal, and Publication Status
- **Locations:** `manuscript/main.tex` lines 28, 230; `README.md` lines 246, 270; `CLAIMS.md` line 276; `CITATION.cff` line 332; `.zenodo.json` line 324.
- **Verification:** All metadata documents uniformly reflect candidate status: preparation-stage, uncertified, unpublished, no DOI authorized, and no PaperMill registration.

---

## 4. Attempted Falsifiers & Diagnostic Checks

1. **Attempted Falsifier 1: Hidden Code-Dimension Dependency in AQEC Bound**
   - *Hypothesis:* The reduction from operational recovery to operator compression might hide a dimension factor $O(\log \dim \mathcal{H})$ or $O(\dim \mathcal{H})$ in the trace-norm bounds.
   - *Test:* In Theorem 2, Lemma 1 is applied directly on the environment Hilbert space $\mathcal{H}_E = \mathbb{C}^4$ of the two-qubit amplitude-damping channel. The reference space size is eliminated by Uhlmann's purification theorem on $\mathcal{H}_E$, and the operator norm on the logical space is extracted via the numerical radius of Hermitian operators.
   - *Result:* Falsifier failed; the bounds $e_P$ and $e_J$ are strictly independent of code and spectator dimension.

2. **Attempted Falsifier 2: Divergence of Distinguishability Generator at $p=0$**
   - *Hypothesis:* If $p \to 0$ along a trajectory, the term $\frac{gj}{2\sqrt{p}} E_P$ could cause an unbounded rate of trace-distance expansion.
   - *Test:* The off-diagonal nature of $J$ relative to $P$ enforces $|j| \le 2\sqrt{p(1-p)}$. Consequently, $\left\|\frac{gj}{2\sqrt{p}} E_P\right\| \le |g|\sqrt{1-p} e_P \le |g| e_P$. Combined with $\|g\sqrt{p} E_J\| \le |g| e_J$, the residual norm is unconditionally capped by $|g|(e_P + e_J)$.
   - *Result:* Falsifier failed; the generator remains Lipschitz-continuous and bounded down to $p=0$.

3. **Attempted Falsifier 3: Inconsistency of Numerical Pre-factor 22 in Theorem 3**
   - *Hypothesis:* Combining $e_P$ and $e_J$ under $r = \sup_t \eta(t)/\gamma(t) \le 1$ might exceed 22 when accounting for the factor of 2 from the two trajectories.
   - *Test:* With $b(\eta) \le \sqrt{2\eta}$, we have $e_P \le 2\sqrt{2}\sqrt{r} + 2r$ and $e_J \le 4\sqrt{r} + 2r$. For $r \le 1$, $r \le \sqrt{r}$, yielding $e_P + e_J \le (4 + 2\sqrt{2})\sqrt{r} + 4r \le (8 + 2\sqrt{2})\sqrt{r} \approx 10.8284\sqrt{r} < 11\sqrt{r}$. Multiplied by the trajectory factor 2, the bound is $(16 + 4\sqrt{2}) A \sqrt{r} \approx 21.6568 A \sqrt{r} \le 22 A \sqrt{r}$.
   - *Result:* Falsifier failed; the constant 22 is mathematically sound.

4. **Attempted Falsifier 4: Ambiguity in Infidelity Definition**
   - *Hypothesis:* The manuscript might conflate root infidelity $1 - F$, squared infidelity $1 - F^2$, and diamond distance, invalidating the scaling in eq. (72) vs. Lemma 1.
   - *Test:* The manuscript explicitly defines $\eta$ in eq. (70) as $F^2 \ge 1-\eta$, meaning $\eta$ is squared-fidelity infidelity. In Lemma 1, $f(\rho, \sigma) \ge \sqrt{1-\eta}$ is used, and $b(\eta) = \sqrt{2(1-\sqrt{1-\eta})} \le \sqrt{2\eta}$. This matches Bény–Oreshkov's root-fidelity duality $F(\widehat{\mathcal{N}}, \mathcal{S}_\sigma) \ge \sqrt{1-\eta}$.
   - *Result:* Falsifier failed; definitions are tracked consistently across all steps.

---

## 5. Severity-Tagged Findings

### Finding 1: [INFORMATIONAL / EXPOSITORY] Clarification of Triangle Bound on Residual Generator
- **Location:** `manuscript/main.tex`, eq. (18), lines 163–169.
- **Detail:** In eq. (18), $R_\Psi = g\sqrt{p} E_J + \frac{g j}{2\sqrt{p}} E_P$. The text derives $|j| \le 2\sqrt{p(1-p)}$ and immediately concludes $\|R_\Psi\| \le |g|(e_J + e_P)$. While mathematically exact (since $\sqrt{p} \le 1$ and $\sqrt{1-p} \le 1$), the intermediate inequality $\|R_\Psi\| \le |g|(\sqrt{p} e_J + \sqrt{1-p} e_P) \le |g|(e_P + e_J)$ is omitted in the exposition.
- **Action:** Optional exposition improvement for future revisions. Does not affect validity.

### Finding 2: [INFORMATIONAL / ATTRIBUTION] Alignment of Duality Notation with Source arXiv Record
- **Location:** `manuscript/main.tex`, Section 2, lines 75–80; `SOURCES.md`, Item 1.
- **Detail:** The manuscript uses root fidelity $F$ and defines $\eta$ as worst-case squared infidelity ($F^2 \ge 1-\eta$). Bény–Oreshkov (arXiv:0907.5391v4) Theorem 1 uses root fidelity directly without squaring. The text in lines 71–73 and SOURCES.md carefully explains this difference, preventing any ambiguity in citation.
- **Action:** Retain this explicit clarification in any final revision.

### Finding 3: [INFORMATIONAL / SCOPE INTEGRITY] Preservation of Non-Claims across Downstream Summaries
- **Location:** `README.md`, lines 268–271; `CLAIMS.md`, lines 291–293.
- **Detail:** The negative claims (no physical implementation, no universal fault-tolerance impossibility, no BPP/BQP consequence) are prominently placed in the README and CLAIMS files. When preparing any external submission or archiving metadata, these boundary statements must be preserved verbatim.
- **Action:** No edit needed; verify during eventual disposition.

---

## 6. Conclusion

The manuscript candidate 0.1.0 cleanly separates established AQEC channel duality and linear metrology principles from its specific finite-damping operational bounds and the non-sharp dynamical distinguishability estimate. It satisfies all attribution, scoping, and non-claims criteria required by the investigation protocol.
