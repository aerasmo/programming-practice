def wave(people):
    i = 0
    wave = []
    while i < len(people):
        if people[i] == " ":
            i += 1
        else:
            wave.append(people[:i] + people[i].upper() + people[i+1:]) 
            i += 1
    return wave