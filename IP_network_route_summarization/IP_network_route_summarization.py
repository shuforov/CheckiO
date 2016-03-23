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
    # for x in tempo_list:
    #     print x
    counter = 0
    s = ''
    for x in tempo_list[0]:
        # print tempo_list[0][counter],
        counter_num = 0
        for go in tempo_list[1:]:
            if go[counter] == x:
                counter_num += 1
        if counter_num == len(data) - 1:
            s += x
        elif counter_num != len(data) - 1:
            break
        counter += 1
    # print s

    mask = 0
    for x in s:
        if x in dict_match:
            mask += 1
    # print mask
    number = ''
    counter_8 = 0
    correct = ''
    for x in s:
        if x in dict_match:
            number += x
            counter_8 += 1
        if counter_8 == 8:
            correct += number + '.'
            counter_8 = 0
            number = ''

    if counter_8 < 8:
        some = 8 - counter_8
        number += '0' * some
        correct += number

    while len(correct) != 35:
        correct += '.' + '0' * 8
    # print correct
    from_bin_to_dec = ''
    number_bin = ''
    for x in correct:
        if x in dict_match:
            from_bin_to_dec += x
        if len(from_bin_to_dec) == 8:
            number_bin += str(int(from_bin_to_dec,2)) + '.'
            from_bin_to_dec = ''

    return number_bin[:-1] + '/' + str(mask)



print checkio(["172.16.12.11", "172.16.13.0", "172.16.14.0", "172.16.15.0"])
print checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"])
print checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"])

#These "asserts" using only for self-checking and not necessary for auto-testing

# (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
# (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"