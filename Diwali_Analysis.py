# import python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # visualizing data
import seaborn as sns

# import csv file
df = pd.read_csv("Diwali_Sales_Data.csv", encoding="unicode_escape")

# drop unrelated/blank columns
df.drop(["Status", "unnamed1"], axis=1, inplace=True)

# drop null values
df.dropna(inplace=True)

# change data type
df["Amount"] = df["Amount"].astype("int")

# rename column
df.rename(columns={"Age Group": "Age_Group"}, inplace=True)

# use describe() for specific columns
df[["Age", "Orders", "Amount"]].describe()

##EDA

# plotting a bar chart for Gender and it's count
ax = sns.countplot(x="Gender", data=df)
for bars in ax.containers:
    ax.bar_label(bars)

# plotting a bar chart for gender vs total amount
sales_gen = (
    df.groupby(["Gender"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
)
sns.barplot(x="Gender", y="Amount", data=sales_gen)

print(
    "From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men"
)

# Age
ax = sns.countplot(data=df, x="Age_Group", hue="Gender")
for bars in ax.containers:
    ax.bar_label(bars)

# Total Amount vs Age Group
sales_age = (
    df.groupby(["Age_Group"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
)
sns.barplot(x="Age_Group", y="Amount", data=sales_age)

print(
    "From above graphs we can see that most of the buyers are of age group between 26-35 yrs female"
)

# State
# total number of orders from top 10 states

sales_state = (
    df.groupby(["State"], as_index=False)["Orders"]
    .sum()
    .sort_values(by="Orders", ascending=False)
    .head(10)
)
sns.set(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x="State", y="Orders")

# total amount/sales from top 10 states

sales_state = (
    df.groupby(["State"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
    .head(10)
)
sns.set(rc={"figure.figsize": (15, 5)})
sns.barplot(data=sales_state, x="State", y="Amount")

print(
    "From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively"
)

# Marital Status
ax = sns.countplot(data=df, x="Marital_Status")
sns.set(rc={"figure.figsize": (15, 3)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_state = (
    df.groupby(["Marital_Status", "Gender"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
)
sns.set(rc={"figure.figsize": (6, 5)})
sns.barplot(data=sales_state, x="Marital_Status", y="Amount", hue="Gender")

print(
    "From above graphs we can see that most of the buyers are married (women) and they have high purchasing power"
)

# Occupation
sns.set(rc={"figure.figsize": (20, 5)})
ax = sns.countplot(data=df, x="Occupation")
for bars in ax.containers:
    ax.bar_label(bars)

sales_state = (
    df.groupby(["Occupation"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
)
sns.set(rc={"figure.figsize": (20, 5)})
sns.barplot(data=sales_state, x="Occupation", y="Amount")

print(
    "From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector"
)

# Product Category
sns.set(rc={"figure.figsize": (20, 5)})
ax = sns.countplot(data=df, x="Product_Category")
for bars in ax.containers:
    ax.bar_label(bars)

sales_state = (
    df.groupby(["Product_Category"], as_index=False)["Amount"]
    .sum()
    .sort_values(by="Amount", ascending=False)
    .head(10)
)
sns.set(rc={"figure.figsize": (20, 5)})
sns.barplot(data=sales_state, x="Product_Category", y="Amount")

print(
    "From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category"
)

# Product and Orders
sales_state = (
    df.groupby(["Product_ID"], as_index=False)["Orders"]
    .sum()
    .sort_values(by="Orders", ascending=False)
    .head(10)
)
sns.set(rc={"figure.figsize": (20, 5)})
sns.barplot(data=sales_state, x="Product_ID", y="Orders")

# top 10 most sold products (same thing as above)
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby("Product_ID")["Orders"].sum().nlargest(10).sort_values(ascending=False).plot(
    kind="bar"
)

print("""Conclusion:\n
Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT,\nHealthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
\n\n
Thank you!""")