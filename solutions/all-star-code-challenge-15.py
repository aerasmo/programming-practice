def rotate(str_):
    res = []
    for _ in range(len(str_)):
        str_ = str_[1:] + str_[0]
        res.append(str_) 
    return res

# rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
# test.assert_equals(rotate("123"), ["231", "312", "123"])