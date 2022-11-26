matrix = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
]
matrix2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
matrix3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
sr = 0
sc = 0
new_color = 2

# all pixels connected with a path starting with same color will be colored as new color
global visited

def flood_fill(image, sr, sc, new_color):
    # get adjacent
    edges = []
    if sr > 0:
        edges.append((sr-1, sc))
    if sc > 0:
        edges.append((sr, sc-1))
    if sr < (len(image) - 1):
        edges.append((sr+1, sc))
    if sc < (len(image[0]) - 1):
        edges.append((sr, sc+1))

    # flood fill on new images
    col = image[sr][sc]
    for edge in edges:
        if image[edge[0]][edge[1]] == col and image[edge[0]][edge[1]] != new_color:
            image[sr][sc] = new_color
            image = flood_fill(image, edge[0], edge[1], new_color)

    image[sr][sc] = new_color
    return image
print(flood_fill(matrix, 1, 1, new_color))
print(flood_fill(matrix2, 1, 1, new_color))
print(flood_fill(matrix3, 0, 0, 2))

""" best sol
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    r, c = len(image), len(image[0])
    color = image[sr][sc]
    def dfs(i, j):
        if i < 0 or i>=r or j < 0 or j >= c:
            return
        if image[i][j] == newColor or image[i][j] != color:
            return
        image[i][j] = newColor
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i,j+1)
        dfs(i, j-1)
    dfs(sr, sc)
    return image 
"""