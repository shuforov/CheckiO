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
    print board


print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
##print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
##print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
##print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1