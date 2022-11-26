def correct(s):
    return s.translate(s.maketrans("501", "SOI"))