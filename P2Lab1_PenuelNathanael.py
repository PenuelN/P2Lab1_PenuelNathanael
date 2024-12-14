# Nathanael Penuel
# 10/4
# P2LAB1
# This program calculates and displays the measurements of a circle.

import math

# Ask for the radius as a float
radius = float(input("What is the radius of the circle? "))

# Calculate the diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
