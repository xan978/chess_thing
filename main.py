from board import Board
import os
from logic import Piece

game = Board()
game.board_setup()

def clear():
   os.system("cls" if os.name == "nt" else "clear")

def cord_input(string):
    user_input_pos = input(string)
    pos_string = user_input_pos.split(",")
    pos = list(map(int, pos_string))
    return pos

def user_move_piece():
    start = cord_input("select piece in x,y format: ")
    end = cord_input("select square in x,y format: ")
    game.move_piece(start_pos=start, end_pos=end)

clear()
mode = mode = int(input("| start game: 1 | test functions: 2 |\n"))

while mode == 1:
    game.print_board()
    user_move_piece()

while mode == 2:
    game.print_board()
    test_mode = int(input("| move piece: 1 | delete piece: 2 | add piece: 3 | setup board: 4 | clear board: 5 |\n"))

    if test_mode == 1:
        user_move_piece()

    elif test_mode == 2:
        pos = cord_input(string="enter x,y to delete piece: ")
        game.remove_piece(pos)

    elif test_mode == 3:
        data = cord_input(string="enter piece and color number in piece,color format: ")
        pos = cord_input(string="select square in x,y format: ")
        game.add_piece(type=data[0], color=data[1], pos=pos)

    elif test_mode == 4:
        game.board_setup()

    elif test_mode == 5:
        game.clear_grid()

    else:
        print("Bye!")
        break


# while True:
#     clear()
#     game.print_board()
#     mode = int(input("| add piece: 1 | move piece: 2 | delete piece: 3 | clear board: 4 | setup board: 5 |\n"))
#
#     if mode == 1:
#         clear()
#         game.print_board()
#         user_input_type = int(input("enter piece number: "))
#         user_input_color = int(input("enter piece color, 1=white 2=black: "))
#         pos = cord_input()
#         game.add_piece(type=user_input_type, color=user_input_color, pos=pos)
#
#     elif mode == 2:
#         pass
#
#     elif mode == 3:
#         clear()
#         game.print_board()
#         pos = cord_input()
#         game.remove_piece(pos)
#
#     elif mode == 4:
#         game.clear_grid()
#
#     elif mode == 5:
#         game.board_setup()
#
#     else:
#         print("bye!")
#         break










