total = 0

# b = default value


def sum_values(a, b=5):
    """
    :param a: 6
    :param b: 5
    :return:
    """
    print("a: ", a)
    print("b: ", b)

    total = a+b
    print("Total inside the function: ", total)
    return total


x = sum_values(a=6)
# position arguments
print("Total Outside the function: ", total)
