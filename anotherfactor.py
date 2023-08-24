#!/usr/bin/python3

import sys
import sympy

def factor(num):
    factors = sympy.factorint(num)
    if len(factors) != 3:
        count = 0
        num2 = 1
        for fct in factors:
            if count >= 1:
                num2 = fct * num2
            count += 1
    else:
        num2 = 3
    num1 = 2
    result = 0
    if num2 > num1:
        result = 1
    if result == 1:
        temp = num1
        num1 = num2
        num2 = temp
    print(f"{num}={num1}*{num2}")




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
            factor(line)
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)
except Exception as e:
    print("An error occurred:", e)
    sys.exit(1)
