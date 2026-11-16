**Verdict: GO-WITH-NOTES.** The recomputed recovery scale, caps, constant 22, and constant 1/264 all hold. No essential correction. The scaling witness supports only square-root sharpness of recovery-to-source compression.

Source SHA-256: `0891e8571c5904555500aed76a8c7814e0835061319bf4243afbe38135c04f58`

The 46-assertion diagnostic was not re-executed. It is treated only as the packet’s stated finite Kraus/code check, not as evidence for duality or the trajectory bound.

## Recomputation

**Fidelity scale.** With root fidelity at least \(\sqrt{1-\eta}\), Uhlmann gives purifications at distance \(b(\eta)=\sqrt{2(1-\sqrt{1-\eta})}\). The inequality \(1-\sqrt{1-\eta}\le\eta\) gives \(b\le\sqrt{2\eta}\) and \(b^2\le 2\eta\). Lemma 1’s estimate \(|\operatorname{tr} O(\rho-\sigma)|\le 2b\sqrt{w}+b^2\) matches the Cauchy–Schwarz expansion. As \(\eta\to 0\), \(b\sim\sqrt{\eta}\).

**Pullbacks.** For \(K_{ij}=A_i\otimes A_j\) and this environment labeling, \(\widehat{\mathcal N}^*(|a\rangle\langle b|)=K_a^\dagger K_b\). Then \(\widehat{\mathcal N}_V^*(\Pi_S)=\gamma V^\dagger N_S V\) and \(\widehat{\mathcal N}_V^*(T)=\gamma V^\dagger J V\), including \(\gamma=1\). The single-jump operator is \(\gamma V^\dagger(N_S+N_B-2\gamma N_S N_B)V\), with eigenvalues \(0,\gamma,\gamma,2\gamma(1-\gamma)\), hence probability at most \(2\gamma\). Source-jump probability is at most \(\gamma\). Both are dimension-free and tensor the spectator identity.

**Caps.** Dividing by \(\gamma\) produces the algebraic branches \(2b/\sqrt{\gamma}+b^2/\gamma\) and \(2\sqrt{2}\,b/\sqrt{\gamma}+b^2/\gamma\). Spectra of \(V^\dagger PV\in[0,1]\) and \(V^\dagger JV\in[-1,1]\) give midpoint caps \(1/2\) and \(1\). The same midpoint meets both the algebraic bound and the cap. At \(\eta=0\) and \(\gamma>0\) both defects are zero. As \(\gamma\to 0\) with \(\eta\) fixed, the algebraic branches diverge and the caps are the stated bounds.

**Residual.** \(|j|\le 2\sqrt{p(1-p)}\) is saturated by superpositions of \(|ge\rangle\) and \(|eg\rangle\). With \(\|E_P\|\le e_P\) and \(\|E_J\|\le e_J\),
\[
\|R_\Psi\|\le |g|\bigl(\sqrt{p}\,e_J+\sqrt{1-p}\,e_P\bigr)\le |g|(e_P+e_J).
\]
The gradient factor \(1/(2\sqrt{p})\) cancels the \(2\) in \(|j|\). Also \(\|(P-pI)\Psi\|=\sqrt{p(1-p)}\), so each nonlinear term in \(H(\Psi)\Psi\) is \(O(|g|\sqrt{p})\) and the zero extension at \(p=0\) is the continuous limit. Trace distance to the common ordinary (plus frame) evolution grows at rate at most \(\|R\|\); two trajectories give the factor \(2\) in (eq:gain). Common channels and retained dilations do not increase that distance. Simultaneous residuals add by the triangle inequality.

**Constant 22.** For \(r\ge\eta/\gamma\) and \(r\le 1\), dropping caps,
\[
e_P+e_J\le(4+2\sqrt{2})\sqrt{r}+4r\le(8+2\sqrt{2})\sqrt{r}.
\]
Here \(8+2\sqrt{2}\approx 10.828<11\), so \(2(e_P+e_J)<22\sqrt{r}\). Thus \(D_{\rm out}\le\min\{1,d_0+22A\sqrt{r}\}\). The chain actually yields \(16+4\sqrt{2}\approx 21.657\) before rounding up to 22.

**Constant 1/264.** Equal priors give success probability \(\tfrac12(1+D)\). Success at least \(2/3\) forces \(D\ge 1/3\). If \(d_0\le 1/4\), then \(\tfrac13-\tfrac14=\tfrac1{12}\) and \(\tfrac1{12}/22=\tfrac1{264}\).

**Witness.** For (eq:code), \(\inf_c\|V^\dagger PV-cI\|=d\) and \(V^\dagger JV=0\). The four no-jump and source-jump vectors are orthogonal, and the decoder multiplies logical coherences by
\[
\lambda=\sqrt{(1-\gamma a)^2-\gamma^2 d^2}+\gamma\sqrt{a^2-d^2}.
\]
Populations are preserved, so this is phase flip with \(\eta_{\rm rec}=(1-\lambda)/2\). Entanglement fidelity is \(1-\eta_{\rm rec}+\eta_{\rm rec}(\operatorname{tr}\rho Z)^2\), with worst case \(\eta_{\rm rec}\). The expansion is exactly
\[
\eta_{\rm rec}=\frac{\gamma d^2}{4a(1-\gamma a)}+O(d^4)
\]
at fixed \(a,\gamma\). Hence \(d\sim 2\sqrt{a(1-\gamma a)}\,\sqrt{\eta/\gamma}\). Any universal \(o(\sqrt{\eta/\gamma})\) compression bound fails on this family. Optimal recovery error is at most the achieved error, so the same ratio is at least as large. A sample point \(a=1/2\), \(d=1/10\), \(\gamma=1/5\) gives \(\eta_{\rm rec}\approx 0.001122\) against the leading term \(0.001111\), and defect \(0.1\) under algebraic \(e_P\approx 0.155\).

