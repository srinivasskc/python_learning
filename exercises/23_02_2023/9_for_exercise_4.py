# Created by Srinivas Kadiyala at 23-02-2023
'''
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
'''

for i in range(5):
    print(f'you have ran {i+1} kms')
    question = input("Are you Tired?")
    if question == 'yes':
        print("you didn't finish the race")
        break
    else:
        continue

if i == 4:
    print(f'Congratulations! You have finished {i+1} kms race')
elif i == 2:
    print(f'you have made half-way through.')
