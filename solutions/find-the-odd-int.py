def get_odd_int(seq):
    for n in set(seq):
        if seq.count(n) % 2 == 1:
            return n