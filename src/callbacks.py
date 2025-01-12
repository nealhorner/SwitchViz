from dash import callback, Output, Input
from data_access import get_data
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler


@callback(
    Output("graph-content", "figure"),
    Input("dropdown-switch-name", "value"),
    Input("dropdown-switch-type", "value"),
    Input("dropdown-switch-manufacturer", "value"),
)
def update_graph(switch_name, switch_type, manufacturer):
    df = get_data()

    if switch_name:
        df = df[df["Switch Name"].isin(switch_name)]
    if switch_type:
        df = df[df["Type"].isin(switch_type)]
    if manufacturer:
        df = df[df["Manufacturer"].isin(manufacturer)]

    df.rename(columns={"Time Wtd. Total": "Total"}, inplace=True)

    # Min-Max Normalization 0 to 100
    if len(df) > 0:
        scaler = MinMaxScaler()
        df[["Push Feel", "Wobble", "Sound", "Context", "Other", "Total"]] = (
            scaler.fit_transform(
                df[["Push Feel", "Wobble", "Sound", "Context", "Other", "Total"]]
            )
            * 100
        )

    # Melt the DataFrame for easier plotting
    melted_df = df.melt(
        id_vars=["Switch Name"],
        value_vars=[
            "Push Feel",
            "Wobble",
            "Sound",
            "Context",
            "Other",
            "Total",
        ],
        var_name="Dimension",
        value_name="Value",
    )

    # Create the line chart
    fig = px.line(
        melted_df,
        x="Dimension",
        y="Value",
        color="Switch Name",
        markers=True,
        # title="Comparison of Switches Across Dimensions",
    )

    fig.update_layout(
        xaxis_title="Dimension",
        yaxis_title="Min-Max Normalized Value",
        legend_title="Switch Name",
        template="plotly",
    )

    # fig.show()
    return fig  # px.line(df, x="year", y="pop")


@callback(
    Output("item-table", "data"),
    Input("dropdown-switch-name", "value"),
    Input("dropdown-switch-type", "value"),
    Input("dropdown-switch-manufacturer", "value"),
)
def update_table(switch_name, switch_type, manufacturer):
    df = get_data()

    if switch_name:
        df = df[df["Switch Name"].isin(switch_name)]
    if switch_type:
        df = df[df["Type"].isin(switch_type)]
    if manufacturer:
        df = df[df["Manufacturer"].isin(manufacturer)]

    return df.to_dict("records")
