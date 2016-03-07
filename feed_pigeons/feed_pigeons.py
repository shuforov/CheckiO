#http://www.checkio.org/mission/feed-pigeons/

def checkio(feed):

    feeds = feed
    count = 0
    pigens = []
    #step by step minus
    g = 0
    s = range(1,11)
    for z in s:
        pigens.append(g)
        g += z
        if g <= feeds:
            feeds -= g
            count += 1

    return pigens[count]


print checkio(1)
print checkio(2)
print checkio(3)
print checkio(5)
print checkio(10)