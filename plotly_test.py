import plotly
import plotly.graph_objs as go

import plotly.express as px

from plotly.subplots import make_subplots
import numpy as np

import pandas as pd

x = np.arange(0, 5, 0.1)
def f(x):
    return x**2

# fig = px.scatter(x=x, y=f(x))
# fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f(x),   mode='lines+markers',name='f(x)=x<sup>2</sup>'))
fig.add_trace(go.Scatter(x=x, y=x,mode='markers', name='g(x)=x',
              marker=dict(color='LightSkyBlue', size=20, line=dict(color='MediumPurple', width=3))))
fig.update_layout(legend_orientation="h", 
                  legend=dict(x=.5, xanchor="center"),
                  title="Plot Title",
                    xaxis_title="x Axis Title",
                    yaxis_title="y Axis Title",
                    hovermode="x",
                  margin=dict(l=0, r=0, t=30, b=0))
fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
fig.show()