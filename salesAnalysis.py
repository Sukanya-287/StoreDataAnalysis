# Order Date, 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Projects\Data analysis\storedata.csv")
#print(df)

# First convert order date to datetime format arrange as day-first
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst = True)

''' # Yearly Analysis

# Grouping by year and summing the sales per year
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()
# Setting new index and renaming the columns
yearly_sales = yearly_sales.reset_index()
yearly_sales = yearly_sales.rename(columns={'Order Date': 'Year', 'Sales' : 'Total Sales'})
print(yearly_sales) 

# ## Ploting Horizontal bar graph
# plt.bar(yearly_sales['Year'], yearly_sales['Total Sales'])

## Ploting Line graph
plt.plot(yearly_sales['Year'], yearly_sales['Total Sales'], marker= 'o', linestyle='--')

plt.title("Yearly Sales")
plt.xlabel('Year')
plt.xticks(rotation = 65)
plt.ylabel('Total Sales')
plt.show()

'''

'''  # Quaterly Sales analysis
# Filter the date according to Year ex for 2018
year_sales = df[df['Order Date'].dt.year == 2018]
quarterly_sales = year_sales.resample('Q',on='Order Date')['Sales'].sum()
quarterly_sales = quarterly_sales.reset_index()
quarterly_sales = quarterly_sales.rename(columns={'Order Date' : 'Quater', 'Sales' : 'Total Sales'})
print(quarterly_sales)

# ## Ploting Horizontal bar graph
# plt.bar(quarterly_sales['Quater'], quaterly_sales['Total Sales'])

## Ploting Line graph
plt.plot(quarterly_sales['Quater'], quarterly_sales['Total Sales'], marker= 'o', linestyle='--')

plt.title("Quaterly Sales")
plt.xlabel('Per Quater')
plt.xticks(rotation = 65)
plt.ylabel('Total Sales')
plt.show()

'''

  # Monthly Sales analysis
# Filter the date according to Year ex for 2018
year_sales = df[df['Order Date'].dt.year == 2018]

monthly_sales = year_sales.reset_index()
monthly_sales_sales = year_sales.resample('M',on='Order Date')['Sales'].sum()
monthly_sales = monthly_sales.rename(columns={'Order Date' : 'Quater', 'Sales' : 'Total Sales'})
print(monthly_sales)

# ## Ploting Horizontal bar graph
# plt.bar(quarterly_sales['Quater'], quaterly_sales['Total Sales'])

## Ploting Line graph
plt.plot(monthly_sales['Months'], monthly_sales['Total Sales'], marker= 'o', linestyle='--')

plt.title("Monthly Sales")
plt.xlabel('Per Month')
plt.xticks(rotation = 65)
plt.ylabel('Total Sales')
plt.show()