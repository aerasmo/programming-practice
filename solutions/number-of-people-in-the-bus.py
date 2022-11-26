def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

# You are provided with a list (or array) of integer arrays (or tuples). 
# Each integer array has two items which represent number of people get into bus (The first item) 
#  and number of people get off the bus (The second item) in a bus stop.


# test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
# test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
# test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)