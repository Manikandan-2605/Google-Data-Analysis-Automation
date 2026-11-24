import pandas as pd
import matplotlib.pyplot as plt
import os

# Create Output Folder
os.makedirs("output", exist_ok=True)

# Load Dataset
data = pd.read_csv("sales_data.csv")

print("Dataset Loaded Successfully!")

# Data Cleaning
data = data.drop_duplicates()
data = data.dropna()

print("Data Cleaning Completed!")

# Calculate Revenue
data["Revenue"] = data["Quantity"] * data["Price"]

# Sales Analysis
total_sales = data["Revenue"].sum()

best_product = data.groupby("Product")["Quantity"].sum().idxmax()

city_sales = data.groupby("City")["Revenue"].sum()

product_sales = data.groupby("Product")["Quantity"].sum()

# Save Cleaned Dataset
data.to_csv("output/cleaned_data.csv", index=False)

# Create Product Sales Chart
product_sales.plot(kind="bar", title="Product Wise Sales")
plt.tight_layout()
plt.savefig("output/product_sales.png")
plt.close()

# Create City Revenue Chart
city_sales.plot(kind="bar", title="City Wise Revenue")
plt.tight_layout()
plt.savefig("output/city_revenue.png")
plt.close()

# Generate Report
with open("output/sales_report.txt", "w") as file:

    file.write("SALES ANALYSIS REPORT\n")
    file.write("--------------------\n")

    file.write(f"Total Revenue: Rs.{total_sales}\n")
    file.write(f"Best Selling Product: {best_product}\n")

    file.write("\nCITY WISE SALES:\n")
    file.write(city_sales.to_string())

print("\nAUTOMATION COMPLETED SUCCESSFULLY!")
print("Check the output folder!")