# Operational recovery bounds for an expectation-dependent quantum amplifier

Research manuscript candidate 0.1.0, 2026-11-16. Daniel Fredriksen, Quantyra Inc., ORCID 0009-0002-9123-7435. **Not published or formally certified. Separate Claude/Grok/AGY three-lens AI review is complete with all essential findings resolved; see the source-bound reports below.** Scientific/preparation owner: Quantum S291.

The earlier protected-source bound used operator-compression defects without relating them to an operational recovery guarantee. This candidate closes that connection for finite amplitude damping. Standard channel-fidelity duality plus a rare-event estimate gives dimension-independent source/exchange bounds in terms of the recovery infidelity divided by damping strength. For the stated common-invariant-moving-code class,

\[
D_{\mathrm{out}}\leq\min\{1,d_0+22A\sqrt r\},
\qquad r\geq\sup_{k,t}\eta_k(t)/\gamma_k(t),\quad r\leq1,
\]

where A is summed native coupling-time, and every active pair separately satisfies its damping recovery test. All record environments are retained until final ordinary readout. The complete coefficient-derivative term of the hypothetical nonlinear primitive is retained. A finite code and recovery show the square-root exponent is necessary for the **recovery-to-source-compression step**. They do not attain the dynamical bound or implement a protected amplifier.

- [Manuscript PDF](manuscript/main.pdf) / [LaTeX](manuscript/main.tex).
- [Claims and limitations](CLAIMS.md), [primary-source transfers and novelty assessment](SOURCES.md).
- [Three-lens review and dispositions](reviews/three-lens-2026-11-16/DISPOSITION.md), [exact review summary](reviews/REVIEW-SUMMARY.json).
- [Full certification plan](formal/CERTIFICATION-PLAN.md): actual channel/fidelity and trajectory dependencies must be costed before any proof job.
- [Historical evidence and provenance](evidence/provenance.json).
- [Exact diagnostic](verification/exact-check.json) and [child-process receipt](verification/exact-process.json): one run, 46 assertions, exit 0, maximum dimension 16, four rational damping choices including a zero-damping control.
- [Build receipt](verification/build.json). Rendering requires Python 3.13.7, PyMuPDF 1.28.2 and Tectonic 0.17.0; the diagnostic uses only the Python standard library.

```text
python -B tools/run_exact.py
python -B tools/build.py --tectonic /path/to/tectonic --render
```

Preserve the frozen receipts before reproducing; those commands replace current local receipts. Full primary-source snapshots are ignored and not redistributed. The manuscript's analytic statements do not follow from a finite diagnostic. No optimal recovery algorithm, code-discovery cost, physical noise budget, native synthesis or arbitrarily fast correction is provided. The common invariant code and finite damping benchmark are essential hypotheses; no general fault-tolerance impossibility or ordinary BPP/BQP result is claimed.

Publication significance/priority remain under review. Channel fidelity duality and the signal/noise-span principle are attributed prior results, not discoveries claimed here. The completed candidate is prepared for PaperMill P013/S026 intake; the canonical planning record determines queue status. The manuscript is a scoped technical application, not a claim of a new general error-correction principle. Remaining work: admitted full dependency/cost audit and certification, and a separate publication/significance decision. No public release, DOI or Lean job is authorized by preparation.
