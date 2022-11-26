def findDifferentBinaryString(nums) -> str:
    import itertools
    
    l = len(nums)
    for comb in itertools.product([1, 0], repeat=l):
        s = "".join(map(lambda x: str(x), comb))
        if s not in nums:
            return s