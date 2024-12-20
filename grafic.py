from matplotlib import pyplot as plt


def paint_grafic(machines,tasks,start_times, end_times,):
    #Построение графика
    fig, ax =plt.subplots(figsize=(10,6))

    #Добавляем задачи на график
    for machine in sorted(machines):
        machines_tasks = [(job, m) for job, m in tasks.keys() if m == machine]  
        for job,m in machines_tasks:
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
    ax.set_xticks(range(0, int(max(end_times.values())) +10, 10))
    ax.set_yticks(sorted(machines))
    ax.grid(True, axis='x')
    plt.show()