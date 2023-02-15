# Created by Srinivas Kadiyala at 15-02-2023

# Check if the file is closed or not
f = open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt", "r")
print(f.read())
print(f.closed)
if not f.closed:
    f.close()
    print(f.closed)
else:
    f.read()
