def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)