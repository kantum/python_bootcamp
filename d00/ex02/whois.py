import sys

if sys.argv[1].lstrip('-+').isdigit() and len(sys.argv) == 2:
    num = abs(int(sys.argv[1]))
    if num == 0:
        print("I'm zero")
    elif (num % 2) == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
else:
    print("ERROR")
