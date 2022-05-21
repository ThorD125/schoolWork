"""
# To Dutch
Write the function`to_dutch`, such that all tests succeed.

The key of this exercise is to start small: make your
function work for simple and small input.
E.G., make your to_dutch function first for digits,
than for 2digit numbers, etc. Just like in the previous exercises
the key is to reuse existing functions.

If the functionality you need already exists in
(a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""
# TODO

# from assignment03 import reverse
small = [
    'nul', 'een', 'twee', 'drie', 'vier',
    'vijf', 'zes', 'zeven', 'acht', 'negen',

    'tien', 'elf', 'twaalf', 'dertien', 'veertien',
    'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien'
]

tens = ['nul', 'tien', 'twintig', 'dertig', 'veertig',
        'vijftig', 'zestig', 'zeventig', 'tachtig', 'negentig']

scales = ['een', 'tien', 'honderd', 'duizend ', ' miljoen ',
          ' miljard ', ' biljoen ', ' biljard ', ' triljoen ', ' triljard ']


def to_dutch(number):
    if 0 <= number and number < 20:
        return small[number]
    else:
        result = ""
        for i in range(0, len(str(number))):
            betweenresult = ""
            if i == 0:
                betweenresult += "en" + small[int(str(number)
                                                  [int(len(str(number)) - i - 1)])]
            elif i == 1:
                betweenresult = ""
                if tens[int(str(number)
                            [int(len(str(number)) - i - 1)])] != "nul":

                    betweenresult += "en" + tens[int(str(number)
                                                     [int(len(str(number)) - i - 1)])]
            elif i >= 2:
                if small[int(str(number)
                             [int(len(str(number)) - i - 1)])] != "nul":

                    betweenresult += "en" + small[int(str(number)
                                                  [int(len(str(number)) - i - 1)])]
                betweenresult += scales[i]

            if result[len(result)] == "e":
                betweenresult = "ë" + betweenresult[1:]

            if len(str(number)) == 2:
                result = result + betweenresult
            else:
                result = betweenresult + result
        return result[2:len(result)]


# print('achttien', to_dutch(18))
# print('zevenenvijftig', to_dutch(57))
# print('tweeëntwintig', to_dutch(22))

# print("part")

# print('honderdtien', to_dutch(110))  # !!!
# print('driehonderdvijftien', to_dutch(315))
# print('driehonderddrieëndertig', to_dutch(333))
# print('driehonderd', to_dutch(300))
# print('driehonderdenzeven', to_dutch(307))

# print("part")

# print('zevenhonderdeenentachtig miljoen '
#       'vierhonderdtweeënvijftigduizend '
#       'driehonderdeenentwintig',
#       to_dutch(781452321))
# print('min '
#       'zevenhonderdeenentachtig miljoen '
#       'vierhonderdtweeënvijftigduizend '
#       'driehonderdeenentwintig',
#       to_dutch(-781452321))
