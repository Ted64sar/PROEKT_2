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
        self.plants = [[] * columns for _ in range(rows)]
        self.image = load_image('POLE_IGRY.png')
        # значения по умолчанию
        self.plant1 = load_image('CRAZY_CUCUMBER.png')
        self.plant2 = load_image('KAKTUS.png')
        self.plant3 = load_image('PEASHOOT.png')
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    board.render()
    if clock == 0:
        zo1 = True
        z1 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby1.png')
    elif clock == 150:
        zo2 = True
        z2 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby2.png')
    elif clock == 300:
        zo3 = True
        z3 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby3.png')
    elif clock == 450:
        zo4 = True
        z4 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby4.png')
    elif clock == 600:
        zo5 = True
        z5 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby5.png')
    elif clock == 750:
        zo6 = True
        z6 = Zomb(800, random.randint(1, 6) * 80 + 20, 'zomby6.png')
    if z1.rect.x > 0 and zo1:
        screen.blit(z1.image, z1.rect)
        pygame.display.update()
        z1.rect.x -= 2
    if z2.rect.x > 0 and zo2:
        screen.blit(z2.image, z2.rect)
        pygame.display.update()
        z2.rect.x -= 2
    if z3.rect.x > 0 and zo3:
        screen.blit(z3.image, z3.rect)
        pygame.display.update()
        z3.rect.x -= 2
    if z4.rect.x > 0 and zo4:
        screen.blit(z4.image, z4.rect)
        pygame.display.update()
        z4.rect.x -= 2
    if z5.rect.x > 0 and zo5:
        screen.blit(z5.image, z5.rect)
        pygame.display.update()
        z5.rect.x -= 2
    if z6.rect.x > 0 and zo6:
        screen.blit(z6.image, z6.rect)
        pygame.display.update()
        z6.rect.x -= 2
    pygame.time.delay(10)
    clock += 1

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()







