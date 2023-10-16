## Importing the python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt     # For visualization

## Importing the database-CSV file
df = pd.read_csv(r"D:\Projects\Data analysis\storedata.csv") #df is variable as data file

#print(df.head(10))    #Difault it ll display starting 5 rows 

## Checking for shape of data - General overview of data
print(df.info())

## Calculating the numbers of null values
null_count = df['Postal Code'].isnull().sum()
print(null_count)

## Filling empty colm with 0's
print(df.describe())

## Data cleaning -  it ensures that the data is accurate and reliable, preventing misleading insights or erroneous conclusions.
##1 Checking for duplicates using conditional statements
if df.duplicated().sum()>0:
    #print(df.duplicated())     -->This ll print all the rows with true or false statement
    print("Duplicates are present and nor of duplicated keys = ")
    print(df.duplicated(keep=False).sum())         #This ll count the nor of duplicated keys  
else:
    print("No duplicates exists")


## Exploration Data Analysis
##1 Customer Analysis
##(i) Customer Segmentation
print(df.head())        #This function is used to display the first few rows(Default 5 rows)

##(ii) types of customers
types_of_customers = df['Segment'].unique()
#print(types_of_customers)

##(iii) nor of customers in each segments
'''
nor_of_customers = df['Segment'].value_counts().reset_index()
print(nor_of_customers, "\n")
nor_of_customers = nor_of_customers.rename(columns={'Segment': 'Customer Type', 'count':"Total Customers"}) #Renaming the colm names from segment n count
print(nor_of_customers)

## Plotting a pie chart
plt.pie(nor_of_customers['Total Customers'], labels=nor_of_customers['Customer Type'],autopct='%1.1f%%')
## set pie chart labels
plt.title('Distribution of Customers')
plt.show()
'''


## Sales and  Costomers

sales_per_category = df.groupby('Segment')['Sales'].sum().reset_index()
sales_per_category = sales_per_category.rename(columns={'Segment': 'Customer Type', 'Sales':"Total Sales"})
print(sales_per_category)

## Plotting a pie chart
plt.pie(sales_per_category['Total Sales'], labels=sales_per_category['Customer Type'],autopct='%1.1f%%')
## set pie chart labels
plt.title('Sales Per Customer Category')
plt.show()

## Bar Graph
plt.bar(sales_per_category['Customer Type'], sales_per_category['Total Sales'])
##Label
plt.title('Sales Per Customer Category')
plt.xlabel('Customer Type ------>')
plt.ylabel('Total Sales ------>')
plt.show()


## Customer Loyality check

#Group data according to : ID, Customer Name, Segment and Calculate freq. of their orders
customer_order_freq = df.groupby(['Customer ID','Customer Name','Segment'])['Order ID'].count().reset_index()
##Rename the Order ID column
customer_order_freq.rename(columns={'Order ID': 'Total Orders'}, inplace='True')
#print(customer_order_freq)
## Identify the repeat customers
repeat_customers = customer_order_freq[customer_order_freq['Total Orders']>=1]
##sort repeat customers in descending order
sorted_repeat_customers = repeat_customers.sort_values(by='Total Orders', ascending=False)
#print(sorted_repeat_customers.head(10).reset_index(drop=True))      #This ll return starting 10 max 

## Ranking the Customers according to sales

# Group dat based on ID, Customer Name, Segment and sales
customer_sales = df.groupby(['Customer ID','Customer Name','Segment'])['Sales'].sum().reset_index()
# sort in desc order
top_spenders = customer_sales.sort_values(by='Sales', ascending=False)
#print(top_spenders.head(10).reset_index(drop=True))

## Analysing the Shipping Classes or Modes of shipping

types_of_shipping = df['Ship Mode'].unique()
#print(types_of_shipping)
# Frequency use of shipping methods
shipping_mode = df['Ship Mode'].value_counts().reset_index()
shipping_mode = shipping_mode.rename(columns={'Ship Mode':'Mode of Shipment','count':'Use Frequency'})
#print(shipping_mode)
# Ploting a Pie chart
plt.pie(shipping_mode['Use Frequency'], labels=shipping_mode['Mode of Shipment'], autopct='%1.1f%%')
plt.title("Popular Shipping Methods")
plt.show()
