def checkio(number_n):
    if (number_n > 0) and (number_n < 1000):
        one_to_nine = {1:"one", 2:"two", 3:"three",
                      4:"four", 5:"five", 6:"six",
                      7:"seven", 8:"eight", 9:"nine"}
        teen_to_nineten = {10:"teen", 11:"eleven", 12:"twelve",
                            13:"thirteen", 14:"fourteen", 15:"fifteen",
                            16:"sixteen", 17:"seventeen", 18:"eighteen",
                            19:"nineteen"}
        twenty_ninety ={20:"twenty", 30:"thirty", 40:"forty",50:"fifty",
                        60:"sixty", 70:"seventy", 80:"eighty" ,90:"ninety"}
        hundred_one_space = " hundred"
        hundred_two_space = " hundred "
        str_number = str(number_n)
        def one_number_size(one_number_n):
            if len(one_number_n) == 1:
                for x in one_to_nine:
                    if int(one_number_n) == x:
                        return one_to_nine[x]
        def two_number_size(two_number_n):
            if len(two_number_n) == 2:
                if (int(two_number_n[0]) == 1) and (int(two_number_n[1]) == 0):
                    for x in teen_to_nineten:
                        if number_n == x:
                            return teen_to_nineten[x]
                elif (int(two_number_n[0]) == 1) and (int(two_number_n[1]) > 0):
                    for x in teen_to_nineten:
                        if int(two_number_n) == x:
                            return teen_to_nineten[x]
                elif (int(two_number_n[0]) == 2) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 2) and (int(two_number_n[1]) > 0):
                    tempo_n = "twenty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 3) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 3) and (int(two_number_n[1]) > 0):
                    tempo_n = "thirty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 4) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 4) and (int(two_number_n[1]) > 0):
                    tempo_n = "forty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 5) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 5) and (int(two_number_n[1]) > 0):
                    tempo_n = "fifty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 6) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 6) and (int(two_number_n[1]) > 0):
                    tempo_n = "sixty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 7) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 7) and (int(two_number_n[1]) > 0):
                    tempo_n = "seventy "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 8) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 8) and (int(two_number_n[1]) > 0):
                    tempo_n = "eighty "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
                elif (int(two_number_n[0]) == 9) and (int(two_number_n[1]) == 0):
                    for x in twenty_ninety:
                        if int(two_number_n) == x:
                            return twenty_ninety[x]
                elif (int(two_number_n[0]) == 9) and (int(two_number_n[1]) > 0):
                    tempo_n = "ninety "
                    for x in one_to_nine:
                        if int(two_number_n[1]) == x:
                            tempo_n += one_to_nine[x]
                    return tempo_n
        def three_number_size(three_number_n):
            temp_n = ''
            if len(three_number_n) == 3:
                temp_n = three_number_n[1:]
            if (int(temp_n[0]) == 0) and (int(temp_n[1]) == 0):
                return one_number_size(three_number_n[0]) + hundred_one_space
            elif (int(temp_n[0]) == 0) and (int(temp_n[1]) > 0):
                return one_number_size(three_number_n[0]) + hundred_two_space + one_number_size(three_number_n[2])

        if len(str_number) == 1:
            return one_number_size(str_number)
        elif len(str_number) == 2:
            return two_number_size(str_number)
        elif len(str_number) == 3:
            return three_number_size(str_number)
print checkio(200)