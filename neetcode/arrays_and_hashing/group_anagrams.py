from typing import List
import collections

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sorted_set = collections.defaultdict(list)
    for s in strs:
        sorted_set[tuple(sorted(s))].append(s)
    return sorted_set.values()

# neetcode solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
