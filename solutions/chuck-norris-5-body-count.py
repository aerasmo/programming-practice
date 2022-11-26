import re
def body_count(code):
    exp = r'([A-Z]\d){5}\.-[A-Z]%\d\.\d\d\.'
    return bool(re.search(exp, code))


# clever solution ---

# pattern = re.compile('A8A8A8A8A8.-A%8.88.'.replace('A', '[A-Z]').replace('8', '[0-9]').replace('.', r'\.'))
# def body_count(code):
#     return bool(pattern.search(code))

# ---

# print(body_count('A6C2E5Z9A4.-F%8.08..'))
# print(body_count('B2L4D0A8C6.-T%8.90'))
# print(body_count(' 76     B2L4D0A8C6.-T%8.90.       lkd'))
# print(body_count('b4A1D1I8B4.-E%8.76.'))
# print(body_count( 'X3B7V2H7N5.-S%5.65B.aY-J'))