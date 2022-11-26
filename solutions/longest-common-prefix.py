# https://leetcode.com/problems/longest-common-prefix/
from typing import List

# vertical scanning 
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix_l = []
    break_loop = False    
    i = 0
    while not break_loop:
        try:
            char = strs[0][i] 
            for s in strs:
                if s[i] != char:
                    break_loop = True
                    break
        except IndexError:
            break

        if break_loop:
            continue

        prefix_l.append(char)
        i += 1

    prefix = "".join(prefix_l)
    return prefix


strs = []

print(longestCommonPrefix(strs))