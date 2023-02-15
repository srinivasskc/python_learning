def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


joe_exp_list = [1000, 2000, 3000]
doe_exp_list = [4000, 5000, 6000]

total_joe_exp = calculate_total(joe_exp_list)
total_doe_exp = calculate_total(doe_exp_list)

print("Total Joe Expenses: ", total_joe_exp)
print("Total Doe Expenses: ", total_doe_exp)



# Using For loop
"""
total_joe = 0
for item in joe_exp_list:
    total_joe = total_joe + item
print("Total Expense by Joe: ", total_joe)

total_doe = 0
for item in doe_exp_list:
    total_doe = total_doe + item
print("Total Expense by Doe: ", total_doe)
"""
