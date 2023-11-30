#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

counter = len(sys.argv) - 1

if counter != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = sys.argv[2]
total = 0

if __name__ == "__main__":

    if operator == '+':
        total = add(a, b)
        print("{0} + {1} = {2}".format(a, b, total))
    elif operator == '-':
        total = sub(a, b)
        print("{0} - {1} = {2}".format(a, b, total))
    elif operator == '*':
        total = mul(a, b)
        print("{0} * {1} = {2}".format(a, b, total))
    elif operator == '/':
        total = div(a, b)
        print("{0} / {1} = {2}".format(a, b, total))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
