def iq_test(numbers):
    numbers = list(map(int, numbers.split(" ")))
    first_three = numbers[:3]
    evens = len([ n for n in first_three if n % 2 == 0])
    odds = len([ n for n in first_three if n % 2 == 1])

    find = 1
    if evens < odds:
        find = 0

    for i, n in enumerate(numbers, 1):
        if find == n % 2:
            return i

# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd