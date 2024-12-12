from plotly.figure_factory import create_gantt
# Make data for chart
df = [dict(Task="Job A", Start='01', Finish='30'),
      dict(Task="Job B", Start='05', Finish='15'),
      dict(Task="Job C", Start='20', Finish='30')]
# Create a figure
fig = create_gantt(df)
fig.show()