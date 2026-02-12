import pandas as pd
import numpy as np


df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:")
print(df)


total_sales = np.sum(df["Total"])
average_sales = np.mean(df["Total"])
standard_deviation = np.std(df["Total"])

print("\nTotal Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation of Daily Sales:", standard_deviation)

product_sales = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_sales.idxmax()

print("\nBest Selling Product:", best_selling_product)
