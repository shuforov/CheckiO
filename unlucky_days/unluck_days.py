# http://www.checkio.org/mission/unlucky-days/
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

def checkio(year):
    y = range(1,13)
    count = 0
    for x in y:
        z = calendar.weekday(year, x, 13)
        if z == 4:
            count += 1

    return count


print checkio(2015)
print checkio(1986)