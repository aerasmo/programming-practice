import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    l = 0
    for x in range(n):
        print(x)
        for y in range(x+1, n):
            if x == y:
                continue
            s = ar[x] + ar[y]
            if s % k == 0:
                l += 1
    return l
    # e % k == 0
       # l += 1
if __name__ == '__main__':
    ar = [1, 3, 2, 6, 1, 2]
    k = 3
    n = len(ar)
    print(divisibleSumPairs(n, k, ar))