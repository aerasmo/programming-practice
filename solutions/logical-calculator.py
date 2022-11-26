import operator
from functools import reduce

OPS = {
    "AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor
}

def logical_calc(array, op):
    return reduce(OPS[op], array)

# booleans = [True, True, False], operator = "AND"
# True AND True -> True
# True AND False -> False
# return False

# booleans = [True, True, False], operator = "OR"
# True OR True -> True
# True OR False -> True
# return True

# booleans = [True, True, False], operator = "XOR"
# True XOR True -> False
# False XOR False -> False
# return False