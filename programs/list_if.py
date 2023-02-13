indian=["naan","samosa","dal"]
chinese=["noodles","egg role","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter the dish name: ")

if dish in indian:
    print("Dish is Indian")
elif dish in chinese:
    print("Dish is chinese")
elif dish in italian:
    print("Dish is Italian")
else:
    print("Dish is not available")