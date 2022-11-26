def number(lines):
    numbered_lines = []
    for i, c in enumerate(lines, 1):
        numbered_lines.append("{}: {}".format(i, c))
    return numbered_lines