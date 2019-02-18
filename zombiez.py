import pygame
import os
import random

pygame.init()
size = width, height = 1050, 660
screen = pygame.display.set_mode(size)

Board = []

class line:
    def __init__(self, zombiez):
        Board[self.line].append(zombiez)
        return Board


class Pole:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.plants = [[] * columns for _ in range(rows)]
        self.image = load_image('POLE_IGRY.png')
        self.plant1 = load_image('cucumber.png')
        self.plant2 = load_image('kaktus1.png')
        self.plant3 = load_image('shoot.png')
        self.x = 100
        self.y = 50
        self.cell_size = 80


    def render(self):
        image1 = pygame.transform.scale(self.image, (1000, 580))
        screen.blit(image1, (50, 0))
        screen.blit(self.plant1, (150, 580))
        screen.blit(self.plant2, (250, 580))
        screen.blit(self.plant3, (350, 580))





def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image
board = Pole(10, 6)


class Zomb(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        filename = os.path.join('data', name)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


f = open('level.txt', 'r')
zombies = f.read().split(',')
z1 = z2 = z3 = z4 = z5 = z6 = Zomb(800, 100, 'zomby1.png')

zo1 = zo2 = zo3 = zo4 = zo5 = zo6= False
screen.fill((100, 255, 10))
clock = 0
clockT = pygame.time.Clock();
while pygame.event.wait().type != pygame.QUIT:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        board.render()
        if clock ==0:
           zo1 = True
           z1 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby1.png')
        elif clock ==150:
            zo2 = True
            z2 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby2.png')
        elif clock ==300:
            zo3 = True
            z3 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby3.png')
        elif clock ==450:
            zo4 = True
            z4 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby4.png')
        elif clock ==600:
            zo5 = True
            z5 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby5.png')
        elif clock ==750:
            zo6 = True
            z6 = Zomb(800, random.randint(1, 6) * 80 + 10, 'zomby6.png')
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
        clock +=1

pygame.quit()
