def tower_builder(n_floors):
    blocks = ['*' * ((2 * n) - 1) for n in range(1, n_floors + 1)]
    return [block.center(len(blocks[-1])) for block in blocks]

#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
def tower_builder(n_floors):
    max_width = n_floors * 2 - 1
    tower = []
    for i in range(n_floors): 
        tower.append(f"{'*' * (i * 2 + 1)}".center(max_width))
    return tower