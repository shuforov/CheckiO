"""http://www.checkio.org/mission/min-max/"""


def calculate_min(*args, **kwargs):
    """min and maximum"""
    key = kwargs.get("key", None)
    # print type(args)
    # print args
    # print type(args)
    # print list(args)
    if key is None:
        if isinstance(args[0], tuple):
            sorted_list = []
            for elemnt in args[0]:
                sorted_list.append(elemnt)
                sorted_list = sorted(sorted_list)
            return sorted_list[0]
        elif isinstance(args[0], (list, int, str)):
            temp = 0
            list_for_sort = []
            string_v = ''
            type_of_var = 0
            for argument in args:
                if isinstance(argument, list):
                    temp = argument
                    temp = sorted(temp)
                    type_of_var = 0
                elif isinstance(argument, int):
                    list_for_sort.append(argument)
                    list_for_sort = sorted(list_for_sort)
                    type_of_var = 1
                elif isinstance(argument, str):
                    string_v += argument
                    string_v = ''.join(sorted(string_v))
                    type_of_var = 2
            list_return = [temp, list_for_sort, string_v]
            return list_return[type_of_var][0]
        # need fix elif to check if is generator!!
        elif True: 
            min_generator_number = next(args[0])
            while True:
                try:
                    if next(args[0]) < min_generator_number:
                        min_generator_number = next(args[0])
                except StopIteration:
                    return min_generator_number

    elif key is not None:
        if isinstance(args[0], list):
            check_num = key(args[0][0])
            counter = 0
            the_min = 0
            for temp in args:
                for argument in temp:
                    if key(argument) < check_num:
                        check_num = key(argument)
                        the_min = counter
                    counter += 1
            return args[0][the_min]


def calculate_max(*args, **kwargs):
    """calculate maximum"""
    key = kwargs.get("key", None)
    # print type(args)
    # print kwargs
    if key is None:
        temp = 0
        list_for_sort = []
        string_v = ''
        type_of_var = 0
        for argument in args:
            if isinstance(argument, list):
                temp = argument
                temp = sorted(temp)
                type_of_var = 0
            elif isinstance(argument, int):
                list_for_sort.append(argument)
                list_for_sort = sorted(list_for_sort)
                type_of_var = 1
            elif isinstance(argument, str):
                string_v += argument
                string_v = ''.join(sorted(string_v))
                type_of_var = 2
        list_return = [temp, list_for_sort, string_v]
        return list_return[type_of_var][len(list_return[type_of_var]) - 1]
    elif key is not None:
        # print key
        # print key(args[0])
        if isinstance(args[0], list):
            check_num = key(args[0][0])
            counter = 0
            the_max = 0
            for temp in args:
                for argument in temp:
                    if key(argument) > check_num:
                        check_num = key(argument)
                        the_max = counter
                        counter += 1
            return args[0][the_max]
        elif isinstance(args[0], float):
            check_num = key(args[0])
            counter = 0
            for argumentx in args:
                if key(argumentx) > check_num:
                    check_num = key(argumentx)
                    counter += 1
            return args[counter]
# 3, "Simple case max"
print calculate_max(3, 2)
# = 2, "Simple case min"
print calculate_min(3, 2)
# = 4, "From a list"
print calculate_max([1, 2, 0, 3, 4])
# = "e", "From string"
print calculate_min("hello")
# = 5.6, "Two maximal items"
print calculate_max(2.2, 5.6, 5.9, key=int)
# [9, 0], "lambda key"
print calculate_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])
# 9
print calculate_min((9,))
# ???!?!??!!?!?
print calculate_min(abs(i) for i in range(-10, 10))
