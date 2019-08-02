# LUODAAN NOUSUTIETOIHIN LIITTYVÄ GRAFIIKKA

import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import json
import app.demand.wrangle as wr

def events_by_line_graph(line, startdate, enddate):
    df = wr.get_events_by_line(line, startdate, enddate)

    data = [go.Bar(x=df['Tuote'], y=df['Total'])]

    layout = go.Layout(title="Linja " + line + " Aikaväli: " + str(startdate) + " - " + str(enddate), xaxis=dict(type="category"), showlegend=True)
    fig = go.Figure(data=data, layout=layout)

    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph
