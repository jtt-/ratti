# AIKATAULUDATAAN LIITTYVÄ GRAFIIKKA

import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import app.ontime.wrangle as wr
import json

# PYSÄKKIKOHTAINEN VIIVE

def ontime_stop_graph(stop):

    df = wr.get_events_by_stop(stop).reset_index()
    lines = df["LINE_CODE"].unique()
    traces = []

    for line in lines:
        df_by_line = df[df["LINE_CODE"] == line]
        traces.append(go.Scatter(x=df_by_line["OPD_DATE"], y=df_by_line["ARR_TIME_DELAY"], mode="markers", name = str(line)))

    data = traces
    layout = go.Layout(title = stop, xaxis = {"title":"Päivämäärä"}, yaxis = {"title":"Viive (s)","range":[-1000,3000]}, showlegend = True)
    figure = go.Figure(data=data,layout=layout)
    graph = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)

    return graph
