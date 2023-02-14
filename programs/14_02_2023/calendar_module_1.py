import calendar

# Documentation: https://docs.python.org/3/library/calendar.html

# All functions in calendar module.
cal_functions = dir(calendar)
print(cal_functions)


# print the calendar of the month/year
cal = calendar.month(2023,2)
print(cal)

# check if the year is leap year or not.
leap = calendar.isleap(2023)
print(leap)

leapdays = calendar.leapdays(2024,2025)
print(leapdays)