import string
def printer_error(s):
    a_to_m = string.ascii_lowercase[:13]
    errors = 0
    for n in s:
        if n not in a_to_m:
            errors += 1
    return "{}/{}".format(errors, len(s))


# n characters onwards are considered error


# s="aaabbbbhaijjjm"
# error_printer(s) => "0/14"


# s="aaaxbbbbyyhwawiwjjjwwm"
# error_printer(s) => "8/22"