'''Exercise 3: Compute descriptive statistics such as Mean, Median, Mode, Variance, Standard Deviation, Quartiles, and Percentiles using Python libraries. '''

import pandas as pd
import numpy as np

print("="*60)
print("0. LOADING DATASET")
print("="*60)
df = pd.read_csv('statistics_data.csv')
print(df)
print()

# Automatically identify numeric columns, excluding ID columns like 'EmployeeID'
numeric_columns = [col for col in df.select_dtypes(include=[np.number]).columns if 'ID' not in col]

for data_column in numeric_columns:
    data = df[data_column].dropna()

    print("="*60)
    print(f"1. DESCRIPTIVE STATISTICS FOR: {data_column}")
    print("="*60)

    # Compute descriptive statistics using pandas and numpy
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = data.mode()[0] if not data.mode().empty else np.nan
    variance_val = np.var(data, ddof=1) # Sample variance
    std_dev_val = np.std(data, ddof=1)  # Sample standard deviation

    # Quartiles and Percentiles using numpy
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50) # Same as median
    q3 = np.percentile(data, 75)

    percentile_10 = np.percentile(data, 10)
    percentile_90 = np.percentile(data, 90)

    print(f"Count:              {len(data)}")
    print(f"Mean:               {mean_val:.2f}")
    print(f"Median:             {median_val:.2f}")
    print(f"Mode:               {mode_val}")
    print(f"Variance:           {variance_val:.2f}")
    print(f"Standard Deviation: {std_dev_val:.2f}")

    print("\n--- Quartiles ---")
    print(f"Q1 (25th Percentile): {q1:.2f}")
    print(f"Q2 (50th Percentile): {q2:.2f}")
    print(f"Q3 (75th Percentile): {q3:.2f}")

    print("\n--- Additional Percentiles ---")
    print(f"10th Percentile:      {percentile_10:.2f}")
    print(f"90th Percentile:      {percentile_90:.2f}\n")

print("="*60)
print("2. USING PANDAS DESCRIBE()")
print("="*60)
# Pandas describe provides a quick summary of all numeric columns
print(df[numeric_columns].describe())
