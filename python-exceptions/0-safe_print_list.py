#!/usr/bin/python3

def safe_print_list(my_list=[], x= 0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print("")    
    except IndexError:
        print("")
    return count


safe_print_list([2,3], x= 30 )