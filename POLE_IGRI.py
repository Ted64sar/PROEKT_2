import pygame

pygame.init()
size = width, height = 500, 500
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
        self.x = 10
        self.y = 10
        self.cell_size = 30

    def render(self):
        for i in range(self.rows):
            for j in range(self.columns):
                pygame.draw.rect(screen, (255, 255, 255),
                                 [self.x + j * self.cell_size, self.y + i * self.cell_size, self.cell_size, self.cell_size], 1)

    # настройка внешнего вида
    def set_view(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size




board = Pole(8, 2)
board.set_view(100, 100, 50)
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







