def migratoryBirds(arr):
    birds = {}
    for bird in arr: 
        if bird not in birds:
            birds[bird] = 1
        else:
            birds[bird] += 1

    maxCount = max(list(birds.values()))
    birdslist = sorted(birds)

    for bird in birdslist:
        if birds[bird] == maxCount:
            return bird