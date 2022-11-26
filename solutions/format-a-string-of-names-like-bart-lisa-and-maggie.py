def namelist(names):
    if len(names):
        names = [c.get('name') for c in names]
        retval = ', '.join(names[:-1]) + " & " + names[-1] if len(names) != 1 else names[0]
        return retval
    return ''