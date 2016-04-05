#https://checkio.org/mission/the-most-frequent-weekdays/
import calendar
z = calendar.Calendar(calendar.MONDAY)
v = calendar.TextCalendar(firstweekday=0)
def most_frequent_days(year):
    month = 1
    print calendar.monthrange(year, month)
    list_temp = []
    for x in calendar.day_name:
        list_temp.append(x)
    print list_temp
    g = z.iterweekdays()
    list_for_days = []
    for x in g:
        list_for_days.append(x)
    print list_for_days
    t = z.itermonthdays(year, month)
    print v.formatmonth(year,month,w=0,l=0)
    print calendar.MONDAY
print most_frequent_days(2399)

    # assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    # assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    # assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    # assert most_frequent_days(2909) == ['Tuesday'], "4th example"