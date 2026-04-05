import pandas as pd

df = pd.read_csv("test.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())


print("\nMissing Values:")
print(df.isnull().sum())


df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


if 'Cabin' in df.columns:
    df = df.drop('Cabin', axis=1)

numeric_df = df.select_dtypes(include=['int64', 'float64'])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | 
            (numeric_df > (Q3 + 1.5 * IQR)))

print("\nOutliers count BEFORE capping:")
print(outliers.sum())


for col in numeric_df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower=lower_limit, upper=upper_limit)


numeric_df = df.select_dtypes(include=['int64', 'float64'])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

outliers_after = ((numeric_df < (Q1 - 1.5 * IQR)) | 
                  (numeric_df > (Q3 + 1.5 * IQR)))

print("\nOutliers count AFTER capping:")
print(outliers_after.sum())


df = df[['PassengerId','Pclass','Name','Sex','Age',
         'SibSp','Parch','Ticket','Fare','Embarked']]


df_small = df.sample(30, random_state=1)


df_small = df_small.reset_index(drop=True)


df_small.to_csv("final_30x10_dataset.csv", index=False)

print("\n Final 30x10 dataset created successfully!")
