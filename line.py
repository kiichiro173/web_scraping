
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go 
import pandas as pd 

df = pd.read_csv('./Dash/time_series.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id='sample-line',
        figure={
            'data':[
                go.Scatter(
                    x = df["date"] , y = df["MSFT"] , mode = 'lines',opacity = 0.7 , marker={
                        'size':15
                    },
                    name='Microsoft'
                )
            ]
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
