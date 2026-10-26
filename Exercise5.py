'''Exercise 5: Create visualizations including Histogram, Bar Chart, Line Chart, Pie Chart, Scatter Plot, and Box Plot using Matplotlib and Seaborn. Interpret the insights obtained from each visualization. '''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

print("="*60)
print("LOADING DATASET FOR VISUALIZATION")
print("="*60)

csv_file = 'retail_sales.csv'
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found.")
    exit()

df = pd.read_csv(csv_file)
# Convert Date to datetime for proper line charting
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())
print("\nGenerating 6 distinct visualizations with plt.show()...")

# Initialize subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Exploratory Data Analysis: Retail Sales', fontsize=18)

# 1. Histogram (Customer Age Distribution)
sns.histplot(ax=axes[0, 0], data=df, x='CustomerAge', bins=6, color='skyblue', kde=True)
axes[0, 0].set_title('1. Histogram (Customer Age)')

# 2. Bar Chart (Total Sales by Category)
sales_by_cat = df.groupby('ProductCategory')['Sales'].sum().reset_index()
sns.barplot(ax=axes[0, 1], data=sales_by_cat, x='ProductCategory', y='Sales', hue='ProductCategory', palette='viridis', legend=False)
axes[0, 1].set_title('2. Bar Chart (Total Sales by Category)')

# 3. Line Chart (Sales Trend over Time)
df_sorted = df.sort_values('Date')
sns.lineplot(ax=axes[0, 2], data=df_sorted, x='Date', y='Sales', marker='o', color='purple')
axes[0, 2].set_title('3. Line Chart (Sales Trend over Time)')
axes[0, 2].tick_params(axis='x', rotation=45)

# 4. Pie Chart (Quantity Sold by Category)
qty_by_cat = df.groupby('ProductCategory')['Quantity'].sum()
axes[1, 0].pie(qty_by_cat, labels=qty_by_cat.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
axes[1, 0].set_title('4. Pie Chart (Total Quantity by Category)')

# 5. Scatter Plot (Sales vs Profit)
sns.scatterplot(ax=axes[1, 1], data=df, x='Sales', y='Profit', hue='ProductCategory', s=100)
axes[1, 1].set_title('5. Scatter Plot (Sales vs Profit)')

# 6. Box Plot (Sales Distribution by Category)
sns.boxplot(ax=axes[1, 2], data=df, x='ProductCategory', y='Sales', hue='ProductCategory', palette='Set3', legend=False)
axes[1, 2].set_title('6. Box Plot (Sales Distribution by Category)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Insights
print("\n" + "="*60)
print("INSIGHTS OBTAINED FROM VISUALIZATIONS:")
print("="*60)
print("1. Histogram: The Customer Age distribution spans from early 20s to mid 50s, highlighting the demographic spread.")
print("2. Bar Chart: Electronics completely dominates total sales revenue, followed by Clothing.")
print("3. Line Chart: Sales show day-to-day fluctuations, peaking notably on specific dates (e.g., Jan 10).")
print("4. Pie Chart: While Electronics brings the most revenue, Clothing accounts for the highest physical quantity sold (over 40%).")
print("5. Scatter Plot: There is a strong positive correlation between Sales and Profit across all categories.")
print("6. Box Plot: Electronics has the highest median sales and largest spread, whereas Beauty has consistently low sales with minimal variance.")
