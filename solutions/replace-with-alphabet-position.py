import string
def alphabet_position(text):
    lowers = string.ascii_lowercase
    return " ".join(map(str, [lowers.index(c) + 1 for c in text.lower() if c in lowers]))

# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)