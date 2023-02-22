# Created by Srinivas Kadiyala at 22-02-2023
'''
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
'''

result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails",
          "tails", "tails"]

count = 0

for item in result:
    if item == 'heads':
        count = count + 1
print("Heads Count: ", count)

count = 0
for item in result:
    if item == 'tails':
        count = count + 1
print("Tails Count: ", count)
