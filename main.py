from board import Board
import os
# from logic import Piece

game = Board()
game.board_setup()

def clear():
   os.system("cls" if os.name == "nt" else "clear")

def cord_input():
    user_input_pos = input("enter cordinate in x,y format: ")
    pos_string = user_input_pos.split(",")
    pos = list(map(int, pos_string))
    return pos

while True:
    clear()
    game.print_board()
    mode = int(input("| add piece: 1 | move piece: 2 | delete piece: 3 | clear board: 4 | setup board: 5 |\n"))

    if mode == 1:
        clear()
        game.print_board()
        user_input_type = int(input("enter piece number: "))
        user_input_color = int(input("enter piece color, 1=white 2=black: "))
        pos = cord_input()
        game.add_piece(type=user_input_type, color=user_input_color, pos=pos)

    elif mode == 2:
        pass

    elif mode == 3:
        clear()
        game.print_board()
        pos = cord_input()
        game.remove_piece(pos)

    elif mode == 4:
        game.clear_grid()

    elif mode == 5:
        game.board_setup()

    else:
        print("bye!")
        break










