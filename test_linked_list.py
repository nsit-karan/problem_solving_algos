# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 15:55:43 2015

@author: karana
"""
from node import UnorderedList

def test_unordered_list():
    ulist = UnorderedList();
    ulist.add(1)
    ulist.add(2)
    ulist.add(3)
    
    print ulist.size()
    print ulist.search(4)
    print ulist.search(10)
    print ulist.search(2)

    ulist.print_ulist()
    ulist.remove(20)
    ulist.remove(3)
    ulist.remove(1)
    
    ulist.print_ulist()
    
    ulist.add(1)
    ulist.add(10)
    ulist.add(20)
    
    ulist.print_ulist()
    
    ulist.append(70)
    ulist.print_ulist()
    
    
l = test_unordered_list()