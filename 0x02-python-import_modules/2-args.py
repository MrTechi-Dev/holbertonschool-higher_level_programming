#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    n = len(sys.argv) - 1

if n == 0:
    print("0 arguments")
else:
    if n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(n, argv[n]))
    else:
        print("{} argument:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, argv[i]))
