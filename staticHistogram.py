import matplotlib.pyplot as plt

salaries = [10000, 15000, 15000, 20000, 25000, 25000, 25000, 30000, 30000, 40000]

plt.hist(salaries)

plt.xlabel("Salary Range")
plt.ylabel("Number Of Employees")
plt.title("Salary Distribution")

plt.show()
