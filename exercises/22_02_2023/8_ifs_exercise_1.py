# Created by Srinivas Kadiyala at 22-02-2023
'''
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to
'''

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

print("Cities in India: ", india)
print("Cities in pakistan: ", pakistan)
print("Cities in bangladesh: ", bangladesh)

city_name = input("Enter a City Name: ")

if city_name in india:
    print("City is in India")
elif city_name in pakistan:
    print("City is in pakistan")
elif city_name in bangladesh:
    print("City is in Bangladesh")
else:
    print(f'sorry i dont know this city - {city_name}')