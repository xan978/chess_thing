from board import Board
import os
# from logic import Piece

def clear():
   os.system("cls" if os.name == "nt" else "clear")

game = Board()

while True:
    clear()
    game.print_board()
    mode = int(input("| add piece: 1 | move piece: 2 | delete piece: 3 |\n"))

    if mode == 1:
        clear()
        game.print_board()
        pos = []
        user_input_piece = int(input("enter piece number: \n"))
        user_input_pos = int(input("enter xy cordinate: "))

    elif mode == 2:
        pass

    elif mode == 3:
        pass

    else:
        print("bye!")
        break





# game.add_piece(icon="*", type=10, pos=pos, color=1)




