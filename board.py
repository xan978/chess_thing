class Board:
    def __init__(self):
        self.grid = []

        for i in range(8):
            row = []
            for j in range(8):
                data = [" ", 0, 0]
                row.append(data)
            self.grid.append(row)

    def clear_grid(self):
        self.grid = []
        for i in range(8):
            row = []
            for j in range(8):
                data = [" ", 0, 0]
                row.append(data)
            self.grid.append(row)

    def print_board(self):
        for i in range(8):
            print(8-i, end="")
            for x in range(8):
                print(f"[{self.grid[i][x][0]}] ", end="")
            print()
        print(f"  1   2   3   4   5   6   7   8 \n")

    def add_piece(self, type, pos, color):
        pos = self.pos_conversion(pos)
        x = pos[0]
        y = pos[1]
        icon = self.get_icon(type=type, color=color)
        self.grid[y][x][0] = icon
        self.grid[y][x][1] = type
        self.grid[y][x][2] = color

    def remove_piece(self, pos):
        self.add_piece(type=0, pos=pos, color=0)

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







