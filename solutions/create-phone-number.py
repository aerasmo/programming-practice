def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number2(n):
    n = list(map(str, n))
    return "({}) {}-{}".format( "".join(n[:3]), "".join(n[3:6]), "".join(n[6:10]))

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890