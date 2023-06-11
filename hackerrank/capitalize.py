def solve(s):
    newStr = []
    for word in s.split(" "):
        try: 
            if word[0].isalpha():
                word = word.capitalize()
        except IndexError:
            pass
            # word is ''
        finally:
            newStr.append(word)
    
    newStr = " ".join(newStr)
    return newStr 