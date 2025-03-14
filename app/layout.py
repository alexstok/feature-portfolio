from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return html.Div([
        html.H1("Dashboard de FIIs"),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='Visão Geral', children=[
                html.Div(id="overview-content")
            ]),
            dcc.Tab(label='Portfólio', children=[
                html.Div(id="portfolio-content")
            ])
        ])
    ])