#!/usr/bin/python3

import sys
import sympy


def factorize(number):

    factors = sympy.factorint(number)

    factor_pairs = []
    for prime in factors.keys():
        other_factor = number // prime
        factor_pairs.append((prime, other_factor))
        break

    return factor_pairs


with open(sys.argv[1], "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = int(line)
        result = factorize(line)
        for fact1, fact2 in result:
            print("{}={}*{}".format(line, fact2, fact1))
