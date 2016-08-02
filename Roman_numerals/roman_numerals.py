"""translater from latin number to roman"""


def roman_numerals(number_lat):
    """translate number"""
    roman_num = {1: 'I',
                 2: 'II',
                 3: 'III',
                 4: 'IV',
                 5: 'V',
                 6: 'VI',
                 7: 'VII',
                 8: 'VIII',
                 9: 'IX',
                 10: 'X',
                 20: 'XX',
                 30: 'XXX',
                 40: 'XL',
                 50: 'L',
                 60: 'LX',
                 70: 'LXX',
                 80: 'LXXX',
                 90: 'XC',
                 100: 'C',
                 200: 'CC',
                 300: 'CCC',
                 400: 'CD',
                 500: 'D',
                 600: 'DC',
                 700: 'DCC',
                 800: 'DCCC',
                 900: 'CM',
                 1000: 'M',
                 2000: 'MM',
                 3000: 'MMM',
                 3999: 'MMMCMXCIX'}
    if number_lat < 9 and number_lat > 1:
        for key in roman_num:
            if key == number_lat:
                return roman_num[key]
    elif number_lat < 90 and number_lat > 9:
        number_complite = ''
        for key in roman_num:
            if key == int(str(number_lat)[0] + '0'):
                number_complite = roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[1]):
                number_complite += roman_num[key]
        return number_complite
    elif number_lat < 900 and number_lat > 90:
        number_complite = ''
        for key in roman_num:
            if key == int(str(number_lat)[0] + '00'):
                number_complite = roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[1] + '0'):
                number_complite += roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[2]):
                number_complite += roman_num[key]
        return number_complite
    elif number_lat <= 3999 and number_lat > 900:
        number_complite = ''
        for key in roman_num:
            if key == int(str(number_lat)[0] + '000'):
                number_complite = roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[1] + '00'):
                number_complite += roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[2] + '0'):
                number_complite += roman_num[key]
        for key in roman_num:
            if key == int(str(number_lat)[3]):
                number_complite += roman_num[key]
        return number_complite


print roman_numerals(2)
print roman_numerals(6)
print roman_numerals(76)
print roman_numerals(13)
print roman_numerals(40)
print roman_numerals(3999)
