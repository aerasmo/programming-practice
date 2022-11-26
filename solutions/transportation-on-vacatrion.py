def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20
    return cost

# After a hard quarter in the office you decide to get some rest on a vacation. 
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. 
# The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or mo
# Write a code that gives out the total amount for different days(d).