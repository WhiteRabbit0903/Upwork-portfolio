"""
Data Cleaning Demo
Example project for Upwork portfolio
Author: WhiteRabbit0903
"""

import pandas as pd

# example data
data = {
    "name": ["Alice", "Bob", None, "Alice"],
    "age": [25, None, 30, 25],
    "salary": [50000, 60000, None, 50000]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

# remove duplicates
df = df.drop_duplicates()

# fill missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())

# remove empty names
df = df.dropna(subset=["name"])

print("\nCleaned data:")
print(df)
