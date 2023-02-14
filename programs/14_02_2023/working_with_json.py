# first, we will create a dictionary object
# In Python, we do not have JSON object.
# JSON is a format.

book = {}

# In this dictionary, we will add the data

book['tom'] = {
    "name": "tom",
    "address": "123 street, ny, 12014",
    "phone": 474541512
}

book['bob'] = {
    "name": "bob",
    "address": "1234 street, nj, 14121",
    "phone": 447412141
}

print(book)
print(type(book))
# printing the book dictionary.

# import the dictionary book to JSON String
import json
s = json.dumps(book)
print(s)
print(type(s))

# Write the data to file.
print("Writing the data to file")
with open("E:\\development\\my_python_project\\programs\\14_02_2023\\bookJson.txt", "w") as f:
    f.write(s)

# open and read the file
print("Reading the data from file")
file = open("E:\\development\\my_python_project\\programs\\14_02_2023\\bookJson.txt", "r")
s = file.read()
print(s)

import json
book1 = json.loads(s)
print(type(book1))
print(book1)
print(book1["tom"])
print(book1["bob"]["phone"])

# for loop: print all values from book1
for person in book1:
    print(book1[person])
