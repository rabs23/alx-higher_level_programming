#!/usr/bin/python3
import sys

total_arg = len(sys.argv)
total = 0

if __name__ == "__main__":
    if total_arg > 1:
        for i in range(1, total_arg):
            total += int(sys.argv[i])
    print("{}".format(total))
