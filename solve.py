import numpy as np

SIZE = 9

def create_puzzle(puzzle_string="000000000000000000000000000000000000000000000000000000000000000000000000000000000"):
    """Creates the puzzle with a string as an input (defaults to blank matrix). String must be 81 digits long"""
    puzzle = []
    for i in range(0, SIZE**2, SIZE):
        temp = []
        row = puzzle_string[i:i+SIZE]
        for num in row:
            temp.append(int(num))
        puzzle.append(temp)
    print(np.matrix(puzzle))
    return puzzle


def possible(puzzle, row, column, digit):
    """Returns true if the location is valid. Valid if digit does not appear in row, column, or square"""
    
    # make sure digit does not appear in row or column
    for i in range(SIZE):
        if puzzle[i][column] == digit:
            return False
        if puzzle[row][i] == digit:
            return False
    
    # make sure digit does not appear in square
    rowsq = row // 3
    colsq = column // 3
    for i in range(3):
        for j in range(3):
            if puzzle[rowsq*3 + i][colsq*3 + j] == digit:
                return False

    return True

def solve(puzzle):
    """Input puzzle as 2D array and yield a stream of the solutions"""

    for row in range(SIZE):
        for col in range(SIZE):
            if puzzle[row][col] == 0:
                for digit in range(1, 10):
                    if possible(puzzle, row, col, digit):
                        puzzle[row][col] = digit
                        yield from solve(puzzle)
                        puzzle[row][col] = 0
                return
    yield puzzle


