def miniMaxSum(arr):
    total = sum(arr)
    maxVal = max(arr)
    minVal = min(arr)

    print(total - maxVal, total - minVal)
