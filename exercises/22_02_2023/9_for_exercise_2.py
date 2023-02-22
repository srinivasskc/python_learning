# Created by Srinivas Kadiyala at 22-02-2023
'''
Print square of all numbers between 1 to 10 except even numbers
'''

for i in range(1, 11):
    if(i % 2 == 0):
        continue
    print(i * i)
