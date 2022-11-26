def sort_array(source_array):
    if source_array:
        odds = sorted([n for n in source_array if n % 2 == 1]) # gets odds in the array
        for n in range(len(source_array)):
            if source_array[n] % 2: # if index[n] is odd
                source_array[n] = odds.pop(odds.index(min(odds))) # min then pop

    return source_array

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]