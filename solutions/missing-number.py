def findMissing(n, nums):
    total = n * ((1 + n) / 2)
    sums = sum(nums)
    missing = int(total - sums)
    return missing
        
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))
    print(findMissing(n, nums))