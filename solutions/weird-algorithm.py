
l = []
def weird(n):
    l.append(str(n))
    if n == 1:
        return " ".join(l)
    elif n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
    return weird(n)

if __name__ == '__main__':
    n = int(input())
    print(weird(n))

    