#http://www.checkio.org/mission/feed-pigeons/

def checkio(number):

    feeds = number
    feed_to_need = []
    number_of_pigens_feed = 0
    g = 0
    s = ''
    if number > 1:
        s = range(1,number)
    elif number <= 1:
        s = range(1,11)
    for z in s:
        g += z
        if g <= feeds:
            feeds -= g
            number_of_pigens_feed += 1
            feed_to_need.append(g)
            if feeds == 0:
                v = feed_to_need[-1:]
                v = v.pop(0)
                return v
        if g > feeds:
            v = feed_to_need[-1:]
            v = v.pop(0)
            h = feeds - v
            if h < 0:
                feed_to_need.append(g)
                b = feed_to_need[-1:]
                b = b.pop(0)
                return b
            if h > 0:
                return v + h

print 'one =>',checkio(1)
# print 'two =>',checkio(2)
# print 'three =>',checkio(3)
# print 'four =>',checkio(4)
# print 'five =>',checkio(5)
# print 'six =>',checkio(6)
# print 'seven =>',checkio(7)
# print 'eight =>',checkio(8)
# print 'nine =>',checkio(9)
# print 'teen =>',checkio(10)
# print 'eighteen =>',checkio(18)
print '10000 =>', checkio(10000)