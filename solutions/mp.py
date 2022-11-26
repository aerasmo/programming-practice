from itertools import permutations
import math

def middle_permutation(string):
    string = sorted(string)
    if len(string) < 10:
        for i, x in enumerate(permutations(string), 1):
            if i == math.factorial(len(string)) // 2: 
                return ''.join(list(x))
    else:
        if len(string) % 2 == 1:
            first = string[(len(string) // 2) + 1]
        elif len(string) % 2 == 0:
            first = string[(len(string) // 2)]
        second = ''
        if len(string) % 2 == 1: # odds
            second = string[string.index(first) - 1]

        contains = [first, second]
        rev = reversed(string)
        string = ''.join(contains) + ''.join(list(filter(lambda x: x not in contains, rev)))
        return string


        
        
    #your code here

print('', middle_permutation("acwjiftedsvbkrpynuq"))
print('', middle_permutation('lvirodekbqmnshxtfwapj'))
print('', middle_permutation("xazgtkvcfpysebmdnhqo"))
print('', middle_permutation("qrstub"))
# print('', middle_permutation("abcde"))
# print('', middle_permutation("abcdef"))
# print('', middle_permutation("abcdefg"))
# print('', middle_permutation("abcdefgh"))
# print('', middle_permutation("abcdefghi"))
# print('', middle_permutation("abcdefghij"))
# print('', middle_permutation("abcdefghijk"))
# print('', middle_permutation("abcdefghijkl"))
# print('', middle_permutation("abcdefghijklm"))
# print('', middle_permutation("abcndefghijklm"))
# print('', middle_permutation("abcdefghijklmnopqrstuvwxzy"))

