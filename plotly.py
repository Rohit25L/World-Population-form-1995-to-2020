import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')

population.isnull().sum()
population['Density (P/Km²)'] = population['Density (P/Km²)'].str.replace(',','')
population['Country'] = population['Country'].astype(str)


current_population = population[population['Year'] == 2020][:10]
ax=sns.barplot(x=current_population['Country'][:10],y=current_population['Population'][:10],data=current_population,palette='rocket')
plt.xticks(rotation = 70)
plt.show()


current_population = population[population['Year'] == 2020][:10]
xa=current_population['Country'][:10]
ya=current_population['Population'][:10]
fig=go.Figure(go.Bar(x=xa,y=ya))
fig.show()

current_population = population[population['Year'] == 2020][:10]
xa=current_population['Country'][:10]
ya=current_population['Population'][:10]
fig=px.bar(x=xa,y=ya,color=ya)
fig.update_layout(title="top ten most populated country").update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()

india_p = population[population['Country'] == 'India']
fig = plt.figure(figsize=(10,5))
xa=india_p['Year']
ya=india_p['Yearly Change']
fig=px.bar(x=xa,y=ya,color=xa,color_continuous_scale = 'viridis').add_traces(
    px.line(x=xa, y=ya).data
)
fig.show()

current_population = population[population['Year'] == 2020][:10]
xa=current_population['Country'][:10]
ya=current_population['Population'][:10]
fig=px.bar(x=xa,y=ya,color=ya,template='simple_white')
fig.update_layout(title="top ten most populated country").update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()

current_population = population[population['Year'] == 1955][:10]
current_population.sort_values('Population', ascending=False, inplace=True)
xa=current_population['Country'][:10]
ya=current_population['Population'][:10]
fig=px.bar(x=xa,y=ya,color=ya,template='simple_white')
fig.update_layout(title='<b>top ten most populated country in 1995</b><br><sup></sup>').update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()




both_p=population.query("Country=='Pakistan'|Country=='Indonesia'")
fig=px.line(both_p,x='Year',y='Yearly % Change',color='Country', markers=True,template='simple_white')
fig.update_layout(title="").update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()


both_p=population.query("Country=='Pakistan'|Country=='Indonesia'")
fig=px.line(both_p,x='Year',y='Fertility Rate',color='Country', markers=True,template='simple_white')
fig.update_layout(title="").update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()



china_population = population[population['Country'] == 'China']
india_p = population[population['Country'] == 'India']
both_p=population.query("Country=='India'|Country=='China'")
fig=px.line(both_p,x='Year',y='Population',color='Country')
fig.update_layout(title="").update_xaxes(title="year").update_yaxes(title="population in billion")
fig.show()