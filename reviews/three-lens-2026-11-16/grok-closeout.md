Source SHA-256: `1f0219515ba8af76fcc077ac2c145aba5b06aea3b4a4494b96fcc3748fe5a419`

Verdict: **GO-WITH-NOTES**. The eta/gamma scale, spectral caps, trajectory factor 22, and discrimination threshold 1/264 all recompute correctly. No essential residual defect under this quantitative/resource lens.

### Recomputation
Rare-event scale in Lemma 1: \(b(\eta)=\sqrt{2(1-\sqrt{1-\eta})}\leq\sqrt{2\eta}\) because \(1-\sqrt{1-\eta}\leq\eta\). With \(\lVert O\rVert\leq 1\) and \(O=\Pi O\Pi\), the purified estimate is \(|\operatorname{tr} O(\rho-\sigma)|\leq b(2\sqrt{w}+b)\).

Kraus adjoints match (3): \(\widehat{\mathcal N}^*( \Pi_S)=\gamma N_S\) and \(\widehat{\mathcal N}^*(T)=\gamma J\), including \(\gamma=1\). Single-jump mass is at most \(2\gamma\); source-jump mass is at most \(\gamma\).

Theorem 2 then gives
\[
e_P=\min\Bigl\{\tfrac12,\ \frac{2b}{\sqrt\gamma}+\frac{b^2}{\gamma}\Bigr\},\qquad
e_J=\min\Bigl\{1,\ \frac{2\sqrt2\,b}{\sqrt\gamma}+\frac{b^2}{\gamma}\Bigr\}.
\]
Dividing the \(\Pi_S\) bound by \(\gamma\) produces the \(e_P\) rare-event term. Dividing the \(T\) bound on \(\Pi_1\) (\(w=2\gamma\)) produces the \(e_J\) term. Midpoint scalars convert a uniform expectation window into an operator-norm bound; the caps are the half-widths of \([0,1]\) and \([-1,1]\).

Generator residual (4): \(|j|\leq 2\sqrt{p(1-p)}\) because \(J\) is off-diagonal across \(P\), so
\[
\lVert R_\Psi\rVert\leq |g|\bigl(\sqrt p\, e_J+\sqrt{1-p}\, e_P\bigr)\leq |g|(e_P+e_J)\leq\tfrac32|g|.
\]
The \(1/\sqrt p\) coefficient stays bounded. The state-vector nonlinear piece is \(O(|g|\sqrt p)\) and the \(p=0\) extension keeps \(\omega N\). A state-dependent multiple of the identity does not affect the density-operator derivative. Each clean trajectory drifts from the common ordinary-plus-frame evolution by at most \(\int |g|(e_P+e_J)\,dt\); the triangle inequality supplies the leading 2. Input-independent boundary isometries preserve trace distance, and the final readout contracts it.

Uniform ratio \(r\leq 1\): dropping caps,
\[
e_P+e_J\leq(4+2\sqrt2)\sqrt r+4r\leq(8+2\sqrt2)\sqrt r<11\sqrt r,
\]
since \(4r\leq 4\sqrt r\). Twice that coefficient is the stated 22. For equal priors, success at least \(2/3\) needs \(D_{\mathrm{out}}\geq 1/3\). With \(d_0\leq 1/4\),
\[
\tfrac13-\tfrac14=\tfrac1{12},\qquad \frac{1/12}{22}=\frac1{264}.
\]

Section 5: the code defect is exactly \(d\). The decoder multiplier is the stated \(\lambda\), and \(\eta_{\mathrm{rec}}=(1-\lambda)/2\). The expansion
\[
\eta_{\mathrm{rec}}=\frac{\gamma d^2}{4a(1-\gamma a)}+O(d^4)
\]
holds for fixed \(a\in(0,1)\) and \(\gamma\in(0,1]\). Thus \(d/\sqrt{\eta/\gamma}\) tends to the positive constant \(2\sqrt{a(1-\gamma a)}\). An optimal recovery, having infidelity no larger than this decoder, leaves that ratio at least as large. \(J\) annihilates the code, so the witness is a source-compression witness. The manuscript limits the sharpness claim to that step.

### Essential findings
None. Prior gaps called out in the closeout (multi-pair generator, record-retaining boundaries, regularity, \(p=0\) extension, purification phase, coupling-time versus duration, sharpness scope) are present in this source with the quantifiers used above.

### Attempted falsifiers
- \(\gamma\to 0\) with \(\eta\) fixed: rare-event terms diverge and the minima saturate at the trivial caps \(1/2\) and \(1\). The ratio form is the non-trivial statement.
- \(\eta\to 0\): both compressed operators become scalar, including the \(w=0\) case inside Lemma 1.
- Spectators and references: damping and \(P,J\) act as the identity off \(SB\); fidelity is monotone under the partial trace over the reference, so a reduced environment state remains at least \(\sqrt{1-\eta}\) from \(\sigma\). The norm bounds do not grow with dimension.
- Moving \(C^1\) codes: the frame connection and \(\omega V^\dagger NV\) are common ordinary generators. Only non-scalar \(E_P,E_J\) remain in \(R_\Psi\).
- Interval boundaries: fresh Stinespring environments enlarge the space isometrically; trace distance is preserved until the final discard.
- Simultaneous pairs: residuals add by the triangle inequality without a commutation hypothesis. Each pair is a separate native-off damping test.
- Optimal versus achieved recovery: a smaller optimal \(\eta\) makes \(d=o(\sqrt{\eta/\gamma})\) harder, not easier.
- Coefficient check on \(e_P\): this family can push \(d/\sqrt{\eta/\gamma}\) arbitrarily close to the leading coefficient 2 (small \(\gamma\), \(a\to 1\)). That saturates the rare-event leading term and does not break it.
- Discrimination arithmetic: equality \(A\sqrt r=1/264\) produces the endpoint \(D_{\mathrm{out}}\leq 1/3\), so the stated necessary condition is the closed bound.

### Costs and premises
The charged resource in (4) and the display after Theorem 3 is summed native coupling-time \(A=\int\sum_k|g_k|\,dt\). Encoding, recovery, synthesis, control accuracy, classical construction, and code discovery are stated additional requirements. Finding \(\sigma\) is existence only. The recovery hypothesis is a native-off ordinary channel on the common code; the gain statement then integrates the clean generator on absolutely continuous solutions that remain in that code. Correction-cycle time and \(\eta(\Delta t)\) are explicitly not derived.

### Optional exposition (not corrections)
The integer 22 is a convenient upper bound on \(2(8+2\sqrt 2)\approx 21.66\). For small \(r\) the \(4r\leq 4\sqrt r\) step is the main slack; the caps bind only when \(r\) is not small. A tighter universal prefactor is optional. The fixed diagnostic, as described, checks Kraus, source, code, and syndrome substitutions on rational points, including a zero-damping control. It does not carry the duality step or the trajectory integral. No new sharpness, Lipschitz, or well-posedness theorem is needed for the claims as quantified.
