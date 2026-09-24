import pandas as pd
import numpy as np

data = [
    [101, "Laptop", 45000, 1],
    [102, "Mobile", 25000, 2],
    [103, "Keyboard", 1500, 2],
    [104, "Monitor", 8000, 1],
    [105, "Mouse", 800, 3],
    [106, "Headphones", 3000, 2],
    [107, "Printer", 12000, 1],
    [108, "USB Cable", 500, 4],
    [109, "Tablet", 18000, 1],
    [110, "Webcam", 2500, 2]
]

df = pd.DataFrame(
    data,
    columns=["product_id", "name", "price", "quantity"]
)

# Total price
df["total_price"] = df["price"] * df["quantity"]

# Discount
df["discount"] = np.where(
    df["total_price"] >= 5000,
    df["total_price"] * 0.10,
    df["total_price"] * 0.05
)

# Price after discount
df["after_discount"] = df["total_price"] - df["discount"]

# Delivery
df["delivery"] = np.where(
    df["total_price"] >= 2000,
    0,
    100
)

# GST
df["GST"] = df["after_discount"] * 0.08

# finall price
df["final_price"] = (
    df["after_discount"]
    + df["delivery"]
    + df["GST"]
)

print(df)