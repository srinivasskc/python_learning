# Created by Srinivas Kadiyala at 15-02-2023

# opening files - With will close file automatically

with open("E:\\development\\my_python_project\\programs\\15_02_2023\\rhymes.txt","r") as f:
    print(f.read())

print(f.closed)