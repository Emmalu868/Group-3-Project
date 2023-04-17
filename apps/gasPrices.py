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
import plotly.io as pio

# get relative data folder
# PATH = pathlib.Path(__file__).parent
# IMG_PATH = PATH.joinpath("../assets").resolve()

# dfg = pd.read_csv(DATA_PATH.joinpath("theData_IfWeHave.csv"))

# ----------Datasets-----------------------
# -- Import and clean data (importing csv into pandas)
# For choropleth
df = pd.read_csv(r"./Resources/for_choropleth.csv", sep=",")
df = df.groupby(['regions', 'Year', 'iso_alpha'])[
    ['price']].mean()
df.reset_index(inplace=True)
# print(df[:5])

# ----- For animation
df_ani = pd.read_csv(r"./Resources/for_animation_year.csv", sep=",")


# -----------------------------------------

card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/monthly_pump_price.png", top=True),
        dbc.CardBody(
            [
                html.H5("Gasoline Prices Fluctuations between 2012-2013",
                        className="card-title"),
                # html.P(
                #     "Introduction ",
                #     className="card-text",
                # ),

            ]
        ),
    ],
    # style={"width": "45%"},
),

card2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/pump_price_geoview.png", top=True),
        dbc.CardBody(
            [
                html.H5("Average Gasoline Prices between 2012-2013",
                        className="card-title"),
                # html.P(
                #     "Introduction",
                #     className="card-text",
                # ),

            ]
        ),
    ],
    # style={"width": "45%"},
),


# -------------------------------------------
layout = html.Div([
    html.Div(html.H2("International Gasoline Prices"),
             style={"text-align": "center"}),
    html.Hr(),
    # ----------
    dbc.Container([
        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card1),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),
        dbc.Row([
            dbc.Col([
                html.Div(card2),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),


    ], fluid=True),
    # ----------
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Br(),
                    html.H4("Please select the year",
                            style={'text-align': 'left'}),

                    dcc.Dropdown(id="slct_year",
                                 options=[
                                    {"label": "2012", "value": 2012},
                                    {"label": "2013", "value": 2013},
                                    {"label": "2014", "value": 2014},
                                    {"label": "2015", "value": 2015},
                                    {"label": "2016", "value": 2016},
                                    {"label": "2017", "value": 2017},
                                    {"label": "2018", "value": 2018},
                                    {"label": "2019", "value": 2019},
                                    {"label": "2020", "value": 2020},
                                    {"label": "2021", "value": 2021},
                                    {"label": "2022", "value": 2022},
                                    {"label": "2023", "value": 2023}],
                                 multi=False,
                                 value=2022,
                                 style={'width': "40%"}
                                 ),

                    html.Div(id='output_container', children=[]),
                    html.Br(),

                    dcc.Graph(id='my_map', figure={}),
                    html.Br(),

                    html.H3("International Gasoline Prices Fluctuations for the Selected Year",
                            style={'text-align': 'center'}),

                    html.P("Select an animation type:"),
                    dcc.RadioItems(
                        id='selection',
                        options=["Scatter", "Bar"],
                        value='Bar',
                    ),
                    # dcc.Graph(id='animation', figure={}),
                    dcc.Loading(dcc.Graph(id="animation"), type="cube"),
                    # html.Div(id="animation"),

                    html.Br(),
                    html.H3("International Gasoline Prices Fluctuations between 2012-2013",
                            style={'text-align': 'center'}),

                    html.P("Select an animation type:"),
                    dcc.RadioItems(
                        id='selection1',
                        options=["Scatter", "Bar"],
                        value='Scatter',
                    ),
                    dcc.Loading(dcc.Graph(id="animation1"), type="cube"),




                ])

            ], xs=12, sm=12, md=12, lg=11, xl=11),
        ],
            # justify='around', # around; between
            align='right'),  # center

    ], fluid=True),
    # ----------


])

# -------------------------------
# Connect the Plotly graphs with Dash Components


@ app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_map(option_slctd):
    # print(option_slctd)
    # print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    # print(dff)
    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locations="iso_alpha",
        color='price',
        hover_data=['regions', 'price'],
        projection='natural earth',
        # color_continuous_scale=px.colors.sequential.Turbo,
        labels={'Year average Gasoline Price': '% Canadian cents per litre'},
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )
    return container, fig

# Animation for selected year


@ app.callback(
    Output(component_id='animation', component_property='figure'),
    Input(component_id='slct_year', component_property='value'),
    Input(component_id='selection', component_property='value')
)
def update_graph(option_slctd, selection):
    dff1 = df_ani.copy()
    dff1 = dff1[dff1["Year"] == option_slctd]

    # print(dff1[: 9])

    if selection == "Scatter":
        fig = px.scatter(
            dff1, x="regions", y="price",
            color="regions",
            animation_frame="day",
            range_y=[0.00, 330.00],
            range_x=[-0.5, 5.5],
            animation_group="regions",
            title="International gasoline prices",
            labels={
                "price": "Monthly gasoline prices (Canadian cents per litre)", "regions": "Regions"}
        )
    if selection == "Bar":
        fig = px.bar(
            dff1, x="regions", y="price",
            color="regions",
            animation_frame="day",
            range_y=[0.00, 330.00],
            # range_x=[-0.5, 5.5],
            animation_group="regions",
            title="International gasoline prices",
            labels={
                "price": "Monthly gasoline prices (Canadian cents per litre)", "regions": "Regions"}
        )

    return fig

# Animation for whole 12 years


@ app.callback(
    Output(component_id='animation1', component_property='figure'),
    Input(component_id='selection1', component_property='value')
)
def update_graph1(selection1):
    if selection1 == "Scatter":
        fig = px.scatter(
            df_ani, x="regions", y="price",
            color="regions",
            animation_frame="day",
            range_y=[0.00, 330.00],
            range_x=[-0.5, 5.5],
            animation_group="regions",
            title="International gasoline prices",
            labels={
                "price": "Monthly gasoline prices (Canadian cents per litre)", "regions": "Regions"}
        )
    if selection1 == "Bar":
        fig = px.bar(
            df_ani, x="regions", y="price",
            color="regions",
            animation_frame="day",
            range_y=[0.00, 330.00],
            # range_x=[-0.5, 5.5],
            animation_group="regions",
            title="International gasoline prices",
            labels={
                "price": "Monthly gasoline prices (Canadian cents per litre)", "regions": "Regions"}
        )

    return fig
