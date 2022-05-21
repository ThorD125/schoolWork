"""
Program the turtle to show all possible RGB colors.
"""

import turtle

r = int(input("Input number for red??"))
while not (0 <= r and r <= 255):
    r = int(input("Input number for red??"))
g = int(input("Input number for green??"))
while not (0 <= g and g <= 255):
    g = int(input("Input number for green??"))
b = int(input("Input number for blue??"))
while not (0 <= b and b <= 255):
    b = int(input("Input number for blue??"))


rgb = r, g, b


turtle.shape('turtle')
turtle.colormode(255)
turtle.color(rgb)

turtle.exitonclick()
