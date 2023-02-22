# Created by Srinivas Kadiyala at 22-02-2023

'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

monthly_expenses = [2200, 2350, 2600, 2130, 2190]
print(type(monthly_expenses))
print(monthly_expenses)

expense_jan_feb = monthly_expenses[1]-monthly_expenses[0]
print("dollars spent extra in month of feb", expense_jan_feb)

expenses_first_quarter = monthly_expenses[1] + monthly_expenses[2] + monthly_expenses[3]
print("Expenses in first quarter: ", expenses_first_quarter)

monthly_expenses.append(1980)
print("June Expenses", monthly_expenses)

monthly_expenses[3] = monthly_expenses[3] - 200
print("Correction in April Expenses: ", monthly_expenses[3])

print("Updated Monthly Expenses: ", monthly_expenses)

print("Did I spend $2000 in any month?: ", 2000 in monthly_expenses)

print("Did I spend $2200 in any month?: ", 2200 in monthly_expenses)
