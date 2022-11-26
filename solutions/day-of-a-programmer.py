def dayOfProgrammer(year):
    programmerDay = 256
    daySum = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year >= 1700 and year < 1917 and year % 4 == 0):
        days[1] += 1
    elif year == 1918:
        days[1] = 15
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days[1] += 1
    
    
    month = 1
    for day in days:
        if daySum + day <= 256:
            month += 1
            daySum += day
    
    strDay = str(programmerDay - daySum)
    strMonth = "0" + str(month)
    strYear = str(year)

    return ".".join([strDay, strMonth, strYear])

print(dayOfProgrammer(1918))
