
import pandas as pd
from grafic import paint_grafic
from solve_model import solve

#Чтение Excel файла
tasks_df = pd.read_excel("plan_data.xlsx", sheet_name="tasks")
constr_df = pd.read_excel("plan_data.xlsx", sheet_name = "constr")
downtime_df = pd.read_excel("plan_data.xlsx", sheet_name = "downtime")

#Преобразование данных в подходящий формат
tasks = {(row['job'], row['machine']): row['duration'] for _, row in tasks_df.iterrows()} #{(j1, r1): d1}
constraints = [(row['job_cur'], row['job_prev']) for _, row in constr_df.iterrows()] # (job1, job2)

#Ограничения на начало (например, r1 простаивает с 10 до 20 )
downtime = {(row['job'],row['machine']):(row['duration'], row['dt_start'], row['dt_end']) for _, row in downtime_df.iterrows()} #{(DT1, R1): (10, 10, 20)}

# Добавть простои в виде job
downtime1 = {key:value[0] for key, value in downtime.items()}
tasks.update(downtime1)

#Список работ и машин
jobs = set(job for job, machine in tasks.keys())
machines = set(machine for job, machine in tasks.keys())


start_times,end_times = solve(jobs,constraints,tasks,machines,downtime)

for job in jobs:
        print(f"job {job}: start = {start_times[job]}, end = {end_times[job]}")

paint_grafic(machines,tasks,start_times,end_times)