# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

# case where input columns are randomized but we know the columns

# no of students
n = int(input())
Grade = namedtuple("Grades", input().split())

total = 0
average = 0 
for i in range(n):
    # unpack list
    grade = Grade(*input().split())
    # print(grade)
    total += int(grade.MARKS)

average = round(total / n, 2)
print(average)

