#!/usr/sbin/env python3
''' 
OPS435 Assignment 1 - Winter 2020
Program: a1_sthapa17.py 
Author: "Saurav Thapa"
The python code in this file (a1_sthapa17.py) is original work written by
"Saurav Thapa". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken. 
'''
import sys

def dbda(date,days):
    '''
    The dbda() function should be the main function of your script. The dbda() function will take a date in "YYYY-MM-DD" format, a positive or negative integer, and return a date either before or after the given date according to the value of the given integer in the same format.
    '''
    i = 0
    total = 0
    today = date
    if len(str(days)) == 10:
        valid_date(days)
        if date < days:
            while today < days:
                total +=1
                today = after(today)
        elif date > days:
            while today > days:
                total +=1
                today = before(today)
        print(total)

    else:
        if int(days) > 0:
            while i < int(days):
                i += 1
                if sys.argv[1] == '--step':
                    today = after(today)
                    print(today)
                else:
                    today = after(today)


        elif int(days) < 0:
            while i > int(days):
                i = i - 1
                if sys.argv[1] == '--step':
                    today = before(today)
                    print(today)
                else:
                    today = before(today)

        else:
            today = today

        if sys.argv[1] == '--step':
            print('', end='')
        else:
            print(today)

def after(date):
    '''
    The after() function will take a date in "YYYY-MM-DD" format and return the date of the next day in the same format. Next paragraph is a sample python code for the after() function.
    '''
    valid_date(date)
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    mon_max = days_in_mon(year)
    tmp_day = day + 1

    if tmp_day > mon_max[month]:
        tmp_day = 1
        month = month + 1
        if month > 12:
           month = 1
           year = year + 1
   
    next_date = str(year)+"-"+str(month).zfill(2)+"-"+str(tmp_day).zfill(2)
    return next_date

def before(date):
    '''
    The before() function will take a date in "YYYY-MM-DD" format and return the date of the previous day in the same format
    '''
    valid_date(date)
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    mon_max = days_in_mon(year)
    to_day = day - 1
    if to_day == 0:
        month = month - 1
        if month == 0:
            year = year -1
            month = 12
            to_day = 31
        else:
            to_day = mon_max[month]

    day_before = str(year)+"-"+str(month).zfill(2)+"-"+str(to_day).zfill(2)
    return day_before

def valid_date(date):
    '''
    The valid_date() function will take a date in "YYYY-MM-DD" format, and return True if the given date is a valid date, otherwise return False plus an appropriate status message. The valid_date() function should make use of the days_in_mon() function.
    '''


    if (len(date) != 10):
        print("Error: wrong date entered")
        exit()
    else:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        mon_max = days_in_mon(year)

        if month not in mon_max.keys():
            print("Error: wrong month entered")
            exit()
        else:
            day_max = mon_max[month]
            if day not in range (1,day_max+1):
                print("Error: wrong day entered")
                exit()

def leap_year(lyear):
    '''
    The leap_year() function will take a year in "YYYY" format, and return True if the given year is a leap year, otherwise return False.
    '''
    if ((lyear % 4 == 0) or (lyear == lyear % 100) or (lyear % 400 ==0)):
        leap_year = True
    else:
        leap_year = False
    return leap_year

def days_in_mon(yvalue):
    '''
    The days_in_mon() function will take a year in "YYYY" format, and return a dictionary object which contains the total number of days in each month for the given year. The days_in_mon() function should make use of the leap_year() function.
    '''
    if leap_year(yvalue):
        feb = 29
    else:
        feb = 28

    mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max


def usage():
    '''
    The usage() function will take no argument and return a string describing the usage of the script. 
    '''
    NumberOfArgument = len(sys.argv)

    if ((NumberOfArgument != 4) and NumberOfArgument != 3):
        print ('Usage: a1_sthapa17.py [--step] YYYY-MM-DD +/-n')
        exit()

if __name__ == "__main__":
    usage()
    if sys.argv[1] == '--step':
        date = sys.argv[2]
        days = sys.argv[3]
    else:
        date = sys.argv[1]
        days = sys.argv[2]

    dbda(date,days)

