


    # return len(string) == len(set(string))

def last_survivors(string):
# \b([a-z])\1+\b
    # regex = r'[a-z]{2}'
    while True:
        prev = ''
        has_duplicate = False
        # get the string with dups then convert
        for i, s in enumerate(string):
            ss = string[i+1:]
            sss = ''
            if s in ss:
                j = ss.index(s)
                has_duplicate = True
                n = ord(s) 
                converted = chr(n + 1)
                if s == 'z':
                    converted = 'a'
                sss = ss[:j] + ss[j+1:]
                string = ss[:i] + converted + sss
                print(j, string)
            prev = s
        if not has_duplicate:
            break
    return string

    
s = input()
print(last_survivors(s))
