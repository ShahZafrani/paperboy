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
    12: "twelve",
    13: "one",
    14: "two",
    15: "three",
    16: "four",
    17: "five",
    18: "six",
    19: "seven",
    20: "eight",
    21: "nine",
    22: "ten",
    23: "eleven",
    24: "twelve" # easiest fix for when it's past 23:30 and we're adding 1 to the hour 
}

minutes = {
    1: "five",
    2: "ten",
    3: "quarter",
    4: "twenty",
    5: "twentyfive",
    6: "half",
    7: "twentyfive",
    8: "twenty",
    9: "quarter",
    10: "ten",
    11: "five"
}

months = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "setptember",
    10: "october",
    11: "november",
    12: "december"
}

days = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth",
    21: "twentyfirst",
    22: "twentysecond",
    23: "twentythird",
    24: "twentyfourth",
    25: "twentyfifth",
    26: "twentysixth",
    27: "twentyseventh",
    28: "twentyeighth",
    29: "twentyninth",
    30: "thirtieth",
    31: "thirtyfirst"
}

years = {
    2020: "twenty twenty",
    2021: "upgrade this damn clock"
}

def getDate(now):
    month = months.get(now.month)
    day = days.get(now.day)
    year = years.get(now.year)
    return "{} {}, {}".format(month, day, year)

def updateTime(offset, now):
    offsetMinute = (int) (now.minute + offset)
    print(offsetMinute)
    if offsetMinute < 5:
        return " ", getHour(now.hour), "o clock"
    relation = "past"
    minute = minutes.get((int) (offsetMinute / 5))
    if offsetMinute > 34:
        return minute, "to", getHour(now.hour + 1) 
    else:
        return minute, "past", getHour(now.hour)

def getHour(hour):
    if hour > 11: 
        return hours.get(hour - 12)
    else:
        return hours.get(hour)

if __name__ == "__main__":
    now = datetime.datetime.now()
    print(updateTime(2, now))
