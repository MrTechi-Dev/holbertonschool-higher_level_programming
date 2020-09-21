#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    counter = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except (TypeError, ValueError):
            pass
        counter = counter + 1
    print()
    return count
