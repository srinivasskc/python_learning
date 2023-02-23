# Created by Srinivas Kadiyala at 23-02-2023
'''
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and
program should tell you in which month that expense occurred.
If expense is not found then it should print that as well.
'''

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
expense_list = [2340, 2500, 2100, 3100, 2980]

expense = input("Enter the expense amount:")
expense = int(expense)
# print(expense)

month = -1

# print(range(len(expense_list)))

for item in range(len(expense_list)):
    if expense == expense_list[item]:
        month = item
        break

if(month != -1):
    print(f'You have spent {expense} in the {month_list[month]}')
else:
    print(f'Entered {expense} is not in the Expense_List: {expense_list}')

