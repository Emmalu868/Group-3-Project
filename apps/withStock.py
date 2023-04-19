
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

# ----------Datasets-----------------------
# -- Import and clean data (importing csv into pandas)
# For choropleth
# df_gasPrice = pd.read_csv(r"./Resources/corr_gasPrice.csv", sep=",")

# df_airPrice = pd.read_csv(r"./Resources/corr_airPrice.csv", sep=",")
df_air_gas = pd.read_csv(r"./Resources/concat_gas_airPice.csv", sep=",")

df_Melt_airChange = pd.read_csv(r"./Resources/melt_airPctChange.csv", sep=",")

df_Melt_airprice = pd.read_csv(r"./Resources/melt_airPice.csv", sep=",")

df_gas = pd.read_csv(r"./Resources/for_animation_year.csv", sep=",")


def melt_dataset(df):
    data = df.drop(['Year'], axis=1, inplace=False)
    data = data.set_index('Date').T.rename_axis(
        'regions').rename_axis(columns=None).reset_index()
    time_lines = data.columns.to_list()[1:]
    df_melt = pd.melt(data, id_vars=['regions'],
                      value_vars=time_lines,
                      var_name='day', value_name='price', ignore_index=False)

    df_melt.sort_values(["day", "regions"], inplace=True)
    return df_melt
# ------------------------------------------------------


card3 = dbc.Card(
    [
        # dbc.CardImg(src="/assets/CorrelationAirline.png", top=True),
        dbc.CardBody(
            [
                html.H5("Correlation between gasoline price and airline stocks",
                        className="card-title"),
                # html.P(
                #     "Introduction ",
                #     className="card-text",
                # ),

            ]
        ),
        dbc.CardImg(src="/assets/CorrelationAirline.png", top=True),
    ],
    # style={"width": "45%"},
),

# -----------------------------------------
layout = html.Div([
    html.Div(html.H2("Examining the Relationship Between Oil Price and Stocks"),
             style={"text-align": "center"}),
    html.Hr(),
    # --------------------
    dbc.Container([
        dbc.Row([
            # dbc.Col([
            #     html.Div(card2),
            # ], xs=12, sm=12, md=12, lg=4, xl=4),
            dbc.Col([
                html.Div(card3),
            ], xs=12, sm=12, md=12, lg=9, xl=9),

        ], justify='around'),


    ], fluid=True),
    # ----------
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Br(),
                    html.H4("Please select the country",
                            style={'text-align': 'left'}),

                    dcc.Dropdown(id="slct_region",
                                 options=[
                                    {"label": "Canada", "value": "Canada"},
                                    {"label": "France", "value": "France"},
                                    {"label": "Germany", "value": "Germany"},
                                    {"label": "Japan", "value": "Japan"},
                                    {"label": "UK", "value": "UK"},
                                    {"label": "USA", "value": "USA"}
                                 ],
                                 multi=False,
                                 value='Canada',
                                 style={'width': "60%"}
                                 ),

                    html.Div(id='output_container2', children=[]),
                    html.Br(),

                ]),
            ], xs=12, sm=12, md=12, lg=10, xl=10),

        ], justify='around'),


    ], fluid=True),
    # ----------
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Correlation between Airline Stocks Prices and Gasoline Prices for the Selected Country",
                            style={'text-align': 'left'}),
                    dcc.Graph(id='corr', figure={}),
                    html.Br(),
                ]),
            ], xs=12, sm=12, md=12, lg=10, xl=10),

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

                    dcc.Dropdown(id="slct_year1",
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
                                 style={'width': "60%"}
                                 ),

                    html.Div(id='output_container1', children=[]),
                    html.Br(),
                ]),
            ], xs=12, sm=12, md=12, lg=10, xl=10),

        ], justify='around'),


    ], fluid=True),
    # ----------
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Airline Stocks Prices Fluctuations for the Selected Year",
                            style={'text-align': 'left'}),
                    dcc.Graph(id='ailinePrice', figure={}),
                    html.H5("Airline Stocks Prices Monthly Percentage Chage for the Selected Year",
                            style={'text-align': 'left'}),
                    dcc.Graph(id='ailineChange', figure={}),
                    html.H5("International Gasoline Prices Fluctuations for the Selected Year",
                            style={'text-align': 'left'}),
                    html.Br(),
                    dcc.Graph(id='gas', figure={}),
                    html.Br(),

                ]),
            ], xs=12, sm=12, md=12, lg=10, xl=10),

        ], justify='around'),


    ], fluid=True),
    # ----------

]),


# --------------------------------------------------------

# Airline Stocks Prices Vs. Airline Stocks Prices for the Selected Country
@ app.callback(
    [Output(component_id='output_container2', component_property='children'),
     Output(component_id='corr', component_property='figure')],
    [Input(component_id='slct_region', component_property='value')]
)
def update_fig(region):

    container_region = "The region chosen by user was: {}".format(region)

    fig = px.scatter(df_air_gas, x=region, y=region.lower(), trendline="ols",
                     ).update_layout(
        xaxis_title="Gasoline Prices", yaxis_title="Airline Stocks Prices"
    )
    return container_region, fig

# Airline Stocks Prices Fluctuations for the Selected Year


@ app.callback(
    [Output(component_id='output_container1', component_property='children'),
     Output(component_id='ailinePrice', component_property='figure')],
    [Input(component_id='slct_year1', component_property='value')]
)
def update_fig(year):
    print(year)
    container_year = "The year chosen by user was: {}".format(year)

    dff_airPrice = df_Melt_airprice.copy()
    dff_airPrice = dff_airPrice[dff_airPrice["Year"] == year]

    # print('data for airline price')
    print(dff_airPrice[:6])

    fig = px.line(
        dff_airPrice, x="day", y="price",
        color="regions",
        hover_name='regions').update_layout(
        xaxis_title="Date", yaxis_title="Airline Stocks Prices"
    )

    return container_year, fig

# Airline Stocks Prices Monthly Percentage Chage for the Selected Year


@ app.callback(
    Output(component_id='ailineChange', component_property='figure'),
    Input(component_id='slct_year1', component_property='value')
)
def update_fig(year):
    print(year)
    dff_airChange = df_Melt_airChange .copy()
    dff_airChange = dff_airChange[dff_airChange["Year"] == year]

    # print('data for change price')
    print(dff_airChange[:6])
    fig = px.line(
        dff_airChange, x="day", y="price",
        color="regions",
        hover_name='regions').update_layout(
        xaxis_title="Date", yaxis_title="Airline Stocks Prices Monthly Percentage Chage"
    )

    return fig

# International Gasoline Prices Fluctuations for the Selected Year


@ app.callback(
    Output(component_id='gas', component_property='figure'),
    Input(component_id='slct_year1', component_property='value')
)
def update_fig(year):
    print(year)
    dff_gas = df_gas.copy()
    dff_gas = dff_gas[dff_gas["Year"] == year]
    # print('data for gas price')
    print(dff_gas[:5])
    fig = px.line(
        dff_gas, x="day", y="price",
        color="regions",
        hover_name='regions').update_layout(
        xaxis_title="Date", yaxis_title="Gasoline Prices"
    )

    return fig
