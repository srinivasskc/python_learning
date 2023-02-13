'''
Dictionary with Telephone Directory Example
'''

d = {"John": 9011422100,"Mike": 2011001200, "Casey": 2017411421}

# Print the dictionary.
print(d)

# Print John Number
print(d["John"])

# Add Sam to Dictionary
d["Sam"]=7411411423
print(d)

# delete number from dictionary
del d["John"]
print(d)

print("sam" in d)
print("Sam" in d)

d.clear()
print(d)


