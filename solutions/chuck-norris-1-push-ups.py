import re

def chuck_push_ups(st): 
    if not isinstance(st, str) or not st:
        return "FAIL!!"

    max_global = 0
    n = -1

    # split 
    for word in st.split():
        # find binary per word
        b_list = re.findall(r'[10]', word)
        if b_list:
            b = ''.join(b_list)
            n = int(b, 2)
            if n > max_global:
                max_global = n

    # get the highest number he counted to    
    if n != -1:
        return max_global
    else:
        # valid string, no number
        return "CHUCK SMASH!!"


# print(chuck_push_ups('baaaasa1aa2 12201a20 1241ane212'))
# print(chuck_push_ups('1 "Chuck" 10 "Stop that!" 11 "Your vest looks stupid" 100 101 110'))
# print(chuck_push_ups('1ee1gf00t10h1011tr00'))
# print(chuck_push_ups(''))