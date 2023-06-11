def breakingRecords(scores):
    record = scores[0]
    lowestRecords = [record]
    highestRecords = [record]
    for score in scores:
        if score < lowestRecords[-1]:
            lowestRecords.append(score)
        elif score > highestRecords[-1]:
            highestRecords.append(score)
    return [len(highestRecords) -1, len(lowestRecords) -1]