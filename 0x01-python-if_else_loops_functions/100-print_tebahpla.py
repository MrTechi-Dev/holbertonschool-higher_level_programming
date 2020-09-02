#!/usr/bin/python3
for g in range(0, 26):
    if (g % 2 == 0):
        print("{:s}".format(chr(122 - g)), end="")
    else:
        print("{:s}".format(chr(122 - g - 32)), end="")
