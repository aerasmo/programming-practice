def task(weekday,n,cost):
    names = {'Monday': 'James',  'Tuesday': 'John', 'Wednesday': 'Robert', 'Thursday': 'Michael', 'Friday': 'William',}
    return f'It is {weekday} today, {names[weekday]}, you have to work, you must spray {n} trees and you need {n * cost} dollars to buy liquid'