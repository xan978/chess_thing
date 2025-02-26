class Board:
    def __init__(self):
        self.grid = []

        for i in range(8):
            row = []
            for j in range(8):
                row.append(" ")
            self.grid.append(row)

    def print_board(self):
        for i in range(8):
            print(8-i, end="")
            for x in range(8):
                print(f"[{self.grid[i][x]}] ", end="")
            print()
        print(f"  1   2   3   4   5   6   7   8")



