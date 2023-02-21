# break = 5
# cannot use break as variable name.

birth_year = input("Enter the Birth Year in YYYY format: ")
birth_year = int(birth_year)
current_year = input("Enter the current year: ")
current_year = int(current_year)

age = current_year-birth_year
print("Age of the employee: ", age)
