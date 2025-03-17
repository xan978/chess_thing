import os
from logic import Piece
class Board:
    def __init__(self):
        self.grid = []

        for i in range(8):
            row = []
            for j in range(8):
                # order of data: icon, type, color, moves
                data = [" ", 0, 0, 0]
                row.append(data)
            self.grid.append(row)

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def clear_grid(self):
        self.grid = []
        for i in range(8):
            row = []
            for j in range(8):
                data = [" ", 0, 0, 0]
                row.append(data)
            self.grid.append(row)

    def print_board(self, clear=True, color=1):
        if clear != False:
            self.clear()
        if color == 1:
            for i in range(8):
                print(8-i, end="")
                for x in range(8):
                    print(f"[{self.grid[i][x][0]}] ", end="")
                print()
            print(f"  1   2   3   4   5   6   7   8 \n")
        else:
            for i in range(8):
                print(i+1, end="")
                for x in range(8):
                    print(f"[{self.grid[7-i][7-x][0]}] ", end="")
                print()
            print(f"  8   7   6   5   4   3   2   1 \n")

    def add_piece(self, type, pos, color, moves=0):
        pos = self.pos_conversion(pos)
        x = pos[0]
        y = pos[1]
        icon = self.get_icon(type=type, color=color)
        self.grid[y][x][0] = icon
        self.grid[y][x][1] = type
        self.grid[y][x][2] = color
        self.grid[y][x][3] = moves

    def remove_piece(self, pos):
        self.add_piece(type=0, pos=pos, color=0)

    def move_piece(self, start_pos, end_pos, current_color):

        start_pos2 = self.pos_conversion(start_pos)
        end_pos2 = self.pos_conversion(end_pos)
        type = self.grid[start_pos2[1]][start_pos2[0]][1]
        color = self.grid[start_pos2[1]][start_pos2[0]][2]
        moves = self.grid[start_pos2[1]][start_pos2[0]][3] + 1

        if type == 0:
            return 1  # cant move empty sqaure
        if current_color != color:
            return 2  # wrong color
        logic = Piece(self.grid)
        move_functions = {
            1: logic.move_pawn,
            2: logic.move_rook,
            3: logic.move_knight,
            4: logic.move_bishop,
            5: logic.move_queen,
            6: logic.move_king
        }
        if type in move_functions and not move_functions[type](start_pos, end_pos, start_pos2, end_pos2):
            return 3

        self.add_piece(type=type, pos=end_pos, color=color, moves=moves)
        self.remove_piece(pos=start_pos)

    def get_piece_data(self, pos):
        pos = self.pos_conversion(pos)
        x = pos[0]
        y = pos[1]
        icon = self.grid[y][x][0]
        type = self.grid[y][x][1]
        color = self.grid[y][x][2]
        moves = self.grid[y][x][3]
        return [icon, type, color, moves]

    def pos_conversion(self, pos):
        new_pos = []
        new_pos.append(pos[0] - 1)
        new_pos.append(8 - pos[1])
        return new_pos

    def board_setup(self):
        self.clear_grid()
        piece_row = [2, 3, 4, 5, 6, 4, 3, 2]
        for i in range(8):
            self.add_piece(type=1, pos=[i+1, 2], color=1)
        for i in range(8):
            self.add_piece(type=1, pos=[i+1, 7], color=2)
        for i in range(8):
            self.add_piece(type=piece_row[i], pos=[i+1, 1], color=1)
            self.add_piece(type=piece_row[i], pos=[i+1, 8], color=2)

    def get_icon(self, type, color):
        # 1=pawn 2=rook 3=knight 4=bishop 5=queen 6=king 7=test_piece
        # 1=white 2=black
        data_sheet = {
            (0, 0): " ",
            (1, 1): "P",
            (1, 2): "p",
            (2, 1): "R",
            (2, 2): "r",
            (3, 1): "N",
            (3, 2): "n",
            (4, 1): "B",
            (4, 2): "b",
            (5, 1): "Q",
            (5, 2): "q",
            (6, 1): "K",
            (6, 2): "k",
            (7, 1): "*",
            (7, 2): "*"
        }
        return data_sheet.get((type, color), "?")







