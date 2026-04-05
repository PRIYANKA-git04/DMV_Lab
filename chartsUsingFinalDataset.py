import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("final_30x10_dataset.csv")

# 1. Bar Chart 

class_counts = df['Pclass'].value_counts().sort_index()

plt.figure()
plt.bar(class_counts.index, class_counts.values)
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Passenger Class Distribution")

# 2. Line Chart 

plt.figure()
sorted_df = df.sort_values(by='Age')
plt.plot(sorted_df['Age'], sorted_df['Fare'])
plt.xlabel("Age (Sorted)")
plt.ylabel("Fare")
plt.title("Fare vs Age (Sorted)")

# 3. Pie Chart 

embarked_counts = df['Embarked'].value_counts()

plt.figure()
plt.pie(embarked_counts, labels=embarked_counts.index, autopct='%1.1f%%')
plt.title("Embarked Distribution")

# 4. Stair Chart 

ages = df['Age'].dropna().sort_values()

plt.figure()
plt.step(range(len(ages)), ages)
plt.xlabel("Index")
plt.ylabel("Age")
plt.title("Stair Chart of Age Distribution")

# 5. Histogram Chart

plt.figure()
plt.hist(df['Age'].dropna(), bins=10)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution Histogram")


plt.show()
