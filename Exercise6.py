'''Exercise 6: Design an interactive dashboard using Tableau or Power BI (or Python libraries such as Plotly). Create a dashboard containing multiple visualizations and present a data-driven story. '''

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

print("="*60)
print("LOADING DATASET FOR INTERACTIVE DASHBOARD")
print("="*60)

csv_file = 'retail_sales.csv'
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found. Please run Exercise 5 to generate it.")
    exit()

df = pd.read_csv(csv_file)
df['Date'] = pd.to_datetime(df['Date'])

# Initialize the figure with 4 subplots
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}],
           [{"type": "xy"}, {"type": "xy"}]],
    subplot_titles=(
        "1. Daily Sales Trend", 
        "2. Profit Contribution by Category", 
        "3. Average Discount by Category", 
        "4. Sales Distribution (Boxplot)"
    )
)

# 1. Line chart: Sales Trend over Time (Row 1, Col 1)
df_trend = df.groupby('Date')['Sales'].sum().reset_index()
fig.add_trace(
    go.Scatter(x=df_trend['Date'], y=df_trend['Sales'], mode='lines+markers', name='Daily Sales', line=dict(color='royalblue')),
    row=1, col=1
)

# 2. Pie chart: Profit Contribution (Row 1, Col 2)
df_profit = df.groupby('ProductCategory')['Profit'].sum().reset_index()
fig.add_trace(
    go.Pie(labels=df_profit['ProductCategory'], values=df_profit['Profit'], name='Profit', hole=0.3),
    row=1, col=2
)

# 3. Bar chart: Average Discount by Category (Row 2, Col 1)
df_discount = df.groupby('ProductCategory')['Discount'].mean().reset_index()
fig.add_trace(
    go.Bar(x=df_discount['ProductCategory'], y=df_discount['Discount'], name='Avg Discount', marker_color='orange'),
    row=2, col=1
)

# 4. Box plot: Sales Distribution (Row 2, Col 2)
categories = df['ProductCategory'].unique()
colors = ['#EF553B', '#00CC96', '#AB63FA', '#FFA15A']
for i, cat in enumerate(categories):
    df_cat = df[df['ProductCategory'] == cat]
    fig.add_trace(
        go.Box(y=df_cat['Sales'], name=cat, marker_color=colors[i % len(colors)]),
        row=2, col=2
    )

# Update layout to simulate a cohesive dashboard
fig.update_layout(
    title_text="Retail Performance Interactive Dashboard - A Data-Driven Story",
    title_font_size=24,
    height=800,
    showlegend=False,
    template="plotly_white"
)

# Render the interactive dashboard in the default browser
print("Generating and opening interactive Plotly dashboard in your web browser...")
fig.show()

print("\n" + "="*60)
print("DATA-DRIVEN STORY INSIGHTS:")
print("="*60)
print("1. Sales Consistency: Sales maintain a relatively steady trend but show clear peaks (e.g., around Jan 10).")
print("2. Profit Drivers: Electronics generates the vast majority of our overall profit, representing the core business driver.")
print("3. Promotional Strategy: Home and Clothing categories are given higher average discounts compared to Electronics, likely to drive volume.")
print("4. Revenue Quality: Even though Electronics orders are discounted less, their base sales value (median and variance) is significantly higher than all other categories.")
