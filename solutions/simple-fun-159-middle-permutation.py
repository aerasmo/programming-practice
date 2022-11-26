from itertools import permutations
import math

def middle_permutation(string):
    string = sorted(string)
    if len(string) < 10:
        for i, x in enumerate(permutations(string), 1):
            if i == math.factorial(len(string)) // 2: 
                return ''.join(list(x))
    else:
        first = string[(len(string) // 2)]
        if len(string) % 2 == 0:
            first = string[(len(string) // 2)-1]
        second = ''
        if len(string) % 2 == 1: # odds
            second = string[string.index(first) - 1]

        contains = [first, second]
        rev = reversed(string)
        string = ''.join(contains) + ''.join(list(filter(lambda x: x not in contains, rev)))
        return string

# memorable this was solved during a CS DEPT session in preparation for algolympics

# For s = "abc", the result should be "bac".

# The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".