# http://www.checkio.org/mission/ip-network-route-summarization/


def checkio(data):
    int_num = range(1,256)
    dict_match = {'0':'0'*8}
    for z in int_num:
        dict_match[str(z)] = bin(z)[2:].zfill(8)
    tempo_list = []
    for x in data:
        tempo = ''
        bin_num = ''
        for y in x:
            if y in dict_match and x.index(y) == len(x)-1:
                tempo += y
            elif y in dict_match:
                tempo += y
            elif y == '.':
                tempo += '.'
                bin_num += dict_match[tempo[:-1]]+'.'
                tempo = ''
        bin_num += dict_match[tempo]
        tempo_list.append(bin_num)
    print tempo_list
print checkio(["172.16.12.11", "172.16.13.0", "172.16.14.0", "172.16.15.0"])

#These "asserts" using only for self-checking and not necessary for auto-testing

# (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"