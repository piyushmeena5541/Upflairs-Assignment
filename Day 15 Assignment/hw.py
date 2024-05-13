import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://drive.google.com/uc?id=1ALJd8DxNyV6PrVTh037DeU9aw9TeR4Ue"
df = pd.read_csv(url)

# Print top 5 rows
print("Top 5 rows:")
print(df.head())

# Print last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Find the number of rows and columns
num_rows = df.shape[0]
num_cols = df.shape[1]
print(f"\nNumber of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Find number of entries for each day and plot a bar plot
entries_per_day = df['day'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(entries_per_day.index, entries_per_day.values)
plt.title('Number of Entries for Each Day')
plt.xlabel('Day')
plt.ylabel('Number of Entries')
plt.show()

# Relationship between "total bill" and "tip" using scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['total_bill'], df['tip'])
plt.title('Relationship between Total Bill and Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Distribution of 'tip' and 'total_bill' using histograms
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['tip'], bins=20, alpha=0.7)
plt.title('Distribution of Tip')
plt.xlabel('Tip')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(df['total_bill'], bins=20, alpha=0.7)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Total sales for each day by 'total_bill' using group by and graphical representation
total_sales_per_day = df.groupby('day')['total_bill'].sum()
plt.figure(figsize=(8, 6))
plt.bar(total_sales_per_day.index, total_sales_per_day.values)
plt.title('Total Sales for Each Day')
plt.xlabel('Day')
plt.ylabel('Total Price')
plt.show()

# Pie plot on 'smoker' column representing the percentage of smoker "yes" and "no"
smoker_percentage = df['smoker'].value_counts(normalize=True) * 100
plt.figure(figsize=(6, 6))
plt.pie(smoker_percentage, labels=smoker_percentage.index, autopct='%1.1f%%')
plt.title('Smoker Percentage')
plt.show()
