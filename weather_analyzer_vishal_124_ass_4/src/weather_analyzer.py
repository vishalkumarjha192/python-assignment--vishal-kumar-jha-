
# Full Weather Data Visualizer Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = os.path.join('data', 'weather.csv')
df = pd.read_csv(data_path)

# Convert date
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Clean
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(method='ffill')
df['rainfall'] = df['rainfall'].fillna(0)

# Extract month
df['month'] = df['date'].dt.month

# Export cleaned data
df.to_csv('data/cleaned_weather_data.csv', index=False)

# Generate plots directory
os.makedirs('images', exist_ok=True)

# Plot 1: Temperature trend
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.savefig('images/daily_temperature.png')
plt.close()

# Plot 2: Monthly rainfall
monthly_rain = df.groupby('month')['rainfall'].sum()
plt.figure(figsize=(8,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.savefig('images/monthly_rainfall.png')
plt.close()

# Plot 3: humidity vs temperature
plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.savefig('images/humidity_vs_temperature.png')
plt.close()

print("✔ Analysis complete. Check images/ and data/ folders.")
