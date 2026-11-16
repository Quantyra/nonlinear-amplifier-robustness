### Independent AI Manuscript Review: Non-Claims and Attribution Lens

**Source SHA-256:** `1f0219515ba8af76fcc077ac2c145aba5b06aea3b4a4494b96fcc3748fe5a419`  
**Review Target:** `manuscript/main.tex`, `README.md`, `CLAIMS.md`, `SOURCES.md`, `.zenodo.json`, `CITATION.cff`  
**Review Lens:** Non-claims, provenance, attribution hygiene, and scope boundary audit  

---

### Executive Summary & Technical Contribution Assessment

The candidate manuscript, *"Operational recovery bounds for an expectation-dependent quantum amplifier"* (v0.1.0, 2026-11-16), is evaluated under the non-claims and attribution lens.

**Is the candidate a coherent scoped technical contribution, or only a restatement?**  
The work is a **coherent, rigorously scoped technical contribution**, distinct from a mere restatement of imported theorems:
1. **Separation from Imported QEC Duality:** The manuscript imports the channel-fidelity duality of Béni & Oreshkov (PRL 2010, arXiv:0907.5391v4) for *ordinary* quantum channels. It does not attempt to assert duality for nonlinear channels; rather, it benchmarks the code against an ordinary native-off finite amplitude-damping channel.
2. **Separation from Linear Metrology:** The connection between noise-operator spans and signal preservation is established prior art in linear metrology (Zhou et al., *Nature Comm.* 2018; Zhou & Jiang, *PRR* 2020). The candidate explicitly disclaims novelty for this organizing principle and avoids importing linear quantum Fisher information (QFI) sufficiency into nonlinear computation.
3. **The Novel Analytical Bridge:** The technical advance consists of:
   - Calculating the exact pullbacks of finite two-qubit amplitude-damping Kraus operators onto the complementary environment to isolate source population $P$ and exchange $J$ (Eqs. 120–121).
   - Formulating a rare-event observable estimate (Lemma 1) that exploits the $O(\gamma)$ event mass of environmental jumps to secure an $O(\sqrt{\eta/\gamma} + \eta/\gamma)$ scaling, bypassing the dimension-dependent or $O(\sqrt{\eta}/\gamma)$ loss of a plain trace-distance estimate.
   - Integrating the full non-Lipschitz, expectation-dependent generator (including the homogeneous functional gradient term $\frac{gj}{2\sqrt{p}}(P-pI)$) along trajectories confined to a common invariant moving code, rigorously proving that $|j| \le 2\sqrt{p(1-p)}$ bounds the residual operator norm by $|g|(e_P + e_J)$ uniformly down to $p \to 0$ without dividing by a lower bound on $p$.
   - Constructing a finite code and isometric decoder (Section 5) demonstrating that the square-root exponent $\sqrt{\eta/\gamma}$ in the recovery-to-source-compression bound is necessary.

---

### Scope & Attribution Audit

