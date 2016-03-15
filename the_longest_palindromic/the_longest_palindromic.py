#http://www.checkio.org/mission/the-longest-palindromic/

def longest_palindromic(text):
    temp_text = text
    matrix = []
    count_one = 0
    count_two = 0
    while count_one < len(temp_text):
        y = []
        two = count_two
        while two < len(temp_text):
            if temp_text[count_one] == temp_text[two]:
                y.append('T')
                two += 1
            elif temp_text[count_one] != temp_text[two]:
                y.append('F')
                two += 1
        y.reverse()
        matrix.append(y)
        count_one += 1
        count_two += 1
    for x in matrix:
        print x



print longest_palindromic("artrartrt")
# longest_palindromic("artrartrt") == "rtrartr"