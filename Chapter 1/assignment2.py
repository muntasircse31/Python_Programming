# Question - Take radius as input and calculate the area of a circle

# Formula = Area = π × r²

pi = 3.1416 # pi value

r = float(input("Enter your radius: ")) # Input function user can input value

area = pi * (r * r) #formula of area of circle

print("Area of a circle is -", area) # Area of circle value output


# Question - Take diameter as input and calculate the area of a circle.

# Formula:
# Diameter = 2r
# Radius = Diameter / 2
# Area = π × r²

diameter = float(input("Enter the value of diameter: "))

radius = diameter / 2

area = 3.14 * (radius ** 2)

print("Area of a circle is -", area)
