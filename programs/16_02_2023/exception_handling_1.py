# Created by Srinivas Kadiyala at 16-02-2023

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
try:
    num3 = int(num1) / int(num2)
except Exception as e:
    print("exception occurred: ", e)
    num3 = None
print("Division by number: ", num3)
