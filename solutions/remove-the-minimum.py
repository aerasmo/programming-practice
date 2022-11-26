def remove_smallest(numbers):
    copy = numbers[:]
    if copy:
        copy.remove(min(copy))
    return copy

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
#  If there are multiple elements with the same value, remove the one with a lower index.
#  If you get an empty array/list, return an empty array/list.