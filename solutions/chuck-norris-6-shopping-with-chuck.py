def price(start, soil, age): 
    # valid arguments check
    if not( isinstance(start, (float, int))
        and isinstance(soil, str)
        and isinstance(age, (float, int))):
        # "if not number, if str, if not number"
        return 'Chuck is bottomless!'

    soil_value = {
        'Barely used': 10,
        'Seen a few high kicks': 25,
        'Blood stained': 30,
        'Heavily soiled': 50,
    }
    try: 
        r = soil_value[soil]
    except KeyError:
        return 'Chuck is bottomless!'

    compound_interest = start * (1 + r/100) ** age
    return f'${compound_interest:.2f}'

# compound interest problem

# print(price(19.95, 'Barely used', 3))
# print(price(27.76, 'Seen a few high kicks', 15))
# print(price(13.26, 'Blood stained', 25))
