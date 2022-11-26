from collections import Counter 

# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
'''
Task

 is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
'''

# SOLUTION 
# X number of shoes
x = int(input())

# list of number of shoe sizes available
counter = Counter(map(int, input().split(" ")))

# n number of customers
n = int(input())

# compute how much money Raghu earned
total = 0
for _ in range(n):
    size, price = (map(int, input().split(" ")))
    if counter[size] > 0:
        total += price
        counter[size] -= 1
    # else:
        # print(f"size {size} not available")
    # print(counter[size])    

print(total)
