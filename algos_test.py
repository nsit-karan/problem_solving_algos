# -*- coding: utf-8 -*-
"""
Created on Sat May 02 17:08:04 2015

@author: karana
"""

def min_list(list_nos):
    min_no = list_nos[0]
    for i in list_nos:
        if i < min_no:
            min_no = i
    return min_no
    
    
def min_list_quadratic(list_nos):
    min_no = list_nos[0]
    for no in list_nos:
        local_min = no
        for i in list_nos:
            if i < local_min:
                local_min = i
        if local_min < min_no:
            min_no = local_min
    return min_no

def paranthesis_match(expr):
    parantheses = []
    balanced = True
    len_expr = len(expr)
    index = 0
    
    while index < len_expr and balanced == True:
        symbol = expr[index]
        if symbol == '(':
            parantheses.append(symbol)
        else:
            if len(parantheses) == 0:
                balanced = False
                break
            else:
                parantheses.pop()
        index = index + 1
    
    return balanced and len(parantheses) == 0

def convert_dec_bin(no):
    bin_list = []
    while no > 0:
        rem = no % 2
        bin_list.append(rem)
        no = no / 2
        
    bin_str = ""
    while len(bin_list) > 0:
        bin_str = bin_str + str(bin_list.pop())
    
    return bin_str
    
str_par = '(((()))'
print paranthesis_match(str_par)