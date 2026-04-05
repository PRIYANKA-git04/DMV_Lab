import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    var1 = float(input(f"Enter Day no.: "))
    var2 = float(input(f"Enter sales value: "))
    
    x.append(var1)
    y.append(var2)


plt.plot(x, y, marker='o')

plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Distribution")

plt.grid(True)
# Also ran code with grid=False
plt.show()
