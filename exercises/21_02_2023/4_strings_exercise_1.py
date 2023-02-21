# Created by Srinivas Kadiyala at 21-02-2023

'''
Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable,
one using + operator and the other using f-string.
Now Print the address in such a way that the street,
city and country prints in a separate line
'''

street = input("Enter the street name: ")
city = input("Enter the city name: ")
country = input("Enter the country name: ")

# print using + operator
address = street + " " + city + " " + country
print(address)
print(street + "\n" + city + "\n" + country)

# Printing address using f-string
address = f'{street}\n{city}\n{country}'
print("Printing Address using f-string:\n", address)


