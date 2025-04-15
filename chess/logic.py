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

    def promotion_check(self, end_y, color):
        if (
            (color == 1 and end_y == 8)
            or (color == 2 and end_y == 1)
        ):
            return "promotion"
        else:
            return True

    def pos_conversion(self, x=0, y=0):
        if x != 0:
            return x-1
        else:
            return 8-y

    def is_square_attacked(self, pos, pos2, color):
        functions = {
            1:self.move_pawn,
            2:self.move_rook,
            3:self.move_knight,
            4:self.move_bishop,
            5:self.move_queen,
            6:self.move_king_simple,
        }
        for y in range(8):
            for x in range(8):
                start2 = [x, y]
                start = [x+1, 8-y]
                piece_number = self.grid[y][x][1]
                piece_color = self.grid[y][x][2]
                if start != pos and piece_number != 0 and piece_color != color:
                    move_check = functions[piece_number](start, pos, start2, pos2)
                else:
                    move_check = False

                if move_check == True or move_check == "promotion":
                    return True

        return False

    def is_list_attacked(self, cords, color):
        # if any square in the list is being attacked, return true
        # list is to be formated like so: [cord, cord2], [cord, cord2]
        # the 2 after the second item in each list means the unconverted number
        for cord in cords:
            if (
                self.is_square_attacked(cord[0], cord[1], color)
            ):
                return True
        return False

    def move_pawn(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end
        color = self.grid[start2[1]][start2[0]][2]
        end_type = self.grid[end2[1]][end2[0]][1]
        start_moves = self.grid[start2[1]][start2[0]][3]

        direction = 1 if color == 1 else -1
        if start_x == end_x and end_y == start_y + direction and end_type == 0:
            return self.promotion_check(end_y, color)

        if (
            start_x == end_x
            and end_y == start_y + (direction * 2)
            and end_type == 0
            and start_moves == 0
            and self.grid[start2[1] - direction][start2[0]][1] == 0
        ):
            return True

        if (
            (self.is_enemy(start2, end2) == True
            and end_x == start_x + 1
            and end_y == start_y + direction)

            or (self.is_enemy(start2, end2) == True
            and end_x == start_x - 1
            and end_y == start_y + direction)
        ):
            return self.promotion_check(end_y, color)

        return False

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
                    and self.grid[start2[1]][start2[0] + (x+1)][1] != 0
                    and start_x + (x+1) != end_x
                ):
                    return False
                if (
                    direction == -1
                    and self.grid[start2[1]][start2[0] - (x + 1)][1] != 0
                    and start_x - (x + 1) != end_x
                ):
                    return False

        if one_direction != 1:
            return False
        else:
            return True

    def move_knight(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end

        if self.friendly_fire(start2, end2) == True:
            return False

        if (
            (start_y + 2 == end_y or start_y - 2 == end_y)
             and (start_x + 1 == end_x or start_x - 1 == end_x)
        ):
            return True

        if (
            (start_x + 2 == end_x or start_x - 2 == end_x)
            and (start_y + 1 == end_y or start_y - 1 == end_y)
        ):
            return True

        return False

    def move_bishop(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end
        if abs(start_x - end_x) != abs(start_y - end_y):
            return False
        if self.friendly_fire(start2, end2):
            return False

        direction_x = 1 if end_x > start_x else -1
        direction_y = 1 if end_y > start_y else -1
        x, y = start_x + direction_x, start_y + direction_y
        while (x, y) != (end_x, end_y):
            x2, y2 = self.pos_conversion(x=x), self.pos_conversion(y=y)
            if self.grid[y2][x2][1] != 0:
                return False
            x += direction_x
            y += direction_y

        return True

    def move_queen(self, start, end, start2, end2):
        return self.move_rook(start, end, start2, end2) or self.move_bishop(start, end, start2, end2)

    def move_king_simple(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end

        abs_x = abs(start_x - end_x)
        abs_y = abs(start_y - end_y)
        if self.friendly_fire(start2, end2) == True: return False
        if (abs_x > 1) or (abs_y > 1):
            return False

        return True

    def move_king(self, start, end, start2, end2):
        start_x, start_y = start
        end_x, end_y = end
        color = self.grid[start2[1]][start2[0]][2]
        lw_list = [ [[2,1],[7,1]], [[3,1],[7,2]], [[4,1],[7,3]] ]
        rw_list = [ [[6,1],[7,5]], [[7,1],[7,6]] ]
        lb_list = [ [[2,8],[0,1]], [[3,8],[0,2]], [[4,8],[0,3]] ]
        rb_list = [ [[6,8],[0,5]], [[7,8],[0,6]] ]

        if (
            self.grid[end2[1]][end2[0]][1] == 2      # landing on rook
            and self.grid[end2[1]][end2[0]][3] == 0  # rook has not moved
            and self.grid[start2[1]][start2[0]][3] == 0 # the king piece has not moved
            and (end_x == 1 or end_x == 8) # can only be the corners of the board
        ):
            if end_y == 1:
                # white castle
                # IMPORTANT: add check so that no squares the king go through are threatend
                if(
                    end_x == 1 # left rook
                    and self.grid[7][1][1] == 0 # going through empty squares
                    and self.grid[7][2][1] == 0
                    and self.grid[7][3][1] == 0
                ):
                    if not self.is_list_attacked(lw_list, color=1):
                        # makes sure not to pass through any squares under attack
                        return "castleLW"
                elif(
                    self.grid[7][5][1] == 0
                    and self.grid[7][6][1] == 0
                ):
                    if not self.is_list_attacked(rw_list, color=1):
                        return "castleRW"
            elif end_y == 8:
                # black castle
                if(
                    end_x == 1 # left rook
                    and self.grid[0][1][1] == 0
                    and self.grid[0][2][1] == 0
                    and self.grid[0][3][1] == 0
                ):
                    if not self.is_list_attacked(lb_list, color=2):
                        return "castleLB"
                elif(
                     self.grid[0][5][1] == 0
                     and self.grid[0][6][1] == 0
                ):
                    if not self.is_list_attacked(rb_list, color=2):
                        return "castleRB"

        if not self.move_king_simple(start, end, start2, end2):
            return False

        if self.is_square_attacked(end, end2, color):
            return False

        return True