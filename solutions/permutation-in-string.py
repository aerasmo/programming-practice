# https://leetcode.com/problems/permutation-in-string/submissions/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        characters = dict()
        for char in s1:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
        l = 0
        found = dict()
        for r in range(0, len(s2)):
            if s2[r] not in found:
                found[s2[r]] = 1
            else:
                found[s2[r]] += 1

            if r >= len(s1):
                found[s2[l]] -= 1
                l+=1

            for char in characters:
                if char not in found:
                    break
                elif characters[char] != found[char]:
                    break
            else:
                return True
        return False