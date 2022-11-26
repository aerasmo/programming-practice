# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        found = dict() 
        l = 0
        for r in range(len(s)):
            if s[r] not in found:
                found[s[r]] = 1
            elif found[s[r]] == 0:
                found[s[r]] += 1
            else:
                found[s[r]] += 1
                while s[l] != s[r]:
                    found[s[l]] -= 1
                    l += 1
                if s[l] == s[r]:
                    found[s[l]] -= 1
                    l += 1

            current_length = r - l + 1
            if current_length > longest_length:
                longest_length = current_length

        return longest_length