##http://www.checkio.org/mission/pawn-brotherhood/solve/
import string

def safe_pawns(pawns):
    board = []
    def creat_board():
        for num in reversed(range(1,9)):
            temp_list = []
            for alp in string.ascii_lowercase[0:8]:
                temp_list.append(alp + str(num))
            board.append(temp_list)
    creat_board()
    board_bin = board
    def create_bin_bord(elements):
        elem = elements
        count_one = 0
        for x in board:
            count = 0
            for z in x:
                if z in elem:
                    board_bin[count_one][count] = 1
                else:
                    board_bin[count_one][count] = 0
                count += 1
            count_one += 1
    create_bin_bord(pawns)

    def check_save():
        count_safe = 0
        list_temp = []
        count_row = 0
        for vol in board_bin:
            count_1 = 0
            for zx in vol:
                if zx == 1:
                    list_temp.append((count_row,count_1))
                count_1 += 1
            count_row += 1
        for x in list_temp:
            if ((x[0]+1,x[1]-1)in list_temp) or ((x[0]+1,x[1]+1) in list_temp):
                count_safe += 1
        return count_safe
    return check_save()







print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
##print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
##print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1