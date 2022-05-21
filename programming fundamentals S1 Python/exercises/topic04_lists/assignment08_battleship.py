"""
# Battleship
Battleship (zeeslag) is a pen-and-paper game played on a field of 10 by 10.
Variables `a` and `b` contain such a field, which is represented in Python as
a list of lists.

Variable `a` contains the field on which all vessels are marked:
-  `False` implies empty, no vessel;
- a single letter implies a part of vessel;
- no other content is possible.


Variable `b` contains the field on which all attacks are marked:
-  `False` implies no attacks recorded;
- the letter 'x' implies successful attack;
- the letter 'o' implies failed attack;
- no other content is possible.

Write a program that computes two ratios:
- **Damage**: what amount of the fleets has been hit
    (the number of successful attacks divided by
    the total number of vessel(parts));
- **Efficiency**: what amount of the attacks was successful
    (number of successful attacks divided by total number of attacks);

Your programs should print these two ratios
(see example, use `format(3.1415, '.2f')`)

Example output:
Damage: 0.50
Efficiency: 0.50
"""

a = [
    [False, "I", False, False, False, False, False, False, False, False],
    [False, False, "I", False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False]
]
b = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, "x", False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, "o", False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False]
]
succes = 0
failed = 0
ships = 0

for i in a:
    for j in i:
        if j == "I":
            ships += 1


for i in b:
    for j in i:
        if j == "x":
            succes += 1
        if j == "o":
            failed += 1

print("Damage:", format(succes / (succes + failed), '.2f'))
print("Efficiency:", format(succes / ships, '.2f'))
