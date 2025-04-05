from board import Board
import os

class Main():

    def __init__(self):
        self.game = Board()
        self.game.board_setup()

    def clear(self):
       os.system("cls" if os.name == "nt" else "clear")

    def cord_input(self, string):
        user_input_pos = input(string)
        pos_string = user_input_pos.split(",")
        pos = list(map(int, pos_string))
        return pos

    def get_current_color(self, move_number):
        if move_number % 2 == 0:
            return 2
        else:
            return 1

    def move_check(self, current_color, start, end):
        is_valid_move = self.game.move_piece(start_pos=start, end_pos=end, current_color=current_color)
        messages = {
            1: "Selected square is empty, please select new one",
            2: "wrong color",
            3: "can't move onto self",
            4: "illegal move",
            8: "cant move king into check"
        }
        return messages.get(is_valid_move, True)

    def start_game(self):
        self.clear()
        mode = int(input("| start game: 1 | test functions: 2 |\n"))
        move_number = 1
        current_color = 1
        error_message = False

        while mode == 1:

            current_color = self.get_current_color(move_number)
            self.game.print_board(color=current_color)
            if error_message != False: print(f"error: {move_check_data}")
            print(f"move number = {move_number} | current color = {current_color}")

            start = self.cord_input("select piece in x,y format: ")
            end = self.cord_input("select square in x,y format: ")
            move_check_data = self.move_check(current_color, start, end)
            if move_check_data == True:
                move_number += 1; error_message = False
            else:
                error_message = move_check_data


        while mode == 2:
            self.game.print_board(color=current_color)
            print(f"current color = {current_color}")
            if error_message != False: print(f"error: {move_check_data}")
            s = "| move piece: 1 | delete piece: 2 | add piece: 3 | change color: 4 | get info: 5| setup board: 6 | clear board: 7 |\n"
            test_mode = int(input(s))

            if test_mode == 1:
                start = self.cord_input("select piece in x,y format: ")
                end = self.cord_input("select square in x,y format: ")
                move_check_data = self.move_check(current_color, start, end)
                if move_check_data == True:
                    move_number += 1;
                    error_message = False
                else:
                    error_message = move_check_data

            elif test_mode == 2:
                pos = self.cord_input(string="enter x,y to delete piece: ")
                self.game.remove_piece(pos)

            elif test_mode == 3:
                data = self.cord_input(string="enter piece and color number in piece,color format: ")
                pos = self.cord_input(string="select square in x,y format: ")
                self.game.add_piece(type=data[0], color=data[1], pos=pos)

            elif test_mode == 4:
                if current_color == 1:
                    current_color = 2
                else:
                    current_color = 1

            elif test_mode == 5:
                pos = self.cord_input(string="select square in x,y format: ")
                piece_data = self.game.get_piece_data(pos=pos)
                print(f"icon = {piece_data[0]}, piece number = {piece_data[1]}, piece color = {piece_data[2]}, piece moves = {piece_data[3]}")
                input("press enter to continue")

            elif test_mode == 6:
                self.game.board_setup()

            elif test_mode == 7:
                self.game.clear_grid()

            else:
                print("Bye!")
                break

        # self.start_game()
main = Main()
main.start_game()


