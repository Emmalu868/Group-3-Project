from typing import Container
import dash
from dash import Dash, html, dcc
#from dash import dcc
#from dash import html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app
import pandas as pd
import pathlib

# get relative data folder
#PATH = pathlib.Path(__file__).parent
#IMG_PATH = PATH.joinpath("../assets").resolve()

#dfg = pd.read_csv(DATA_PATH.joinpath("theData_IfWeHave.csv"))

card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/pump-jack.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("This is the title of our project", className="card-title"),
                html.H6(
                    "sub title, if we have ",
                    className="card-text",
                ),
                html.P(
                    "Some introduction",
                    className="card-text",
                ),
                dbc.CardLink("GitHub", href="https://github.com/Emmalu868/Group-3-Project"),
            ]
        ),
    ],
    #style={"width": 1000, "height": 1000},
    #style = { "width": '80%' }
)



#-----------------------------------------
layout = html.Div([
    html.Div(html.H2("Gasoline report"), style={"text-align":"center"}),
    html.Hr(),
    #----------
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(card1),
            ],xs=12, sm=12, md=12, lg=11, xl=11),
            

         ],
         #justify='around', # around; between
         align='right'),   #center
         
         ],fluid=True),
    

]),

