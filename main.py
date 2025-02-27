from board import Board
import os
# from logic import Piece

os.system("clear")
game = Board()
game.print_board()

# def clear():
#    os.system("cls" if os.name == "nt" else "clear")

pos = []
x = input("put in x: ")
y = input("put in y: ")
pos.append(int(x))
pos.append(int(y))

os.system("clear")
game.add_piece(icon="*", type=10, pos=pos, color=1)
game.print_board()




