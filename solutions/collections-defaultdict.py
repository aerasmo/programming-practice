# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict 

# length of a and b ( n , m )
n, m = map(int, input().split())

indices = defaultdict(list)

# record all elements in n
for i in range(1, n+1):
    word = input()
    indices[word].append(str(i))

# print(indices)
# for each element in m check the indices of this on a
for _ in range(m):
    word = input()
    word_index = indices[word]
    res = " ".join(word_index) if word_index else -1
    print(res)


