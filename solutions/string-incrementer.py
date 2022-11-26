def increment_string(string):
    digits = []
    if all([not char.isdigit() for char in string]): digits = 0
    else:
        for char in string[::-1]:
            if char.isdigit():
                digits.append(char)
            else:
                break
        digits = digits[::-1]
    if digits:
        digitstr = ''.join(digits) 
        string = string.replace(''.join(digitstr), '')     
        if '0' in digits:
            chars = []
            for i in digits:
                if i != '0':
                    first = i
                    break
                else:
                    chars.append('0')
            if all([i == '0' for i in digits]): 
                string += ''.join(chars)[:-1]
                digits = 0 
            else:
                string += ''.join(chars)
                digits = int(''.join(digits).replace(' ', ''))   
        else:
            digits = int(''.join(digits))
    if len(str(digits + 1)) > len(str(digits)) and '0' in string:
        string = string[:-1]
        
    string += str(digits + 1)     
    return string

# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100