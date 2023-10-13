from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df=pd.read_csv(r"E:\AC_projects_programs\quantium-starter-repo\data\updated_daily_sales_data.csv")

df=df.sort_values(by="date")

app.layout = html.Div(children=[html.H1(children="Soul Food's Sales", id="header"),
                                dcc.Graph(id='sales-graph'),
                                dcc.RadioItems(
    ["east", "west", "north", "south", "all"], "all", id="region-picker", inline=True)])

@callback(Output('sales-graph', 'figure'), Input('region-picker', 'value'))

def update_figure(region):
    if region=="all":
        trimmed_df=df
    else:
        trimmed_df=df[df["region"] == region]

    # generate a new line chart with the filtered data
    figure=px.line(trimmed_df, x="date", y="sales", color="region")
    figure.update_layout(transition_duration=500)
    return figure

if __name__ == '__main__':
    app.run(debug=True)