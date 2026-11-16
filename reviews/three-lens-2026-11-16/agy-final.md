# Independent Review: Non-Claims and Attribution Lens

**Audit Target**: Research Manuscript Candidate 0.1.0 (`manuscript/main.tex`, `README.md`, `CLAIMS.md`, `SOURCES.md`, `.zenodo.json`, `CITATION.cff`)  
**Supplied Source SHA-256**: `07d0f17d9bc09aae4f713cb988e51363812f37e8030963513ecf022000819b46`  
**Review Scope**: Non-claims, attribution boundaries, technical coherence, and hypothesis consistency based strictly on the provided packet.

---

## 1. Executive Summary & Technical Coherence Assessment

### Coherent Scoped Contribution vs. Mere Restatement
The candidate manuscript is **a coherent, narrowly scoped technical contribution**, not merely a restatement of existing theorems.

While the mathematical spine rests on established foundational tools—specifically channel-fidelity duality from Bény & Oreshkov (2010), standard purification/fidelity geometry from Watrous (2018), and the general signal-versus-noise-span organizing principle from Zhou et al. (2018) / Zhou & Jiang (2020)—the candidate formulates a distinct, self-contained application:
1. **Kraus Environmental Pullbacks**: Explicitly identifies the dual action of two-qubit amplitude damping on complementary environment observables ($\Pi_S \mapsto \gamma V^\dagger N_S V$ and $T \mapsto \gamma V^\dagger J V$), which map directly to the source population and exchange operators of the non-linear amplifier model.
2. **Rare-Event Scaling Refinement**: Leverages an environment-event support bound ($w = O(\gamma)$) in Lemma 1 to convert worst-case entanglement recovery infidelity $\eta$ into operator-compression defects bounded by $\sqrt{\eta/\gamma} + \eta/\gamma$, preventing spurious $1/\gamma$ divergences as $\gamma \to 0$ when $\eta/\gamma$ is bounded.
3. **Trajectory Distinguishability Integration**: Integrates the state-dependent nonlinear generator (including the required functional gradient correction $\frac{g j}{2\sqrt{p}}(P - pI)$) across common invariant moving codes, establishing an explicit distinguishability bound ($D_{\mathrm{out}} \le d_0 + 22 A \sqrt{r}$) that holds without requiring an ad-hoc positive lower bound on source population $p$.
4. **Sharpness Separation**: Constructs a concrete finite code and isometric decoder establishing that the $\sqrt{\eta/\gamma}$ exponent in the recovery-to-source-compression bound is unimprovable, while rigorously disclaiming dynamical sharpness or working amplifier realization.

The boundaries between prior work and new technical derivations are kept scrupulously sharp throughout the manuscript, repository documents, and metadata.

---

## 2. Attribution Demarcation Audit

| Reference / Prior Work | Role in Manuscript | Attribution & Boundary Audit |
|---|---|---|
| **Bény & Oreshkov (2010)**<br>`arXiv:0907.5391v4` / `PRL 104, 120501` | **Imported Theorem (I1)**<br>Theorem 1, eq. (3) specialized to identity target. | **Cleanly Attributed.** Explicitly marked as imported in Section 2 (eqs. 77–81), Section 6, `CLAIMS.md`, and `SOURCES.md`. Acknowledged as an existence statement for a constant environment state $\sigma$ under native-off ordinary damping, with explicit disclaimers against general nonlinear channel duality or polynomial-time SDP recovery discovery. |
| **Zhou et al. (2018)**<br>`arXiv:1706.02445v2` / `Nat. Commun. 9, 78`<br>**Zhou & Jiang (2020)**<br>`arXiv:1910.08472v1` / `PRR 2, 013235` | **Background Organizing Principle**<br>Signal-vs-noise Lindblad span conditions in linear quantum metrology. | **Cleanly Attributed.** Section 1 and `SOURCES.md` explicitly cite these works as establishing the signal/noise-span principle. Section 1 explicitly disclaims novelty for this principle and states that linear metrological sufficiency theorems are not imported as nonlinear computational sufficiency. |
| **Childs & Young (2016)**<br>`arXiv:1507.06334v2` / `PRA 93, 022314` | **Baseline Comparison**<br>Ideal nonlinear state discrimination limits. | **Cleanly Attributed.** Cited in Section 1 and `SOURCES.md` as standard baseline for state discrimination under hypothetical nonlinear dynamics. The candidate explicitly disclaims claiming the first fast nonlinear state discrimination. |
| **Watrous (2018)**<br>`TQI, Cambridge Univ. Press` | **Standard Machinery**<br>Uhlmann's theorem, fidelity and trace norm relations. | **Cleanly Attributed.** Cited in Lemma 1 and Section 6 as standard fidelity machinery. No claim of novel information-theoretic identities. |

