#http://www.checkio.org/mission/find-friends/

def check_connection(tup,first,second):
    g = ()
    for x in tup:
        g = g + (x,)

    gggg = []
    for z in g:
        temp = z.index('-')
        gggg.append([z[:temp], z[temp+1:]])

    list_n2 = []
    h = second
    for x in gggg:
        if h in x:
            for z in x:
                list_n2.append(z)
                if z != h:
                    h = z

    list_two = []
    for x in list_n2:
        if x not in list_two:
            list_two.append(x)


    list_temp = []
    for x in list_two:
        list_temp.append(x)

    count = 0
    while count < len(list_temp):
        for x in gggg:
            if list_temp[count] in x:
                for z in x:
                    if z not in list_temp:
                        list_temp.append(z)
        count += 1

    if first in list_temp and second in list_temp:
        return True
    else:
        return False



print check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"scout2", "scout3")
print check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"dr101", "sscout")
##print check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"scout2", "scout3") == True
##check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"dr101", "sscout") == False