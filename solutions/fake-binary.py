def fake_bin(arr):
    return ''.join(['0' if int(x) < 5 else '1' for x in arr ])