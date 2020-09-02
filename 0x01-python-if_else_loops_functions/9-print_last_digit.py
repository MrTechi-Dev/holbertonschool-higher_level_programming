#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        numberpos = n * -1
    else:
        numberpos = n
    r = numberpos % 10
    print(r, end='')
    return r