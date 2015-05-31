# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:55:28 2015

@author: karana
"""

import random

def roll_die(num_sides):
    """
    Add 1 to the result since the result is:
    0 <= result <= num_sides - 1 and typically
    die rolls are from 1 to num_sides
    """
    result = random.randrange(0, num_sides) + 1
    return result
    
def roll_test(num_sides, no_rolls):
    for _ in range(no_rolls):
        roll = roll_die(num_sides)
        print roll

