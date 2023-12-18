#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for x in range(list_length):
        try:
            a = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            a = 0
            print("division by 0")
        except TypeError:
            a = 0
            print("wrong type")
        except IndexError:
            a = 0
            print("out of range")
        finally:
            new_list.append(a)
    return new_list
