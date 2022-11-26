# https://leetcode.com/problems/first-bad-version/
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API

def isBadVersion(x):
    return True if x > 25  else False

def firstBadVersion(self, n: int) -> int:
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low