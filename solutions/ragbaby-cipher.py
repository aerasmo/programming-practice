def keyed_caesar(key: str) -> str:
    from string import ascii_lowercase
    if len(key) != len(set(key)): 
        # reduce multiple chars to single char
        keys = []
        for c in key:
            if c not in keys:
                keys.append(c)
        key = "".join(keys)

    key = key + "".join([x for x in ascii_lowercase if x not in key])
    return key

def encode(text: str, key: str, mul=1) -> str:    
    assert mul in (1, -1), "invalid argument" # mul = 1 for shift right / encode ;  -1 for shift left / decode 
    
    key = keyed_caesar(key)
    res = []
    to_upper = False
    n = 1 # shift setter

    for c in text:
        if c.isupper(): # remember that this is an upper
            c = c.lower()
            to_upper = True

        # --- 
        if c in key:
            idx = key.index(c)
            shift = idx + (mul * n)
            if shift >= len(key) or shift < 0: # if shift overflows left or right index
                enc_c = key[(shift % len(key))]
            else:
                enc_c = key[shift]
            
            if to_upper: # if char is originally upper
                enc_c = enc_c.upper()
                to_upper = False
            n += 1

        else: # whitespace etc. 
            enc_c = c
            n = 1 # reset shift 

        res.append(enc_c)
    return "".join(res)

def decode(text:str , key: str) -> str:
    return encode(text, key, -1)

    

print(encode("cipher","cipher"))
print(encode("cipher","cccciiiiippphheeeeerrrrr"))
print(encode("This is an example.","cipher"))
print(decode("ihrbfj","cipher"))
print(decode("Urew.uRew.urEw.ureW...","cipher"))
print(decode("This is an example.", "secretkey"))
print(encode(decode("This is an example.", "secretkey"), "secretkey"))
print(encode("ZpOg,VHRtyrB XQHy eMLN  nM  kV EURlMC aS dyUS pRIXQXzdQDexqbUFbAjzkKmpJmsh,p Mbc  G yvVMl yYsvOErBTdM. gJrUnUgwKDcBnFaXHl  ENarZpT. hXU,qRFyNJuSMQHknjWrFGdJYfomHhhJQBGWDLVPUv ", "irejry"))



def encode2(text, key):
    key = keyed_caesar(key)
    res = []
    to_upper = False
    n = 1 # shift setter

    for c in text:
        if c.isupper(): # remember that this is an upper
            c = c.lower()
            to_upper = True

        # --- 
        if c in key:
            idx = key.index(c)
            shift = idx + n
            if shift >= len(key): # if shift overflows positively
                enc_c = key[shift % len(key)]
            else:
                enc_c = key[shift]
            
            if to_upper: # if char is originally upper
                enc_c = enc_c.upper()
                to_upper = False
            n += 1

        else: # whitespace etc. 
            enc_c = c
            n = 1 # reset shift 
        res.append(enc_c)

    return "".join(res)

def decode2(text, key):
    key = keyed_caesar(key)
    res = []
    to_upper = False
    n = 1 # shift setter

    for c in text:
        if c.isupper(): # remember that this is an upper
            c = c.lower()
            to_upper = True

        # --- 
        if c in key: # if character in keys
            idx = key.index(c)
            shift = idx - n
            if shift < 0: # if shift overflows negatively
                enc_c = key[-(abs(shift) % len(key))] # negative indexing
            else:
                enc_c = key[shift]

            if to_upper: # if char is originally upper
                enc_c = enc_c.upper()
                to_upper = False
            n += 1

        else: # whitespace etc. 
            enc_c = c
            n = 1 # reset shift 

        res.append(enc_c)

    return "".join(res)
