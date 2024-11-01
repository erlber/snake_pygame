import pygame
from slangeObj import Snake

if __name__ == "__main__":
    pygame.init()
    CELL_SIZE = 60
    CELL_NUMBER = 15
    WIDTH = CELL_SIZE * CELL_NUMBER
    HEIGHT = CELL_SIZE * CELL_NUMBER
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    fps = 60

    #farger
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def draw_line():
        for x in range(CELL_NUMBER):
            pygame.draw.line(screen, BLACK, (CELL_SIZE * x, 0), (CELL_SIZE * x, HEIGHT))
            pygame.draw.line(screen, BLACK, (0, CELL_SIZE * x), (WIDTH ,CELL_SIZE * x))

    def update():
        screen.fill(WHITE)
        draw_line()
        player.draw()
        player2.draw()
        pygame.display.update()

    run = True
    player = Snake(7, 7, CELL_SIZE, GREEN, screen)
    player2 = Snake(5, 5, CELL_SIZE, RED, screen)
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_d:
                    player.dir = "r"
                elif event.key == pygame.K_a:
                    player.dir = "l"
        update()