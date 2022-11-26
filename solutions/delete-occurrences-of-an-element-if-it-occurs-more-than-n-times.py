def delete_nth(order,max_e):
    num_count = {num: 0 for num in order}
    reorderd = []
    for num in order:
        if num_count[num] == max_e: 
            continue
        num_count[num] += 1
        reorderd.append(num) 
    return reorderd        