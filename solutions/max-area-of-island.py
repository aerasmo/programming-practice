grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    max_area = 0
    print(rows, cols)
    def dfs(i, j):
        if (i < 0 or i >= rows) or \
            (j < 0 or j >= cols):
            return 0
        if grid[i][j] == 0:
            return 0
        print("{} is an island ".format((i, j)))
        # change to zero instead so it will not be used in future dfs
        grid[i][j] = 0
        return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

    for i in range(rows):
        for j in range(cols):
            current = dfs(i, j)
            if current > max_area:
                max_area = current
    return max_area
print(max_area_of_island(grid))

