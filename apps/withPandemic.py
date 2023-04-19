from typing import Container
import dash
from dash import Dash, html, dcc
# from dash import dcc
# from dash import html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app
import pandas as pd
import pathlib

# get relative data folder
# PATH = pathlib.Path(__file__).parent
# IMG_PATH = PATH.joinpath("../assets").resolve()

# dfg = pd.read_csv(DATA_PATH.joinpath("theData_IfWeHave.csv"))

card4 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/correlation_bf_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),

card5 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/growth_canada_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),

card6 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/growth_france_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),

card7 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/growth_japan_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),

card8 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/growth_UK_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),

card9 = dbc.Card(
    [
        dbc.CardBody(
            # [
            #     html.H5("Correlation between gasoline price and airline stocks",
            #             className="card-title"),
            #     # html.P(
            #     #     "Introduction ",
            #     #     className="card-text",
            #     # ),

            # ]
        ),
        dbc.CardImg(src="/assets/growth_USA_pandemic.png", top=True),
    ],
    # style={"width": "45%"},
),


# -----------------------------------------
layout = html.Div([
    html.Div(html.H2("Trend Analysis of Gasoline Prices before and after Pandemic"),
             style={"text-align": "center"}),
    html.Hr(),

    # --------------------
    dbc.Container([
        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card4),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),

        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card5),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),

        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card6),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),

        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card7),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),

        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card8),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),

        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card9),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),
        # ------------------

    ], fluid=True),


]),
