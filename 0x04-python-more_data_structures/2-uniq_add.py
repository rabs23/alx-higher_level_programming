#!/usr/bin/python3

def uniq_add(my_list=[]):
    total_sum = 0
    for val in set(my_list):
        total_sum += int(val)
    return total_sum
