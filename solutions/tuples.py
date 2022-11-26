def hashTuple(t):
    return hash(t)


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    hash = hashTuple(tuple(integer_list))
    print(hash)