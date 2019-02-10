import pygame

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
        # значения по умолчанию
        self.x = 100
        self.y = 50
        self.cell_size = 80

    def render(self):
        for i in range(self.rows):
            for j in range(self.columns):
                pygame.draw.rect(screen, (255, 255, 255),
                                 [self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size], 1)





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







