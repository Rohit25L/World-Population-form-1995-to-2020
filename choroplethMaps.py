import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')
import plotly.graph_objects as go


population_2020 = population[population['Year'] == 2020]
fig = px.choropleth(population_2020, locations="Country", 
                    locationmode='country names', color="Population", 
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma, 
                    title='Population of Countries in 2020')
fig.update(layout_coloraxis_showscale=True)
fig.show()

fig = px.choropleth(population, locations="Country", 
                    locationmode='country names', color="Population", animation_frame="Year",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma, 
                    title='Population of Countries in 2020')
fig.update(layout_coloraxis_showscale=True)
fig.show()


fig = px.choropleth(population, locations="Country", 
                    locationmode='country names', color="Fertility Rate", animation_frame="Year",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.GnBu, 
                    title='fertility rate')
fig.update(layout_coloraxis_showscale=True)
fig.show()
