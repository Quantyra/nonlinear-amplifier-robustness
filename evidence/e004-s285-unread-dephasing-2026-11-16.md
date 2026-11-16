# Unread dephasing: monotone amplification and a population-error boundary

S285 / E004, 2026-11-16. Base `361251108154e10deda13e81684680b540c8471a`. Internal analytic investigation in S282/S284's declared nonlinear model, not physical realization, a fault-tolerance theorem, novelty certification or an ordinary BPP/BQP result. Full goal `prove nonlinear quantum computing` ACTIVE. [Protocol including S3173](https://github.com/Quantyra/quantyra-planning/blob/main/docs/research-investigation-protocol.md); [planning story](https://github.com/Quantyra/quantyra-quantum-planning/blob/main/stories/S285-test-unread-dephasing-amplification.md). Preserve prior results, jobs, ownership, inputs, stops and PaperMill.

**Outcome.** Retaining the same detector while copying the source basis into fresh unread ancillas yields an exact monotone population recurrence. It solves fixed-input SAT in this model with eight circuit evaluations, O(L+n) ordinary gates, O(W+n) qubits and O(n/g0) native time. It tolerates constant pulse-area uncertainty and arbitrary diagonal phase channels immediately before the copy operations. However, one unread source-bit error of probability 2^-n per module makes an unsatisfiable circuit accept with probability greater than 7/8. Thus the operation improves conditional algorithmic resources and a specified phase/clock contract, but does not protect against general population errors. RETAIN these scoped results; PARK its use as a complete error-control solution; successor SELECTION NONE.

## 1. Selection and exact physical-state contract

S284 removed the pure-source preparation assumption but required O(n) fresh evaluations and O(n^2/g0) total native time to cover unknown peak times. Its sufficient generic residual budget was exp(-O(n^2)); no affordable physical implementation followed. This attempt tests one new finite operation: a short native pulse on the retained source/detector pair, followed by ordinary coherent recording of the source's basis value. The new structure is removal of exchange coherence while preserving accumulated detector population. A monotone recurrence could remove the peak-time search. It does not supply a different native nonlinear law.

A continuous dephasing master equation would be an approximation or representation of this mechanism, not an independent alternative; nonlinear source correspondence and finite-time errors would additionally need proof. S281's fresh MEASURED detectors already fail in their conditional-source class. S283's generic encoded repair still lacks a native encoded source. No second or third new qualifying mechanism is manufactured.

Named primary transfer questions:

- [Ciccarello et al., 2106.11974v2, Section 3 equations 3-8 and Sections 23/27](https://arxiv.org/html/2106.11974v2): a finite system-ancilla unitary and partial trace describe unread records in ordinary collision models. Fresh independent ancillas are available here. Their standard equivalence between averaging conditional trajectories and an unconditional equation cannot be imported through a nonlinear source without proof. Only the ordinary copy gate and its exact reduced action are imported below; the native evolution is derived from the full state.
- [Bennett--Leung--Smith--Smolin, 0908.3023v2, linearity-trap discussion](https://arxiv.org/html/0908.3023v2): the evolution of a nonlinear mixture cannot be inferred by averaging separately evolved components. The present calculation retains the complete pure state and one common source. It does not assert success on a reference-labeled distribution of different circuits.

Input is a fixed classical Boolean circuit F on n>=1 bits, with reversible size L and workspace W. No accepting count or probability is available to the controller. Native evolution can be switched off for ordinary gates. During a native pulse, all registers other than the active pair SB are retained spectators. Standard basis initialization, ideal storage and final Born readout are assumed as in S284. Native source, switching/isolation, causal preparation, operational energy and physical error costs remain unimplemented.

Use the same operators P=|g><g|_S tensor I_B, N=N_S+N_B and J=|eg><ge|+|ge><eg|. On the complete normalized pure state, p=<P>, j=<J>, and

    H(Psi)=omega N+g(t) sqrt(p)J
               +g(t) j/(2sqrt(p))(P-pI).              (1)

Use S282's unique regular vector-field extension at p=0, including the full coefficient derivative. An unknown constant g in [g0/2,2g0] is sufficient; the proof also allows predetermined positive g(t) within those bounds. The known g0 is a fixed clock-unit constant or a positive rational of polynomial description length. Require g0^-1 polynomially bounded for polynomial native time, and omega>=2g0. This is still the assumed native operation, not classical estimation of p or j.

## 2. Exact reduced closure and one finite cycle

Let R contain every circuit and past copy record. Since the complete generator is H(rho_SB) tensor I_R, partial tracing its commutator gives EXACTLY

    dot(rho_SB)=-i[H(rho_SB),rho_SB].                  (2)

This identity holds for entangled SB-R states. The partial trace is an analysis operation, not physical deletion. It works because the specified source depends only on p and j of the pair marginal; arbitrary nonlocal/history-dependent sources do not inherit it. No sum of independently amplified branches appears.

Write q for the conserved gg population and p for the source-ground population at the beginning of a pulse. Consider the pair marginal, in order gg,ge,eg,ee,

    rho_(q,p)=diag(q,p-q,1-p,0),
    q<=p<=(1+q)/2.                                  (3)

S284's direct coherent F preparation with all input/workspace records gives (3) with p=q=a/2^n. Its accepting and rejecting input records are orthogonal. More generally every purification of (3) is permitted by (2).

Put z=1+q-2p>=0. During the pulse the exact solution is the ordinary rotation of this diagonal matrix by exp(-i omega Nt) exp(-i theta J), with

    theta(0)=0,
    dot(theta)=g(t) sqrt(p+z sin(theta)^2),
    p(t)=p+z sin(theta)^2,
    rho_(ge,eg)(t)=-i z cos(theta)sin(theta).         (4)

Thus j=2 Re rho_(ge,eg)=0 throughout. The full correction in (1) vanishes on this invariant set; it remains part of the off-orbit law. Direct differentiation verifies (2). Uniqueness of the complete flow supplies the actual solution. At q=p=0 the unique vector-field extension keeps the null state fixed; there is no spontaneous departure from zero. At q=p=1 the pair is gg and fixed.

After the pulse, turn native evolution off and apply the ordinary unitary

    V=P tensor X_A + (I-P) tensor I_A                (5)

to a fresh ancilla A initially |0>. Retain A without measurement or reset. Its exact action on the pair marginal is

    D_S(rho)=P rho P+(I-P)rho(I-P).                  (6)

It removes the ge/eg coherence in (4) and leaves the populations unchanged. The pair returns to (3), now with

    p_next=p+(1+q-2p) sin(theta_end)^2.              (7)

The same detector remains available. Old ancillas can be entangled with the pair and each other; equation (2) continues to apply. No conditional source is assigned to any value stored in an unread ancilla. This is an exact finite unitary construction, with no Lindblad/weak-coupling limit or uncharged Trotter approximation.

## 3. Uniform monotonic growth with uncertain pulse area

Use physical duration tau=1/(4g0) per pulse. It suffices that EACH pulse has actual area

    u=integral_pulse g(t)dt in [1/8,1/2].             (8)

The stated coupling bounds guarantee this. Areas need not be equal across pulses or known individually. Clock/coupling perturbations are covered only insofar as they preserve (8) and the generator's form; arbitrary detuning or extra Hamiltonian terms are not included.

Since p(t)<=1, equation (4) gives 0<=theta_end<=u<=1/2. If p<=(1+q)/2, then p(t)>=p and theta_end>=u sqrt(p)>=sqrt(p)/8. Using sin(theta)>=theta/2 on [0,1/2],

    sin(theta_end)^2>=p/256,
    sin(theta_end)^2<=1/4.                           (9)

With c=(1+q)/2, equation (7) therefore implies

    p<=p_next<=p+(c-p)/2<=c.                         (10)

When p<=1/4, z=1+q-2p>=1/2, so

    p_next>=p(1+1/512).                             (11)

For any q>=2^-n, K=1024n cycles suffice to reach p>=1/4. Otherwise (11) would hold for all K cycles and

    p_K>=2^-n(1+1/512)^(1024n)>2^-n exp(n)>1,

contradicting p_K<1/4. Here ln(1+1/512)>=1/513>1/1024. Once 1/4 is reached, (10) keeps it. For q=0, p stays zero exactly. The same K works for every accepting count, including q=1, without finding the unknown first maximum.

## 4. Decision algorithm and complete ideal resources

Prepare r=8 fresh modules using ordinary coherent F evaluation, each with a ground-state detector. Evolve each for K cycles above, with a fresh retained ancilla per cycle. Modules are initially products for fixed F; the pair-local source and private records preserve their product structure. Switch native evolution off and compute a coherent OR of the eight source-ground indicators, then measure that bit once. For every fixed F,

    Pr(accept | a>0)>=1-(3/4)^8>7/8,
    Pr(accept | a=0)=0.                             (12)

The product property justifies the eight-module repetition. An arbitrary correlated external noise source is not granted this property. With n=0, evaluate the circuit classically.

The resource account is:

| Resource | Complete count/bound |
| --- | --- |
| Reversible F evaluations | Eight, from the supplied circuit description |
| Native pulses and source-copy gates | rK=8192n each |
| Retained copy ancillas | rK; none reset, measured or discarded |
| Total ordinary gates | O(L+n), including all preparation, copy, routing/readout gates |
| Live qubits | O(W+n), including eight circuit records, detectors and every ancilla |
| Total native time | rK/(4g0)=2048n/g0 |
| Schedule arithmetic | Integer K and one rational duration; polynomial bit cost |
| Native operator strength | O(omega+g), with S282's regular extension |

These improve S284's O(n) F evaluations, O(n(L+n)) gates and O(n^2/g0) total native time within the SAME assumed interface. Large displayed constants are not optimized. Ordinary gate/copy time, initial ancilla preparation, switching, storage, geometry, source/control and energy/work must still be implemented. Bounded pair energy is not a complete apparatus energy theorem.

## 5. What noise is controlled, and what is not

At a checkpoint immediately BEFORE (5), allow any pair channel Phi with diagonal Kraus operators in gg,ge,eg,ee and trace preservation, during native-off control. Such a channel fixes every population and only multiplies off-diagonal entries. On the state (4), D_S Phi(rho)=D_S(rho) exactly. Therefore arbitrary-strength phase kicks or phase damping at these checkpoints do not change the recurrence. A private ordinary unitary dilation can retain their environment too; no collapse-conditioned fields are invoked. Together with (8), this is an exact phase/checkpoint and pulse-area tolerance statement. It does not cover continuous dephasing during a pulse, population-changing errors, failed copy gates, cross-module correlations or arbitrary storage noise.

For otherwise arbitrary normalized pure-state implementation residuals, S282's dimension-independent vector-field bound still gives a conservative sufficient contract. Let E be initial global vector error plus the sum of ordinary gate operator-norm errors and integrated native vector-field residual norms. Across all rK pulses, unitary gate telescoping and Gronwall give

    ||Psi_impl-Psi_ideal||<=exp(10 sum_pulses u) E
                         <=exp(5rK) E.              (13)

Thus E<=exp(-5rK)/24 plus final readout total-variation error <=1/24 suffices for output error <=1/12 and success >7/8-1/12=19/24. The bound now has exp(-O(n)) rather than S284's exp(-O(n^2)) sufficient tolerance. This is an asymptotic upper allowance, not an optimized robustness theorem; the constants can make it smaller at modest n. A pure-state/dilation residual must actually be justified for any noise being included. Its O(n)-bit tolerance description does not establish affordable physical accuracy.

**Population-error falsifier.** Take the null circuit F=0. Immediately after each module's preparation, apply the allowed ordinary error dilation

    |e>|0>_E -> sqrt(1-epsilon)|e>|0>_E
                         +sqrt(epsilon)|g>|1>_E,     (14)

with orthogonal retained records and a unitary extension on the other input basis states. It can be chosen as the usual dilation of the source bit-flip channel (1-epsilon)Id+epsilon X(.)X; the relative phase of the second term is irrelevant. The detector remains ground. The pair marginal is exactly rho_(q,p) with q=p=epsilon, despite the true accepting count being zero. Choose epsilon=2^-n. Equations (7)-(12) then give false acceptance greater than 7/8. The eight error ancillas can be private, so the repetition/product argument still applies.

For the reduced source channel, half its diamond-norm distance from identity is epsilon (the upper bound follows by convexity and the value is attained on |e>). This does NOT mean the complete retained-environment vector error is epsilon: for (14) it is sqrt(2-2sqrt(1-epsilon))=Theta(sqrt(epsilon)). Both norms are charged. The witness proves that this algorithm cannot tolerate ALL such unread bit-flip channels up to error epsilon_max(n) when epsilon_max(n)>=2^-n. It is not a universal lower bound for every structured noise law or every nonlinear algorithm, and it does not prove that achieving smaller errors is physically exponentially costly.

The failure is substantive: phase dephasing preserves null population, whereas the population error seeds exactly the quantity the device amplifies. A general population-noise allowance cannot be inferred from the phase/clock result. Actual objective reduction of the error record would change the subsequent source prescription and requires a separate causal model; it is not equivalent to the retained dilation (14). This sharpens the existing null-population concern for the tested operation, not a second universal no-go theorem.

## 6. Original-objective audit and stopping decision

S281 is preserved: its survival identity used fresh measured detectors and fields conditioned on actual outcomes. Here the detector is retained, no outcomes occur until final readout, and one full-state source drives all unread records. The equations cannot be transferred between these protocols by averaging the conditional fields. S284's fixed classical-input hypothesis is also preserved; a coherent reference labeling distinct circuits still invokes one shared source and does not inherit separate-instance computational success. Neither the source/composition obstruction nor S282's operational energy limitation has been removed.

| Obligation | Evidence/status |
| --- | --- |
| Exact finite operation with all records | (1)-(7), derived from the same complete source |
| Every-count algorithm and total resources | (8)-(12); conditional improvement to constant F calls and linear native time |
| Phase/clock tolerance under a specified contract | (8) and D_S Phi=D_S at native-off checkpoints |
| General physical noise robustness | Not established; explicit bit-flip falsifier (14) |
| Native source, causal input history, operational energy and affordable implementation | Still missing |
| Ordinary general BPP/BQP bound | S218/S222 unchanged |
| Novelty, independent/formal certification or empirical realization | Not established or attempted |

General-bound improvement: none. Discharged conditional obligations: exact monotone amplification, count-independent finite schedule and full ideal resource account; a narrow phase/clock error contract. Useful auxiliary mathematics: recurrence and population-error witness. External work: named primary-source transfer checks only. Operational work: one isolated analytic pass, source records and repository verification. No numerical test, continuous-limit simulation, hardware/cloud, Lean/provider review or PaperMill action occurred.

The protocol improved the actual investigation: it replaced an unproved phenomenological noise equation with a finite ordinary operation, then distinguished phase tolerance from population-error protection through an exact falsifier. No native physical feasibility obligation is discharged. To change selection, a concrete operation must protect the null population under the intended physical error/source law, with its costs; a generic code name or another gain curve is insufficient. RETAIN conditional algorithm/scoped tolerance and counterexample; PARK dephasing as a complete noise solution; successor SELECTION NONE. Full objective remains ACTIVE and unproved; the pending completion-scope clarification is unchanged.

Remaining to-do list: none for this bounded analytic test; paid native source/causal preparation and protection against population-seeding errors remain unresolved. This changes the next research decision because unread dephasing removes unknown peak timing and improves ideal resources, but even exponentially small population errors can make the null circuit accept, so phase robustness alone cannot justify a physical nonlinear computer.
