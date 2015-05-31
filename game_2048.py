"""
Created on Wed Apr 15 22:46:27 2015

@author: karana

Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

"""
Offsets for computing tile indices in each direction.

DO NOT MODIFY this dictionary
   
This is reverse of what someone would assume.
"""

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function which merges a row,i.e, collapses the adjacent duplicate elements
    and replaces them with double value for the same(similar to 2048 game)
    """
    if (len(line) == 1):
        return line
    
    new_line = [s for s in line if s != 0]
    num_zeros = len(line) - len(new_line)
    non_zero_len = len(new_line)
    
    for index in range(num_zeros):
        new_line.append(0)
    
    final_line = []
    j = 0
    while j < non_zero_len:
        if j == non_zero_len - 1 or new_line[j] != new_line[j + 1]:
            final_line.append(new_line[j])
            j = j + 1
        else:
            final_line.append(2*new_line[j])
            j = j + 2
    
    num_zeros = len(line) - len(final_line)
    for i in range(num_zeros):
        final_line.append(0)
    
    return final_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.initial_indices = {}
        self.path_len = {}
        self.reset()
    
    def init_initial_indices(self):
        """
        Initialize the initial_indices
        which will have the initial indices in case
        the different operations are done
        """
        
        up_indices = []
        down_indices = []
        for i in range(self.grid_width):
            up_indices.append((0, i))
            down_indices.append((self.grid_height - 1, i))
        
        self.initial_indices[UP] = up_indices
        self.initial_indices[DOWN] = down_indices
                
        left_indices = []
        right_indices = []
        for i in range(self.grid_height):
            left_indices.append((i, 0))
            right_indices.append((i, self.grid_width - 1))
        
        self.initial_indices[LEFT] = left_indices
        self.initial_indices[RIGHT] = right_indices
        
    def init_path_len(self):
        """
        Initialize the map where key is the direction and
        value is the length in that direction.
        For instance:
        For UP, len_path will be row_count
        for LEFT, len_path will be col_cound
        """
        self.path_len = {}
        self.path_len[UP] = self.get_grid_height()
        self.path_len[DOWN] = self.get_grid_height()
        self.path_len[LEFT] = self.get_grid_width()
        self.path_len[RIGHT] = self.get_grid_width()
        
    def traverse_grid(self, direction, start_cell, no_of_steps):
        #print 'direction: ', direction, ',start_cell: ', start_cell, ',no_steps: ', no_of_steps
        values = []
        for step in range(no_of_steps):
            new_row = start_cell[0] + step*direction[0]
            new_col = start_cell[1] + step*direction[1]
            values.append((self.grid[new_row][new_col]))
        return values
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()
        
        self.init_initial_indices()
        self.init_path_len()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        debug_str = ""
        for row in range(self.grid_height):
            debug_str = debug_str + ' ['
            for col in range(self.grid_width):
                debug_str = debug_str + ' ' + str(self.grid[row][col])
            debug_str = debug_str + '] \n'
        
        print debug_str
        return debug_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        dir_indices = self.initial_indices[direction]
        is_tile_same = True
        for dir_index in dir_indices:
            row = dir_index[0]
            col = dir_index[1]
            
            list_to_merge = self.traverse_grid(OFFSETS[direction], dir_index, self.path_len[direction])
            #print 'list_to_merge' , list_to_merge, ', path_len', self.path_len[direction], ', initial_index', dir_index                
            merged_list = merge(list_to_merge)
            
            is_tile_same = is_tile_same or list_to_merge == merged_list
            #print 'merged list', merged_list
            for i in range(self.path_len[direction]):
                self.set_tile(row + i*OFFSETS[direction][0], col + i*OFFSETS[direction][1], merged_list[i])
                
        
        if is_tile_same == True:
            self.new_tile()
    
    def generate_random(self):
        """
        Generate either 2(with 90% probability) or 4(with 10% probability)
        """
        rand_no = random.random()
        if rand_no < 0.1:
            return 4
        else:
            return 2
    
    def find_random_empty_tile(self):
        empty_tiles = []
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 0:
                    empty_tiles.append((row, col))
        
        if len(empty_tiles) == 0:
            return None
        else:
            return random.choice(empty_tiles)
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        new_tile_no = self.generate_random()
        new_loc = self.find_random_empty_tile()
        if new_loc == None:
            print 'No empty tile found'
        else:
            new_row = new_loc[0]
            new_col = new_loc[1]
            self.set_tile(new_row, new_col, new_tile_no)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


t = TwentyFortyEight(3, 5)
t.__str__()
t.move(UP)
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
