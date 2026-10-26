'''Exercise 2: Perform data preprocessing by handling missing values, removing duplicate records, detecting outliers, performing normalization/standardization, and transforming categorical variables into numerical form. '''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# 0. Load the dataset
print("="*60)
print("0. LOADING DATASET")
print("="*60)
df = pd.read_csv('messy_data.csv')
print("--- Original Dataset ---")
print(df)
print()

# 1. Removing duplicate records
print("="*60)
print("1. REMOVING DUPLICATE RECORDS")
print("="*60)
df.drop_duplicates(inplace=True)
print("--- After Removing Duplicates ---")
print(df)
print()

# 2. Handling missing values (Imputation)
print("="*60)
print("2. HANDLING MISSING VALUES")
print("="*60)
# Dynamically fill missing numeric values with median, and categorical with mode
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
print("--- After Handling Missing Values ---")
print(df)
print()

# 3. Detecting and removing outliers (using IQR method)
print("="*60)
print("3. DETECTING AND REMOVING OUTLIERS")
print("="*60)
def remove_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Dynamically apply to all numeric columns, ignoring ID-like columns
numeric_cols_for_outliers = [col for col in df.select_dtypes(include=[np.number]).columns if 'ID' not in col]
for col in numeric_cols_for_outliers:
    df = remove_outliers(df, col)

print("--- After Removing Outliers (IQR Method) ---")
print(df)
print()

# 4. Transforming categorical variables into numerical form (Label Encoding)
print("="*60)
print("4. CATEGORICAL TO NUMERICAL TRANSFORMATION")
print("="*60)
label_encoder = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns

# Exclude obvious identifier columns like 'Name' if they exist, but encode everything else
for col in categorical_cols:
    if col != 'Name':
        df[col + '_Encoded'] = label_encoder.fit_transform(df[col])

print(f"--- After Label Encoding ---")
print(df)
print()

# 5. Normalization / Standardization
print("="*60)
print("5. NORMALIZATION & STANDARDIZATION")
print("="*60)
scaler = StandardScaler()
minmax = MinMaxScaler()

for col in numeric_cols_for_outliers:
    df[col + '_Standardized'] = scaler.fit_transform(df[[col]])
    df[col + '_Normalized'] = minmax.fit_transform(df[[col]])

print("--- After Scaling ---")
print(df)
print()

print("="*60)
print("--- Final Preprocessed Dataset ---")
print("="*60)
print(df)
