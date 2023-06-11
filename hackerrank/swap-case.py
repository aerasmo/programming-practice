def swap_case(s):
    swapped = ""
    for char in s:
        if char.isupper():
            swapped += char.lower()
        elif char.islower():
            swapped += char.upper()
        else:
            swapped += char

    return swapped