---

## 3. Negative Claims, Scope Limits, and Premise Integrity

The manuscript and associated files adhere to strict negative boundaries:

1. **Hypothetical Native Primitive**:
   - Explicitly defined as hypothetical in Abstract (L33), Section 1 (L58–59), and `.zenodo.json` (L334).
   - "No physical realization, causal completion or operational energy apparatus for (49)–(51) is supplied here." (L58–59).
2. **Common Invariant-Code Premise**:
   - Confined strictly to clean trajectories lying in the range of a common differentiable isometry $V(t)$ (Section 1 L60–61, Section 4 L149–152, Theorem 3 L161).
   - Acknowledged as a stronger restriction than general fault tolerance: "This is a stronger hypothesis than the requirements of an arbitrary successful nonlinear computer." (L60–61).
   - Excursions outside the protected code space, restricted-state recovery, and unread nonlinear branches are explicitly excluded (L60, L151, L237).
3. **Non-Attainment of Dynamical Sharpness**:
   - The sharpness of the $\sqrt{\eta/\gamma}$ exponent is rigorously scoped solely to the **recovery-to-source-compression step** (Abstract L34, Section 5 L205–206, `README.md` L266).
   - Section 5 (L231–233) explicitly demonstrates that the counterexample construction violates the native invariance hypothesis because $J$ maps code states into detector-excited states outside the code space.
   - The manuscript explicitly disclaims tightness of the dynamical bound, optimality of the constant 22, or demonstration of a working protected amplifier (L232–233).
4. **No Unrestricted No-Go or BPP/BQP Claims**:
   - The manuscript, `README.md` (L279–280), `CLAIMS.md` (L303), and `.zenodo.json` (L335) disclaim any unrestricted nonlinear computing impossibility theorem or complexity-class progress.
   - Section 6 (L238) states: "Ordinary BPP versus BQP is unchanged."
5. **Review and Publication Status**:
   - Front matter (L30), `README.md` (L257, L281), `CITATION.cff` (L343), and `.zenodo.json` (L334) clearly mark the document as an uncertified preparation-stage research candidate 0.1.0.
   - No external release, DOI assignment, human peer review claim, or Lean formalization is asserted.
   - `README.md` explicitly bars PaperMill handoff until the completion of the three-lens review process.

---

## 4. Audit of Final Recheck Corrections

The revised text successfully incorporates the required corrections identified in prior rounds:
- **Multi-Pair Summation (Eq. 154–158, Theorem 3)**: The native nonlinear generator is explicitly written as a sum of discrete pairs $\sum_k H_{\mathrm{nl}, k}$. Each pair is required to separately satisfy its own damping test with measurable parameters $\gamma_k, \eta_k$. The bound in Theorem 3 sums the pair-specific norms, relying only on the triangle inequality without demanding mutual commutation between pairs.
- **Boundary Isometries and Record Retention (L150–152)**: Intermediate boundaries between native intervals are explicitly defined as input-independent Stinespring isometries that retain all environmental ancillae and measurement records through all subsequent native intervals. Native operations act trivially on retained records; classical feed-forward is modeled as coherent control on these records. Only final readout may trace out registers.
- **Trajectory Regularity & Well-Posedness (L149, L180–182)**: Trajectories are hypothesized as absolutely continuous solutions on finite unions of compact intervals. As noted in the final recheck instruction, the text does **not** assert global Lipschitz continuity of the generator; instead, lines 180–182 demonstrate continuity of the nonlinear vector contribution at $p=0$ (bounding terms by $|g|\sqrt{p}$) and condition the theorem on the existence of solutions.

