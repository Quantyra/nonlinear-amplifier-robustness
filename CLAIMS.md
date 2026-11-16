# Candidate claim and obligation map

All entries refer to the frozen `manuscript/main.tex` and build receipt. Written arguments and separate Claude/Grok/AGY AI review with dispositions exist; no human peer review or formal coverage is claimed.

| ID | Statement / quantitative output | Required structure and limits | Location |
|---|---|---|---|
| D1 | Full nonlinear generator, normalized homogeneous functional and zero-population extension | P source projector; exchange J off-diagonal relative to P; complete pure state including records; hypothetical native operation | Section 1 |
| I1 | Worst-case channel root-fidelity duality supplies a single constant complementary output with root fidelity >=sqrt(1-eta) | **Imported** Beny--Oreshkov Theorem 1; finite encoded noise channel, identity target, arbitrary ordinary recovery; eta is squared-fidelity infidelity | Section 2 |
| C1 | An observable supported on an event of probability <=w changes expectation by <=2b sqrt(w)+b^2, b=sqrt(2(1-sqrt(1-eta))) | Uhlmann purifications, Hermitian contraction supported on a projector; standard estimates, no novelty claim for the general method | Lemma 1 |
| C2 | Exact complementary pullbacks: source-jump projector ->gamma V†NsV; exchange between jump flags ->gamma V†JV; single-jump probability <=2gamma | Full two-qubit amplitude damping, gamma in (0,1], including no/double jumps; noiseless spectators | Section 3 |
| C3 | Source and exchange compress within eP and eJ of real scalars, independently of code dimension | Operational worst-case entanglement recovery error; bounds include b/sqrt(gamma), b²/gamma and trivial spectral caps | Theorem 2 |
| C4 | Whole-trajectory D_out<=d0+2 integral sum abs(g)(eP+eJ); uniform ratio r<=1 gives <=d0+22A sqrt(r) | Common C1 moving code, absolutely continuous solutions, real integrable generators, measurable parameters; a separate damping guarantee for every pair; boundary isometries retain all records until final readout | Theorem 3 |
| C5 | Constant equal-prior discrimination with d0<=1/4 implies A sqrt(r)>=1/264 | Final ordinary readout; native summed coupling-time, not every algorithm's runtime | Section 4 |
| C6 | Finite code/decoder gives source defect d and exact logical dephasing multiplier lambda; worst-case infidelity (1-lambda)/2 | Known a,d,gamma; detector initially ground, ordinary finite recovery; explicit four orthogonal syndrome directions | Section 5 |
| C7 | eta_rec=gamma d²/[4a(1-gamma a)]+O(d⁴); square-root recovery-to-source-defect exponent cannot be improved generally | d->0 with a,gamma fixed, 0<a<1, 0<gamma<=1; does **not** show optimal dynamical exponent/constant or an invariant amplifier | Section 5 |

Auxiliary claims included in any future full certification: trace/diamond normalization, midpoint scalar radius, fidelity/purification identities, full Kraus completeness, p=0 vector extension, commutator trace-norm bound, common-frame connection and channel-boundary composition, simultaneous-pair summation, decoder extension, exact dephasing worst-case fidelity and Taylor remainder hypotheses.

Excluded claims: a universal nonlinear-computing impossibility, physical native realization, a constructive general recovery algorithm, tight gain bound, finite-excursion theorem, logical-error accumulation for an implemented noisy circuit, or BPP/BQP progress. Historical S282-S288 notes provide provenance; their other results are not silently included as newly reviewed manuscript theorems.
