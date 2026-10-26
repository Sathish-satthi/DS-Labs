'''Exercise 4: Perform Exploratory Data Analysis (EDA) on a real dataset. Calculate correlation and covariance matrices, identify trends, detect outliers, and interpret relationships among variables. '''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

print("="*60)
print("1. LOADING DATASET")
print("="*60)

# We use the housing_data.csv dataset created for this exercise
csv_file = 'housing_data.csv'
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found.")
    exit()

df = pd.read_csv(csv_file)
print("--- Dataset Head ---")
print(df.head())

print("\n--- Basic Information ---")
df.info()

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n" + "="*60)
print("2. CORRELATION & COVARIANCE MATRICES")
print("="*60)

# Select only numerical columns for correlation and covariance
# We drop 'HouseID' since it's just an identifier
numeric_df = df.drop(columns=['HouseID']).select_dtypes(include=['float64', 'int64'])

# Calculate Correlation Matrix
print("\n--- Correlation Matrix ---")
corr_matrix = numeric_df.corr()
print(corr_matrix)

# Calculate Covariance Matrix
print("\n--- Covariance Matrix ---")
cov_matrix = numeric_df.cov()
print(cov_matrix)

print("\n" + "="*60)
print("3. INTERPRETATION OF RELATIONSHIPS & TRENDS")
print("="*60)
print("From the correlation matrix, we can observe:")
print("- High positive correlation between 'Area_sqft' and 'Price'. This means larger houses cost more.")
print("- Strong negative correlation between 'Distance_to_center_km' and 'Price'. Houses further from the center are cheaper.")
print("- Negative correlation between 'Age_years' and 'Price'. Older houses tend to have a lower price.")

print("\n" + "="*60)
print("4. DETECTING OUTLIERS (IQR METHOD)")
print("="*60)

def find_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

area_outliers = find_outliers_iqr(df, 'Area_sqft')
price_outliers = find_outliers_iqr(df, 'Price')

print(f"--- Outliers in Area_sqft ({len(area_outliers)} found) ---")
if not area_outliers.empty:
    print(area_outliers[['HouseID', 'Area_sqft', 'Price']])
else:
    print("No outliers detected.")

print(f"\n--- Outliers in Price ({len(price_outliers)} found) ---")
if not price_outliers.empty:
    print(price_outliers[['HouseID', 'Area_sqft', 'Price']])
else:
    print("No outliers detected.")

print("\n" + "="*60)
print("5. VISUALIZING TRENDS & OUTLIERS")
print("="*60)
print("Generating visualizations with plt.show()...")

# Show plots using plt.show()
plt.figure(figsize=(15, 10))

# 4.1 Boxplots for Outlier Detection
plt.subplot(2, 2, 1)
sns.boxplot(data=df[['Area_sqft']])
plt.title("Boxplot for Area (Outlier Detection)")

plt.subplot(2, 2, 2)
sns.boxplot(data=df[['Price']])
plt.title("Boxplot for Price (Outlier Detection)")

# 4.2 Scatterplot for Trends
plt.subplot(2, 2, 3)
sns.scatterplot(x='Area_sqft', y='Price', data=df)
plt.title("Trend: Area vs Price")

plt.subplot(2, 2, 4)
sns.scatterplot(x='Distance_to_center_km', y='Price', data=df)
plt.title("Trend: Distance vs Price")

plt.tight_layout()
plt.show()
