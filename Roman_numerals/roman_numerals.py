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
    new_lat_num = str(number_lat)
    add_zero = '0' * len(new_lat_num)
    number_rom = ''
    if number_lat in roman_num:
        return roman_num[number_lat]
    else:
        for temp in xrange(len(new_lat_num)):
            if new_lat_num[temp] == '0' and temp == len(new_lat_num)-1:
                break
            if temp + 1 == len(new_lat_num) and int(
                    new_lat_num[-1:] in roman_num):
                number_rom += roman_num[int(new_lat_num[temp])]
            elif temp + 1 == len(new_lat_num) and int(
                    new_lat_num[-2:]) in roman_num:
                number_rom += roman_num[int(new_lat_num[-2:])]
            elif temp < len(new_lat_num) and new_lat_num[temp] != '0':
                number_rom += roman_num[int(
                    new_lat_num[temp] + add_zero[temp+1:])]
        return number_rom

print roman_numerals(2)
print roman_numerals(6)
print roman_numerals(76)
print roman_numerals(13)
print roman_numerals(3910)
print roman_numerals(3999)
