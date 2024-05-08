import datetime

#date is today
today = datetime.date.today()
print(today)

#date is yesterday
yesterday = today - datetime.timedelta(days=1)
print(yesterday)

#set different date format (mm/dd/yy)
formated_today = today.strftime("%m / %d / %y")
print(formated_today)

#set different date format (mmm/dd/yy)
formated_yesterday = (today-datetime.timedelta(days=1)).strftime("%b/%d/%y")
print(formated_yesterday)