def to_jaden_case(string):
    return " ".join([w.capitalize() for w in string.split(" ")])

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"