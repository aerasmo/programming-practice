def duplicate(arr):
    found = set()
    for n in arr:
        if n in found:
            return n
        found.add(n)
    return -1
