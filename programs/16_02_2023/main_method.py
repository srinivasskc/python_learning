# Created by Srinivas Kadiyala at 16-02-2023

def area_of_triangle(base, height):
    print("I am in area of triangle")
    print("__name__", __name__)
    return 1/2 * (base * height)


if __name__ == "__main__":
    print("I am in main_method.py")
    area = area_of_triangle(2, 5)
    print("area of triangle: ", area)



