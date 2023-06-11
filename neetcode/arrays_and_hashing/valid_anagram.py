def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countS[t[i]] = 1 + countS.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

    # Counter trick 
    Counter(s) == Counter(t)

    # O(nlogn) O(1)
    sorted(s) == sorted(t)

    
