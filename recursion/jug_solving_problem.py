# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:40:53 2015

@author: karana
"""

class jug_fill_problem:
    
    def __init__(self, jug1_vol, jug2_vol, goal_vol):
        self.jug1 = (jug1_vol, 0)
        self.jug2 = (jug2_vol, 0)
        self.goal = goal_vol
        
        self.terminal_state = []
        self.terminal_state.append(self.jug1, jug1_vol)
        self.terminal_state.append(self.jug2, jug2_vol)
        
    def is_goal_reached(self):
        
        if (self.jug1[1] == self.goal or self.jug2[1] == self.goal):
            return True
        else:
            return False
    