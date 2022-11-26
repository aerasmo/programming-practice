geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return list(filter(lambda bird: bird not in geese, birds))

# simple filter not in list problem