#https://checkio.org/mission/the-most-frequent-weekdays/
import calendar
z = calendar.Calendar(calendar.MONDAY)
v = calendar.TextCalendar(firstweekday=0)

def most_frequent_days(year):
    month = range(1,13)
    for month_num in month:
        #list days name of the week
        list_temp = []
        for x in calendar.day_name:
            list_temp.append(x)
        print list_temp
        #creating dictionary for counting days
        day_of_the_week = {}
        day_number = range(0,8)
        input_dict_counter = 0
        for x in day_number:
            day_of_the_week[x] = 0
            input_dict_counter += 1
        print day_of_the_week
        #creating list with all days in month
        gg = calendar.monthcalendar(year, month_num)
        list_of_wholl_month = []
        for x in gg:
            list_of_wholl_month.append(x)
        print list_of_wholl_month
        #matching of days and count it
        for x in list_of_wholl_month:
            counter = 0
            for z in x:
                if z > 1:
                    day_of_the_week[counter] += 1
                counter += 1
        #simple output calendar
        print v.formatmonth(year,month_num,w=0,l=0)


print most_frequent_days(2399)

    # assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    # assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    # assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    # assert most_frequent_days(2909) == ['Tuesday'], "4th example"