def leftDiagonal(arr):
    leftSum = 0
    col = 0
    for n in range(0, len(arr)):
        leftSum += arr[n][col]
        col += 1
    return leftSum

def rightDiagonal(arr):
    rightSum = 0
    col = len(arr) - 1
    for n in range(0, len(arr)):
        rightSum += arr[n][col]
        col -= 1
    return rightSum

def diagonalDifference(arr):
    # Write your code here
    return abs(leftDiagonal(arr) - rightDiagonal(arr))