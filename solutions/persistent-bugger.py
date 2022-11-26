from operator import mul
from functools import reduce 


def persistence(n):
    return 0 if n < 10 else persistence(reduce(mul, map(int, str(n))))+1

#recursion

#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit
                  
#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
#                   # 1*2*6=12, and finally 1*2=2

#  persistence(4) # returns 0, because 4 is already a one-digit number