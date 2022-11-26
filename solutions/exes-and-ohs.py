def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true