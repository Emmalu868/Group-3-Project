import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
# Connect to main app.py file
from app import app
# Connect to your app pages
from apps import homePage, K, S, H, W


#------------------------------------

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "26rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H6("UofT FinTech Boot Camp ", className="display-4"),
        html.Hr(),
       # html.H3(
        #     " ", className='text-center text-primary mb-3'
        # ),
        dbc.Nav(
            [dbc.NavLink("Home", href='/apps/homePage', active="exact"),
            dbc.NavLink("Page K", href='/apps/K', active="exact"),
            dbc.NavLink("Page S", href='/apps/S', active="exact"),
            dbc.NavLink("Page H", href='/apps/H', active="exact"),
            dbc.NavLink("Page W", href='/apps/W', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/homePage': 
        return homePage.layout
    if pathname == '/apps/K': 
       return K.layout
    if pathname == '/apps/S':
        return S.layout
    if pathname == '/apps/H':
        return H.layout
    if pathname == '/apps/W':
        return W.layout
    else:
        return homePage.layout 


if __name__ == '__main__':
    app.run_server(debug=True)