from board import Board
# from display import Display
import os
import copy

demo1 = [[['r', 2, 2, 0], ['n', 3, 2, 0], ['b', 4, 2, 0], ['q', 5, 2, 0], ['k', 6, 2, 0], ['b', 4, 2, 0], ['n', 3, 2, 0], ['r', 2, 2, 0]], [['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['P', 1, 1, 0], ['P', 1, 1, 0], [' ', 0, 0, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0]], [['R', 2, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['K', 6, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['R', 2, 1, 0]]]
demo2 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['p', 1, 2, 0], [' ', 0, 0, 0], ['R', 2, 1, 0], ['P', 1, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]
demo3 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['K', 6, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]
demo4 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['R', 2, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['B', 4, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['K', 6, 1, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]


# display = Display()
# display.display_loop()
game = Board()
game.board_setup()
clear_term = True

def clear():
   if clear_term:
       os.system("cls" if os.name == "nt" else "clear")
   else:
       pass

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

def move_check(current_color, start, end):
    is_valid_move = game.move_piece(start_pos=start, end_pos=end, current_color=current_color)
    messages = {
        1: "Illegal move",
        2: "must move out of check"
    }
    return messages.get(is_valid_move, True)


clear()
mode = int(input("| start game: 1 | test functions: 2 |\n"))
move_number = 1
current_color = 1
error_message = False

while mode == 1:

    current_color = get_current_color(move_number)
    game.print_board(color=current_color)
    if error_message != False: print(f"error: {move_check_data}")
    print(f"move number = {move_number} | current color = {current_color}")

    start = cord_input("select piece in x,y format: ")
    end = cord_input("select square in x,y format: ")
    move_check_data = move_check(current_color, start, end)
    if move_check_data == True:
        move_number += 1; error_message = False
    else:
        error_message = move_check_data


while mode == 2:
    game.print_board(color=current_color)
    print(f"current color = {current_color}")
    if error_message != False:
        print(f"error: {move_check_data}")
        error_message = False
    s = "| move piece: 1 | delete piece: 2 | add piece: 3 | change color: 4 | get info: 5| setup board: 6 | clear board: 7 | print gird: 8 | board: 9| toggle clear: 10\n"
    test_mode = int(input(s))

    if test_mode == 1:
        start = cord_input("select piece in x,y format: ")
        end = cord_input("select square in x,y format: ")
        move_check_data = move_check(current_color, start, end)
        if move_check_data == True:
            move_number += 1
            error_message = False
        else:
            error_message = move_check_data

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

    elif test_mode == 8:
        print(game.grid)
        input("press enter to continue")

    elif test_mode == 9:
        clear()
        game.print_board()
        print("| 1: castle | 2: rook | 3: check | 4: check2 |")
        board_state = int(input("enter which board state to pick: "))
        if board_state == 1:
            game.grid = copy.deepcopy(demo1)
        elif board_state == 2:
            game.grid = copy.deepcopy(demo2)
        elif board_state == 3:
            game.grid = copy.deepcopy(demo3)
        elif board_state == 4:
            game.grid = copy.deepcopy(demo4)

    elif test_mode == 10:
        clear_term = not clear_term
        game.clear_term = clear_term

    else:
        print("Bye!")
        break
