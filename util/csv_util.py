import datetime
import csv

def print_csv(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(', '.join(row))



def get_file_path(now, city):
    return "prayer_times/" + str(now.year) + "/" + str(now.month) + "/" + str(city) + ".csv"

def get_salat_times(day, filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        todays_times = [row for idx, row in enumerate(reader) if idx == day]
        return todays_times[0]


if __name__ == "__main__":
    now = datetime.datetime.now()
    filepath = get_file_path(now, "augusta")
    print(filepath)
    # print_csv(filepath)
    today_times = get_salat_times(now.day, filepath)
    print("{}/{}/{}".format(now.month, now.day, now.year))
    print("fajr- {}\nzuhr- {} \nasr- {} \nmaghrib- {} \nisha- {}".format(today_times[1], today_times[3], today_times[4], today_times[5], today_times[6]))


