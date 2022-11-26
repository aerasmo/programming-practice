def formatOct(string, w):
    return string.replace('0o', '').rjust(w)

def formatHex(i, w):
    return "0x{:X}".format(i).replace('0x', '').rjust(w)

def formatBin(string, w):
    return stripBin(string).rjust(w)

def stripBin(string):
    return string.replace('0b', '')

def print_formatted(number):
    width = len(stripBin(bin(number)))
    for i in range(1, number + 1):
        print(f'{str(i).rjust(width)} {formatOct(oct(i), width)} {formatHex(i, width)} {formatBin(bin(i), width)} ')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)