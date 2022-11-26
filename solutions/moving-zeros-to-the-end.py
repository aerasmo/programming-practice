def move_zeros(array):
    new_arr = []
    zero_count = 0
    for item in array:
        if item == 0 and (type(item) == int or type(item) == float):
            zero_count += 1
            continue
        else:
            new_arr.append(item)
    return new_arr + [0] * zero_count

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]