# -*- coding: utf-8 -*-

##Никола обожает классифицировать все, что видит вокруг. Однажды Стефан подарил ему устройство для ярлыков на день рождение, и затем они неделями отдирали наклейки со всех поверхностей и вещей на корабле. Он категоризировал все реагенты в своей лаборатории, книги в библиотеке и даже заметки на столе. Но когда он узнал о том, что в Python есть тип данных словарь, он категоризировал все конфигурационные файлы дронов Софии. Теперь эти файлы организованы в сложную вложенную структуру, что очень не нравится Софии. Помогите ей упростить эти словари словарей.
##
##Словари - это удобный тип данных для хранения и обработки различных конфигураций. Они позволяют хранить данные по ключам и создавать вложенные структуры. Дан словарь, в котором в качестве ключей используются строки, а в качестве значений строки или словари. Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах. Результатом будет словарь без вложенных словарей. Ключи должны содержать путь, составленный из родительских ключей из начального словаря, разделенных "/". Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой (""). Взглянем на пример:
##
##    {
##        "name": {
##            "first": "One",
##            "last": "Drone"
##        },
##        "job": "scout",
##        "recent": {},
##        "additional": {
##            "place": {
##                "zone": "1",
##                "cell": "2"}
##        }
##    }
##Результатом будет:
##
##    {"name/first": "One",           #один прародитель
##     "name/last": "Drone",
##     "job": "scout",                #ключ корневого уровня
##     "recent": "",                  #пустой словарь
##     "additional/place/zone": "1",  #третий уровень
##     "additional/place/cell": "2"}
##
##София уже написала код для этой задачи, но в нем есть ошибка. Вам достаточно найти и исправить эту ошибку.
##
##Входные данные: Оригинальный словарь (dict).
##
##Выходные данные: "Плоский" словарь (dict).
##
##Примеры:
##
##    flatten({"key": "value"}) == {"key": "value"}
##    flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
##    flatten({"empty": {}}) == {"empty": ""}
##
##Связь с реальной жизнью: Методы из этой задачи будут полезны, чтобы разобрать и упростить структуры конфигураций или файлов. Вы легко можете улучшить данную концепцию для ваших конкретных задач. А также, чтение чужого кода и поиск ошибок - это очень полезный навык.
##
##Предусловия:
##Ключи в словаре - не пустые строки.
##Значения в словаре - строки или другие словари.
##root_dictionary != {}

def flatten(dict_n):
    temp_dict = dict_n
    new_dict = temp_dict
    temp_list = []
##    print dict([(temp_key, temp_dict)])

    while isinstance(new_dict,dict) == True:
        temp_key = new_dict.keys()
        temp_key = temp_key[0]
        temp_list.append(temp_key)
        new_dict = new_dict.pop(temp_key)
        print new_dict
    join_words = ''
    for x in temp_list:
        join_words += x + '/'
    join_words = join_words[:-1]
    print join_words


##print flatten({"key": "value"})
print flatten({"key": {"deeper": {"more": {"enough": "value"}}}})
##print flatten({"empty": {}})













