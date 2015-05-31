# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:31:03 2015

@author: karana
"""

def sum_list(list_nos):
    if len(list_nos) == 1:
        return list_nos[0]
    else:
        return list_nos[0] + sum_list(list_nos[1:])
        
def is_palin(str_palin):
    if len(str_palin) == 2:
        return str_palin[0] == str_palin[-1]
    else:
        return str_palin[0] == str_palin[-1] and is_palin(str_palin[1 : -1])
        
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

"""
Reverses the list in-place by swappning elements recursively
"""
def rev_list(orig_list, start_loc, end_loc):
    """
    Calculate the length to reverse:
    """
    len_to_rev = end_loc - start_loc + 1
    if len_to_rev == 1:
        return
    elif len_to_rev == 2:
        temp = orig_list[start_loc]
        orig_list[start_loc] = orig_list[end_loc]
        orig_list[end_loc] = temp
    else:
        """
        Swap the start_loc with end_loc
        Recursively invoke the call for the list excluding the start_loc
        and end_loc
        """
        temp = orig_list[start_loc]
        orig_list[start_loc] = orig_list[end_loc]
        orig_list[end_loc] = temp
        rev_list(orig_list, start_loc + 1, end_loc - 1)

def print_fib(n):
    i = 0
    j = 1
    count = 0
    while count < n:
        print i
        sum = i + j
        i = j
        j = sum
        count = count + 1