#==========================================================MINESWEEPER==========================================================#

# Define and assign grid as a list

grid = [["-", "-", "-", "#", "#"], 
        ["-", "#", "-", "-", "-"], 
        ["-", "-", "#", "-", "-"], 
        ["-", "#", "#", "-", "-"], 
        ["-", "-", "-", "-", "-"]]

#==========================================================MINESWEEPER==========================================================#

# Define print_grid() as a function that prints each row, using a loop to print each line in the grid for the purpose of the game

def print_grid():
    for row in grid:
        print(row)

# Define mining() with parameters 'r_index, c_index'
# Assign variables to the total number of rows and columns, which is calculated using len() function
# Set the mine counter to 0

def mining(r_index, c_index):

    total_rows = len(grid)
    total_col = len(grid[r_index])
    mine = 0

# Use conditional statements to count each mine within the grid, using index coordinates
# If a mine is found in one of the block, mine count to go up in increments of 1

    if (r_index > 0 and r_index < total_rows -1) and (c_index > 0 and c_index < total_col -1):
        print(f'row = {r_index}, col  = {c_index}')
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1
    elif (r_index == 0) and (c_index > 0 and c_index < total_col -2):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
    elif (c_index == 0) and (r_index > 0 and r_index < total_rows - 1):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index -1][c_index + 1] == "#":
            mine += 1
    elif (r_index == total_rows - 1) and (c_index > 0 and c_index < total_col - 1):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
    elif (c_index == total_col - 1) and (r_index > 0 and r_index < total_rows - 1):
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
    elif (r_index > 1 and r_index < total_rows -1) and (c_index > 1 and c_index < total_col -1):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
    elif (r_index > 2 and r_index < total_rows -1) and (c_index > 1 and c_index < total_col -1):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
    elif (r_index > 3 and r_index < total_rows -2) and (c_index > 3 and c_index < total_col -2):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
    elif (r_index == 0) and (c_index == 0):
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            mine += 1
    elif (r_index == 0) and (c_index == total_col - 1):
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index + 1][c_index] == "#":
            mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            mine += 1
    elif (r_index == total_rows - 1) and (c_index == 0):
        if grid[r_index - 1][c_index] == "#":
            mine += 1
        if grid[r_index][c_index + 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            mine += 1
    elif (r_index == total_rows - 1) and (c_index == total_col - 1):
        if grid[r_index][c_index - 1] == "#":
            mine += 1
        if grid[r_index -1][c_index - 1] == "#":
            mine += 1
        if grid[r_index - 1][c_index] == "#":
            mine += 1

# Return the mine count once the checks are completed 

    return mine

#==========================================================OUTPUT=============================================================#

# Print before and after mine fields using print_grid() function

print("Before,\n=========\n")
print_grid()

# Using the enumerate() function to print out the mine count by calling mining() function
# If the squares contain '-', then print the mine count

for row_index, row in enumerate(grid):
    for col_index, col in enumerate(grid[row_index]):
        if col == '-':
            grid[row_index][col_index] = mining(row_index, col_index)
            

print("\nAfter,\n=========\n")
print_grid()

#==========================================================END OF PROGRAM======================================================#





