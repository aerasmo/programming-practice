import itertools
def fist_beard(arr): 
    # merged = list(itertools.chain(*arr))
    merged = list(itertools.chain.from_iterable(arr))
    return ''.join(list(map(chr, merged)))


# for really  deep list 
# import collections
# def flatten(x):
#     if isinstance(x, collections.Iterable):
#         return [a for i in x for a in flatten(i)]
#     else:
#         return [x]

# print(fist_beard([[78], [117, [110, 123], 99], [104, 117], [107, 115]]))
