# http://www.checkio.org/mission/ip-network-route-summarization/


def checkio(data):
    int_num = range(0,256)
    dict_match = {}
    for z in int_num:
        dict_match[str(z)] = bin(z)[2:].zfill(8)
    tempo_list = []
    for x in data:
        tempo = ''
        for y in x:
            if y in dict_match:
                tempo += y
            elif y == '.':
                tempo += '.'
                print dict_match[tempo[:-1]]+'.'
                tempo = ''
        print tempo

print checkio(["172.16.12.0", "172.16.13.0"])

#These "asserts" using only for self-checking and not necessary for auto-testing

# (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"