"""
# Check Sign (2)
Read one integer (int).
The program prints a ```+``` when the number is positive.
The program prints a ```-``` when the number is negative.
The program prints a ```0``` when the number is zero.
"""

number = int(input("Input a number"))

if number == 0:
    print('0')
elif number > 0:
    print('+')
else:
    print('-')
