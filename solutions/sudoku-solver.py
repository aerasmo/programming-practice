def sudoku_solver(puzzle):
    return solve(puzzle)

def valid(puzzle, x, y, n):
    for i in range(0, 9):
        if puzzle[y][i] == n :
            return False
    for i in range(0, 9):
        if puzzle[i][x] == n:
            return False 
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y1 + i][x1 + j] == n:
                return False
    return True

def issolved(puzzle):
    solved = True
    for i in range(9):
        if 0 in puzzle[i]:
            solved = False
    return solved

def solve(puzzle):
    for y in range(0, 9):
        for x in range(0, 9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if valid(puzzle, x, y, n):
                        puzzle[y][x] = n
                        solve(puzzle)
                        if issolved(puzzle):
                            return puzzle
                        puzzle[y][x] = 0
                return

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


print(sudoku_solver(puzzle))