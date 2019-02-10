import pygame
import os

pygame.init()
size = width, height = 1000, 580
screen = pygame.display.set_mode(size)

Board = []

class line:
    def __init__(self, zombiez):
        Board[self.line].append(zombiez)
        return Board


class Pole:
    # создание поля
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.board = [[0] * columns for _ in range(rows)]
        self.image = load_image('POLE_IGRY.png')
        # значения по умолчанию
        self.x = 100
        self.y = 50
        self.cell_size = 80

    def render(self):
        image1 = pygame.transform.scale(self.image, (1000, 580))
        screen.blit(image1, (0, 0))





def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image
board = Pole(10, 6)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()







