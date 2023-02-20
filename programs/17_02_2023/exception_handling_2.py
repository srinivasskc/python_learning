# Created by Srinivas Kadiyala at 17-02-2023
x = input("Enter a number: ")
y = input("Enter a number: ")
try:
  z = x / int(y)
except Exception as e:
    print("Exception is: ", e)
    print("Exception Type is: ", type(e).__name__)
    z = None
print("Division is: ", z)

