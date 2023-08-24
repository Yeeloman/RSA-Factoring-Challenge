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


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    exit(1)
try:
    with open(sys.argv[1], "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = int(line)
            result = factorize(line)
            for fact1, fact2 in result:
                print("{}={}*{}".format(line, fact2, fact1))
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)
except Exception as e:
    print("An error occurred:", e)
