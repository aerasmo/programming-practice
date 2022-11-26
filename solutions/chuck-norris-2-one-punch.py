import re

def one_punch(item):    
    return re.sub(r'[AaeE]', '', ' '.join(sorted([e for e in item.split()]))) if isinstance(item, str) and len(item) > 0 else "Broken!"

# Chuck expects his list of favourite items to be split, sorted, joined 
# AND have any occurrences of the letters 'e' and 'a' removed - why, you ask? 
# Well Nunchuks hasn't got the letters 'a' or 'e' in it has it?? 
# Chuck says shut your mouth... and don't forget the capitals.

# print(one_punch('Beard Knife Grenade Motorbike Hat'))
# print(one_punch('Horse Rope Cups Car Beard'))
# print(one_punch('Friend Beer Beard Monkey Laptop'))