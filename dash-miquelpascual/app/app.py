import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from flask import Flask
# Load data
from sqlalchemy import create_engine

server = Flask(__name__)
app = dash.Dash(server=server, external_stylesheets=[dbc.themes.FLATLY])
app.title = 'miquelpascual_plotlyEEX'

dialect='mysql+pymysql://root:Bigdata2122@192.168.193.133:3306/scrapping'
sqlEngine=create_engine(dialect)
dfLlistaElectricitat=pd.read_sql('miquelpascual_valorseex',con=sqlEngine)

fig = go.Figure()

fig.add_trace(go.Scatter(x=dfLlistaElectricitat['dia'], y=dfLlistaElectricitat['m1'],
                    mode='lines',name='m1'))
fig.add_trace(go.Scatter(x=dfLlistaElectricitat['dia'], y=dfLlistaElectricitat['m2'],
                    mode='lines',name='m2'))
fig.add_trace(go.Scatter(x=dfLlistaElectricitat['dia'], y=dfLlistaElectricitat['m3'],
                    mode='lines',name='m3'))

fig.update_layout(go.Layout(xaxis = {'title':'Dies'},
    yaxis = {'title':'eex'},title="Web Scrapping eex"))

# Initialize the app
app.config.suppress_callback_exceptions = True

navbar = dbc.Navbar(
    [dbc.NavbarBrand("Exercici Web Scrapping Miquel Pascual"),
    ],
    color="#E93636",
    className="justify-content-center",
    style={"height":"100px"},
    dark=True
)

grafica1=dcc.Graph(id='grafica1', 
                    figure = fig,
        )

def serve_layout():
	return html.Div(children=[navbar,
    	dbc.Row([
        dbc.Col(html.Div([grafica1]),width=12),
       	]),
    	dbc.Row([
        dbc.Col(html.Div([dbc.Alert("Dissenyat per Miquel Pascual", 		color="#E93636", style ={'textAlign': 'center', 'color':'white', 		'marginTop':'100px'})
                          ]))
    	])
    	])

app.layout =  serve_layout
    
if __name__=='__main__':
    app.run_server()
