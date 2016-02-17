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

        str_number = str(number_n)

        if len(str_number) == 1:
            for x in one_to_nine:
                if number_n == x:
                    return one_to_nine[x]
        if len(str_number) == 2:
            if (int(str_number[0]) == 1) and (int(str_number[1]) == 0):
                for x in teen_to_nineten:
                    if number_n == x:
                        return teen_to_nineten[x]
            elif (int(str_number[0]) == 1) and (int(str_number[1]) > 0):
                for x in teen_to_nineten:
                    if int(str_number) == x:
                        return teen_to_nineten[x]
            elif (int(str_number[0]) == 2) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 2) and (int(str_number[1]) > 0):
                tempo_n = "twenty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 3) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 3) and (int(str_number[1]) > 0):
                tempo_n = "thirty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 4) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 4) and (int(str_number[1]) > 0):
                tempo_n = "forty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 5) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 5) and (int(str_number[1]) > 0):
                tempo_n = "fifty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 6) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 6) and (int(str_number[1]) > 0):
                tempo_n = "sixty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 7) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 7) and (int(str_number[1]) > 0):
                tempo_n = "seventy "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 8) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 8) and (int(str_number[1]) > 0):
                tempo_n = "eighty "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n
            elif (int(str_number[0]) == 9) and (int(str_number[1]) == 0):
                for x in twenty_ninety:
                    if int(str_number) == x:
                        return twenty_ninety[x]
            elif (int(str_number[0]) == 9) and (int(str_number[1]) > 0):
                tempo_n = "ninety "
                for x in one_to_nine:
                    if int(str_number[1]) == x:
                        tempo_n += one_to_nine[x]
                return tempo_n

print checkio(91)