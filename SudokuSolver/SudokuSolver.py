import numpy as np
# import time

# # Sudoku Test Problem
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]


def is_possible(y, x, n):
    # # Check if the input number can be inserted in the specified position

    # # Check if number is repeated in x-axis
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # # Check if number is repeated in y-axis
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # # Check if number is repeated in its square
    # # x0 and y0 are the top left indices for each square
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):   # x-axis
        for j in range(0, 3):   # y-axis
            if grid[y0 + j][x0 + i] == n:
                return False

    return True


def solve():
    # # Going through the entire grid
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    print(np.matrix(grid))
    input('More solutions?')


if __name__ == "__main__":
    solve()