---

## 5. Attempted Falsifiers

| Falsifier Probe | Audit Target | Mechanism / Stress Test | Result |
|---|---|---|---|
| **F1: Universal No-Go Smuggling** | Section 1, Section 4, Section 6, `CLAIMS.md` | Check if the operational distinguishability bound is portrayed as a universal barrier to nonlinear quantum computing. | **Refuted.** The bound is explicitly conditional on trajectories remaining confined to a common $C^1$ moving code $V(t)$. Unprotected excursions, non-Markovian noise, and alternative architectures are explicitly stated as unconstrained. |
| **F2: Attribution Laundering of Channel Duality** | Section 2 (eqs. 77–81), `SOURCES.md` (item 1) | Check if the constant complementary state guarantee is claimed as a new theorem. | **Refuted.** Directly attributed to Bény & Oreshkov (2010), Theorem 1 / eq. (3). The candidate claims only the application to the native-off two-qubit damping benchmark. |
| **F3: Dynamical Sharpness Overclaim** | Abstract (L34), Section 5 (L205–233) | Check whether the finite dephasing code is claimed to saturate the whole-trajectory gain bound. | **Refuted.** Section 5 explicitly points out that the construction leaks out of the code under $J$, disproving invariant dynamical attainment and explicitly stating that neither the exponent nor the constant 22 is proved tight. |
| **F4: Implicit Well-Posedness Assumption** | Section 4 (L149, L172–186) | Check if Picard-Lindelöf existence/uniqueness is falsely asserted for the non-Lipschitz $\sqrt{p}$ field. | **Refuted.** Theorem 3 assumes solutions exist and remain in the code. Lines 180–182 prove only continuity of the vector field at $p=0$ and explicitly avoid claiming a general well-posedness theorem. |
| **F5: Ancilla & Syndrome Information Leak** | Section 4 (L151–152), Section 5 (L215–216) | Check whether syndrome measurement or reset could secretly discard distinguishability before final readout. | **Refuted.** The model explicitly mandates that all Stinespring environments and syndrome flags remain coherent and unread until the terminal readout. |

---

## 6. Severity-Tagged Findings

### Findings Summary
- **[CRITICAL]**: None.
- **[MAJOR]**: None.
- **[MINOR]**: None.
- **[NOTE] Title Parity between Files**:
  - `manuscript/main.tex`, `.zenodo.json`, and `CITATION.cff` use:  
    `Operational recovery bounds for an expectation-dependent quantum amplifier`
  - `README.md` uses:  
    `Operational recovery bounds for a nonlinear amplifier`  
  *Recommendation*: When synchronizing files for archival readiness, harmonize the README header with the formal manuscript title. This does not affect technical validity or attribution boundaries.
- **[NOTE] Constant Factor 22 (Theorem 3)**:
  - From line 191: $e_P + e_J \le (8 + 2\sqrt{2})\sqrt{r} < 10.8284\sqrt{r} < 11\sqrt{r}$. Multiplied by the factor 2 from the triangle inequality (L164), this yields $22\sqrt{r}$. The text explicitly acknowledges that the constant 22 is an unoptimized upper bound (L233).

---

## 7. Disposition

### **Verdict: GO-WITH-NOTES**

**Disposition Rationale**:
The manuscript candidate (`0.1.0`) strictly respects all non-claims, attribution, and operational boundaries:
1. It accurately cites and demarcates imported theorems (Bény–Oreshkov, Zhou et al., Watrous) from its specific finite-damping application.
2. It scrupulously confines all dynamical conclusions to the common invariant-code premise, avoiding any overreach into general physical implementations, unrestricted fault-tolerance impossibility, or BPP/BQP progress.
3. It limits sharpness claims strictly to the recovery-to-source-compression conversion, explicitly demonstrating why its scaling witness does not achieve dynamical saturation.
4. All multi-pair, Stinespring boundary, and trajectory regularity hypotheses are explicitly formulated and mathematically consistent.
5. All metadata, README, and provenance files reflect the candidate's preliminary preparation status without premature registration or publication claims.
