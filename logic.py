class Piece:
    def __init__(self, grid):
        self.grid = grid

    def is_enemy(self, start2, end2):
        # start2 and end2 is the converted start and end data
        start_color = self.grid[start2[1]][start2[0]][2]
        end_color = self.grid[end2[1]][end2[0]][2]
        if end_color != start_color and end_color != 0:
            return True
        else:
            return False

    def friendly_fire(self, start2, end2):
        start_color = self.grid[start2[1]][start2[0]][2]
        end_color = self.grid[end2[1]][end2[0]][2]
        if start_color == end_color:
            return True
        else:
            return False

    def move_pawn(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end
        color = self.grid[start2[1]][start2[0]][2]
        end_type = self.grid[end2[1]][end2[0]][1]
        start_moves = self.grid[start2[1]][start2[0]][3]

        if color == 1:
            direction = 1
        else:
            direction = -1
        if start_x == end_x and end_y == start_y + direction and end_type == 0:
            return True

        if (
            start_x == end_x
            and end_y == start_y + (direction * 2)
            and end_type == 0
            and start_moves == 0
        ):
            return True

        if (
            self.is_enemy(start2, end2) == True
            and end_x == start_x + 1
            and end_y == start_y + direction

        ):
            return True

        if (
            self.is_enemy(start2, end2) == True
            and end_x == start_x - 1
            and end_y == start_y + direction
        ):
            return True

    def move_rook(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end
        one_direction = 0

        if self.friendly_fire(start2, end2) == True:
            return False

        if start_x == end_x:
            direction = 1 if end_y > start_y else -1
            length = abs(start_y - end_y)
            one_direction += 1
            for y in range(length):
                if(
                    direction == 1
                    and self.grid[start2[1] - (y+1)][start2[0]][1] != 0
                    and start_y + (y+1) != end_y
                ):
                    return False
                if (
                    direction == -1
                    and self.grid[start2[1] + (y + 1)][start2[0]][1] != 0
                    and start_y - (y + 1) != end_y
                ):
                    return False

        if start_y == end_y:
            direction = 1 if end_x > start_x else -1
            length = abs(start_x - end_x)
            one_direction += 1
            for x in range(length):
                if(
                    direction ==  1
                    and self.grid[start2[1]][start2[0] + (x+1)][2] != 0
                    and start_x + (x+1) != end_x
                ):
                    return False
                if (
                    direction == -1
                    and self.grid[start2[1]][start2[0] - (x + 1)][2] != 0
                    and start_x - (x + 1) != end_x
                ):
                    return False

        if one_direction != 1:
            return False
        else:
            return True

    def move_knight(self, start, end, start2, end2):
        return True

    def move_bishop(self, start, end, start2, end2):
        return True

    def move_queen(self, start, end, start2, end2):
        return True

    def move_king(self, start, end, start2, end2):
        return True

