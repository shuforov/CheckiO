    #http://www.checkio.org/mission/the-longest-palindromic/

def longest_palindromic(text):
    matrix = []
    matrix_x = []
    def matrix_make(some_l):
        temp_text = some_l
        count_one = 0
        count_two = 0
        #making of matrix of True and False value, and make matrix from later position.
        while count_one < len(temp_text):
            y = []
            m = []
            two = count_two
            while two < len(temp_text):
                zx = count_one,two
                if temp_text[count_one] == temp_text[two]:
                    y.append('T')
                    m.append(zx)
                    two += 1
                elif temp_text[count_one] != temp_text[two]:
                    y.append('F')
                    m.append(zx)
                    two += 1
            y.reverse()
            matrix.append(y)
            matrix_x.append(m)
            count_one += 1
            count_two += 1

    matrix_make(text)

    # for x in matrix:
    #      print x
    # for x in matrix_x:
    #     print x

    #make full matrix in right way
    counter_h = 1
    while counter_h != len(text):
        while len(matrix[counter_h]) < len(text):
            matrix[counter_h].append('F')
        counter_h += 1
    for z in matrix:
        z.reverse()
        # print z
    # #calculate how mach True in first matrix and put them in to list
    counter_m = 0
    lists_of_pal = []
    counter_for_loop = 0
    for x in matrix:
        counter_for_loop = 0
        for s in x:
            if s == 'T' and counter_for_loop > 1:
                z = counter_m
                j = counter_for_loop
                counter_for_size = 0
                list_temp = []
                while z < len(matrix) and matrix[z][j] == 'T':
                    # print 'T',z,j
                    list_temp.append(j)
                    z += 1
                    j = j - 1
                    counter_for_size += 1
                # print '--------'
                if counter_for_size > 1:
                    # print list_temp
                # print s, counter_for_loop
                    lists_of_pal.append(list_temp)
            counter_for_loop += 1
        # print '\n'
        counter_m += 1
    #search for longest index palindromes in lists
    if len(lists_of_pal) > 1:
        tempo_var = lists_of_pal[0]
        for y in lists_of_pal:
            if len(tempo_var) < len(y):
                tempo_var = y
        for x in reversed(tempo_var[:-1]):
            tempo_var.append(x)
        # print ''
        # print tempo_var
        temp_lists = []
        for x in tempo_var:
            temp_lists.append(text[x])
        return ''.join(temp_lists)
    elif len(lists_of_pal) <= 0:
        return text[0]

print longest_palindromic("artrartrt")
print longest_palindromic("abacada")
print longest_palindromic("aaaa")
print longest_palindromic('abc')

# longest_palindromic("artrartrt") == "rtrartr", "The Longest"
# longest_palindromic("abacada") == "aba", "The First"
# longest_palindromic("aaaa") == "aaaa", "The A"