def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3