1. **Title, Abstract, and Metadata Consistency:**
   - The title is identical across `main.tex` [L30](file:///[local-path-redacted]), `README.md` [L259](file:///[local-path-redacted]), `.zenodo.json` [L336](file:///[local-path-redacted]), and `CITATION.cff` [L349](file:///[local-path-redacted]).
   - The abstract explicitly disclaims dynamical sharpness, physical implementation, unrestricted excursions, and restricted-state recovery, accurately characterizing the manuscript as an application of approximate QEC to the specified nonlinear model.
   - Author metadata, ORCID (`0009-0002-9123-7435`), affiliation (`Quantyra Inc.`), candidate version (`0.1.0`), and CC-BY-4.0 license are harmonized.

2. **Strict Common Invariant-Code Premise:**
   - Confined strictly to clean trajectories lying in the range of a common $C^1$ moving isometry $V(t)$ [L61-63, L151](file:///[local-path-redacted]).
   - The text explicitly notes that this hypothesis is stronger than what an arbitrary nonlinear computer might require, and that it does not model arbitrary simultaneous noisy nonlinear flow [L62-63](file:///[local-path-redacted]).

3. **Hypothetical Primitive & Physical Realization:**
   - The native interaction is consistently described as a hypothetical primitive [L35, L60, L270, L295](file:///[local-path-redacted]).
   - Disclaimers confirm that no physical realization, causal completion, or operational apparatus is provided [L60, L241, L283, L307](file:///[local-path-redacted]).

4. **Non-Attainment of Dynamical Sharpness:**
   - Section 5 explicitly demarcates the scope of the scaling example: it applies strictly to the *recovery-to-compression* step ($d \sim \sqrt{\eta/\gamma}$), not to the dynamical distinguishability gain [L209, L236-237](file:///[local-path-redacted]).
   - The text explicitly highlights that the example violates the native invariance premise because $J$ maps code states into detector-excited states outside the code [L236-237](file:///[local-path-redacted]). Neither constant 22 nor the dynamical exponent is claimed to be sharp.

5. **No Unrestricted No-Go or BPP/BQP Progress:**
   - The bounds lower-bound only the summed native coupling-time $A$ for this specific common-invariant trajectory class.
   - Section 6 explicitly disclaims any unrestricted fault-tolerance impossibility, physical noise budgeting, or progress on ordinary BPP versus BQP [L241-242, L283, L307](file:///[local-path-redacted]).

6. **Publication, Review, and Certification Status:**
   - Clearly labeled as "Manuscript candidate 0.1.0; not formally certified" [L32, L261, L347](file:///[local-path-redacted]).
   - No claim of human peer review, formal kernel (Lean) verification, or archival publication is made.
   - Explicit acknowledgments describe the assistance of OpenAI Codex and the multi-lens AI review process [L245](file:///[local-path-redacted]).
   - `README.md` confirms that no PaperMill registration, DOI, public release, or Lean job is authorized [L261, L285](file:///[local-path-redacted]).

---

### Attempted Falsifiers

1. **Attempted Falsifier 1 (Conflation of Imported Approximate QEC Duality):**
   - *Test:* Did the manuscript claim the channel-fidelity duality theorem as its own discovery or apply it directly to a non-linear channel where Stinespring dilations fail?
   - *Outcome:* **Falsified / Clear.** Bény & Oreshkov (Theorem 1 / Eq. 3) is cited with exact attribution in Section 2 [L79-82](file:///[local-path-redacted]), listed as imported claim I1 in `CLAIMS.md` [L296](file:///[local-path-redacted]), and detailed in `SOURCES.md` [L315](file:///[local-path-redacted]). It is applied strictly to the linear, ordinary amplitude-damping channel $\mathcal{N}_V$ with native nonlinear evolution turned off.

2. **Attempted Falsifier 2 (Appropriation of Metrology Organizing Principles):**
   - *Test:* Does the manuscript claim the noise-span / signal-commutation criteria from quantum metrology as novel, or treat linear QFI sufficiency as proof of nonlinear protection?
   - *Outcome:* **Falsified / Clear.** Section 1 [L40-42](file:///[local-path-redacted]) and `SOURCES.md` [L317-319](file:///[local-path-redacted]) explicitly state that the organizing principle of signal/noise spans originates in prior linear metrology work (Zhou et al., 2018; Zhou & Jiang, 2020), and explicitly disclaims importing linear metrology theorems as nonlinear sufficiency.

3. **Attempted Falsifier 3 (Overclaiming Lower-Bound Witness as Dynamical Sharpness):**
   - *Test:* Does the Section 5 finite code construction claim that the dynamical bound $D_{\rm out} \le d_0 + 22 A \sqrt{r}$ is sharp or that the constant 22 is tight?
   - *Outcome:* **Falsified / Clear.** Section 5 explicitly restricts the sharpness conclusion to the recovery-to-compression step [L209, L236-237](file:///[local-path-redacted]), openly admitting that the code does not preserve native invariance under $J$.

4. **Attempted Falsifier 4 (Vanishing Population Singularity & Well-Posedness):**
   - *Test:* Does the $1/\sqrt{p}$ term in the gradient functional lead to singular blowup or a hidden assumption of global Lipschitz continuity?
   - *Outcome:* **Falsified / Clear.** The proof of Theorem 3 [L180-186](file:///[local-path-redacted]) proves that because $P J P = (I-P) J (I-P) = 0$, the expectation value satisfies $|j| \le 2\sqrt{p(1-p)}$. Consequently, the coefficient $\frac{gj}{2\sqrt{p}}$ is bounded by $|g|\sqrt{1-p} \le |g|$, and the residual norm satisfies $\|R_\Psi\| \le |g|(e_P + e_J)$ uniformly for all $p > 0$. At $p=0$, the nonlinear vector field is defined as 0, which is continuous since both $\|g\sqrt{p}J\Psi\| \le |g|\sqrt{p}$ and $\|\frac{gj}{2\sqrt{p}}(P-pI)\Psi\| \le |g|\sqrt{p}$. The manuscript correctly avoids claiming global Lipschitz continuity or general well-posedness, conditioning the result on the existence of absolutely continuous solutions.

5. **Attempted Falsifier 5 (Status and Provenance Integrity):**
   - *Test:* Are historical S282–S288 notes silently bundled as newly proven theorems, or is archival acceptance implied?
   - *Outcome:* **Falsified / Clear.** Provenance is documented in `README.md` [L274, L283-285](file:///[local-path-redacted]), `CLAIMS.md` [L307-308](file:///[local-path-redacted]), and `SOURCES.md` [L330-332](file:///[local-path-redacted]). Pre-existing results are separated from S291's operational bridge.

---

### Severity-Tagged Findings

*No fatal, high, or medium severity defects were found. The manuscript exhibits exemplary attribution and non-claims hygiene. Three minor informational notes are recorded for completeness:*

- **Finding 1 (Severity: NOTE / Informational): Explicit Moving-Frame Connection in Section 4**  
  *Location:* `manuscript/main.tex` [L176-177](file:///[local-path-redacted])  
  *Detail:* The proof mentions that the ordinary part of the logical generator includes the common moving-frame connection $-i V^\dagger \dot{V}$. Because $V(t)$ is assumed to be an input-independent $C^1$ isometry common to both clean trajectories, this geometric connection is identical for both paths and cancels in the trace-distance variation-of-constants comparison. While mathematically standard, explicitly emphasizing that the connection is purely input-independent underscores the common-invariant-code framing.

- **Finding 2 (Severity: NOTE / Informational): Pre-print Metadata Taxonomy in `.zenodo.json`**  
  *Location:* `.zenodo.json` [L337-339](file:///[local-path-redacted])  
  *Detail:* `.zenodo.json` specifies `"publication_type": "preprint"`, which is Zenodo's schema vocabulary for unrefereed candidate uploads. The description field immediately clarifies that this is a "Preparation-stage candidate... No physical realization, unrestricted impossibility theorem, BPP/BQP result or formal certification is claimed." This conforms to open-science metadata requirements while avoiding any misrepresentation of formal peer review.

- **Finding 3 (Severity: NOTE / Informational): Scoping of Scaling Exponent Witness**  
  *Location:* `manuscript/main.tex` [L209, L236-237](file:///[local-path-redacted])  
  *Detail:* The text in Section 5 appropriately emphasizes that the code construction bounds the recovery-to-source-compression step and does not satisfy the native-invariance condition of Theorem 3. This distinction is vital to prevent casual readers from misconstruing the square-root exponent as a tight bound on all nonlinear amplification dynamics. The manuscript's framing is clear and non-misleading.

---

### Final Disposition

**Verdict: GO-WITH-NOTES**

**Disposition Summary:**  
The candidate manuscript passes the Non-Claims and Attribution lens without required mathematical or attribution revisions. All imported results (Bény–Oreshkov channel duality, linear metrology error-operator principles, Watrous fidelity bounds, Childs–Young baseline) are cited with precision. The new technical contribution—converting operational finite-damping error to source/exchange compression defects without dimensional loss, integrating the gradient functional, and establishing the necessity of the square-root recovery-to-compression exponent—is clearly delimited. All negative constraints, hypothetical model scopes, moving-code assumptions, and non-certification disclaimers are preserved across the manuscript and metadata. No PaperMill registration or public release is warranted until the companion lenses complete their disposition.
