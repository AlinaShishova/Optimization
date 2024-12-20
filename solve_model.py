from pulp import  PULP_CBC_CMD, LpProblem, LpStatus, LpVariable, LpBinary,LpMinimize


def solve(jobs, constraints, tasks,machines, downtime):
    #Создание задачи минимизации
    model = LpProblem("Optimisation", LpMinimize)
    #Переменные: время начала и конца выполнения для каждой работы
    start =LpVariable.dicts("start", jobs, lowBound=0, cat="Integer")
    end = LpVariable.dicts("end", jobs, lowBound=0,cat="Integer")


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

    # Простои
    for (job, machine), (duration, dt_start, dt_end) in downtime.items():
        model+= start[job] >= dt_start
        model+=end[job]<=dt_end


    # #Целевая функция 
    model += sum(end[job]for job in jobs)

    #Решение модели
    model.solve(PULP_CBC_CMD(timeLimit = 60))
    print(LpStatus[model.status])
    model.writeLP("1.txt")

    #Получение времени начала и кончания работ
    start_times = {job:start[job].value() for job in jobs}
    end_times = {job:end[job].value() for job in jobs}

    return start_times, end_times