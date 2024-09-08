import pandas as pd
import matplotlib.pyplot as plt
population = pd.read_csv('C:/Users/ASUS/OneDrive/Desktop/python project/Countries Population from 1995 to 2020.csv')
print(population.head(20))
population.isnull().sum()
population['Density (P/Km²)'] = population['Density (P/Km²)'].str.replace(',','')
population['Country'] = population['Country'].astype(str)

current_population = population[population['Year'] == 2020][:30]
x = current_population['Country'][:30]
y = current_population['Population'][:30]

plt.bar(x,y,color='g')

plt.xlabel('Country')
plt.ylabel('Population in Billion')
plt.xticks(rotation = 70)

plt.show()
current_population = population[population['Year'] == 2020][:30]
x = current_population['Country'][:30]
y = current_population['Population'][:30]

plt.plot(x,y,color='r')

plt.xlabel('Country')
plt.ylabel('Population in Billion')
plt.xticks(rotation = 70)

plt.show()

china_population = population[population['Country'] == 'China']
fig = plt.figure(figsize=(10,5))
plt.plot(china_population['Year'], china_population['Yearly Change'],color='g')
plt.title('Yearly Population Change in China')
plt.xlabel('Year')
plt.ylabel('Population in 10 Million')
plt.show()

india_p = population[population['Country'] == 'India']
fig = plt.figure(figsize=(10,5))
plt.plot(india_p['Year'], india_p['Yearly Change'],color='orange')
plt.title('Yearly Population Change in india')
plt.xlabel('Year')
plt.ylabel('Population in 10 Million')
plt.show()

Usa_p=population[population['Country'] == 'United States']

fig = plt.figure(figsize=(10,5))
plt.plot(Usa_p['Year'], Usa_p['Yearly Change'])
plt.title('Yearly Population Change in india')
plt.xlabel('Year')
plt.ylabel('Population in 10 Million')
plt.show()

Indonesia_p=population[population['Country'] == 'Indonesia']
Pakistan_p=population[population['Country'] == 'Pakistan']

fig = plt.figure(figsize=(10,5))
plt.plot(china_population['Year'], china_population['Population'])
plt.plot(india_p['Year'], india_p['Population'])
plt.plot(Usa_p['Year'], Usa_p['Population'])
plt.plot(Indonesia_p['Year'], Indonesia_p['Population'])
plt.plot(Pakistan_p['Year'], Pakistan_p['Population'])

plt.title("Yearly Population Change in top 5 Country's")
plt.xlabel('Year')
plt.ylabel('Population in 10 Million')
plt.show()