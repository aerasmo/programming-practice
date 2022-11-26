def snail(snail_map):
    s = []
    isreversed = False
    if [] in snail_map:
        return s
    
    while snail_map:
        first = snail_map.pop(0) # first
        for n in first:
            s.append(n)

        if not snail_map: break

            
        for r in range(len(snail_map)):
            s.append(snail_map[r].pop(-1))

        last = snail_map.pop(-1)
        for n in last[::-1]:
            s.append(n)
    
        if not snail_map: break

        print(len(snail_map))
        for r in range(len(snail_map) - 1, -1, -1):
            s.append(snail_map[r].pop(0))
    return s


# def flatten(items):
#     for x in items:
#         if isinstance(x, Iterable):
#             yield from flatten(x)
#         else:
#             yield x

# array = [[1,2,3,],
#          [4,5,6,],
#          [5,8,9,]]


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]