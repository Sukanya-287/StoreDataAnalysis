import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Projects\Data analysis\storedata.csv")
#print(df)

## Geo-graphical analysis of customers and sales

state = df['State'].value_counts().reset_index()
state = state.rename(columns={'State':'Number of Customers', 'count' : 'State'})
city = df['City'].value_counts().reset_index()
city = city.rename(columns={'count':'Number of Customers'})

#print(city.head(7))

# Sales per state
state_sales = df.groupby(['State'])['Sales'].sum().reset_index()
# Sorting starting from highest state
top_state_sales = state_sales.sort_values(by = 'Sales', ascending=False)
#print(top_state_sales.head(10).reset_index(drop=True))

# Sales per city
city_sales = df.groupby(['City'])['Sales'].sum().reset_index()
# Sorting starting from highest city
top_city_sales = city_sales.sort_values(by = 'Sales', ascending=False)
#print(top_city_sales.head(10).reset_index(drop=True))