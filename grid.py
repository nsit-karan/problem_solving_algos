"""
Create a rectagular grid and iterate through 
a subset of its cells in a specified direction
"""

GRID_HEIGHT = 4
GRID_WIDTH = 6

# Create a rectangular grid using nested list comprehension 
# Inner comprehension creates a single row
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                           for row in range(GRID_HEIGHT)]

def traverse_grid(start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    
    for step in range(num_steps):
        new_row = start_cell[0] + step * direction[0]
        new_col = start_cell[1] + step * direction[1]
        print "Processing cell", (new_row, new_col), 
        print "with value", EXAMPLE_GRID[new_row][new_col]

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
    

def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print
        
    print "Traversing diagonal"
    traverse_grid((0, 0), (1, 1), min(GRID_WIDTH, GRID_HEIGHT))
    
    line1 = [1,2,0,2,0,0,5]
    print merge(line1)
    
    line2 = [4,8]
    print merge(line2)
    
run_example()


