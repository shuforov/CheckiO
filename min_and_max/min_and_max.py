#http://www.checkio.org/mission/min-max/

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    print type(args)
    print kwargs

    z = 0
    list_for_sort = []
    string_v = ''
    type_of_var = 0
    for x in args:
        if isinstance(x,list):
            z = x
            z = sorted(z)
            type_of_var = 0
        elif isinstance(x,int):
            list_for_sort.append(x)
            list_for_sort = sorted(list_for_sort)
            type_of_var = 1
        elif isinstance(x,str):
            string_v += x
            string_v = ''.join(sorted(string_v))
            type_of_var = 2
    list_return = [z,list_for_sort,string_v]
    return list_return[type_of_var][0]

def max(*args, **kwargs):
    key = kwargs.get("key", None)

print min([1,5,0,9])

# print max(3, 2) == 3, "Simple case max"
# print min(3, 2) == 2, "Simple case min"
# print max([1, 2, 0, 3, 4]) == 4, "From a list"
# print min("hello") == "e", "From string"
# print max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
# print min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"