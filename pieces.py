class Piece:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos

    def move_check(self, start_pos, end_pos, grid):
        raise NotImplementedError("bruh")

    def symbol(self):
        raise NotImplementedError("BRUH")
