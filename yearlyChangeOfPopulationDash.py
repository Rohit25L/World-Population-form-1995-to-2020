from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='World Yearly Change population using map', style={'textAlign':'center'}),
    dcc.Dropdown(population.Year.unique(), '2020', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    population_2020 = population[population['Year'] == value]
    fig = px.choropleth(population_2020, locations="Country", 
                    locationmode='country names', color="Yearly Change", animation_frame="Year",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.gray, 
                    title='Population of Countries in {}'.format(value))
    fig.update(layout_coloraxis_showscale=True)

    return fig

if __name__ == '__main__':
    app.run(debug=True)
