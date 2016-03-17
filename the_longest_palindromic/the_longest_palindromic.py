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
        print z
    # #calculate how mach True in first matrix and put them in to list
    counter_m = 0

    lists_of_pal = []
    while counter_m != len(text):
        counter_t = 0
        for x in matrix[counter_m]:
            if x == 'T':
                counter_t += 1
        if counter_t > 1:
            lists_s = []
            z = counter_m
            t = matrix[counter_m][matrix[counter_m].index(x)]
            while t == 'T':
                lists_s.append((z, matrix[z].index(x)))
                t = matrix[z][matrix[z].index(x) - 1]
                z += 1
            lists_of_pal.append(lists_s)
        elif counter_t == 1:
            counter_t = 0
        counter_m += 1
    print(lists_of_pal)
print longest_palindromic("artrartrt")
# longest_palindromic("artrartrt") == "rtrartr"