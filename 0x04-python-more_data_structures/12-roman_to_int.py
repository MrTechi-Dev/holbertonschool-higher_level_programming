#!/usr/bin/python3
def roman_to_int(roman_string):
    x = 0
    if type(roman_string) != str:
        return x
    if roman_string is None:
        return x
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            x = x + roman[roman_string[i]] - 2 * roman[roman_string[i - 1]]
        else:
            x = x + roman[roman_string[i]]
    return x
