"""Run the fixed S291 diagnostic once with the preregistered 60-second cap."""
import datetime,json,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
row={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cap_seconds':60,'command':'python -B tools/check_exact.py'}
try:
 p=subprocess.run([sys.executable,'-B',str(R/'tools/check_exact.py')],cwd=R,capture_output=True,text=True,encoding='utf-8',timeout=60)
 row.update(exit_code=p.returncode,within_cap=True,stdout=p.stdout,stderr=p.stderr)
except subprocess.TimeoutExpired as e:row.update(exit_code=None,within_cap=False,error=str(e))
row['wall_seconds']=time.perf_counter()-start
(R/'verification/exact-process.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
print(json.dumps(row));sys.exit(0 if row.get('exit_code')==0 else 1)
