import re
def to_camel_case(text):
    words = re.split('[_-]', text)
    return "".join([words[0]] + [w.title() for w in words[1:]])
