class Piece:
    def __init__(self, grid):
        self.grid = grid

    def is_enemy(self, start, end):
        start_color = self.grid[start[1]][start[0]][2]
        end_color = self.grid[end[1]][end[0]][2]
        if end_color != start_color and end_color != 0:
            return True
        else:
            return False

    def move_pawn(self, start, end):
        return True

    def move_rook(self, start, end):
        return True

    def move_knight(self, start, end):
        return True

    def move_bishop(self, start, end):
        return True

    def move_queen(self, start, end):
        return True

    def move_king(self, start, end):
        return True

