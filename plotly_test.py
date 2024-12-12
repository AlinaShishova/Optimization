from plotly.figure_factory import create_gantt
# Make data for chart
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-30'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
# Create a figure
fig = create_gantt(df)
fig.show()