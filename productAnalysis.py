## ProductID,  Category, Sub-Category, Product Name, Sales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Projects\Data analysis\storedata.csv")
#print(df)

## Tyes of product categories
product_category = df['Category'].unique()
print(product_category)

## Tyes of product sub-categories
product_sub_category = df.groupby('Category')['Sub-Category'].nunique().reset_index()
#sort by ascending order
sub_category_count = product_sub_category.sort_values(by='Sub-Category',ascending=False)
print(sub_category_count.reset_index(drop=True))

## Sales per each category
category_sales = df.groupby(['Category'])['Sales'].sum().reset_index()
category_sales = category_sales.sort_values(by='Sales',ascending=False)
print(category_sales.reset_index(drop=True))

## Ploting a pie chart
plt.pie(category_sales['Sales'], labels = category_sales['Category'], autopct = "%1.1f%%")
plt.title("Top product Category baased on sales")
plt.show()

## Sales per product
## Group data by product Sub-Category vs sales
pdt_subcategory = df.groupby(['Sub-Category'])['Sales'].sum().reset_index()
# Sorting in descending order
top_pdt_subcategory = pdt_subcategory.sort_values(by='Sales', ascending=False)
print(top_pdt_subcategory.reset_index(drop=True))

top_pdt_subcategory = top_pdt_subcategory.sort_values(by='Sales', ascending=True)  # To make Ascending order
# Ploting the Horizontal bar graph
plt.barh(top_pdt_subcategory['Sub-Category'], top_pdt_subcategory['Sales'])
#Label
plt.title("Top Product Sub-Categories based on sales")
plt.xlabel("Product Sub-Categories")
plt.ylabel("Total Sales")
plt.show()