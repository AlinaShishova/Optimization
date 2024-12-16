import plotly.express as px
import pandas as pd

data = {
   ("Job 1","Resoursce A"): ("2024-12-01","2024-12-04" ),
   ("Job 2","Resoursce A"):("2024-12-05", "2024-12-08"),
   ("Job 3","Resoursce B"):("2024-12-03", "2024-12-06" ),
   ("Job 4","Resoursce C"):("2024-12-07", "2024-12-10" ),
   ("Job 5","Resoursce C"):("2024-12-10", "2024-12-12" ),

}

df = pd.DataFrame([
    {"Job":job, "Resource": machine, "Start":times[0], "Finish": times[1]}
    for (job, machine), times in data.items() 
])

fig= px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y = "Resource",
    color="Job",
    text = "Job",
    title="Диаграмма Ганта",
)

fig.update_traces(
    textposition ="inside",
    insidetextanchor = "middle",
    textfont = dict(size =12),

)

fig.update_yaxes(title="Resoures")
fig.update_layout(
    xaxis_title = "Data",
    showlegend=True,
    bargap = 0.8
)

fig.show()