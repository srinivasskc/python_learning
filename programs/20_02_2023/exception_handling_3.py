# Created by Srinivas Kadiyala at 20-02-2023
x = input("Enter a number: ")
y = input("Enter another number: ")
try:
    z = x / int(y)
except TypeError as e:
    # print("Exception is : ", e)
    # print("Exception Type is: ", type(e).__name__)
    print("Type Error Exception Occurred")
    z = None
print("Division is : ", z)