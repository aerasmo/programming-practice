def isPalindrome(x):
    s = str(x)
    l = len(s) // 2

    if len(s) % 2 == 0:
        return s[0: l] == s[l:len(s)][::-1]
    else:
        return s[0: l + 1] == s[l:len(s)][::-1]

def intPalindrome(x):
    if (x < 0 or # -num
        x % 10 == 0 and x != 0 ): # 200 # should be 020
        return False

    reversed_ = 0
    while x > reversed_:
        reversed_ = reversed_ * 10 + x % 10
        x //= 10
    
    return x == reversed_ or x == reversed_ // 10





s = int(input())
print(intPalindrome(s))