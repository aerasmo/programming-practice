

from re import L


def determinant(mat):
    size = len(mat)
    if size == 1:
        return mat[0][0]
    if size == 2:
        return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

    # n = 1
    total = 0
    for i in range(size):
        n = 1 if i % 2 == 0 else -1
        for j in range(size):
            # print(n, end=" ")
            submat = []
            for k in range(size):
                row = []
                for l in range(size):
                    if (k == i) or (l == j):
                        continue
                    row.append(mat[k][l])
                if row == []:
                    continue
                submat.append(row)
            # print(submat)
            
            s = n * mat[i][j] * determinant(submat) 
            print(n, mat[i][j], determinant(submat))
            print(submat, s, n)
            total += s
            n *= -1

        
    return total



size = int(input())
mat = []
for _ in range(size):
    mat.append(list(map(int, input().split())))

# print(mat)
print(determinant(mat))
