#https://checkio.org/mission/the-most-frequent-weekdays/
import calendar
z = calendar.Calendar(calendar.MONDAY)
v = calendar.TextCalendar(firstweekday=0)

def most_frequent_days(year):
    month = range(1,13)
    # creating dictionary for counting days
    day_of_the_week = {}
    day_number = range(0, 7)
    input_dict_counter = 0
    for x in day_number:
        day_of_the_week[x] = 0
        input_dict_counter += 1
    #perform each month
    for month_num in month:
        #list days name of the week
        list_temp = []
        for x in calendar.day_name:
            list_temp.append(x)
        #creating list with all days in month
        gg = calendar.monthcalendar(year, month_num)
        list_of_wholl_month = []
        for x in gg:
            list_of_wholl_month.append(x)
        #matching of days and count it
        for x in list_of_wholl_month:
            counter = 0
            for z in x:
                if z >= 1:
                    day_of_the_week[counter] += 1
                counter += 1

        #simple output calendar
        # print v.formatmonth(year,month_num,w=0,l=0)
        #sorting the most frequent day and return it
    couple_day_list = []
    sorted_val_of_dict = sorted(day_of_the_week.values())
    for x in day_of_the_week:
        if day_of_the_week[x] == sorted_val_of_dict[len(sorted_val_of_dict) - 1]:
            couple_day_list.append(list_temp[x])
    return couple_day_list

print most_frequent_days(2399)

    # assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    # assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    # assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    # assert most_frequent_days(2909) == ['Tuesday'], "4th example"