from collections import OrderedDict

# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

n = int(input())

items = OrderedDict()

for _ in range(n):
    # unpacking spaced items like BANANA FRIES 12
    *item, price = tuple(input().split())
    item = " ".join(item)
    if item not in items:
        items[item] = int(price)
    else:
        items[item] += int(price)

# printing 
for item in items:
    print(f"{item} {items[item]}")