"""
Take the times as two numerical inputs: hours and minutes.
Program the turtle to draw a clock (circle) with large
ticks for the hours and smaller ticks for the minutes.
Finally draw the hands of time.
"""

import turtle

line = 0
lines = 12

hours = int(input("Hours??"))
# hours = 2
minutes = int(input("Minutes??"))
# minutes = 49


hoursangle = hours / 12 * 360

minutesangle = minutes / 60 * 360

forward_int = 100

turtle.speed(10000)
turtle.left(90)

turtle.right(hoursangle)
turtle.forward(forward_int/2)
turtle.forward(-forward_int/2)
turtle.left(hoursangle)

turtle.right(minutesangle)
turtle.forward(forward_int*0.8)
turtle.forward(-forward_int*0.8)
turtle.left(minutesangle)

turtle.color("white")

turtle.forward(forward_int)
turtle.right(90)
turtle.forward(-forward_int / 4)

turtle.color("black")

while line < 12:
    turtle.forward(forward_int / 2)
    turtle.right(360 / lines)
    line += 1


turtle.shape("turtle")


turtle.exitonclick()
