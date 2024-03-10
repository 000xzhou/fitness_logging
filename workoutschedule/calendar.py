import calendar
import datetime

today_month = datetime.date().month
today_year = datetime.date().year

print(today_month,today_year)


this_month = calendar.HTMLCalendar()
str = this_month.formatmonth(today_year, today_month)
# this will give you html... so you can edit it 
print(str)


# cal = calendar.Calendar()
# x = list(cal.monthdatescalendar(today_year, today_month))
# for i in x:
#     for a in i:
#         # a is type datetime.date 
#         print(a.month)
#         print(a.day)