def index(array, n):
    if n >= len(array): 
        return - 1
    return array[n] ** n

# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.