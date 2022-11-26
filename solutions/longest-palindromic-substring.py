def longestPalindrome(s):
    def palindrome(l, r):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    max_global = ''
    for i in range(len(s)):
        word1 = palindrome(i, i)
        word2 = palindrome(i, i+1)

        if len(word1) > len(word2):
            max_current= word1 
        else:
            max_current = word2
        
        max_current = word1 if len(word1) > len(word2) else word2
        if len(max_current) > len(max_global):
            max_global = max_current

    return max_global

s = input()
print(longestPalindrome(s))