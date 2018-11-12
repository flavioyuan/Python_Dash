# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Leitura do arquivo

df = pd.read_csv("BVSP.csv")
df = df.reindex(index=df.index[::-1])

colors = {
    'background': 'black',
    'background2': 'lightgreen',
    'text': 'powderblue',
    'text2': 'black'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for Python.''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    dcc.Graph(
        id='example-graph-3',
        figure={
            'data': [
                {'x': df["Data"], 'y': df["IndiceR"], 'type': 'line', 'name': 'BVSP  Real'},
                {'x': df["Data"], 'y': df["IndiceUSD"], 'type': 'line', 'name': 'BVSP USD'},
            ],
            'layout': {
                'title': 'BOVESPA',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)