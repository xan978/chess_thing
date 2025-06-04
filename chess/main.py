from board import Board
import os, copy, pygame, time

demo1 = [[['r', 2, 2, 0], ['n', 3, 2, 0], ['b', 4, 2, 0], ['q', 5, 2, 0], ['k', 6, 2, 0], ['b', 4, 2, 0], ['n', 3, 2, 0], ['r', 2, 2, 0]], [['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0], ['p', 1, 2, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['P', 1, 1, 0], ['P', 1, 1, 0], [' ', 0, 0, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0], ['P', 1, 1, 0]], [['R', 2, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['K', 6, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['R', 2, 1, 0]]]
demo2 = [[['K', 6, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['k', 6, 2, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['p', 1, 2, 0], [' ', 0, 0, 0], ['R', 2, 1, 0], ['P', 1, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]
demo3 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['k', 6, 2, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['K', 6, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]
demo4 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['k', 6, 2, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['R', 2, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['B', 4, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['K', 6, 1, 0], [' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]
demo5 = [[[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], ['K', 6, 1, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], ['r', 2, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], ['R', 2, 1, 0], ['R', 2, 1, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [[' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]], [['k', 6, 2, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0], [' ', 0, 0, 0]]]

# declaring board, pygame, and piece images
game = Board()
game.board_setup()
clear_term = True
pygame.init()
pygame.display.set_caption("chess_thing")

piece_images = {}

# this is to load the images into pygame and store it into a dictionary
piece_types = ["P", "R", "N", "B", "Q", "K"]
color_mapping = {1: 'w', 2: 'b'}
for color_number, color_letter in color_mapping.items():
    for piece in piece_types:
        image_path = f"images/{color_letter}{piece}.png"
        loaded_image = pygame.image.load(image_path)
        resized_image = pygame.transform.scale(loaded_image, (100, 100))
        piece_images[(piece.lower(), color_number)] = resized_image

"""
the way the piece_types dictionary works is that it stores the chess images
using a key that is a tuple of the piece type (as a lowercase letter) and
the piece color (as a number). for example, to get the image of the black
queen, you would do image = piece_images.get(("q", 2))
"""

def clear(): # this is so i can clear the terminal
   if clear_term:
       os.system("cls" if os.name == "nt" else "clear")
   else:
       pass

def cord_input(string): # converts a user input to a list of cords
    user_input_pos = input(string)
    pos_string = user_input_pos.split(",")
    pos = list(map(int, pos_string))
    return pos

def get_current_color(move_number): # takes the number of moves that have been made and determines what color is sposed to mve
    if move_number % 2 == 0:
        return 2
    else:
        return 1

def move_check(current_color, start, end): # checks the legality of a move and returns an error message if illegal
    is_valid_move = game.move_piece(start_pos=start, end_pos=end, current_color=current_color)
    messages = {
        1: "Illegal move",
        2: "must move out of check",
        3: "checkmate",
        4: "stalemate"
    }
    return messages.get(is_valid_move, True)


clear()
mode = int(input("| test functions: 1 | start game with display: 2 |\n"))
move_number = 1
current_color = 1
error_message = False

while mode == 1:
    game.print_board(color=current_color)
    print(f"current color = {current_color}")
    if error_message == "checkmate":
        print("checkmate: you win!")
        break
    elif error_message == "stalemate":
        game.print_board(current_color)
        print("stalemate: draw!")
        break
    elif error_message != False:
        print(f"error: {move_check_data}")
        error_message = False
    s = "| move piece: 1 | delete piece: 2 | add piece: 3 | change color: 4 | get info: 5| setup board: 6 | clear board: 7 | print gird: 8 | board: 9| toggle clear: 10\n"
    test_mode = int(input(s))

    if test_mode == 1:
        start = cord_input("select piece in x,y format: ")
        end = cord_input("select square in x,y format: ")
        move_check_data = move_check(current_color, start, end)
        if move_check_data == True:
            move_number += 1
            error_message = False
        else:
            error_message = move_check_data

    elif test_mode == 2:
        pos = cord_input(string="enter x,y to delete piece: ")
        game.remove_piece(pos)

    elif test_mode == 3:
        data = cord_input(string="enter piece and color number in piece,color format: ")
        pos = cord_input(string="select square in x,y format: ")
        game.add_piece(type=data[0], color=data[1], pos=pos)

    elif test_mode == 4:
        if current_color == 1:
            current_color = 2
        else:
            current_color = 1

    elif test_mode == 5:
        pos = cord_input(string="select square in x,y format: ")
        piece_data = game.get_piece_data(pos=pos)
        print(f"icon = {piece_data[0]}, piece number = {piece_data[1]}, piece color = {piece_data[2]}, piece moves = {piece_data[3]}")
        input("press enter to continue")

    elif test_mode == 6:
        game.board_setup()

    elif test_mode == 7:
        game.clear_grid()

    elif test_mode == 8:
        print(game.grid)
        input("press enter to continue")

    elif test_mode == 9:
        clear()
        game.print_board()
        print("| 1: castle | 2: rook | 3: check | 4: check2 | 5: checkmate1 |")
        board_state = int(input("enter which board state to pick: "))
        if board_state == 1:
            game.grid = copy.deepcopy(demo1)
        elif board_state == 2:
            game.grid = copy.deepcopy(demo2)
        elif board_state == 3:
            game.grid = copy.deepcopy(demo3)
        elif board_state == 4:
            game.grid = copy.deepcopy(demo4)
        elif board_state == 5:
            game.grid = copy.deepcopy(demo5)

    elif test_mode == 10:
        clear_term = not clear_term
        game.clear_term = clear_term

    else:
        print("Bye!")
        break

if mode == 2:

    # declaring varibals
    colors = [(240, 217, 181), (181, 136, 99)] # colors of the two squares
    tile_size = 100
    clock = pygame.time.Clock()  # i need 60 fps,

    def chess_move(screen, start, end):

        global move_number, current_color, error_message, move_check_data
        current_color = get_current_color(move_number)

        move_check_data = move_check(current_color, start, end)
        if move_check_data == True:
            move_number += 1; game.print_board()
        elif move_check_data == "checkmate":
            game.print_board(); print("checkmate")
            winner_screen(screen, current_color)
        elif move_check_data == "stalemate":
            game.print_board(); print("stalemate")
        else:
            error_message = move_check_data

        if error_message != False: print(f"error: {move_check_data}") # tells you why your previos move was illegal if needed
        print(f"current color is {current_color}")


    def chess_screen(screen):
        screen.fill((255, 255, 255))

        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                )

                grid_x = col + 1; grid_y = 8 - row  # have to add one because of zero indexing
                piece = game.get_piece_data([grid_x, grid_y])

                if piece[1] != 0:
                    image = piece_images.get((piece[0].lower(), piece[2]))
                    screen.blit(image, (col * tile_size, row * tile_size))

    def winner_screen(screen, color):
        global move_number, current_color, error_message, move_check_data

        color_str = "white" if color == 1 else "black"
        message = f"{color_str} wins!"
        font = pygame.font.SysFont(None, 100)
        text = font.render(message, True, (0, 0, 0))
        rect = text.get_rect(center=(400, 400))
        screen.fill((181, 136, 99))
        screen.blit(text, rect)
        pygame.display.flip()

        end = True
        time.sleep(1.5)
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.board_setup()
                    move_number = 1
                    current_color = 1
                    error_message = False
                    end = False

    def display_loop():
        # pygame.init()
        screen = pygame.display.set_mode([800, 800])
        running = True
        start_square = []
        end_square = []

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    x = (mouse_x // 100) + 1
                    y = 8 - (mouse_y // 100)

                    if len(start_square) == 0: # if the list is empty
                        start_square.append(x); start_square.append(y)
                        print(f"selected {start_square}")
                    elif start_square[0] == x and start_square[1] == y:
                        start_square = []
                        print("canceled move")
                    else:
                        end_square.append(x); end_square.append(y)
                        print(f"{start_square} to {end_square}")
                        chess_move(screen, start_square, end_square)
                        start_square = []; end_square = []

            chess_screen(screen)
            pygame.display.flip()
            clock.tick(40)

        pygame.quit()

    game.print_board()
    display_loop()
