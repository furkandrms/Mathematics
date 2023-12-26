import plotly.graph_objects as go 
from MetricSpaces import MetricSpace
def plot_points(points): 

    x, y = zip(*points)

    fig = go.Figure(data= go.Scatter(x=x, y=y, mode="markers", marker=dict(size=10)))
    fig.update_layout(title = "Two Points Of Metric Space",
                      xaxis_title = "X",
                      yaxis_title = "Y",
                      margin = dict(l=40, r=40, b=40, t=40))
    fig.show()


