import sys
import string


def operations(x, y):
    print("Sum:\t\t", x + y)
    print("Difference:\t", x - y)
    print("Product:\t", x * y)
    if y != 0:
        print("Quotient:\t", x / y)
        print("Remainder:\t", x % y)
    else:
        print("Quotient:\tERROR (div by zero)")
        print("Remainder:\tERROR (modulo by zero)")

    args = len(sys.argv) - 1
    if args == 0:
        print("prout")
    elif sys.argv[1].lstrip('-+').isdigit() \
        and sys.argv[2].lstrip('-+').isdigit() \
            and len(sys.argv) == 2:
        operations(sys.argv[1], sys.argv[2])
