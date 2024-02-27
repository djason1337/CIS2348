# Dominic Jason 2203959

import datetime

current_date = datetime.datetime.now()
current_date = current_date.replace(second=0, microsecond=0)
current_date_year = int(current_date.strftime("%Y"))
current_date_month = int(current_date.strftime("%m"))
current_date_day = int(current_date.strftime("%d"))


user_date = input()
dates_start = []
dates_end = []
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

month_numbers = {
  "January": 1,
  "February": 2,
  "March": 3,
  "April": 4,
  "May": 5,
  "June": 6,
  "July": 7,
  "August": 8,
  "September": 9,
  "October": 10,
  "November": 11,
  "December": 12
}

# Read dates from input and stop when -1 is inputted
while user_date != '-1':
    dates_start.append(user_date)
    user_date = input()


# Check if dates include valid month(case insensitive) and comma
for date in dates_start:
    for month in months:
        if month.lower() in date:
            if date.find(',') >= 1:
                dates_end.append(date)
        elif month in date:
            if date.find(',') >= 1:
                dates_end.append(date)

# Use find() to parse month day and year, check to make sure no future date is accepted
for date in dates_end:
    comma = date.find(',')
    space = date.find(' ')
    month = date[:space]
    day = date[space+1:comma]
    year = date[comma+2:]
    month_number = month_numbers[month]
    int_day = int(day)
    int_year = int(year)
    if int_year < current_date_year:
        print(f'{month_numbers[month]}/{day}/{year}')