\(J\) sends the excited-source leg to a detector-excited vector outside the code, so (eq:code) does not meet Theorem 3’s invariance hypothesis.

## Attempted falsifiers

| Probe | Result |
|---|---|
| \(\gamma\to 0\), \(\eta\) fixed | Division by \(\gamma\) diverges; published caps \(1/2\) and \(1\) hold. No \(\gamma=0\) claim after division. |
| \(\eta\to 0\), \(\gamma>0\) | Both compressions become scalar; gain integrand vanishes. |
| \(1/\sqrt{p}\) residue | Cancelled by \(\|j\|\le 2\sqrt{p(1-p)}\). Vector field extends continuously by zero. |
| Spectators | Kraus identities tensor by \(I\); no dimension factor in \(e_P\), \(e_J\), or \(22\). |
| Moving \(V(t)\) | Frame connection is a common ordinary generator under the stated hypothesis. |
| Channel boundaries | Common CPTP maps and retained dilations do not increase \(D\); interval gains add. |
| Optimal vs achieved \(\eta\) | \(\eta_\star\le\eta_{\rm rec}\) preserves the anti-little-o statement. |
| Numerical plug-in of (eq:code) | Lies under the Theorem 2 cap and matches (eq:scaling). |
| Constant 22 overrun | Capped and uncapped corners tried stay at or below \(16+4\sqrt{2}<22\). |

## Costs

The only quantity given a numerical lower bound is summed native coupling-time \(A\) in (eq:cost), and only for equal-prior success \(2/3\), \(d_0\le 1/4\), \(r\le 1\), and a common invariant moving code whose native-off damping benchmark meets \(\eta/\gamma\le r\).

Encoding, recovery implementation, native synthesis, control accuracy, classical construction, and SDP search for \(V\), \(\mathcal R\), or \(\sigma\) are uncharged. The text states that, and the proofs do not insert those costs. Ordinary controls and the frame connection are likewise uncharged because they are common. Retained dilation records are uncharged; the bounds have no dimension penalty that would price them.

No hidden simultaneous-noise premise was found. Theorem 3 integrates clean native evolution inside a code that passes a native-off damping test. Section 1, the theorem preamble, the abstract, and the limitations paragraph all say that this is not a simultaneous noisy nonlinear flow. Correction-cycle time and an \(\eta(\Delta t)\) budget are also outside the bound; the damping-normalization paragraph says absolute recovery error going to zero does not by itself suppress the amplifier.

Repetition does not evade (eq:cost): parallel pairs add into \(A\), and a global output state is still trace-distance bounded by total \(A\).

## Findings

**Essential corrections.** None. The duality specialization is used only as an existence statement for one constant complement; \(\eta=0\), the Kraus identities, the caps, the \(p\)-uniform residual, the factor \(22\), the factor \(1/264\), and the Taylor coefficient all agree with the displayed equations.

**Optional exposition.**

1. Section 4 chain to (eq:simple). The proved pre-rounding coefficient is \(16+4\sqrt{2}\approx 21.657\), not a sharp \(22\). Further slack comes from \(b\le\sqrt{2\eta}\) (leading \(b\sim\sqrt{\eta}\)), \(4r\le 4\sqrt{r}\), \(\sqrt{p}\,e_J+\sqrt{1-p}\,e_P\le\sqrt{e_P^2+e_J^2}\), the factor-two trajectory split, \(w=2\gamma\), and dropped caps. For \(r\) near \(1\), the capped form \(2(e_P+e_J)\le 3\) is the operative estimate. The pair \(22\) and \(1/264\) is internally consistent. This does not affect correctness.
2. Equation (1). \(N_B\) is used as detector excitation but has no ket definition beside \(N_S=I-P\). The single-jump identity matches \(N_B=I_S\otimes|e\rangle\langle e|_B\).
3. Section 2, diamond remark. \(\tfrac12\|\mathcal{RN}_V-\mathrm{id}\|_\diamond\le\eta\) forces purified overlap to drop by at most \(\eta^2\), which is enough for (eq:recovery). The printed phrase “at most \(\eta\)” is the weaker true statement.
4. Section 5. The displayed formula \(1-\eta_{\rm rec}+\eta_{\rm rec}(\operatorname{tr}\rho Z)^2\) is the entanglement fidelity, equal to the square of root fidelity. “Squared entanglement fidelity” is easy to misread as the square of that quantity. The worst-case identification \(\eta=\eta_{\rm rec}\) still matches (eq:recovery).
5. Theorem 3 proof. Continuity at \(p=0\) is shown; Lipschitz continuity of the vector field is not. The gain statement assumes given trajectories, so the integral bound does not require a new existence proof.

**Confirmed scope, not a defect.** Section 5 shows only that the recovery-to-source-compression exponent \(\sqrt{\eta/\gamma}\) cannot be replaced by a universal little-o. In the example the exchange compression is exactly zero, and the code is not native-invariant. Constant \(22\), constant \(1/264\), and the dynamical exponent stay unwitnessed, as the manuscript states.

This is an independent analytic check of the supplied packet. It is not human peer review, kernel acceptance, or a novelty clearance.
