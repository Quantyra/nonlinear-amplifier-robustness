# Finite dissipative phase amplification: full-record dynamics and an input-bias obstruction

S288 / E004, 2026-11-16. Base `e841fb1b95b59baf442124f8a99bacc3f9a97201`. [Preregistered story](https://github.com/Quantyra/quantyra-quantum-planning/blob/3c75ba72/stories/S288-test-dissipative-nonlinear-phase-cycle.md); [shared protocol including S3173](https://github.com/Quantyra/quantyra-planning/blob/main/docs/research-investigation-protocol.md). The original attached goal (SHA-256 `4109e642da92ee569aabf0fc51bd95021f45e6a21de6e4a3037cc58715d054b6`) asks for a bounded proof/refutation and specifies stopping if amplified bias needs unprovided protection. Preserve prior results, counterexamples, jobs, owners, inputs, stops and PaperMill.

**Decision: RETAIN the exact conditional map and scoped obstruction; PARK this uncalibrated-noise implementation; successor SELECTION NONE.** An ordinary preparation error of half-diamond size at most 2^-n makes the null source exactly equal to a valid signal source from the retained circuit construction. The declared source-local nonlinear law, all later bath records and any common source/bath readout then give identical distributions at every duration. Ideal amplification cannot repair this identification. This is a failure of the stated robust decision pipeline, not a theorem ruling out all nonlinear computers, every physically restricted error model, or algorithms that continue processing the original program/workspace. No general bound or physical realization is established. Native source, causal composition, operational energy and affordable bias protection remain unprovided.

## 1. Contract, existing bounds and primary transfers

The available input is a circuit F, size L, workspace W, on n bits. Its satisfying fraction p is unknown. Preparation is ordinary reversible computation with retained records, as in S280, followed by the fixed Hadamard H on the output. The amplifier operates on this output S and fresh bath qubits; original preparation registers R are passive. No count, answer bit, state reader, postselection or separately evolved unread branch is available. Its controls do not depend on p. Ordinary final measurements may use S and every bath qubit introduced after preparation. Access to R for a new input-dependent computation would be an additional operation, outside this tested cycle.

The intended contract is a uniformly correct zero/nonzero-signal decision with success >=2/3 and polynomial total resources, including robustness to the specified unwanted rotations, bath imperfections and native symmetry-breaking errors. The negative theorem below is quantified for **unknown preparation errors in a half-diamond-norm ball**. It does not assume a derived microscopic noise law; identifying whether that ball can legitimately be replaced by a narrower physically protected family is the stop gate. A calibrated known error map, reference-assisted calibration with extra operations, and a proven symmetry-protected noise law are not ruled out by the theorem.

S285 retains a different hypothetical primitive's eight-evaluation, O(n/g0)-native-time conditional algorithm. S218/S222 retain the ordinary bound `poly(L) 2^O(min{phi(G), n[1+log_+(G/B_n)]})`, polynomial space, where `phi(G)=(G+2)/sqrt(log2(G+2))` and `B_n=ceil(n sqrt(ceil(log2(n+2))))`. Neither bound improves here. Repeated absence of a paid source/noise law is one bottleneck, not an additional discovery each time.

Named transfers checked against primary sources, not an exhaustive novelty review:

- [Geller, 2111.05977v2, 4 July 2023, Section III](https://arxiv.org/html/2111.05977v2): attracting decision outputs motivate dissipation. The introduction leaves model error untreated; after equation 52, positivity of equation 40 still requires intervention. That structure does not supply our microscopic source or bias protection. Our finite dilation below enforces positivity conditionally, but does not import a fault-tolerance theorem.
- [Childs--Young, 1507.06334v2, 27 April 2016, Sections 2, 3.1, 4](https://arxiv.org/html/1507.06334v2): phase amplification and heralded preparation are known. S280 retains flags coherently; the present analysis uses its exact marginal. Their mean-field validity discussion prevents treating a condensate amplitude as a free fundamental nonlinear qubit. Our coefficient g in g*z*Z is twice the coefficient multiplying z*Z in their usual Gross--Pitaevskii convention.
- [Ciccarello et al., 2106.11974v2, 14 March 2022, equations 7-8 and 29-32](https://arxiv.org/html/2106.11974v2): finite unitary system/bath collisions give damping. The bath is fresh and initially independent, while past records remain present. We derive closure through the nonlinear pulse instead of assuming linear averaging remains valid.

The concrete alternative remains monitored full-run abort/restart: clean duration T under independent constant hazard r has survival exp(-r*T), hence mean exp(r*T) attempts. For T=Theta(n/g) and constant r/g it is not a polynomial implementation. This is scoped to that restart policy. S287's exact-code/frame variants retain their obstruction. No third distinct paid operation is supplied.

## 2. A preparation in the actual unresolved regime

Use exactly one S280 preparation/routing attempt. Set

    s=(1-p)^2+p^2,  a=(1-p)/sqrt(s),  b=p/sqrt(s),
    |phi_p>=a|+X>+b|-X>,  P_+=|+X><+X|.

The complete state, after the ordinary output Hadamard, is

    |Omega_F>=sqrt(s)|phi_p>_S|J_F>_R
                  +sqrt(1-s)|+X>_S|K_F>_R,   <J_F|K_F>=0.       (1)

All amplitudes, including the failed preparation, remain. There is no heralded success claim or retry. Its source marginal is exactly

    sigma_p=s|phi_p><phi_p|+(1-s)P_+,
    (x_p,y_p,z_p)=(1-2p^2, 0, 2p(1-p)).                         (2)

For p=0 this is P_+. For p=2^-n and n>=2, z_p>=2^-n. Thus the unique-solution subfamily already lies in the requested exponentially small signal regime; it suffices for refutation of a guarantee for every allowed nonzero signal. We do not assume that every satisfying fraction automatically gives positive z: p=1 gives z=0. If covering every count in an ideal algorithm were needed, replace F(x) by F(x) AND a fresh bit. This uses one extra bit and O(1) extra gates, halves p and ensures 0<p<=1/2, with the corresponding one-bit signal loss. No ideal all-count algorithm is asserted here.

One preparation costs O(L+n) ordinary reversible gates and O(W+n) qubits, with constant compute/uncompute invocations of F. Rotation H and routing are ordinary gates; no unknown-state construction is needed. These are circuit resources, not a completed physical preparation/noise cost theorem.

## 3. Complete joint cycle, including the scalar derivative term

Let Psi contain S, R and every bath record. For nonzero unnormalized Psi define the real homogeneous functional

    F(Psi)=(g/2) <Psi|Z_S|Psi>^2/<Psi|Psi>.

On normalized states its full gradient is

    H_full(Psi)=g*z*Z_S-(g/2)*z^2*I,  z=<Psi|Z_S|Psi>.           (3)

The scalar term contributes a global phase but is not omitted from the derivation. During a native pulse z is constant, so for g>0 and tau=1/g the exact joint flow is

    Phi(Psi)=exp(i*z^2/2) [exp(-i*z*Z_S) tensor I_records] Psi.   (4)

It has bounded generator norm <=3g/2 and no singularity at z=0. Native operation is off during ordinary controls. Apply U_X=exp(-i*pi*X/8). Append a fresh bath in |+X>. In the X eigenbasis 0=+X, 1=-X, use the ordinary unitary C with c=d=1/sqrt(2):

    C|00>=|00>,       C|11>=|11>,
    C|10>=c|10>+d|01>,
    C|01>=c|01>-d|10>.                                          (5)

The next complete state is C_SB [(U_X tensor I) Phi(Psi) tensor |0>_B], with R and all older B registers retained. This recursive vector expression specifies the entire finite trajectory. It never evolves the summands of (1) independently. A mixed bath error is represented by a purification and the same ordinary unitary.

The source reduced equation closes because (3) depends only on Tr(rho_S Z), and each fresh bath is independent. Taking a partial trace only for observable calculation gives the **exact**, not infinitesimal, map

    u=x*cos(2z)-y*sin(2z),  v=y*cos(2z)+x*sin(2z),
    T(x,y,z)=((1+u)/2, (v-z)/2, (v+z)/2).                       (6)

Every step is a state-dependent unitary followed by an ordinary unitary dilation; the source stays in the Bloch ball for all cycle counts. This conditional positivity improvement over an unconstrained phenomenological drift does not establish physical implementability. The null (1,0,0) is fixed. Its transverse tangent is

    M=(1/2) [[1,1],[1,3]],  eigenvalues 1 +/- 1/sqrt(2).         (7)

An expanding tangent alone proves neither a global basin theorem nor the whole unknown-signal decision contract. We deliberately test false signals before pursuing such a theorem.

**Full-trajectory closure lemma.** Suppose two preparations have the same source marginal, possibly different purifications in passive R. Their joint reduced state on S plus all subsequent fresh baths is identical after every cycle, and during every pulse. At the first pulse the equal marginals give the same z and hence the same unitary. Appending the same independent bath, applying (5), and taking the partial trace of R preserves equality. Induct on cycles; during a pulse z is constant. The argument also permits common ordinary operations on the active registers. Thus every common POVM on all active registers has identical output distributions. Different R purifications or an unmeasured error flag do not supply distinct branchwise fields. This lemma is not a claim about additional controls/readout on the original R.

## 4. First falsifier: exact signal imitation by an ordinary error

In the X basis define the real unitary

    V_p=[[a,-b],[b,a]],
    E_p(rho)=s V_p rho V_p^dagger+(1-s)rho.                      (8)

It is one small ordinary rotation applied under a retained error flag: start a fresh flag in sqrt(s)|0>+sqrt(1-s)|1>, apply V_p controlled on 0, and retain it. This dilation uses no state reader. For the witness choose p=2^-n; every control parameter then depends only on n, not on an unknown satisfying string or the actual count. Equations (1)-(2) give the exact equality

    E_p(P_+)=sigma_p.                                           (9)

In half-diamond distance, the unitary-channel error from V_p is b (its eigenphases are +/-arcsin b). Multiplying the channel difference by s gives

    (1/2)||E_p-id||_diamond=s*b=p*sqrt(s)<=p=2^-n.               (10)

Equivalently, ||E_p-id||_diamond/2 is at least the output distance on P_+, which is p*sqrt(s); the unitary bound gives the matching upper bound. There is no missing square root between this channel distance and a pure-state purification distance.

Compare two allowed cases: a genuine p=2^-n preparation with no error, and a null preparation with error E_p. They have exactly the same active input, and the closure lemma makes their entire source/bath trajectories identical, for **every K**, not merely polynomial K. If the probability of reporting signal is q, completeness is q and soundness success is 1-q; one is <=1/2. Therefore no common readout achieves >=2/3 on both. If the ideal signal never becomes readable, completeness already fails; if it does, the erroneous null is equally readable. This dichotomy refutes the joint reliable-amplification contract without requiring an ideal convergence theorem.

Any uniform unknown-error ball of radius eta_n>=p*sqrt(s) contains this witness and identity, so in particular inverse-polynomial-radius balls fail asymptotically. Error budgets are upper bounds and include smaller errors. The theorem is about uncertainty over allowed implementations; it does not assert that the same calibrated error map produces equality on both inputs, that real noise must adversarially select E_p, or that all physically realizable error laws contain E_p. Avoiding this witness requires excluding or identifying this bias by a justified additional structure. Such a mechanism is not supplied by damping or stable output attractors.

Even with a pure supplied signal, R_Y(-theta) sends P_+ to (cos(theta),0,sin(theta)), with channel error |sin(theta/2)|. Thus a pure rotation seeds a valid exponentially small signal; the unread ordinary channel (8) additionally matches the **actual mixed prepared input** exactly. The rotation's coefficient needs O(n) bits for the witness scale; this is not a claim that physically controlling or suppressing it has polynomial cost.

## 5. The other requested error tests and the symmetry escape

**Imperfect bath.** At a null source, a fresh bath with physical Bloch vector (x_B,y_B,z_B) gives, by (5),

    (x_out,y_out,z_out)=((1+x_B)/2,-y_B/sqrt(2),-z_B/sqrt(2)).    (11)

A small coherent bath tilt seeds a transverse false signal linearly in its tilt. Its newly retained bath record can contain information; unlike (9), this observation alone is not an indistinguishability theorem for collective bath readout. By contrast, a bath mixture (1-q)|+X><+X|+q|-X><-X| has no transverse bias. More generally such a bath gives x_out=(u+1-2q)/2 with the same last two components in (6). The zero-signal axis is invariant and x tends to x_*=1-2q. Its tangent is

    M(x_*)=(1/2)[[1,2x_*-1],[1,2x_*+1]],
    det M=1/2,  tr M=1+x_*.

There is an eigenvalue >1 for x_*>1/2, equivalently q<1/4. This is local gain with symmetric impurity, not a full noisy decision theorem. It explicitly prevents the false inference that every bath imperfection necessarily creates a false mean signal, or that symmetry must preserve null purity.

**Native symmetry breaking.** Add a small ordinary term epsilon*g*Y to (3), with all records still retained. The Bloch equations during the native interval are

    dx/dt=2g(epsilon*z-z*y),  dy/dt=2g*z*x,
    dz/dt=-2g*epsilon*x.                                       (12)

At the null, dz/dt=-2g*epsilon. Expanding the finite pulse of duration 1/g gives y=-2epsilon+O(epsilon^2), z=-2epsilon+O(epsilon^2), x=1+O(epsilon^2). After the X rotation and ideal collision, y_out=O(epsilon^2) and z_out=-2epsilon+O(epsilon^2). Thus a native bias is converted into transverse signal at first order. This is a local perturbative test; it does not assert an exact all-time state match for that particular continuous perturbation. Equation (9) is the stronger full-trajectory falsifier.

**What could exclude the witness?** The ideal source map is covariant under X conjugation: z changes sign and the phase operator conjugates accordingly. U_X commutes with X; (5) commutes with simultaneous X_S X_B, and an X-diagonal bath respects this symmetry. Hence the x-axis stays invariant. The functional F is invariant under this parity, so the symmetry is algebraically compatible with the hypothetical primitive. A *joint* source/controller/bath/error law enforcing it could forbid additive transverse seeds while allowing small-signal gain. No such physical law, finite-error implementation or paid calibration mechanism has been derived here or supplied by the imported papers. Ordinary gate-approximation error and exact microscopic symmetry are different assumptions.

Randomly X-twirling a retained source does not provide the missing protection for free. With an unread coherent/random control, averaging X rho X and rho makes the actual marginal z zero; the shared nonlinear coefficient then vanishes. Evolving the two flag sectors separately before averaging would change the law. A deterministic error-cancellation design might behave differently but would require an explicit sequence and proof; none is silently commissioned. Exact common-mode bias information or a justified symmetry could change selection, but arbitrary uncalibrated noise plus the current cycle cannot.

## 6. Whole-system resources and error accounting

For K cycles and the single preparation (1), the declared ideal circuit cost is O(L+n+K) ordinary gates, O(W+n+K) qubits including every bath and record, K/|g| native duration, and integrated native strength K. Constant bath-collision angle and X rotation are charged once per cycle; bounded-strength implementations require their full summed durations, not the largest single interval. No failed preparation is discarded and no retry cost is hidden. Independent repetitions multiply these costs; tensoring identical active inputs in the two cases of (9) does not resolve their equality under common source-local operations.

For completeness, the phase step has trace-distance Lipschitz constant at most 3 even on S plus active records: compare its two propagators, use |z_rho-z_sigma|<=2D(rho,sigma), and bound the extra unitary rotation's distance by |z_rho-z_sigma|. Ordinary controls and appending fresh baths are contractive/isometric. If eta_0 is initial active-state error and eta_j bounds the full per-cycle implementation discrepancy, then

    D_K <= 3^K eta_0 + sum_(j=0)^(K-1) 3^(K-1-j) eta_j.         (13)

This is a sufficient stability budget, not an optimal necessary tolerance or a readout theorem. For a hypothetical K=O(n) ideal decision algorithm, exponentially small errors can be described with O(n) bits. That fact pays neither calibration shots nor physical noise suppression. The necessary exclusion of (10) is separate from (13); no claim that its scale is tight is made. Ordinary gate synthesis costs must be multiplied by the number of gates and required precision. Native field calibration, isolation from preparation records, switching and deviations from the source-local law are additional errors, not free consequences of unitary notation.

C conserves the X-basis excitation number of its two qubits. If a bath excitation has assigned energy Delta, K fresh pure baths and their disposal/reset must be charged, and the controls/native pulse need a compatible work/source model. The native functional F is conserved during an isolated native pulse because z is constant, but U_X changes it. Bounded F and conservation of collision excitation are **not** a complete physical energy conservation or work-cost theorem. The apparatus providing g and its causal law are unspecified. A condensate/mean-field implementation additionally owes particle number and validity-time costs from Childs--Young; no exponential physical advantage is inferred.

Consequently there is no proved polynomial total physical-resource realization, nor an exponential-cost theorem inferred solely from the small necessary tolerance. The original explicit stop condition is met: this route requires protection against amplified bias that the present specification does not provide.

## 7. Resolution audit and evidence classification

| Original requirement | Authoritative result / limit |
|---|---|
| Explicit nonlinear pulse, X rotation, finite relaxation | Equations (3)-(6) specify the joint finite cycle, including scalar derivative and ordinary bath dilation. |
| Retain all preparation/bath records | Equations (1), (4)-(5), with the closure induction; no branchwise nonlinear evolution or discarded failure. |
| Test exponentially small unknown signal, >=2/3 and full trajectory | Equations (2), (9)-(10) give an allowed subfamily and exact input imitation; identical all-K distributions forbid the robust two-sided contract. Not a universal SAT lower bound. |
| Unwanted rotation, imperfect bath, native error | Sections 4-5 distinguish exact imitation, coherent bath seeding, harmless-axis impurity and first-order native bias. |
| Determine whether protection is supplied at polynomial cost | Exact covariance is a conditional escape, but no joint physical symmetry/calibration implementation is supplied; the stated stop rule applies. No proof that all such implementations are impossible. |
| Charge every resource and failed attempt | Section 6 gives K-dependent circuit/native/bath totals, one retained preparation, precision recurrence and explicitly unresolved physical energy/source/error costs. |
| Prove or refute useful amplification and readout | The conjunction is refuted under the declared uncalibrated-error contract, whether or not an ideal basin theorem holds. A noiseless global convergence theorem is not claimed and is not pursued after the first falsifier. |
| Preserve results; distinguish conditional/physical; resolution decision | Prior S280-S287 evidence and ordinary bounds stay unchanged; RETAIN conditional algebra/obstruction, PARK implementation, SELECTION NONE. |

The theorem is analytic for all n>=2 and every cycle count; the fixed diagnostic is supporting evidence only. [Script](../scripts/s288-dissipative-phase-cycle-check.cjs), [check receipt](../artifacts/s288-dissipative-phase-cycle-check-2026-11-16.json) and [process receipt](../artifacts/s288-dissipative-phase-cycle-process-2026-11-16.json): one run passed 38 exact BigInt assertions and 656 floating matrix-component checks, maximum dimension 8, n in {2,3,4,8,16,32}. Maximum floating residual was 3.3306690738754696e-16 against tolerance 2e-12; exact rational checks cover small-signal algebra independently of that tolerance. Internal runtime 0.0213788 seconds, process wall time 0.4156511 seconds, child exit 0 within the 30-second cap, empty stderr. No numerical attractor search, physical/cloud experiment, provider review, Lean certification or PaperMill action was performed. No independent novelty claim is made: identical-input indistinguishability is elementary, and this is its model-specific application to the selected candidate.

General-bound improvements: none. Discharged conditional obligations: exact joint cycle, source closure and prepared-input correspondence. Useful auxiliary mathematics: explicit error-channel equality and scoped robustness failure, plus bath-symmetry distinctions. External validation: targeted primary-source transfer checks, not independent validation of this note. Operational work: preregistration, isolated worktree, fixed diagnostic and focused Git custody. The false-signal result sharpens the same unresolved bias/source requirement; it is not counted as another universal impossibility.

The protocol improved actual selection by making exact false-input imitation the first gate; it prevented extending the ideal tangent calculation into an unsupported physical claim. Remaining to-do list: none for this bounded proof/refutation audit; native physical realization and a paid symmetry/calibration escape remain unresolved and unselected. This changes the next research decision because the proposed dissipation preserves an error-generated signal just as it preserves a genuine one, so further ideal gain or attractor analysis cannot supply the missing bias protection.
