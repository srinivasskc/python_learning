# Created by Srinivas Kadiyala at 22-02-2023
'''
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
'''

india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name1 = input("Enter first city name: ")
city_name2 = input("Enter second city name: ")

if city_name1 in india and city_name2 in india:
    print("Both Cities are in India")
elif city_name1 in pakistan and city_name2 in pakistan:
    print("Both Cities are in Pakistan")
elif city_name1 in bangladesh and city_name2 in bangladesh:
    print("Both Cities are in Bangladesh")
else:
    print("They dont belong to same country")
