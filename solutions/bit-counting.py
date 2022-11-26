def count_bits(n):
    #return "{:b}".format(n).count("1")
    return bin(n).count("1")

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case