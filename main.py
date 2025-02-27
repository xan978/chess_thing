from board import Board
import os
# from logic import Piece

game = Board()
game.print_board()

pos = []
x = input("put in x: ")
y = input("put in y: ")
pos.append(int(x))
pos.append(int(y))

if os.name == 'nt': os.system('cls') else: os.system('clear')
game.add_piece(icon="*", type=10, pos=pos, color=1)
game.print_board()




