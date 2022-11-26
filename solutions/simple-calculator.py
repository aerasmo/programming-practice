def calculator(x, y, op):
    if str(op) not in '+-*/' \
        or not str(x).isnumeric() \
        or not str(y).isnumeric(): 
        return "unknown value"
    
    return eval("{} {} {}".format(x, op, y))