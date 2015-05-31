# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:41:25 2015

@author: karana
"""
from file_read_write import *

def find_tag(html_str, start_index):
    start_pos = html_str.find('<', start_index)
    end_pos = html_str.find('>', start_index)
    if start_pos < 0 or end_pos < 0:
        return None, None
    else:
        return html_str[start_pos + 1 : end_pos], end_pos
    
def validate_html_tags():
    file_contents = open_file()
    
    tag_stack = []
    html_balanced = True
    start_pos = 0
    content_end = len(file_contents) - 1
    
    while html_balanced == True:
        tag, end_pos  = find_tag(file_contents, start_pos)
        if tag == None:
            html_balanced = False
            break
        
        tag_pos = tag.find('/')
        if tag_pos < 0:
            tag_stack.append(tag)
        else:
            parsed_tag = tag[tag_pos + 1:]
            start_tag = tag_stack.pop()
            if start_tag != parsed_tag:
                html_balanced = False
        
        if end_pos == content_end:
            break
        
        start_pos = end_pos + 1
    
    if html_balanced:
        print 'doc was balanced'
    else:
        print 'doc was not balanced'
        
validate_html_tags()