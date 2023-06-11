def print_rangoli(size):
    import string
    chars = string.ascii_lowercase[:n][::-1]

    strlist = []
    row_str = []
    w = len(chars) * 2 - 1
    w = w * 2 - 1

    for i in range(len(chars)):
        c = '-'.join( strlist + [chars[i]] + strlist[::-1] )
        row_str.append(c.center(w , '-'))
        strlist.append(chars[i])

    row_str = row_str + row_str[-2::-1]
    [print(row) for row in row_str]