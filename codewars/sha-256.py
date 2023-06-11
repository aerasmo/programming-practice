import hashlib
str = input()

result = hashlib.sha256(str.encode())

print(f'the hexadecimal equivalent of {result} sha256 is : ', result.hexdigest())


