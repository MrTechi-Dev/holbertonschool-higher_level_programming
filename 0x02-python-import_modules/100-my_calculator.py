#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    c = len(argv) - 1
    if c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    s = argv[2]
    b = int(argv[3])
    if "+" in s:
        print("{} {} {} = {}".format(a, s, b, add(a, b)))
    elif "-" in s:
        print("{} {} {} = {}".format(a, s, b, sub(a, b)))
    elif "*" in s:
        print("{} {} {} = {}".format(a, s, b, mul(a, b)))
    elif "/" in s:
        print("{} {} {} = {}".format(a, s, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
