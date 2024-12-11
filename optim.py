import pandas as pd
from pulp import LpProblem, LpStatus, LpVariable, LpBinary,LpMinimize, lpSum
import matplotlib.pyplot as plt

#Чтение Excel файла
tasks_df = pd.read_excel("plan_data.xlsx", sheet_name="tasks")
constr_df = pd.read_excel("plan_data.xlsx", sheet_name = "constr")

#Преобразование данных в подходящий формат
tasks = {(row['job'], row['machine']): row['duration'] for _, row in tasks_df.iterrows()}
constraints = [(row['job_cur'], row['job_prev']) for _, row in constr_df.iterrows()]

#Создание задачи минимизации
model = LpProblem("Optimisation", LpMinimize)

#Список работ и машин
jobs = set(job for job, machine in tasks.keys())
machines = set(machine for job,machine in tasks.keys())

#Переменные: время начала и конца выполнения для каждой работы
start =LpVariable.dicts("start", jobs, lowBound=0, cat="Integer")
end = LpVariable.dicts("end", jobs, lowBound=0,cat="Integer")

#Переменная для порядка выполнениея работ на одной машине
order = LpVariable.dicts("order", [(job1, job2, machine1)for job1, machine1 in tasks.keys() for job2,machine2 in tasks.keys() if machine1 == machine2
                                   and job1!=job2], cat=LpBinary)

#Зависимости между работами 
for job1, job2 in constraints:
    model += start[job1]>=end[job2]

for job,machine in tasks.keys():
    model += end[job] == start[job] + tasks[(job, machine)]

#Ограничение на порядок выполнения работ на одной машине
for machine in machines:
    #Список работ, выполняющихся на этой машине
    machines_tasks = [(job, m) for job, m in tasks.keys() if m == machine]
    #Для каждой пары работ на одной машине, добавляем ограничение
    for i , (job1, m1) in enumerate(machines_tasks):
        for j, (job2,m2) in enumerate(machines_tasks[i+1:], start=i+1):
            #Добавляем ограничения: если job1 выполняется раньше, чем job2
            model+= start[job1]+ tasks[(job1,machine)] <= start[job2] + (1-order[job1, job2,machine])*1e6
            model+= start[job2]+ tasks[(job2,machine)] <= start[job1] + order[job1,job2,machine]*1e6




# Минимизация времени завершения (makespan)
makespan = LpVariable("Makespan", lowBound=0, cat = "Integer")
model+= makespan

#Ограничения на makespan
for job in jobs:
    model+= makespan >= end[job]

#Решение модели
model.solve()
print(LpStatus[model.status])
#Получение времени начала и кончания работ
start_times = {job:start[job].value() for job in jobs}
end_times = {job:end[job].value() for job in jobs}

for job in jobs:
    print(f"job {job}: start = {start_times[job]}, end = {end_times[job]}")

#Построение графика
fig, ax =plt.subplots(figsize=(10,6))
for job in jobs:
    ax.barh (job, end_times[job] - start_times[job], left = start_times[job], height = 0.5)

ax.set_xlabel("Time")
ax.set_ylabel("Jobs")

plt.show()