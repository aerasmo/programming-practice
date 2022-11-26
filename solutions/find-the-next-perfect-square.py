import math
def find_next_square(squared):
    root = math.sqrt(squared) + 1
    return root ** 2 if root % 1 == 0 else -1

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect square