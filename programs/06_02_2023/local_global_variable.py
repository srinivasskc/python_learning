total = 0


def sum_values(a, b):
    print("a: ", a)
    print("b: ", b)

    total = a+b
    print("Total inside the function: ", total)
    return total


x = sum_values(b=5, a=6)
# position arguments
print("Total Outside the function: ", total)

# print(total) - cannot access total.