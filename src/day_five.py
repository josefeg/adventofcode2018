#!/usr/bin/env python3

import re
import string


def reduce_polymer(polymer):
    old_polymer = ""
    while old_polymer != polymer:
        old_polymer = polymer
        polymer = re.sub(r"aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz", "", polymer)
    return polymer


def remove_problematic_polymer(polymer):
    min_length = len(polymer)
    for x in string.ascii_lowercase:
        pattern = "{}|{}".format(x, x.upper())
        new_polymer = re.sub(pattern, "", polymer)
        reduced_polymer = reduce_polymer(new_polymer)
        if len(reduced_polymer) < min_length:
            min_length = len(reduced_polymer)
    return min_length


def main():
    with open("resources/day_five.txt") as f:
        polymer = f.read().strip()

    reduced_polymer = reduce_polymer(polymer)
    print(len(reduced_polymer))
    print(remove_problematic_polymer(reduced_polymer))


if __name__ == "__main__":
    main()
