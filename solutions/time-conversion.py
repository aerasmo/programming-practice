
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeList = s.split(':')
    if ('PM' in s):
        hour = int(timeList[0])
        if hour < 12:
            hourConverted = hour + 12 
            timeList[0] = str(hourConverted)
    convertedTime = ':'.join(timeList).rstrip('PM').rstrip('AM')
    return convertedTime

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    times = [
        '02:05:24AM',
        '12:02:24AM',
        '01:05:24PM',
        '06:05:24PM',
        '12:05:24PM',
        ]

    for s in times:
        print(timeConversion(s))

    # f.write(result + '\n')

    # f.close()
