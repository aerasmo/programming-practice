def high_and_low(numbers):
    numbers = list(map(int, numbers.split(" ")))
    return " ".join([str(max(numbers)), str(min(numbers))])