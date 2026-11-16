# Coherent nonlinear exchange: a regular Hamiltonian amplifier and its missing physical completion

S282 / E004, 2026-11-15. Base `08ead716b985558c17caa1203baad882e9937e55`. Internal analytic construction and scoped transfer audit, not a physical realization, complete nonlinear theory, novelty claim or ordinary BPP/BQP result. Full goal `prove nonlinear quantum computing` remains ACTIVE. Apply the [shared protocol including S3173](https://github.com/Quantyra/quantyra-planning/blob/main/docs/research-investigation-protocol.md) and [planning story](https://github.com/Quantyra/quantyra-quantum-planning/blob/main/stories/S282-construct-coherent-exchange-hamiltonian.md). Preserve prior results, jobs, ownership, inputs, stops and PaperMill.

**Outcome.** The proposed homogeneous energy functional has a unique regular state flow, a nonnegative conserved value when omega>=abs(g), conserved bare excitation statistics and an exact O(n/abs(g)) pure-input discriminator. The coefficient-derivative terms do not destroy its invariant amplifying orbit. This escapes S281's measured-detector obstruction in a hypothetical model. It does not escape the retained common-source obstruction for an uncollapsed reference; a conventional spectral interpretation of its instantaneous generator also fails the full energy-statistics test. Native coupling, operational energy/collapse apparatus and physical error costs remain missing. RETAIN the conditional construction; PARK the full-device transfer; successor SELECTION NONE.

## 1. Contract, transfers and scope

One source qubit S and one resonant detector B have basis |gg>,|ge>,|eg>,|ee>. B stays coherent until final readout. Set

    P=|g><g|_S tensor I_B,
    N=|e><e|_S tensor I_B + I_S tensor |e><e|_B,
    J=|eg><ge|+|ge><eg|.

Thus ||J||=1, PJP=(I-P)J(I-P)=0, and [N,P]=[N,J]=0. In units hbar=1 take g>0 and omega>=g; negative g is absorbed in a fixed phase convention. The unknown input is |e> or sqrt(p0)|g>+sqrt(1-p0)|e>, p0=4^-n, n>=1, with detector |g>. The controller knows n and model parameters, not the label or a measurement of its state population. The pure-input promise is a supplied-state contract; it does not by itself give a circuit-to-device preparation theorem.

Relevant transfers, limited to the stated questions:

- [Ciccarello et al., 2106.11974v2 (2022), Section 46](https://arxiv.org/html/2106.11974v2): retained ancilla correlations change repeated-interaction dynamics. This supplies the memory distinction, not a native nonlinear coupling.
- [Childs--Young, 1507.06334v2 (27 April 2016), Sections 3-4](https://arxiv.org/html/1507.06334v2): fast nonlinear discrimination already exists under assumed laws; a condensate mean-field parameter is not a free single-copy quantum state. The result here is not claimed as the first fast nonlinear amplifier.
- [Kent, quant-ph/0204106v2 (28 February 2005), Sections III-V](https://arxiv.org/html/quant-ph/0204106v2): causal-past state dependence is compatible with a stated genuine-reduction hypothesis. Its emulator uses complete information and ideal computation; it is not our finite-cost source or collapse apparatus.
- [NIST DLMF 19.8.1 and 19.8.4](https://dlmf.nist.gov/19.8): the AGM identity supplies the stopping-time evaluation below. This standard identity is attributed, not discovered here.
- The attempted publisher retrieval of Weinberg's *Testing quantum mechanics* returned HTTP 403. No full-paper inspection is claimed. The homogeneous Hamiltonian framework is already referenced by Childs--Young; the derivatives and bounds below are derived explicitly.

This was one analytic pass, with no numerical trajectory, diagnostic run, provider review, experiment or formal verification selected. Small fixed examples cannot certify arbitrary n, composition or physical realization. The new ingredient relative to S281 is coherent detector reuse, not a changed ensemble averaging convention.

## 2. Complete variational generator and the null boundary

For any nonzero vector Psi write r=<Psi|Psi>, p=<Psi|P|Psi>/r and j=<Psi|J|Psi>/r. Define the real homogeneous degree-two functional

    F(Psi)=omega<Psi|N|Psi>+g sqrt(p)<Psi|J|Psi>.       (1)

On the unit sphere, for p>0 its Wirtinger gradient is

    G(Psi):=partial F/partial Psi*
       = H(Psi) Psi,
    H(Psi)=omega N+g sqrt(p)J
               + g j/(2 sqrt(p)) (P-pI).               (2)

The -pI term comes from normalization in p; omitting it changes the variational equation, even though a scalar term only changes a pure state's phase. The hypothetical dynamics is i dot(Psi)=G(Psi). Equation (2) is derived from (1), not a prescription to have an ordinary controller estimate unknown p and j.

Although the operator formula contains a quotient at p=0, the vector field has a unique regular extension there. Put x=P Psi, y=(I-P)Psi, s=||x||, z=Re<x,Jy>, for normalized Psi. Then j=2z and the nonlinear part divided by g is

    A(Psi)=s J Psi + R(x) Jy - s z Psi,
    R(x)v = x Re<x,v>/||x||   (x!=0),  R(0)v=0.        (3)

Here R is a real-linear operator on the realification of the complex Hilbert space. For any x,x',

    ||R(x)-R(x')|| <= 3 ||x-x'||.                       (4)

For s=||x||>=t=||x'||>0, expand the real outer products as

    xx^T/s - x'x'^T/t
      = (x-x')x^T/s + x'(x-x')^T/s
        + x'x'^T(1/s-1/t).

Their three norms are at most d, (t/s)d and (t/s)(s-t), where d=||x-x'||; the t=0 case is immediate. This proves (4) without a lower bound on s.

For normalized Psi,Phi, with d=||Psi-Phi||, the three terms in (3) have difference bounds 2d, 4d and 4d, respectively. The last uses |z|<=1 and |z-z'|<=2d; these deliberately loose constants suffice. Consequently

    ||A(Psi)-A(Phi)|| <= 10 ||Psi-Phi||.                (5)

At p=0 all terms in (3) vanish. The nonlinear part of F is O(||x||^2) near x=0, so its gradient is zero there and (3) is its continuous derivative. Normalization extends this to a locally Lipschitz field on the nonzero ambient vectors. Standard ODE uniqueness therefore applies; p=0 does not permit spontaneous departure from the null state. The apparent quotient in (2) is not a physical singularity or a source of nonunique trajectories. We claim a C1 energy with locally Lipschitz gradient, not a globally analytic functional at p=0.

## 3. What is conserved, and what is not established as energy

For p>0, H is Hermitian. At p=0 the continuous vector-field extension preserves the same identities. Thus norm is constant and

    dF/dt = 2 Re<G,dot(Psi)> = 0.                      (6)

Moreover <Psi|H|Psi>=F on normalized states, because <P-pI>=0. Since |<J>|<=Pr(N=1)<=<N> and sqrt(p)<=1,

    F >= (omega-g)<N> >= 0.                            (7)

The functional is therefore bounded below on normalized states when omega>=g, and homogeneity extends the nonnegativity to every vector. This is more than conservation of an arbitrarily defined time-dependent reset value: F generates the entire proposed flow.

Because H commutes with N, every projector onto an excitation sector commutes with H. Its Born probability is exactly conserved. The closed flow therefore preserves the entire distribution of the BARE observable omega N, not just its mean. The same statement holds with an arbitrary untouched reference tensor factor. It is a mathematical joint conservation law for two qubits; it does not provide switching, source, preparation or calorimeter dynamics.

There is a further important limit on its physical interpretation. Suppose one calls the instantaneous generator H(Psi) the conventional Born spectral-energy observable. On the amplifying orbit below, j=0, so

    <H> = omega(1-p0),
    <H^2> = (1-p0)[omega^2+g^2 p(t)].                  (8)

The second moment increases by g^2(1-p0)^2 between p(t)=p0 and p(t)=1, although F and every bare-N probability stay fixed. For example p0=1/16, omega=2, g=1 gives <H^2> initially 975/256 and finally 1200/256; <H>=15/8 throughout. Hence the usual spectral statistics of that state-dependent operator are NOT a conserved total energy distribution.

This is a test of one proposed energy interpretation, not a theorem that no nonlinear Hamiltonian theory can define an energy observable. A different operational energy/measurement law or additional source apparatus would have to be supplied and checked. Equation (7) alone does not close S278's energy-observable obligation. Calling F the energy does not specify how it is measured or how a device pays to generate (2).

## 4. Exact invariant orbit and logarithmic amplification time

The promised alternative has an exact solution

    Psi(t)=sqrt(p0)|gg>
      +sqrt(1-p0) exp(-i omega t)
        [cos(phi(t))|eg> - i sin(phi(t))|ge>],          (9)
    phi(0)=0,
    dot(phi)=g sqrt(p0+(1-p0)sin(phi)^2).              (10)

Indeed j=2 Re<Psi|ge><eg|Psi>=0 on (9). Both coefficient-derivative terms in (2) vanish on this orbit, while they remain present in the global law. Direct differentiation of (9) then gives (2) and (10). ODE uniqueness proves it is the actual solution, not just an ansatz with an omitted force. The null input |eg> has p=j=0 and remains exp(-i omega t)|eg>.

Let

    u_n = integral_0^(pi/2) [p0+(1-p0)sin(phi)^2]^(-1/2) dphi,
    T_n = u_n/g.                                      (11)

At T_n the alternative is entirely in the source-ground subspace, while the null is entirely source-excited. An ordinary measurement of S in {|g>,|e>} distinguishes them with success 1 in the exact pure-input model. Detector-only readout would instead have an alternative click probability 1-p0; we do not confuse the two readouts. Neither postselection nor intermediate measurement is used.

For 0<p0<=1/4, use sin(phi)<=phi and sin(phi)>=2phi/pi on [0,pi/2], and 1-p0>=3/4, to obtain

    asinh(pi/(2 sqrt(p0))) <= u_n
       <= (pi/sqrt(3)) asinh(sqrt(3)/(2 sqrt(p0)))
       <= (pi/sqrt(3)) [n log(2)+log(sqrt(3)+1)].       (12)

Thus T_n=Theta(n/g), uniformly in n. This is an analytic all-n bound. It does not follow from integrating finitely many trajectories. The input trace distance is sqrt(p0)=2^-n and the final source distance is 1, as permitted by the hypothesized nonlinearity; ordinary unitary evolution of a fixed Hamiltonian would not do this.

The schedule does not require the hidden label. By the standard AGM integral identity,

    u_n = pi/[2 M(1,2^-n)].                            (13)

The known n specifies the candidate alternative, including when the actual input is null. Computing this number is not an evaluation of an unknown instance's answer. Equation (13) does not, however, justify applying this one-promise schedule to an arbitrary unknown nonzero population.

### A paid classical schedule

The arithmetic overhead in (13) can be bounded without a real-number oracle. For exact AGM iterates a_0=1,b_0=2^-n, a_(k+1)=(a_k+b_k)/2, b_(k+1)=sqrt(a_k b_k), one has b_k<=M<=a_k. If q_k=a_k/b_k, then

    q_(k+1)=(q_k+1)/(2 sqrt(q_k))<=sqrt(q_k),
    q_(k+1)-1 <= (q_k-1)^2/8.                         (14)

After ceil(log2 n) steps, q<=2. Subsequently q-1 contracts by at least a factor 1/8 per step. Since u_n=O(n), another O(log(n+2)) steps make the bracket [pi/(2a_k),pi/(2b_k)] have any fixed requested width such as 1/100. All exact iterates lie in [2^-n,1].

Use directed rational intervals for addition, multiplication, division and square root. Rounding each AGM component to absolute error at most 2^-B gives relative error at most 2^(n-B). The two AGM updates are monotone and homogeneous, so componentwise relative error grows by at most a further rounding factor per step, not an exponential derivative in n. Taking B=n+O(log(n+2)) with a sufficiently large constant leaves the accumulated relative error o(1/n), and the interval for u_n still has fixed width. Square roots can be bracketed by bisection on B-bit dyadics in polynomial bit time. Pi needs only O(log(n+2)) accuracy bits for this fixed absolute u_n tolerance and can also be enclosed by a convergent rational series. These give polynomial classical time and storage in n; no optimal arithmetic exponent is claimed. This is an algorithmic bound, not an executed implementation benchmark.

Choose a rational dimensionless stopping time u_hat within 1/24 of u_n. Since |dphi/du|<=1, the alternative source-ground probability differs from its unit peak by at most (u_hat-u_n)^2<=1/576. The null state stays source-excited. Relative coupling calibration of order 1/n suffices for this timing component alone. A laboratory clock, source coefficient and coherence over T_n remain physical resources; the arithmetic bound does not supply them.

## 5. Stability contract and its unpaid implementation

The known free term omega N can be removed by an interaction-picture transformation. P and J commute with N, so the nonlinear vector field is unchanged under that transformation. Its Lipschitz constant is at most 10g by (5). For normalized pure-state trajectories, initial Euclidean vector error e0 and an integrated vector-field residual R_T=integral_0^T ||r(t)||dt give

    ||Psi_actual(T)-Psi_ideal(T)||
       <= exp(10gT) [e0+R_T].                          (15)

Pure-state trace distance is no greater than this vector distance. Thus e0+R_T<=exp(-10u_n)/24 is one sufficient model-error allowance for final trace error <=1/24. Together with an additional <=1/24 output allowance for timing/readout, total output error <=1/12 would imply success >=11/12, above the requested 2/3. These are explicit sufficient contracts, not a measured noise specification or an optimal robustness result. For open-system or mixed-state errors a corresponding trajectory/dilation bound must actually be proved; it is not supplied by relabeling such errors as r(t).

The sufficient tolerance in (15) is exponentially small in n, although its binary specification uses O(n) bits. Those bits do not establish affordable physical control. Nor does an exponentially small tolerance alone prove an exponential implementation cost. A native law might have exact structural protection of the null state; such protection and its preparation/noise model have not been derived here. There is also an elementary necessary preparation distinction: if an allowed preparation-noise set contains the same full physical input and source history for both promises, no deterministic evolution or measurement can recover the label. With a fixed density-state/source-history contract, trace-distance balls of radius >=2^(-n-1) overlap at the average density matrix. Equality of reduced density matrices alone is not asserted to identify every possible nonlinear theory's physical state. This is a scope warning about uniform adversarial preparation tolerance, not a lower bound on every structured circuit preparation.

Resources granted for the conditional theorem are one promised source state, one coherent detector, the exact autonomous law, a duration O(n/g), the computed schedule and ordinary final readout. Resources NOT supplied are a native p,j-dependent apparatus, a preparation theorem under the same source, its energy/work and noise, causal history acquisition/collapse, and a physical implementation of the sufficient error budget. More ordinary copies or tomography cannot be silently substituted at zero cost. No polynomial total physical-resource theorem follows from (12)-(15).

## 6. Retained references and causal composition: the existing obstruction persists

Extend (1) to a joint pure state on reference R and pair SB using P tensor I_R and J tensor I_R. Its gradient is generated on SB by the SAME H(p,j) in every reference component, with

    p=Tr(P rho_SB),  j=Tr(J rho_SB).                    (16)

This extension has positive global pure-state probabilities and a unique flow by the same proof as Section 2; positivity alone is not the missing computational guarantee. For a reference encoding the two inputs,

    |Xi(0)> = [|0>_R |eg> + |1>_R |psi_p0,g>]/sqrt(2),

the conditional SB vectors both evolve by one common time-dependent unitary U(t), even though U itself is determined nonlinearly by the joint state. Their inner product is therefore constant, and

    D(SB conditioned on R=0, SB conditioned on R=1)
       = sqrt(p0)=2^-n.                               (17)

Any local final measurement has equal-prior success at most (1+2^-n)/2, below 2/3 for n>=2. This is an application of S259/S280's shared-source argument, not a new independent impossibility theorem. Here retaining the detector changes S281's survival identity but does not change this source-composition hypothesis. Having access to the hidden reference label would be a different task; arbitrary programs with further accessible registers are not lower-bounded by (17).

An actual objective reduction in the causal past would change the source in (16) and could restore the isolated-input law. Kent's Sections III-V explicitly allow that sort of hypothesis and do not require the same instantaneous shared state after causal synchronization. The present closed Hamiltonian does NOT provide this collapse/source/apparatus law or the energy and precision account of such a device. Merely recording a measurement coherently supplies no such change. Immediate branchwise source assignment at a spacelike remote measurement is also not Kent's causal prescription.

Accordingly, (17) does not refute every possible nonlinear computer, nor does the full objective require solving this particular retained-reference task if a different paid causal preparation is constructed. It does refute the stronger transfer for this proposed law. Constructing a full causal alternative would be separate new structure, not an inference from the conditional pure-state result. The preregistered analytic stop is reached here; no further amplifier variant is commissioned.

## 7. Original-objective audit and decision

| Obligation | Authoritative evidence in this note | Status |
| --- | --- | --- |
| Derive all variational terms and define the zero boundary | (2)-(5), explicit outer-product Lipschitz proof | Discharged for the hypothetical closed flow |
| Positive normalized joint pure states and unique dynamics | Hermiticity, norm preservation, local Lipschitz extension | Discharged for that flow, including untouched references |
| Useful isolated-input amplification and paid schedule | Exact orbit (9)-(14), final source measurement | Conditional mathematical result; Theta(n/g), polynomial schedule arithmetic |
| Bare-energy statistics and lower-bounded generating functional | (6)-(7), excitation projector commutation | Discharged for the stated mathematical quantities |
| Conventional full generator-energy statistics | Counterexample (8) | Contradicted under that interpretation |
| Arbitrary retained-reference input transfer | Common-source invariant (17) | Contradicted in its stated scope; known bottleneck reapplied |
| Causal objective-collapse/source/apparatus law | No such law supplied by (1) | Missing |
| Polynomial total physical preparation/control/noise resources | Sufficient residual budget (15), no implementation | Missing |
| Empirical realization or ordinary BPP/BQP consequence | None | Not established |

General-bound improvement: none. Physical realization obligations discharged: none. Useful auxiliary mathematics: the complete regular Hamiltonian amplifier, energy-functional/bare-energy conservation, exact all-n orbit and paid schedule; the stability estimate is an elementary conditional consequence. External work: targeted transfer/AGM attribution, not independent validation of this proof or exhaustive novelty review. Operational work: isolated satellite, analytic evidence and planning reconciliation; no computational/physical experiment, formal certification, provider review or PaperMill action.

The protocol improved the investigation by allowing a genuine speculative construction, requiring the missing variational terms, and stopping at the source/energy/physical-cost boundary. The common-source failure is counted as the same underlying bottleneck, not another general advance. RETAIN the conditional result; PARK the claimed complete-device construction; successor SELECTION NONE. A future candidate must actually supply the changed causal source/preparation or operational apparatus law, not another gain function. Full objective remains active and unproved.

Remaining to-do list: none for this bounded construction/audit; full physical completion unresolved. This changes the next research decision because coherent exchange does remove the measured-detector cost obstruction, but its complete Hamiltonian still does not supply the causal source or paid physical error law needed for a nonlinear computer.
