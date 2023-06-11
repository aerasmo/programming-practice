def timeConversion(s):
    timeList = s.split(':')
    hour = int(timeList[0])
    if ('PM' in s and hour < 12):
        hourConverted = hour + 12 
        timeList[0] = str(hourConverted)
    elif ('AM' in s and hour == 12):
        timeList[0] = '00'

    convertedTime = ':'.join(timeList).rstrip('PM').rstrip('AM')
    return convertedTime