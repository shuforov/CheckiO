def checkio(number_n):
    if (number_n > 0) and (number_n < 1000):
        one_to_nine = {1:"one", 2:"two", 3:"three",
                      4:"four", 5:"five", 6:"six",
                      7:"seven", 8:"eight", 9:"nine"}
        teen_to_twenty = {10:"teen", 11:"eleven", 12:"twelve",
                            13:"thirteen", 14:"fourteen", 15:"fifteen",
                            16:"sixteen", 17:"seventeen", 18:"eighteen",
                            19:"nineteen", 20:"twenty"}
        str_number = str(number_n)
        if len(str_number) == 1:
            for x in one_to_ten:
                if number_n == x:
                    return teen_to_twenty[x]
        if len(str_number) == 2:
            for x in teen_to_twenty:
                if number_n == x:
                    return teen_to_twenty[x]

print checkio(10)