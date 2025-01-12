from dash import html, dcc
from data_access import (
    get_data,
    get_switch_names,
    get_switch_manufacturers,
    get_switch_types,
)
from dash import dash_table

df = get_data()

app_layout = [
    html.H1(children="SwitchViz"),
    html.P(
        "A visualization of mechanical keyboard switches based on ThereminGoat's Switches data."
    ),
    html.H3(children="Filters"),
    html.Div(
        id="dropdown-container",
        children=[
            dcc.Dropdown(
                get_switch_names(),
                id="dropdown-switch-name",
                multi=True,
                placeholder="Filter By Switch Name",
            ),
            dcc.Dropdown(
                get_switch_types(),
                id="dropdown-switch-type",
                multi=True,
                placeholder="Filter By Switch Type",
            ),
            dcc.Dropdown(
                get_switch_manufacturers(),
                id="dropdown-switch-manufacturer",
                multi=True,
                placeholder="Filter By Manufacturer",
            ),
        ],
    ),
    html.H3(children="Rescaled Switch Metrics"),
    dcc.Graph(id="graph-content"),
    dash_table.DataTable(
        df.to_dict("records"),
        [{"name": i, "id": i} for i in df.columns],
        id="item-table",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=25,
    ),
    html.H3(children="Data Source"),
    html.P(
        [
            "The data used in this visualization is from ",
            html.A(
                "ThereminGoat's Switches blog",
                href="https://www.theremingoat.com",
                target="_blank",
            ),
            ".",
        ]
    ),
    html.H3(children="Project Information"),
    html.P(
        [
            "For more information about this project, please visit the ",
            html.A(
                "GitHub repository",
                href="https://github.com/nealhorner/SwitchViz",
                target="_blank",
            ),
            ".",
        ]
    ),
]
