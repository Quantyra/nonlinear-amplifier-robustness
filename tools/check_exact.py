"""One fixed rational Kraus/code diagnostic; not a proof of channel duality or limits."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
def eq(a,b,label):
 global count
 count+=1
 if a!=b:raise AssertionError(label)
def mat(m,n,f):return [[F(f(i,j)) for j in range(n)] for i in range(m)]
def diag(v):return mat(len(v),len(v),lambda i,j:v[i] if i==j else 0)
def trans(a):return [list(t) for t in zip(*a)]
def mul(a,b):return mat(len(a),len(b[0]),lambda i,j:sum(a[i][k]*b[k][j] for k in range(len(b))))
def add(a,b):return mat(len(a),len(a[0]),lambda i,j:a[i][j]+b[i][j])
def scale(a,c):return [[c*x for x in row] for row in a]
def kron(a,b):return mat(len(a)*len(b),len(a[0])*len(b[0]),lambda i,j:a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])])
def inner(a,b):return mul(trans(a),b)
def total(xs):
 result=scale(xs[0],0)
 for x in xs:result=add(result,x)
 return result
I=diag([1,1]);I4=diag([1]*4);Ns=kron(diag([0,1]),I);Nb=kron(I,diag([0,1]));P=add(I4,scale(Ns,-1))
J=mat(4,4,lambda i,j:1 if (i,j) in [(1,2),(2,1)] else 0)
# Ancilla basis is (logical label j, support flag f); detector is always g.
V=mat(16,2,lambda i,j: (F(3,5) if j==0 else F(4,5)) if i==2*j else ((F(4,5) if j==0 else F(3,5)) if i==8+2*j+1 else 0))
eq(inner(V,V),I,'code isometry')
Pv=inner(V,mul(kron(P,I4),V));Jv=inner(V,mul(kron(J,I4),V))
eq(Pv,diag([F(9,25),F(16,25)]),'source compression')
eq(Jv,diag([0,0]),'exchange compression zero')
eq((Pv[1][1]-Pv[0][0])/2,F(7,50),'source spectral radius')
eq(inner(mul(kron(J,I4),V),mul(kron(J,I4),V)),diag([F(16,25),F(9,25)]),'native leakage is nonzero')
rows=[]
for s,t in [(F(1),F(0)),(F(4,5),F(3,5)),(F(3,5),F(4,5)),(F(0),F(1))]:
 gamma=t*t;eq(s*s+gamma,1,'damping normalization')
 A0=diag([1,s]);A1=[[F(0),t],[F(0),F(0)]]
 # Environment order 00,10,01,11.
 K=[kron(A0,A0),kron(A1,A0),kron(A0,A1),kron(A1,A1)]
 eq(total([inner(k,k) for k in K]),I4,'complete Kraus channel')
 eq(add(inner(K[1],K[1]),inner(K[3],K[3])),scale(Ns,gamma),'source jump effect')
 eq(add(inner(K[1],K[2]),inner(K[2],K[1])),scale(J,gamma),'exchange environment observable')
 eq(add(inner(K[1],K[1]),inner(K[2],K[2])),scale(add(add(Ns,Nb),scale(mul(Ns,Nb),-2*gamma)),gamma),'single jump probability')
 branches=[mul(kron(k,I4),V) for k in K]
 eq(inner(branches[0],branches[0]),diag([1-gamma*F(16,25),1-gamma*F(9,25)]),'no jump norms')
 eq(inner(branches[1],branches[1]),diag([gamma*F(16,25),gamma*F(9,25)]),'source jump norms')
 eq(inner(branches[0],branches[1]),diag([0,0]),'syndrome orthogonality')
 eq(branches[2],mat(16,2,lambda i,j:0),'detector jump absent')
 eq(branches[3],mat(16,2,lambda i,j:0),'double jump absent')
 rows.append({'gamma':str(gamma),'source_defect':'7/50'})
eq((1-F(24,25))/2,F(1,50),'gamma one dephasing error')
result={'status':'pass','assertions':count,'maximum_matrix_dimension':16,'damping_choices':rows,'zero_damping_role':'control only; theorem requires gamma>0','scope':'exact finite Kraus/source/code/syndrome substitutions, not channel-duality or asymptotic validation','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
(R/'verification/exact-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
