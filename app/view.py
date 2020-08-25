
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go 
import pandas as pd 
import datetime


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv("./data.csv")
dates = []
for _date in df["date"]:
  date = datetime.datetime.strptime(_date, '%Y/%m/%d').date()
  dates.append(date)

n_subscribers = df["subscribers"].values
n_reviews = df["reviews"].values

diff_subscribers = df["subscribers"].diff().values
diff_reviews = df["reviews"].diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = [
    html.H2(children = 'PythonによるWebスクレイピング～アプリケーション偏～'),
    html.Div(children=[
        dcc.Graph(
            id = 'subscriver_graph',
            figure={
                'data':[
                     go.Scatter(
                        x=dates,
                        y=n_subscribers,
                        mode = 'lines+markers',
                        name = "受講生総数",
                        opacity=0.7,
                        yaxis='y1'
                    ),  
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,              
                        name = '増加人数',
                        yaxis='y2'
                    )
        
                ],
                'layout':go.Layout(
                    title='受講生総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title="受講生総数" , side = 'left' , showgrid=False ,
                    range=[2500 , max(n_subscribers)+100]),
                    yaxis2=dict(title="増加人数" , side = 'right' , overlaying='y',showgrid=False ,
                    range=[0 , max(diff_subscribers[1:])]),
                    margin=dict(l=200 , r = 200 , b = 100 ,t = 100)
                )
            }
        ),
        dcc.Graph(
            id = 'review_graph',
            figure={
                'data':[
                     go.Scatter(
                        x=dates,
                        y=n_reviews,
                        mode = 'lines+markers',
                        name = "review総数",
                        opacity=0.7,
                        yaxis='y1'
                    ),  
                    go.Bar(
                        x=dates,
                        y=diff_reviews,              
                        name = '増加数',
                        yaxis='y2'
                    )
        
                ],
                'layout':go.Layout(
                    title='review総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title="review総数" , side = 'left' , showgrid=False ,
                    range=[0 , max(n_reviews)+10]),
                    yaxis2=dict(title="増加数" , side = 'right' , overlaying='y',showgrid=False ,
                    range=[0 , max(diff_reviews[1:])]),
                    margin=dict(l=200 , r = 200 , b = 100 ,t = 100)
                )
            }
        )
    ])

])




if __name__ == '__main__':
    app.run_server(debug=True)
