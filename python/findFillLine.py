# You are given a matrix of integer 'field' of size 'n * m' representing a game field, 
# and also a matrix of integers 'figure' of size '3 * 3' representing a figure.
# Both matrices contain only 0s and 1s, where 1 means the cell is occupied, and 0 means the cell is free.

# You choose a position at the top of the game field where you put the figure and then drop it down.
# The figure falls down until it either reaches the ground (bottom of the field) or lands on an occupied cell,
# which blocks it from falling further. \
# After the figure has stopped falling, some of the rows in the field may become fully occupied.

# Your task is to find the dropping position such that at least one full row is formed.
# As a dropping position you should consider the column index of the cell in game field which matches the top left corner of the figure '3 * 3' matrix.
# If there are multiple dropping positions satisfying the condition, feel free to return any of them.
# If there are no such dropping positions, return -1

# Constraints:
# 4 <= field.length <= 100
# 3 <= field[i].length <= 100
# 0 <= field[i][j] <= 1
# figure.length = 3
# figure[i].length = 3
# 0 <= figure[i][j] <= 1

# NOTE: When falling, the 3x3 matrix of the figure must be entirely inside the game field.

# Example 1:
# Input: 
#   field: [[0,0,0],
#           [0,0,0],
#           [0,0,0],
#           [1,0,0],
#           [1,1,0]]
#   figure: [[0,0,1],
#            [0,1,1],
#            [0,0,1]]
# Output: 0

# Example 2:
# Input: 
#   field: [[0,0,0,0,0],
#           [0,0,0,0,0],
#           [0,0,0,0,0],
#           [1,1,0,1,0],
#           [1,0,1,0,1]]
#   figure: [[1,1,1],
#            [1,0,1],
#            [1,0,1]]
# Output: 2

# Example 3:
# Input:
#   field: [[0,0,0,0,0],
#           [0,0,0,0,0],
#           [0,0,0,0,0],
#           [0,0,0,1,0],
#           [0,1,1,1,1],
#           [1,1,0,1,1]]
#   figure: [[1,0,0],
#            [1,0,0],
#            [1,0,0]]
# Output: 0

# Example 4:
# Input:
#   field: [[0,0,0,0,0,0],
#           [0,0,0,0,0,0],
#           [0,0,0,0,0,0],
#           [1,1,1,0,1,0],
#           [1,1,1,1,0,1],
#           [1,1,0,1,0,0],
#           [1,1,1,1,0,1],
#           [1,0,1,1,0,0]]
#   figure: [[1,1,1],
#            [1,0,1],
#            [1,0,1]]
# Output: 3

# Example 5:
# Input: 
#   field: [[0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0],
#           [0,0,0,1,1,1,1]]
#   figure: [[1,1,1],
#            [0,1,0],
#            [0,1,0]]
# Output: -1

# Example 6:
# Input: 
#   field: [[0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0],
#           [0,0,1,1,1,1,1,0,0,0],
#           [1,1,1,0,1,0,1,0,0,0],
#           [1,1,1,1,1,1,1,0,0,0]]
#   figure: [[0,0,0],
#            [1,0,0],
#            [1,1,1]]
# Output: 7

# Example 7:
# Input:
#   field: [[0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [1,1,1,0,1,0,0,1],
#           [1,1,1,0,1,1,1,1]]
#   figure: [[0,0,0],
#            [1,1,0],
#            [1,1,0]]
# Output: -1

# Example 8:
# Input:     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 
#   field: [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#           [0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0],
#           [1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1]]
#   figure: [[1,1,1],
#            [0,1,1],
#            [1,1,0]]
# Output: -1

#checks for collisions
def collision(field, figure, row, col):
    if row+3 > len(field): return True #hit bottom
    for i, r in enumerate(figure):
        for j, c in enumerate(r):
            if c + field[row+i][col+j] == 2: return True
    return False

#returns max row index
def drop(field, figure, col):
    row = 0
    while not collision(field, figure, row, col):
        row += 1
    return row-1

#checks if figure placement forms a line
def line(field, figure, col, row):
    #add figure to temp array
    temp_field = [r[:] for r in field]

    for r in range(3):
        for c in range(3):
            if figure[r][c] == 1:
                temp_field[row+r][col+c] = 1
    
    #check if temp array has a line
    field_width = len(field[0])
    for r in range(3):
        if sum(temp_field[row+r]) == field_width: return True

    return False

def findFillLine(field, figure):
    #edges
    if len(field) < 3: return -1
    if len(field) == 3: return 0

    #column positions
    for col in range(len(field[0])-2):
        row = drop(field, figure, col)
        if line(field, figure, col, row): return col
    return -1

tests = [
    {
        "field": [[0,0,0],[0,0,0],[0,0,0],[1,0,0],[1,1,0]],
        "figure": [[0,0,1],[0,1,1],[0,0,1]],
        "output": 0
    }, {
        "field": [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,0],[1,0,1,0,1]],
        "figure": [[1,1,1],[1,0,1],[1,0,1]],
        "output": 2
    }, {
        "field": [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,1],[1,1,0,1,1]],
        "figure": [[1,0,0],[1,0,0],[1,0,0]],
        "output": 0
    }, {
        "field": [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,0,1,0],[1,1,1,1,0,1],[1,1,0,1,0,0],[1,1,1,1,0,1],[1,0,1,1,0,0]],
        "figure": [[1,1,1],[1,0,1],[1,0,1]],
        "output": 3
    }, {
        "field": [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,1,1,1]],
        "figure": [[1,1,1],[0,1,0],[0,1,0]],
        "output": -1
    }, {
        "field": [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[1,1,1,0,1,0,1,0,0,0],[1,1,1,1,1,1,1,0,0,0]],
        "figure": [[0,0,0],[1,0,0],[1,1,1]],
        "output": 7
    }, {
        "field": [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,0,1,0,0,1],[1,1,1,0,1,1,1,1]],
        "figure": [[0,0,0],[1,1,0],[1,1,0]],
        "output": -1
    }, {
        "field": [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0],[1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1]],
        "figure": [[1,1,1],[0,1,1],[1,1,0]],
        "output": -1
    }
]

test = 0
if test > 0:
    print(f"{test}:", findFillLine(tests[test-1]["field"],tests[test-1]["figure"]), "|", tests[test-1]["output"])
else: 
    for i, t in enumerate(tests):
        print(f"{i+1}:", findFillLine(tests[i]["field"],tests[i]["figure"]), "|", tests[i]["output"])