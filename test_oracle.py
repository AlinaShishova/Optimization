import getpass
from matplotlib import pyplot as plt
import oracledb
from pulp import LpBinary, LpVariable, LpProblem, lpSum, LpStatus, LpMinimize, PULP_CBC_CMD, GLPK, SCIP, CHOCO_CMD


oracledb.init_oracle_client(lib_dir = "C:\instanclient\instantclient_19_25")

connection = oracledb.connect(
    user="111",
    password="111",
    dsn = "11.111.11.1:1521/db1p"
    )

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

cursor.execute("SELECT job, machine, duration FROM OPTIMIZATION_TASKS")

rows = cursor.fetchall()

tasks = {}


for row in rows:
    job, machine, duration = row
    tasks[(job, machine)] = duration


cursor.execute("SELECT job_cur, job_prev FROM OPTIMIZATION_CONSTR")

rows = cursor.fetchall()

constraints = []

for row in rows:
    job_cur, job_prev = row
    constraints.append((job_cur, job_prev))

print(tasks)
print(constraints)

cursor.close()
connection.close()




#Создание задачи минимизации
model = LpProblem("Optimisation", LpMinimize)

#Список работ и машин
jobs = set(job for job, machine in tasks.keys())
machines = set(machine for job,machine in tasks.keys())


#Переменные: время начала и конца выполнения для каждой работы
start =LpVariable.dicts("start", jobs, lowBound=0, cat="Integer")
end = LpVariable.dicts("end", jobs, lowBound=0,cat="Integer")

# Переменная для завершения времени каждой машины
machine_completion = LpVariable.dicts("mahine_completion", machines, lowBound=0, cat="Integer")

#Переменная для порядка выполнениея работ на одной машине
order = LpVariable.dicts("order", [(job1, job2, machine1)for job1, machine1 in tasks.keys() for job2,machine2 in tasks.keys() if machine1 == machine2
                                   and job1!=job2], cat=LpBinary)

#Зависимости между работами 
for job1, job2 in constraints:
    model += start[job1]>=end[job2]

#Конец выполнения = начало выполнения + время выполнения
for job,machine in tasks.keys():
    model += end[job] == start[job] + tasks[(job, machine)]

#Ограничение на порядок выполнения работ на одной машине
for machine in machines:
    #Список работ, выполняющихся на этой машине
    machines_tasks = [(job, m) for job, m in tasks.keys() if m == machine]
    #Для каждой пары работ на одной машине, добавляем ограничение
    for i , (job1, m1) in enumerate(machines_tasks):
        for j, (job2,m2) in enumerate(machines_tasks[i+1:]):
            #Добавляем ограничения: если job1 выполняется раньше, чем job2 и наоборот
            model+= start[job1]+ tasks[(job1,machine)] <= start[job2] + (1-order[job1, job2,machine])*1e6
            model+= start[job2]+ tasks[(job2,machine)] <= start[job1] + order[job1,job2,machine]*1e6
    #Ограничение для времени завершения машины: machine_completion >=  завершение всех задач на машине
    for job, m in machines_tasks:
        model+= machine_completion[machine]>= end[job]


#Целевая функция 
model+= lpSum(machine_completion[machine]for machine in machines)


#Решение модели
model.solve(PULP_CBC_CMD(timeLimit=60))
print(LpStatus[model.status])

#Получение времени начала и кончания работ
start_times = {job:start[job].value() for job in jobs}
end_times = {job:end[job].value() for job in jobs}

for job in jobs:
    print(f"job {job}: start = {start_times[job]}, end = {end_times[job]}")

#Построение графика
fig, ax =plt.subplots(figsize=(10,6))

#Добавляем задачи на график
for machine in sorted(machines):
    machines_tasks = [(job, m) for job, m in tasks.keys() if m == machine]  
    for job,m in machines_tasks:
        # ax.plot( [start_times[job], end_times[job] ], # интервал времени
        #         [machine,machine], # ось у - машина
        #         linewidth = 6,
        #         label = f"{job}")

        ax.barh(
            machine,
            end_times[job] - start_times[job],
            left=start_times[job],
            height=0.25,
            label = f"{job}"
        )
        #Добавляем надписи к названиям работ
        ax.text(
            (start_times[job]+end_times[job])/2, #центр интервала
            machine,
            job,
            ha = "center",
            va = "center",
            color = "black",
            fontsize = 12
        )


ax.set_xlabel("Время выполнения")
ax.set_ylabel("Ресурсы")
ax.set_xticks(range(0, int(max(end_times.values())) +5, 5))
ax.set_yticks(sorted(machines))
ax.grid(True, axis='x')
plt.show()
