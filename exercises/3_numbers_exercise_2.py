# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square

# Area of SQUARE FEET = LENGTH ** 2

length = 5.5
area_sqf_ft = length**2
print("Area of Square Feet: ", area_sqf_ft)
cost_per_sqft = 500
total_cost = area_sqf_ft*cost_per_sqft
print("Total Cost :", total_cost)

