from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Pakkistan and Russia population', style={'textAlign':'center'}),
    dcc.Dropdown(population.Year.unique(), '2020', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),

    
)

def update_graph(value):
    current_population = population[population['Year'] == value][:10]
    current_population.sort_values('Population', ascending=False, inplace=True)
    fig = px.bar(
        current_population,
        x='Country', template='simple_white',
        y='Population',

        title='Pakistan population {}'.format(value),

        text=current_population['Population'],
        color='Country',
        color_discrete_map={'China':'black', 'India':'black', 'United States':'black', 'Indonesia':'black', 
                              'Pakistan':'yellow', 'Brazil':'black', 'Nigeria':'black','Bangladesh':'black','Russia':'yellow',
                                'Mexico':'black'}
    )
   

    return fig

if __name__ == '__main__':
    app.run(debug=True)
