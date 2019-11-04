import sys
import string

newstring = ''
args = len(sys.argv) - 1

for arg in sys.argv[1:]:
    for a in arg:
        if (a.isupper()) is True:
            newstring += (a.lower())
        elif (a.islower()) is True:
            newstring += (a.upper())
        else:
            newstring += a
    args -= 1
    if args > 0:
        newstring += ' '

print(newstring[::-1])
