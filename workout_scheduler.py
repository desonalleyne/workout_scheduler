import os
import ConfigParser
import csv
import math
from sms_mailer import SMS_Mailer
pwd = os.getcwd()

def get_reader(raw_file):
    aFile = open(raw_file, "rb")
    return csv.reader(aFile)


def get_headers(reader):
    rownum = 0
    for row in reader:
        if rownum == 0:
            return row


def get_daily_doses(reader):
    daily_values = []
    for row in reader:
        daily_values.append(row)
    return daily_values


def get_config():
    config = ConfigParser.ConfigParser()
    config.readfp(open('workout_scheduler.conf'))
    return config


def get_day_dose(day):
    config = get_config()
    sms = SMS_Mailer(config.get('main', 'sender'))
    msisdn = config.get('main', 'msisdn')
    sets = config.getint('main', 'sets')

    r = get_reader("exercises.csv")
    exercise = get_headers(r)
    daily_values = get_daily_doses(r)

    day -= 1

    out = "Day: " + str(day + 1) + '\n, '
    out += "Sets: " + str(sets) + '\n, '
    for record in range(1, len(daily_values[day])):
        if daily_values[day][record] == '':
            daily_values[day][record] = 0
        out += str(exercise[record] + ": " + str(int(math.ceil(int(daily_values[day][record]) / sets))) + ', ')
        # out += str(exercise[record] + ": " + str(math.ceil(int(daily_values[day][record]) / sets)) + ', ')

    print out
    sms.send_sms({msisdn},"",out)


def get_day():
    f = open('today', 'r')
    day = f.read()
    f.close()
    return int(day)


def set_day(day):
    f = open('today', 'w')
    f.write(str(day))
    f.close()

day = get_day()
get_day_dose(day)
set_day(day + 1)
