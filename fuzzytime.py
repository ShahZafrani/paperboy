# returns fuzzytext like time
# "quarter past six"
# returns it as three strings so it can be displayed easily on multiple lines
import datetime
hours = {
    0: "twelve",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
}

minutes = {
    1: "five",
    2: "ten",
    3: "quarter",
    4: "twenty",
    5: "twentyfive",
    6: "half"
}

def updateTime(offset):
    now = datetime.datetime.now()
    offsetMinute = now.minute + offset
    if offsetMinute < 5:
        return "", getHour(now.hour), "o clock"
    relation = "past"
    if offsetMinute > 30:
        return minutes.get((60 - offsetMinute) / 5), "to", getHour(now.hour + 1) 
    else:
        return minutes.get(offsetMinute / 5), "past", getHour(now.hour)

def getHour(hour):
    if hour > 11: 
        return hours.get(hour - 12)
    else:
        return hours.get(hour)

if __name__ == "__main__":
    print(datetime.datetime.now().minute)
    print(updateTime(-2))