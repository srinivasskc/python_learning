#search for key in different locations

key_location="desk"
locations=["chair","desk","bedroom","laptop desk","car","living room"]

for i in locations:
    if(i==key_location):
        print("Key is found in ", i)
        break
    else:
        print("Key is not found in ", i)
