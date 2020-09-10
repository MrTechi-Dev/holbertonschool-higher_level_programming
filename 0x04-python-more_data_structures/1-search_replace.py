#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newone = my_list.copy()
    for x in range(len(newone)):
        if newone[x] == search:
            newone[x] = replace
    return newone
