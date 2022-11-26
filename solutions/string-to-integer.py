def myAtoi(s: str) -> int:
    if not s:
        return 0
    n = []
    limit = (2**31) - 1
    neg_limit = -(limit + 1)
    for i in range(len(s)):
        if not n:
            if (s[i] == "-" or s[i] == "+" ) and ((i + 1) != len(s)):
                if s[i+1].isdigit():
                    n.append(s[i])
                else:
                    return 0
            elif s[i].isdigit():
                n.append(s[i])
            elif s[i] == " ":
                pass
            else:
                return 0
        else:
            if s[i].isdigit():
                n.append(s[i])
            else:
                break
    try:
        ans = int("".join(n))   
    except ValueError:
        return 0
    else:
        if ans > limit:
            ans = limit
        elif ans < neg_limit:
            ans = neg_limit
        return ans



s = input()
print(myAtoi(s))


def myAtoi(s: str) -> int:
    if not s:
        return 0
    n = 0
    sign = ""
    limit = (2**31) - 1
    neg_limit = -(limit + 1)
    for i in range(len(s)):
        if not n:
            if (s[i] == "-" or s[i] == "+" ) and ((i + 1) != len(s)):
                if s[i+1].isdigit():
                    sign = s[i]
                else:
                    return 0
            elif s[i].isdigit():
                n = int(s[i])
            elif s[i] == " ":
                pass
            else:
                return 0
        else:
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            else:
                break
    if sign == "-":
        n *= -1
    
    if n > limit:
        n = limit
    elif n < neg_limit:
        n = neg_limit
    return n