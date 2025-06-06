import os, copy
from logic import Piece
class Board:
    def __init__(self):
        self.grid = []
        self.clear_term = True

        for i in range(8):
            row = []
            for j in range(8):
                # order of data: icon, type, color, moves
                data = [" ", 0, 0, 0]
                row.append(data)
            self.grid.append(row)

    def clear(self):
        if self.clear_term == True:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            pass

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

    def king_pos(self, color):
        for y in range(8):
            for x in range(8):
                if self.grid[y][x][1] == 6 and self.grid[y][x][2] == color:
                    return [x+1, 8-y]

    def king_move_check(self, king_pos, king_pos2): # checks if the king can move. true means it can move
        directions = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]
        logic = Piece(self.grid)
        x, y = king_pos
        for i in range(8):
            x2 = x + directions[i][0]
            y2 = y + directions[i][1]
            if(
                x2 > 8
                or x2 < 1
                or y2 > 8
                or y2 < 1
            ):
                continue # skips out of bound squares
            end = [x2, y2]
            end2 = self.pos_conversion(end)
            if logic.move_king(king_pos, end, king_pos2, end2):
                return True
        return False

    def is_checkmate(self, king_pos, king_pos2, color): # check if king is in checkmate
        logic = Piece(self.grid)
        if not logic.is_square_attacked(king_pos, king_pos2, color):
            return False # not checkmate because king is not in check
        if self.king_move_check(king_pos, king_pos2):
            return False # not checkmate because king can move out of the way

        # checks all pieces on the board
        for y in range(8):
            for x in range(8):
                piece_icon, piece_type, piece_color, piece_moves = self.get_piece_data([x+1, 8-y])
                if piece_color != color or piece_type == 6 or piece_type == 0:
                    continue # if not same color as king, skip the rest of this loop
                start = [x+1, 8-y]
                start2 = self.pos_conversion(start)

                # checks for all possible moves for said piece
                for y2 in range(8):
                    for x2 in range(8):
                        end_pos = [x2+1, 8-y2]
                        # end_pos2 = self.pos_conversion(end_pos)
                        backup = copy.deepcopy(self.grid)
                        result = self.move_piece(start, end_pos, color, checks=False)
                        if result == 0:
                            self.grid = backup
                            return False # if theres a legal move, that means king is not in check
        return True # checkmate, not legal moves were found

    def is_stalemate(self, king_pos, king_pos2, color):
        logic = Piece(self.grid)
        if logic.is_square_attacked(king_pos, king_pos2, color):
            return False # not stalemate because king is in check
        if self.king_move_check(king_pos, king_pos2):
            return False # not stalemate because king has legal moves

        # checks all pieces on the board
        for y in range(8):
            for x in range(8):
                piece_icon, piece_type, piece_color, piece_moves = self.get_piece_data([x + 1, 8 - y])
                if piece_color != color or piece_type == 6 or piece_type == 0:
                    continue  # if not same color as king, skip the rest of this loop
                start = [x + 1, 8 - y]

                # checks for all possible moves for said piece
                for y2 in range(8):
                    for x2 in range(8):
                        end_pos = [x2 + 1, 8 - y2]
                        backup = copy.deepcopy(self.grid)
                        result = self.move_piece(start, end_pos, color, checks=False)
                        if result == 0:
                            self.grid = backup
                            return False  # legal move found, king not in stalemate
        return True  # stalemate, not legal moves were found

    def move_piece(self, start_pos, end_pos, current_color, checks=True):

        icon, type, color, moves = self.get_piece_data(start_pos)
        start_pos2 = self.pos_conversion(start_pos)
        end_pos2 = self.pos_conversion(end_pos)
        moves += 1
        backup_grid = copy.deepcopy(self.grid)
        # print(f"TEST DATA: {self.king_pos(current_color)}")

        if (
            type == 0  # cant move empty square
            or current_color != color  # wrong color
            or start_pos == end_pos  # cant move onto self
        ):
            return 1  # illegal move

        logic = Piece(self.grid)
        move_functions = {
            1: logic.move_pawn,
            2: logic.move_rook,
            3: logic.move_knight,
            4: logic.move_bishop,
            5: logic.move_queen,
            6: logic.move_king
        }
        check = move_functions[type](start_pos, end_pos, start_pos2, end_pos2)
        if check == False:
            return 1  # illegal move

        if check == "promotion":
            self.promotion(end_pos, color, moves)
            self.remove_piece(pos=start_pos)
        elif check > 30:
            self.castle(check)
        else:  # complete move
            self.add_piece(type=type, pos=end_pos, color=color, moves=moves)
            self.remove_piece(pos=start_pos)

        # this checks if your king is in check after making you move. if so, it reverts the board
        other_color = self.opposite_color(current_color)
        king_pos = self.king_pos(current_color)
        king_pos2 = self.pos_conversion(king_pos)
        enemy_king_pos = self.king_pos(other_color)
        enemy_king_pos2 = self.pos_conversion(enemy_king_pos)
        if logic.is_square_attacked(king_pos, king_pos2, current_color):
            self.grid = backup_grid
            return 2  # must move out of check

        # this is to see if your move wins the game
        if checks == True: # required so that checkmate and stalemate fuctions dont do an infinite loop
            if self.is_checkmate(enemy_king_pos, enemy_king_pos2, other_color):
                return 3
            if self.is_stalemate(enemy_king_pos, enemy_king_pos2, other_color):
                return 4

        return 0  # legal move

    def promotion(self, pos, color, moves):
        # piece = int(input("Enter promotion piece number: "))
        piece = 5
        self.add_piece(type=piece, pos=pos, color=color, moves=moves)

    def castle(self, castle_number):
        if castle_number == 31:  # left white
            self.move_piece_simple(start_pos=[1, 1], end_pos=[4, 1], add_move=True)  # moves rook
            self.move_piece_simple(start_pos=[5, 1], end_pos=[3, 1], add_move=True)  # moves king
        elif castle_number == 32:  # right white
            self.move_piece_simple(start_pos=[8, 1], end_pos=[6, 1], add_move=True)  # moves rook
            self.move_piece_simple(start_pos=[5, 1], end_pos=[7, 1], add_move=True)  # moves king
        elif castle_number == 33: # left black
            self.move_piece_simple(start_pos=[1, 8], end_pos=[4, 8], add_move=True)  # moves rook
            self.move_piece_simple(start_pos=[5, 8], end_pos=[3, 8], add_move=True)  # moves king
        elif castle_number == 34: # right black
            self.move_piece_simple(start_pos=[8, 8], end_pos=[6, 8], add_move=True)  # moves rook
            self.move_piece_simple(start_pos=[5, 8], end_pos=[7, 8], add_move=True)  # moves king

    def move_piece_simple(self, start_pos, end_pos, add_move=False):  # takes in unconverted numbers
        icon, type, color, moves = self.get_piece_data(start_pos)
        if add_move: moves +=1
        self.add_piece(type, end_pos, color, moves=moves)
        self.remove_piece(start_pos)

    def get_piece_data(self, pos):  # takes in unconverted number
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

    def set_board(self, board):
        self.grid = board

    def opposite_color(self, color):
        if color == 1:
            return 2
        else:
            return 1


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