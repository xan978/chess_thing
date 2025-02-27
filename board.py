class Board:
    def __init__(self):
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

    def board_setup(self):
        pass

    def add_piece(self, icon, type, pos, color):
        pos = self.pos_conversion(pos)
        x = pos[0]
        y = pos[1]
        self.grid[y][x][0] = icon
        self.grid[y][x][1] = type
        self.grid[y][x][2] = color

    def pos_conversion(self, pos):
        new_pos = []
        new_pos.append(pos[0] - 1)
        new_pos.append(8 - pos[1])
        return new_pos



