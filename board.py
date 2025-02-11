class Board:
    def __init__(self):
        self.grid = []

        for i in range(8):
            row = []
            for j in range(8):
                row.append("empty")
            self.grid.append(row)

    def print_board(self):
        for i in range(8):
            print(self.grid[i])

# test = Board()
# test.print_board()
