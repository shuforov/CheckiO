#http://www.checkio.org/mission/feed-pigeons/

def checkio(feed):

    feeds = feed
    pigens = []
    good = 0
    count = 0
    #step by step minus
    g = 0   #how mach need to dec from feeds [1,3,6...]
    s = range(1,11) # list of pigens come avery minutes
    for z in s:    #loop for calculate how much 
        g += z #up the decrement from feed
        if g <= feeds: # if dec low from feed thean feed need decrement -> feed - g 
            feeds -= g
            pigens.append(g) # and up the number of feeded pigens
            count += 1
        elif (g > feeds) and (feeds > 0): # if decrementor biger thean feeds need too cheack how much can feed pigens left
            h = feeds - (count-1)
            z = h - count
            x = (count - 1) + z
            pigens.append(x)
            bgd=0
            for x in pigens:
                bgd += x
            good = bgd
            return good
    return pigens[count-1]                

print 'one =>',checkio(1)
print 'two =>',checkio(2)
print 'three =>',checkio(3)
print 'four =>',checkio(4)
print 'five =>',checkio(5)
print 'six =>',checkio(6)
print 'seven =>',checkio(7)
print 'eight =>',checkio(8)
print 'nine =>',checkio(9)
print 'ten =>',checkio(10)