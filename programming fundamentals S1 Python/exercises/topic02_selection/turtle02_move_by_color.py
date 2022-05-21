"""
Program the turtle to ask for a new color (string).
Change the color of the turtle and make it move differently
depending on the color. You can choose which colors you want
to support and which drawings you want to make
(you are the programmer now, you make the decisions).

**Hint:** Lookup how the change the color of the turtle.
(http://lmgtfy.com/?q=python+turtle+change+color)s
"""
import turtle

user_input_color = input("User input color??")

if user_input_color == "purple":
    turtle.color("purple")
    turtle.forward(100)
else:
    turtle.forward(-100)


turtle.exitonclick()
