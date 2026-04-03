import pandas as pd
import matplotlib.pyplot as plt


df_small = pd.read_csv("final_30x10_dataset.csv")

class_count = df_small['Pclass'].value_counts().sort_index()

class_count.plot(kind='bar')

plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Passenger Class Distribution")

plt.show()
