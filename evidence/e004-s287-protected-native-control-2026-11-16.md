# Protected native control: a decoding construction and a loss-span obstruction

S287 / E004, 2026-11-16. Base `3cfcb6aeadbecb9e2a2dc5a5a60a5f4bc0234123`. Dan explicitly requested the bounded control construction. [Story](https://github.com/Quantyra/quantyra-quantum-planning/blob/main/stories/S287-test-protected-native-control-synthesis.md); [protocol including S3173](https://github.com/Quantyra/quantyra-planning/blob/main/docs/research-investigation-protocol.md). Preserve prior jobs, ownership, inputs, stops, results and PaperMill. The full nonlinear-computing objective is unchanged and unproved. This note does not establish a device, ordinary BPP/BQP consequence, universal nonlinear impossibility, or novelty.

**Decision.** The ordinary decode/native/re-encode sequence implements the desired ideal logical flow, but an excitation loss on its exposed native source is an uncorrectable logical error. Keeping that source inside an exact loss-correcting code instead eliminates the nonlinear logical action. Correcting losses on both active qubits makes the entire compressed native generator scalar. The obstruction survives input-independent changes of control frame. Approximate versions bound the total distinguishability gain without a singularity at zero population. RETAIN these scoped consequences; PARK this standard protected-control construction. No successor native law or code is commissioned.

## 1. Contract and primary transfers

Use exactly S282's primitive on physical qubits S and B, basis gg,ge,eg,ee, with all other registers retained:

    P=|g><g|_S tensor I_B,
    N=N_S+N_B,
    J=|eg><ge|+|ge><eg|,
    p=<P>, j=<J>,
    H(Psi)=omega N+g sqrt(p) J
           +g j/(2 sqrt(p)) (P-pI).                  (1)

The source is computed from the complete pure state, not separately within unread error histories. At p=0 use S282's regular vector-field extension. Both the coefficient derivative and its scalar normalization term are retained. The source and its physical realization remain hypothetical.

Available controls are ordinary state-independent unitaries, isometric encoding/recovery with finite fresh ancillas, and ordinary readout. Classical pulse parameters may use the known code and circuit description, never an unknown population. One may isolate the primitive during ordinary controls as in S284/S285. Even granting perfect instantaneous ordinary controls, the active source must be protected against the declared physical loss family

    L_S=|g><e|_S tensor I_B,
    L_B=I_S tensor |g><e|_B,
    E={I,L_S,L_B}.                                   (2)

This family is the infinitesimal single-excitation-loss test, not a complete finite-time noise or threshold theorem. The no-jump term for rates kappa_S,kappa_B is I-dt(kappa_S N_S+kappa_B N_B)/2+O(dt^2); it must also be accounted for. A physical model with only a different selected error family is outside this test. Protecting against arbitrary local errors would imply these conditions, but is not assumed.

The target is a protected version of the unknown-input amplifier, not an ordinary controller that computes the input's solution count. In particular it must amplify the supplied close pair |eg> and sqrt(q)|gg>+sqrt(1-q)|eg>, with q exponentially small, to a constant decision gap. This gate contract is stronger than saying that some algorithm can solve SAT using its accessible classical program. We do not infer a SAT or BPP/BQP lower bound from failure of this gate.

Two explicit operations are tested: a syndrome decoder followed by the bare primitive and its inverse decoder; and interleaved/conjugated primitive pulses whose clean trajectory remains in a possibly moving loss-correcting subspace. The first falsifier is an uncorrectable source loss or elimination of the intended logical generator. An abstract encoded functional is not a third implementation.

Primary-source correspondence, checked 2026-11-16:

- [Knill--Laflamme, quant-ph/9604034v1, 26 April 1996, Section 3](https://arxiv.org/html/quant-ph/9604034v1): ordinary exact recovery implies scalar compression of error products. This is the inherited coding theorem, not a new result here.
- [Wetherbee et al., 2412.08870v2, 14 October 2025, Sections 2-3 and Appendix E](https://arxiv.org/html/2412.08870v2): matched code/error-sector couplings permit amplitude-mixing bosonic gates; physical implementation adds nontrivial drive requirements. That coupling structure alone does not implement (1)'s unknown-state source.
- [Roy et al., 2603.15356v1, 16 March 2026, Section II](https://arxiv.org/html/2603.15356v1): moving subspaces still have instantaneous correctability and matching conditions. A moving encoding is not by itself permission to expose the source.
- [Zhou--Zhang--Preskill--Jiang, 1706.02445v2, 2 February 2018, Sections 0.2/0.4/0.5](https://arxiv.org/html/1706.02445v2): error-corrected metrology distinguishes a useful signal outside the Lindblad error span from a signal removed with the noise. Its linear, Markovian estimation theorem is NOT a theorem about (1). We reuse its operator-span diagnostic and prove the nonlinear application directly below.

The search answers that named transfer question; it is not exhaustive novelty validation. S283 already established a local-erasure obstruction. Here the actual excitation-loss products suffice, and the approximate estimate uses bounded coefficients of the full generator rather than an assumed source-Lipschitz constant.

## 2. The ideal sequence exists, but exposes the native source

Let W identify a correctable sector with logical pair tensor syndrome. An ordinary unitary extension D of the syndrome decoder satisfies

    D W(|psi>_L tensor |s>)=|psi>_SB tensor |s>_A.     (3)

A finite-dimensional extension exists after adding basis ancillas. Efficient construction for a growing arbitrary code is not automatic and remains chargeable. Conditional on such a D, the control sequence is precisely

    D ; native Phi_t on SB ; D^dagger.                (4)

For any logical state with arbitrary passive reference and retained syndrome, the complete-state expectations during the middle interval are the logical p,j. Therefore (4) realizes the S283 encoded functional, including the full derivative term in (1), exactly in the ideal model. No classical estimation of the source is used. If D has G_D ordinary gates, one call costs 2G_D ordinary gates, one native interval t, and its syndrome/encoding workspace. Repeated subdivision costs the sum of all such gates and native intervals, not merely the longest interval.

But during that middle interval the physical loss L_S acts on the logical source itself. Even on a fixed syndrome s0,

    W_dec^dagger L_S^dagger L_S W_dec
      = |e><e|_logical-source tensor I_logical-detector,  (5)

which is not scalar. Ordinary exact recovery is impossible for that error family on the decoded unknown logical state. Re-encoding carries this error into the logical register, not a distinct correctable syndrome. With logical source |e>, a loss gives |g> with the same encoding-syndrome flag. It is precisely the false-population direction relevant to S285. We do not independently evolve the lost and no-loss branches, and do not claim a new quantitative false-acceptance theorem: S285's explicit unread-error witness remains the retained one.

This fails the requested protection even if D and D^dagger are perfect and instantaneous. Faster decoding or breaking the native time into more intervals does not remove the interval in which the native source is the unencoded logical source. Assuming no loss there would be an additional noise hypothesis.

## 3. Exact source-loss correction removes nonlinear logical action

For the physical operators in (1)-(2), direct multiplication gives

    P=I-L_S^dagger L_S,
    N=L_S^dagger L_S+L_B^dagger L_B,
    J=L_S^dagger L_B+L_B^dagger L_S.                 (6)

Let V be an isometry for an ordinary code correcting E, and let Q=VV^dagger. Knill--Laflamme requires

    V^dagger E_mu^dagger E_nu V=c_(mu,nu) I.          (7)

Already correcting just {I,L_S} forces V^dagger P V=aI. For a>0, compression of the full native generator is then

    V^dagger H(Psi) V=omega V^dagger N V
                         +g sqrt(a) V^dagger J V.    (7a)

The j-dependent correction vanishes after compression, even if j itself depends on the logical input. The right side is a common ordinary logical Hamiltonian. At a=0 the nonlinear vector field vanishes. Thus source-loss correction alone removes nonlinear logical amplification; it need not remove ordinary logical exchange. This distinction matters when transferring ordinary error-transparent amplitude-mixing gates.

When both L_S and L_B are corrected as in (2), (6)-(7) imply V^dagger P V=aI, V^dagger J V=bI and V^dagger N V=cI. For every normalized encoded logical state, even entangled with a passive reference, p=a and j=b. For a>0 the native Hamiltonian is consequently the same physical Hermitian operator for every logical input, and

    V^dagger H(Psi) V=[omega c+g sqrt(a)b] I.         (8)

The derivative term compresses to zero because V^dagger(P-aI)V=0. At a=0, P V=0, j=0 and the nonlinear vector field is zero. Thus there is no boundary exception. The no-jump term also compresses to a scalar to the displayed first order, by (6)-(7); ignoring it would not restore a logical signal.

Equation (8) does NOT assert that the unmodified physical pulse leaves the code invariant. It may leak out. It says that a construction which keeps an exact protected code while acting with this primitive obtains no logical nonlinear motion. If finite pulses deliberately leave every such protected code, their error propagation is a new obligation; this proof does not certify or exclude all such excursions.

### Moving codes and toggling frames

Let V(t) be a differentiable, input-independent encoding during a control interval. Assume every clean encoded trajectory stays in its range and that (7) holds at every native-on instant for the actual physical losses on the active pair. Add any state-independent ordinary control Hamiltonian K(t). In moving coordinates the logical generator is

    V(t)^dagger [K(t)+H(Psi,t)] V(t)
       -i V(t)^dagger dot(V(t)).                     (9)

With both losses corrected the native contribution is scalar by (8); with only source loss corrected it is the state-independent operator (7a). The complete logical generator is state-independent and Hermitian in either case. It therefore preserves distinguishability. Ordinary encoding/recovery/readout steps at interval boundaries cannot increase it. This argument applies to a finite sequence of such protected intervals and common ordinary operations. Passive references and coherently retained records are allowed when the stated common-code condition holds on the joint space. We do not apply the argument separately to unobserved branches or claim an unrestricted adaptive-collapse theorem.

An ordinary conjugation U cannot transform the source but leave its physical error test behind. In the toggling frame P'=U^dagger P U, L'_mu=U^dagger L_mu U, and the identities (6) still hold with primes. Both the corrected error set and the native source must be transformed. Hence a mere control-frame change cannot move the signal out of this error-product span.

For the supplied close pair with q=4^-n the initial trace distance is delta=2^-n. Every protocol in the exact protected class has final distance at most delta, so equal-prior success is at most (1+delta)/2, below 2/3 for n>=2. This is a gate-level scoped consequence, not a complexity lower bound on algorithms using further input-dependent classical information.

## 4. An approximate tradeoff with no inverse-population loss

Exact scalar compression is stronger than needed for a quantitative obstruction. Suppose a common moving encoded subspace is invariant for the compared clean trajectories, and choose real scalars a(t),b(t) such that

    V^dagger P V=aI+A,  ||A||<=epsilon_P(t),
    V^dagger J V=bI+B,  ||B||<=epsilon_J(t).          (10)

No operational recovery error is identified with these defects without a separate theorem. They measure non-scalar compressed source operators, not failure probability.

For every complete physical state, PJP=(I-P)J(I-P)=0 and ||J||<=1 imply

    |j| <= 2 sqrt(p(1-p)),
    |j|/(2sqrt(p)) <= 1  (p>0).                     (11)

Compress (1) and remove scalar terms, which only change a global phase. Besides the common ordinary generator including omega V^dagger N V and the connection in (9), the residual is

    R(Psi,t)=g sqrt(p) B+g j/(2sqrt(p)) A,
    ||R|| <= |g| [epsilon_J+epsilon_P] = r(t).        (12)

At p=0 the native vector field is zero, so the same projective bound holds by its regular extension. No lower bound on p, no branch-probability division and no unsupported operator-Lipschitz estimate are used. This is why the coefficient-derivative term cannot be omitted yet does not spoil the estimate.

Compare each actual logical density operator with the evolution from the same input under the common ordinary generator alone. Variation of constants and

    (1/2)||[R,rho]||_1 <= ||R||

give trace distance at most integral r(t)dt. Applying the triangle inequality to two inputs, and contraction at ordinary channel boundaries, yields

    D_out <= min(1, delta+2 integral |g(t)|
                             [epsilon_P(t)+epsilon_J(t)]dt).  (13)

For several simultaneously active primitive pairs, sum their separate |g_alpha|(epsilon_P,alpha+epsilon_J,alpha) in (13). Coherent/passive registers are included in the norms. Every claimed moving code must satisfy the same hypotheses during the entire native time. No uncontrolled leakage or nonlinear branch-conditioning step can be omitted from the bound.

If (7) holds to operator-norm defect epsilon for each product needed in (6), then epsilon_P<=epsilon and epsilon_J<=2epsilon. Thus

    D_out <= delta+6 integral |g(t)| epsilon(t)dt.    (14)

Consequently equal-prior decision success >=2/3 requires

    integral |g| epsilon dt >= (1/3-delta)/6.         (15)

For delta=2^-n and n>=2 this is at least 1/72. If epsilon(t)<=epsilon_* and A_g=integral |g|dt, then A_g epsilon_*>=1/72. For fixed/polynomially bounded coupling strength and exponentially small uniform compression defects, native time must be exponential in this class. Conversely inverse-polynomial defects over polynomial time are NOT excluded by this necessary condition. They do not establish a fault-tolerant algorithm either: correction quality, false-positive seeds and leakage still require proof. Growing the coupling strength, adding parallel primitives or changing the active duration is charged through A_g (or its sum over pairs).

### Source-only approximate bound

Even without any scalar approximation to J, assume V^dagger P V=aI+A, ||A||<=epsilon_P and a in [0,1]. Use the common ordinary reference generator that additionally includes g sqrt(a) V^dagger J V. Modulo scalar phases, its difference from the actual compressed native generator is

    R_1=g(sqrt(p)-sqrt(a)) V^dagger J V
                         +g j/(2sqrt(p)) A.

Since |p-a|<=epsilon_P, |sqrt(p)-sqrt(a)|<=sqrt(epsilon_P), and (11) holds, ||R_1||<=|g|(sqrt(epsilon_P)+epsilon_P). At p=0 the actual nonlinear vector field is zero and a<=epsilon_P, giving the same projective bound. The preceding Duhamel argument yields

    D_out <= min(1,delta+2 integral |g(t)|
                              [sqrt(epsilon_P(t))+epsilon_P(t)]dt). (16)

Thus even source-only exponentially small compression defects cannot provide constant distinguishability gain with polynomial total native coupling-time. For uniform epsilon_P<=epsilon_*<=1 and delta<=1/4, success >=2/3 requires A_g sqrt(epsilon_*)>=1/48. This is weaker than (14) when both operators have small defects, but requires no protection assumption about the detector. It is still not an identification of compression defect with an operational error rate, nor a bound on trajectories leaving the declared moving code.

## 5. Small exact witnesses and limits of the transfer

The fixed diagnostic uses unnormalized columns for the four-qubit encoding

    |0_L>=(|0000>+|1111>)/sqrt(2),
    |1_L>=(|0011>+|1100>)/sqrt(2).

For source-only correction it also checks the three-qubit encoding (order S,A,B) with codewords (|000>+|110>)/sqrt(2) and (|011>+|101>)/sqrt(2). This satisfies the error-product conditions for {I,L_S}, has compressed P=I/2, but compressed J_(S,B)=X_L/2. Thus (7a) correctly permits ordinary amplitude mixing; a claim that source-only correction forces J to be scalar would be false. This compression example alone is not an invariant physical implementation.

For the four-qubit code, direct matrix products verify (7) for {I,L_1,L_2,L_3,L_4}. With active pair (1,3), the compressed P is I/2 and the compressed J is zero; J nevertheless leaks the second codeword outside the code. This checks the distinction between scalar compression and invariance. It is NOT an assertion of exact correction of the complete finite-time amplitude-damping channel. A decoded source gives the non-scalar matrix (5). A three-bit repetition code passes its bit-flip error-product check but fails the loss test, so the argument cannot be relabeled an obstruction for every error family. Control-frame covariance of (6) is also checked. These finite checks diagnose algebra and scope only; (6)-(16) supply the dimension-independent argument.

The external amplitude-mixing constructions are not contradicted: their signal operators need not be in the relevant loss-product span, and their oscillator/ancilla implementation must be evaluated with its actual errors. Photon loss on an oscillator does not automatically protect a separate native source qubit against its excitation loss. Likewise an oscillator Hamiltonian containing powers of creation/annihilation operators is still linear in the quantum state and does not synthesize (1)'s state-dependent coefficients.

A possible escape must change a hypothesis: a supported native signal/source outside the corrected error-product span; a justified different physical error model; or a quantitatively controlled excursion/approximate code that preserves useful gain and suppresses false positives. The metrology HNLS sufficiency theorem does NOT certify any of these for nonlinear computation. Merely naming an operator outside the span supplies neither its native synthesis nor the remaining causal/energy/error law. No such successor is selected here.

Ordinary correction of an unknown logical state in a common linear code at every native-on instant is stronger than the requirements of an arbitrary bounded-error nonlinear computer. Recovery tailored only to a restricted state family, recovery itself using nonlinear primitives, or an operation protected only over an entire excursion is not ruled out by imposing (7) on that operation. Those alternatives need their own explicit source/error law and paid construction; none is supplied by this note.

## 6. Completion audit

| Requested obligation | Result |
| --- | --- |
| Explicit control sequence with the allowed primitive | (3)-(4) gives the ideal sequence, conditional on an available decoder |
| No unprotected active source | Fails at (5); exact source-loss protection makes the logical dynamics linear by (7a)-(9) |
| Retain the full nonlinear source and all records | Full generator used; no independently evolved unread branches |
| Quantitative connection to amplification and resources | (13)-(16), plus decoder/native/ancilla costs; no affordable physical implementation follows |
| General code/control scope | Arbitrary finite dimensions and common moving protected codes under the stated loss and invariance assumptions; not all noisy nonlinear algorithms |
| Relation to prior work | Attributed error-product/Lindblad-span principle with a direct model-specific application and approximate estimate |
| Full nonlinear-computing goal or ordinary general bound | Unresolved/unchanged; native physical source, causal composition, energy and total noise costs remain missing |

Bounded attempt complete at the first-falsifier endpoint. Useful auxiliary output is the explicit source-loss mismatch and the bounded-coefficient tradeoffs; external validation consists only of primary-source correspondence, not independent or formal certification. No hardware/cloud, Lean/provider, publication or PaperMill action. The [fixed diagnostic](../scripts/s287-protected-native-control-check.cjs) passed 63 exact matrix checks in 0.0337489 process-internal seconds, maximum dimension 16; its [result](../artifacts/s287-protected-native-control-check-2026-11-16.json) and [process receipt](../artifacts/s287-protected-native-control-process-2026-11-16.json) record child exit 0 under a 30-second cap. This is one diagnostic run, not a numerical trajectory experiment. The initial Python availability probe found no executable; Node was already installed and no package or environment change was made. Patch-context retries were operational edits, not scientific failures. The protocol improved selection by replacing the proposed ordinary-gate transfer with its actual source/error compatibility test and identifying its metrology antecedent before a novelty claim.

Remaining to-do list: none for this bounded construction attempt; a protected native operation remains unresolved, successor SELECTION NONE. This changes the next research decision because an ordinary control-frame change cannot separate this primitive's nonlinear source from the excitation-loss operators being corrected; another protected-gate attempt needs a specified change to that structure.
