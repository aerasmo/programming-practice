def unique_in_order(iterable):
    if not iterable: return []
    prev = iterable[0]
    n = [prev]
    for letter in iterable:
        if letter != prev:
            n.append(letter)
            prev = letter
    return n