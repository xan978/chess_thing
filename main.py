from board import Board
import os
# from logic import Piece

game = Board()
game.board_setup()

def clear():
   os.system("cls" if os.name == "nt" else "clear")

def cord_input(string):
    user_input_pos = input(string)
    pos_string = user_input_pos.split(",")
    pos = list(map(int, pos_string))
    return pos

def get_current_color(move_number):
    if move_number % 2 == 0:
        return 2
    else:
        return 1

def move_piece_loop(current_color):
    start = cord_input("select piece in x,y format: ")
    end = cord_input("select square in x,y format: ")   
    is_valid_move = game.move_piece(start_pos=start, end_pos=end, current_color=current_color)
    if is_valid_move == 1:
        game.print_board(color=current_color)
        print(f"move number = {move_number} \nSelected square is empty, please select new one")
        move_piece_loop(current_color=current_color)
    elif is_valid_move == 2:
        game.print_board(color=current_color)
        print(f"move number = {move_number} | color = {current_color} \nwrong color")
        move_piece_loop(current_color=current_color)

clear()
mode = mode = int(input("| start game: 1 | test functions: 2 |\n"))
move_number = 1
current_color = 1

while mode == 1:
    current_color = get_current_color(move_number)
    game.print_board(color=current_color)
    print(f"move number = {move_number} | current color = {current_color}")
    move_piece_loop(current_color=current_color)
    move_number += 1


while mode == 2:
    game.print_board(color=current_color)
    print(f"current color = {current_color}")
    s = "| move piece: 1 | delete piece: 2 | add piece: 3 | change color: 4 | get info: 5| setup board: 6 | clear board: 7 |\n"
    test_mode = int(input(s))

    if test_mode == 1:
        move_piece_loop(current_color)

    elif test_mode == 2:
        pos = cord_input(string="enter x,y to delete piece: ")
        game.remove_piece(pos)

    elif test_mode == 3:
        data = cord_input(string="enter piece and color number in piece,color format: ")
        pos = cord_input(string="select square in x,y format: ")
        game.add_piece(type=data[0], color=data[1], pos=pos)

    elif test_mode == 4:
        if current_color == 1:
            current_color = 2
        else:
            current_color = 1

    elif test_mode == 5:
        pos = cord_input(string="select square in x,y format: ")
        piece_data = game.get_piece_data(pos=pos)
        print(f"icon = {piece_data[0]}, piece number = {piece_data[1]}, piece color = {piece_data[2]}, piece moves = {piece_data[3]}")
        input("press enter to continue")

    elif test_mode == 6:
        game.board_setup()

    elif test_mode == 7:
        game.clear_grid()

    else:
        print("Bye!")
        break