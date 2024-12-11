# --------------------------------------------------------------------------------
# --- распределение очередей, график вынесен в функцию---
# --------------------------------------------------------------------------------
from pulp import LpMinimize, lpSum, LpProblem, LpVariable,LpBinary, LpStatus, value
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# загрузка из xls
file_path = 'plan_data.xlsx'
df = pd.read_excel(file_path, sheet_name='jobs')
# -------список работ ['J1', 'J2',....]-------(C)
list_jobs = df.iloc[:, 0].tolist() 

df = pd.read_excel(file_path, sheet_name='tasks')
# -------Формирование словаря задач-------(tasks)
TASKS = {}
for index, row in df.iterrows():
    jid = row['job']
    resurs = row['machine']
    work_time = row['duration']
    # Создаем вложенный словарь, если jid еще не существует в результирующем словаре
    if jid not in TASKS:
        TASKS[jid] = {}
    # Добавляем resurs и work_time в вложенный словарь
    TASKS[jid][resurs] = work_time

print(TASKS)
# ------Список ресурсов----
resours = df.drop_duplicates(subset=['machine']) 
res = resours['machine'].tolist()
#------------

def solve_model(): # Описание модели
    # Инициализация модели
    model = LpProblem("optimalPlan", LpMinimize)

    #Вспомогательные переменные
    jobs = list(TASKS.keys())# Список работ (job1, job2, ...)
    machines = set(machine for job in TASKS.values() for machine in job.keys()) # Все машины [R1, R2, R3]
    task_list = [(job, machine) for job, machine in TASKS.items() for machine in machine.keys()] # Список пары job, machine (job1, R1), (job2, R1)...
    #---------------------------------- Инициализация переменных----------------------------
    start_times = LpVariable.dicts("start", TASKS.keys(), lowBound=0, cat='Integer') # Переменные времени начала
    completion_times = LpVariable.dicts("completion", TASKS.keys(), lowBound=0, cat='Integer') # Переменные времени завершения

    #---------------------------------- Построение целевой функции -------------------------------------------
    model += lpSum(completion_times[t] for t in TASKS)

    #-----------------------------------Ограничения-----------------------------------------------------------

    # -------Ограничение по последовательности -----
    df = pd.read_excel(file_path, sheet_name='constr') # открываем df с ограничениями (jid - ограничение, jid_in - ограничение входящее в jid)
    i=0 # переменная для формирования имени ограничения
    for index, row in df.iterrows(): # цикл по df
        model += completion_times[row['job_prev']] <= start_times[row['job_cur']], f'lim_line_{i}'
        i+=1
    #-------------------------------------------------------------------------------------------
    # ---------Ограничение что время завершения должно быть равно заданному времени---------------------------
    t_total =0 # сумарное время выполнения всех операций
    for task, options in TASKS.items(): # цикл по tasks
        resource_time = list(options.values())[0]  # Получаем время выполнения выбранной операции
        t_total += resource_time
        model += completion_times[task] == start_times[task] + resource_time, f'lim_time_{task}'
    # ---------------------тест ограничений-----------------------------
    # Ограничение = время окончания текущей работы(i) на машине R <= время начала другой работы(k) на машине R И время окончания 
    # другой работы (k) на машине R  <= время начала текущей работы(i) на машине R
    # Группируем работы по ресурсам 
    resources_to_jobs = {}
    for jid, resources in TASKS.items():
        for time in resources.keys():
            if time not in resources_to_jobs:
                resources_to_jobs[time] = []
            resources_to_jobs[time].append(jid)
    #Добавляем дизъюнктивные ограничения
    # last_key = next(reversed(resources_to_jobs))
    for r, job_list in resources_to_jobs.items():
        for i in range (len(job_list)-1):     
            for j in range(i+1, len(job_list)-1):
                jid1 = job_list[j]
                jid2 = job_list[i]
                model+= start_times[jid1]>=start_times[jid2]+completion_times[jid2]
                model+= start_times[jid2]>=start_times[jid1]+completion_times[jid1]
        if i == len(job_list)-1:
            model+= start_times[job_list[i]]>=start_times[job_list[0]]+completion_times[job_list[0]]
            
            
    print(resources_to_jobs)

        

    # ----------Сохранение задачи в файл-----------------------------------------------------------------------
    model.writeLP("planModel.lp")

    # ----------Решение----------------------------------------------------------------------------------------
    model.solve()
    return(model)

solve1 = solve_model()
# Проверяем статус модели
print("Status", LpStatus[solve1.status])

# Значение целевой функции после решения задачи
obj_value = value(solve1.objective)
obj_value = int(obj_value)  # Преобразование в целочисленное значение

# print(f"Минимальное время выполнения всех операций = {obj_value}")
# # ---Вывод переменных
# for v in solve1.variables():
#     print(v.name, "=", v.varValue)

# Вывод графика распределения операций
def plot_schedule ():
    for c in list_jobs: # Определяем длинну линии по старту и завершению операции циклом по списку всех операций
        for i in solve1.variables(): # Цикл по переменным модели
            if i.name.startswith(f"start_" + c): # проверяем имя переменной на начало операции (в с указан id операции J1,J2...Jn)
                x1 = i.varValue # Если да то присваиваем координату x1
            if i.name.startswith(f"completion_" + c): # Прверяем имя переменной на завершение операции
                x2 = i.varValue # Если да то присваиваем координату x2
                y  = int(list(TASKS.get(c))[0][1:]) # Определяем ресурс и записываем в координату y (срезаем "R")
    # --------
        plt.plot([x1, x2], [y, y],  marker='d', linewidth=5, markersize=10)# Рисуем линию с маркерами
        # добавляем подпись с кодом операции (J)
        mid_x = (x1 + x2) / 2  # X-координата для подписи
        mid_y = (y + y) / 2  # Y-координата для подписи
        plt.text(mid_x, mid_y, c, fontsize=10, ha='center', va='center') 
    # -------   
    plt.xlim (0,100)  # (0, obj_value+1)  -- ограничение графика по оси X
    plt.yticks(np.arange(0, len(resours)+2, 1.0)) # ограничение оси Y
    plt.title = (f"Минимальное время выполнения всех операций ")
    plt.grid()
    plt.show()
   
plot_schedule()

