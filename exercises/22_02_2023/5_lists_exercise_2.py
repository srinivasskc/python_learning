# Created by Srinivas Kadiyala at 22-02-2023

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''


heroes= ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(heroes)

print("length of heroes: ", len(heroes))

heroes.append('black panther')
print("Adding black panther to the list: ", heroes)

heroes.remove(heroes[5])
print("Remove black panther from list: ", heroes)

heroes.insert(3, 'black panther')
print("Adding black panther after hulk: ", heroes)

heroes[1:3] = ['doctor strange']
print("Removed Thor and Hulk and Replaced Doctor Strange: ", heroes)

heroes.sort()
print("Print Heroes in alphabetical order: ", heroes)

