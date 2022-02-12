#range(2, 14, 2)

# for i in range(3, 7, 2):

#     print(i)

total = 0
expenses = []
for i in range(5):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)
print("You spent $", total, sep='')
