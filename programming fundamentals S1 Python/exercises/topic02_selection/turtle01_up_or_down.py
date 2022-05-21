"""
Program the turtle to ask a number.
Regardless of the sign of the number (positive or negative),
the turtle should move a distance, proportionally to the input.
For example: -100 or 100 will make the turtle move further to
the right than -5 or 5.

Then make a 45° turn - upwards when the input was positive,
downwards when the input was negative.
Finally, move the turtle again over the same distance as
before in its new direction.

For positive input the turtle draws something like this:
    /
>--/

For negative input the turtle draws something like this:
>--\
    \

"""
import turtle

user_input_number = int(input("User input number??"))

turtle.forward(abs(user_input_number))

if user_input_number < 0:
    turtle.right(45)
else:
    turtle.left(45)

turtle.forward(abs(user_input_number))

turtle.exitonclick()
