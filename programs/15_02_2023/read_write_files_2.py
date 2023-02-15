# Created by Srinivas Kadiyala at 15-02-2023

# open the file and read the file
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
print(f.read())
f.close()

# reading line by line and print the statements from file
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
for line in f:
    print(line)
f.close()

# split the words from the file and read
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
for line in f:
    words = line.split(" ")
    print(type(words))
    print(words)
    str_words = str(words)
    print(type(str_words))
    print(str_words)
    print(len(str_words))
f.close()

# split the words from the file and read and add length of line words
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
for line in f:
    words = line.split(" ")
    str_words = str(words)
    print(str_words, len(words))
f.close()

# split the words from the file and read and add length of line words and write to another file
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
f_out = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes_wc.txt", "w")
for line in f:
    words = line.split(" ")
    str_words = str(words)
    f_out.write(str_words + "  word count: " + str(len(words)) + "\n")
f_out.close()
f.close()