from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')


app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Top ten most populated country', style={'textAlign':'center'}),
    dcc.Dropdown(population.Year.unique(), '2020', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),

    
)

def update_graph(value):
    current_population = population[population['Year'] ==value ][:10]
    current_population.sort_values('Population', ascending=False, inplace=True)
    xa=current_population['Country']
    ya=current_population['Population']
    fig=px.bar(current_population,x='Country',y='Population',color=ya,template='simple_white')
    fig.update_layout(title='top ten most populated country in {}'.format(value)).update_xaxes(title="year").update_yaxes(title="population in billion")
   

    return fig

if __name__ == '__main__':
    app.run(debug=True)
