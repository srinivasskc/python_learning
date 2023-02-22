# Created by Srinivas Kadiyala at 22-02-2023
'''
Write a python program that can tell you if your sugar is normal or not.
Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
'''

sugar_level = float(input("Print the Fasting Sugar Level: "))
# print(type(sugar_level))
# print("Fasting Sugar Level: ", sugar_level)

if sugar_level < 80:
    print("Low Sugar Level")
elif sugar_level > 100:
    print("High Sugar Level")
else:
    print("Normal Sugar Level")


