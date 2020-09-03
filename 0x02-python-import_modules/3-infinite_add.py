#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    n = len(sys.argv) - 1
    var = 0
    for i in range(1, n + 1):
        var += int(argv[i])
    print(var)
