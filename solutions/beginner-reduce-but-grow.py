import functools

def grow(arr):
    return functools.reduce(lambda output, x: output * x, arr)

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24