def count_by(x, n):
    return [n for n in range(x, n*x+1, x)]

# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]