# Created by Srinivas Kadiyala at 15-02-2023

# Create a new file
f = open("/programs/14_02_2023/feb.txt", "w")
f.write("Hello World!!")
f.close()
f = open("/programs/14_02_2023/feb.txt", "a")
f.write("by Srinivas!!")
f.close()
f = open("/programs/14_02_2023/feb.txt", "a")
f.write("\n - 15th Feb 2023")
f.close()