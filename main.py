import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("kidney_disease.csv")

# IMPORTANT: replace dataset placeholders
df.replace('?', np.nan, inplace=True)

# Drop ID column
df = df.drop('id', axis=1)

# ---- Convert numeric columns ----
num_cols = [
    'age',
    'Packed Cell Volume',
    'White Blood Cell Count',
    'Red Blood Cell Count',
    'Blood Pressure',
    'Blood Glucose Random',
    'Blood Urea',
    'Serum Creatinine',
    'Sodium',
    'Potassium',
    'Hemoglobin'
]

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ---- Missing values (numeric → median) ----
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# ---- Categorical cleaning ----
cat_mode_cols = [
    'Red Blood Cells',
    'Pus Cell Clumps',
    'Bacteria',
    'Hypertension',
    'Diabetes Mellitus',
    'Coronary Artery Disease',
    'Appetite',
    'Pedal Edema',
    'Anemia'
]

for col in cat_mode_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Special categorical handling
df['Diabetes Mellitus'] = df['Diabetes Mellitus'].astype(str).str.strip().str.lower()
df['Coronary Artery Disease'] = df['Coronary Artery Disease'].astype(str).str.strip().str.lower()

# Pus Cell is messy → safer as unknown
df['Pus Cell'] = df['Pus Cell'].fillna('unknown')

# Albumin & Sugar (ordinal numeric-like)
df['Albumin'] = pd.to_numeric(df['Albumin'], errors='coerce')
df['Sugar'] = pd.to_numeric(df['Sugar'], errors='coerce')

df['Albumin'] = df['Albumin'].fillna(df['Albumin'].median())
df['Sugar'] = df['Sugar'].fillna(df['Sugar'].median())

# Classification to numeric 
df['classification'] = df['classification'].str.strip().str.lower()
df['classification'] = df['classification'].map({'ckd': 1, 'notckd': 0})

# ---- Final check ----
print("Remaining missing values:\n", df.isna().sum())

# Plotting
plt.scatter(df['age'], df['Blood Pressure'])
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Age vs Blood Pressure")
plt.show()


corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5,mask=corr.abs()<=.6)
plt.title("Correlation Matrix")
plt.show()
