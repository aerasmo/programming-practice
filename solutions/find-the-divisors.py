def divisors(integer):
    divisors = [n for n in range(2, integer // 2 + 1) if integer % n == 0]
    return divisors if divisors else "{} is prime".format(integer)