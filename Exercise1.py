'''Exercise 1: Import CSV and Excel datasets using Pandas. Identify structured, semi-structured, and unstructured data. Display dataset information, data types, and summary statistics.'''

import pandas as pd
import json

print("="*60)
print("1. IDENTIFYING DATA TYPES")
print("="*60)

# Structured Data
print("--- Structured Data ---")
print("Definition: Data with a high degree of organization, such as tabular data (e.g., CSV, SQL databases).")
print("Example: Loading structured_data.csv...")
df_csv = pd.read_csv('structured_data.csv')
print(df_csv.head())
print()

# Semi-Structured Data
print("--- Semi-Structured Data ---")
print("Definition: Data that does not reside in a relational database but has some organizational properties (e.g., JSON, XML).")
print("Example: Loading semi_structured_data.json...")
with open('semi_structured_data.json', 'r') as file:
    semi_data = json.load(file)
print(json.dumps(semi_data, indent=2))
print()

# Unstructured Data
print("--- Unstructured Data ---")
print("Definition: Data with no predefined format or organization (e.g., Text documents, Images, Videos).")
print("Example: Reading unstructured_data.txt...")
with open('unstructured_data.txt', 'r') as file:
    print(file.read())
print()

print("="*60)
print("2. DATASET INFORMATION, DATA TYPES, & SUMMARY STATISTICS")
print("="*60)

print("\n--- CSV Dataset Information ---")
df_csv.info()

print("\n--- CSV Data Types ---")
print(df_csv.dtypes)

print("\n--- CSV Summary Statistics ---")
print(df_csv.describe())

print("\n" + "="*60)

# Importing Excel as required by the exercise
print("\n--- Importing Excel Dataset ---")
try:
    df_excel = pd.read_excel('structured_data.xlsx')
    
    print("\n--- Excel Dataset Information ---")
    df_excel.info()
    
    print("\n--- Excel Data Types ---")
    print(df_excel.dtypes)
    
    print("\n--- Excel Summary Statistics ---")
    print(df_excel.describe())
except ImportError as e:
    print(f"Failed to load Excel file. Missing dependency: {e}")
except Exception as e:
    print(f"Error loading Excel file: {e}")