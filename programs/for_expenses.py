expenses = [1000,2001,3002,4003,5004]
# total = expenses[0]+expenses[1]+expenses[2]+expenses[3]+expenses[4]
# print(total)

total_exp=0
for item in expenses:
    total_exp=total_exp+item
print(total_exp)

# Print Range of Values
for i in range(1,11):
    print(i)

# Print Square of Numbers
for i in range(1,11):
    print(i*i)

# Expense List by Month
print(len(expenses))
total_expense = 0
for i in range(len(expenses)):
    print('Month: ',(i+1),'Expense: ', expenses[i])
    total_expense=total_expense+expenses[i]

print(total_expense)