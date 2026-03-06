import pandas as pd
import numpy as np

data={
    'Age':[25,30,18,np.nan,20],
    'Salary': [3000,4500,5000,np.nan,2500]
}
df=pd.DataFrame(data)

print("Original dataset:")
print(df)

print("missing values")
print(df.isnull().sum())

#handling missing data
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Salary"].fillna(df["Salary"].mean(),inplace=True)

print("Modified dataset:")
print(df)
