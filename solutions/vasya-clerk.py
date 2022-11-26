def tickets(people):
    money = {'a': 0, 'b': 0, 'c': 0}
    translate = {25: 'a', 50: 'b', 100: 'c'}
    for bill in people:
        key = translate[bill]
        if key == 'a':
            money[key] += 1
        elif key =='b':
            if money['a'] == 0:
                return "NO"
            money['a'] -= 1
            money['b'] += 1
        elif key == 'c':
            if money['a'] >= 1 and money['b'] >= 1:
                money['a'] -= 1
                money['b'] -= 1
                money['c'] += 1
            elif money['a'] >= 3:
                money['a'] -= 3
                money['c'] += 1
            else:
                return "NO"
    return "YES"