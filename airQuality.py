import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load dataset
# -------------------------
df = pd.read_csv("city_day.csv")

# Preview
print("Shape:", df.shape)
print(df.head())

# -------------------------
# 2. Basic Cleaning
# -------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize column names (strip spaces, lowercase, replace special chars)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r'[^\w\s]', '')

# Convert Date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['date'])

# Handle missing values
df.replace(["[null]", "null", "-", ""], np.nan, inplace=True)

# Convert numeric columns to float
numeric_cols = ['pm25','pm10','no','no2','nox','nh3','co','so2']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values with median (you can change to forward-fill if time series)
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

print("\nAfter cleaning:")
print(df.info())

# -------------------------
# 3. Exploratory Data Analysis (EDA)
# -------------------------

# Summary statistics
print("\nSummary stats:")
print(df.describe())

# Missing values heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Distribution of pollutants
plt.figure(figsize=(12,8))
df[numeric_cols].hist(bins=30, figsize=(12,8))
plt.tight_layout()
plt.show()

# Correlation matrix
plt.figure(figsize=(10,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Pollutants")
plt.show()

# City-wise average pollution
plt.figure(figsize=(12,6))
city_avg = df.groupby("city")[numeric_cols].mean().sort_values("pm25", ascending=False).head(10)
city_avg['pm25'].plot(kind='bar', color="red")
plt.title("Top 10 Cities by Average PM2.5")
plt.ylabel("PM2.5 (µg/m³)")
plt.show()

# Trend over time (PM2.5 as example)
plt.figure(figsize=(12,6))
df.groupby("date")["pm25"].mean().plot()
plt.title("PM2.5 Trend Over Time")
plt.ylabel("PM2.5 (µg/m³)")
plt.xlabel("Date")
plt.show()
