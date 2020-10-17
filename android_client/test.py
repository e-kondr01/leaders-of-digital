from datetime import datetime


job_started = 1602958135007 // 1000
job_started_dt = datetime.fromtimestamp(job_started)
print(type(job_started_dt))