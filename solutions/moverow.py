def moverow(arr, index_, dir_, step=1):
        arr = arr[index_]
        row = [None for n in arr]
        print('initial row', arr)   
        for n in range(len(arr)):
            if dir_ == 'left':
                row[n - step] = arr[n]
            elif dir_ == 'right':
                row[-len(arr) + step + n] = arr[n]
        return row

print('moved left 2', moverow([[1,2,3,4], [1, 4, 2, 3], [3, 3, 2, 1]], 2, 'left', 2))
print('moved right 3', moverow([[1,2,3,4], [1, 4, 2, 3], [3, 3, 2, 1]], 2, 'right', 3))
        
            
