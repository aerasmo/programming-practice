def to_alternating_case(string):
    return "".join([c.lower() if c.isupper() else c.upper() for c in string])