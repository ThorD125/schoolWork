"""
Program the turtle ask for a number (integer).
Then draw a regular polygon (shape with equal
sides and equal angles) with that many sides.
"""

import turtle


user_input_sides = int(input("User input number of sides??"))
# user_input_sides = 7

count = 0


while count < user_input_sides:
    turtle.forward(100)
    turtle.right(360 / user_input_sides)
    count += 1

turtle.exitonclick()
