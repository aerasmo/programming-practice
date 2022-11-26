def array_diff(a, b):
    return [x for x in a if x not in b]

# array_diff([1,2],[1]) == [2]
# array_diff([1,2,2,2,3],[2]) == [1,3]

# TODO: implement symmetric difference python