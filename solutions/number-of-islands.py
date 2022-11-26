grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def nums_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(i, j):
        if i < 0 or i >= rows or\
            j < 0 or j >= cols:
            return 0
        if grid[i][j] != "1":
            return 0
        # -- means grid[i][j] == "1" --
        grid[i][j] = "#"
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        return 1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += dfs(i, j)
    return count


print(nums_islands(grid))
print(nums_islands(grid2))

# visiting solution
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid: return 0
    r, c = len(grid), len(grid[0])
    visited = [[False for _ in range(c)] for _ in range(r)]

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count