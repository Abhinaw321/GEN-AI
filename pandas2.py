#give me 10 pandas dataset like id,name,post salary,city and age
import pandas as pd

data = [
    [1, "Aman", "Developer", 45000, "Delhi", 22],
    [2, "Rohit", "Programmer", 55000, "Mumbai", 24],
    [3, "Priya", "HR", 38000, "Noida", 23],
    [4, "Neha", "Designer", 42000, "Pune", 25],
    [5, "Karan", "Manager", 75000, "Bangalore", 29],
    [6, "Rahul", "Tester", 35000, "Chennai", 26],
    [7, "Simran", "Trainer", 30000, "Delhi", 27],
    [8, "Arjun", "Developer", 60000, "Hyderabad", 28],
    [9, "Anjali", "Accountant", 40000, "Jaipur", 24],
    [10, "Vikas", "Clerk", 28000, "Chandigarh", 30]
]

df = pd.DataFrame(
    data,
    columns=["id", "name", "post", "salary", "city", "age"]
)

print(df)

# Bonus
df["bonus"] = df["salary"].apply(
    lambda x: x * 0.05 if x >= 40000 else 0
)

# HRA
df["hra"] = df["salary"] * 0.10

# DA 
df["da"] = df["salary"] * 0.05

# Gross 
df["gross_salary"] = df["salary"] + df["bonus"] + df["hra"] + df["da"]

# Net 
df["net_salary"] = df["gross_salary"]

print(df)