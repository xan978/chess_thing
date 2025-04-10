import pygame, time
class Display:
    def __init__(self):
        self.piece_image = {
            1: "insert here"
            }
    def chess_screen(self, screen):
        screen.fill((255, 255, 255))
        colors = [(240, 217, 181), (181, 136, 99)]
        tile_size = 100

        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                )


    def load_board(self, grid):
        pygame.init()
        screen = pygame.display.set_mode([800, 800])
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    x = (mouse_x // 100) + 1
                    y = 8 - (mouse_y // 100)
                    print(f"you clicked on {x}, {y}")

            self.chess_screen(screen)
            pygame.display.flip()
            time.sleep(0.0084)

        pygame.quit()
