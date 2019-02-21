import pygame
import os
import random


class Pole:
    # создание поля
    def __init__(self, columns, rows):
        self.ChPlant = None
        self.columns = columns
        self.rows = rows
        '''
        1 - тип
        атаки(0 - стрельба, 1 - подрыв)
        2 - перезарядка
        3 - запас
        атаки(растение
        уничтожается
        если
        израсходован)
        4 - изменение
        картинки
        после
        атаки(True
        или
        False)
        5 - урон
        6 - здоровье
        7 - цена
        '''
        self.Pl = [[1, 1, 1, True, 1000, 100, 55, load_image('G_BOOM.png')],
                   [0, 1, 10000, True, 75, 250, 150, load_image('SPIKES.png')],
                   [0, 1, 10000, True, 50, 100, 100, load_image('PEA.png')],
                   [0, 1, 10000, True, 125, 100, 175, load_image('POWER_PEA.png')]]
        self.plants = [[None] * columns for _ in range(rows)]
        self.image = load_image('POLE_IGRY.png')
        self.plant1 = load_image('CRAZY_CUCUMBER_I.png')
        self.plant2 = load_image('KAKTUS_I.png')
        self.plant3 = load_image('PEASHOOT_I.png')
        self.plant4 = load_image('POWER_PEASHOOT_I.png')
        self.x = 100
        self.y = 50
        self.cell_size = 80
        self.suns = 3000


    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if 950 > x > 150 and 530 > y > 50:
            x = (x - 150) // 80
            y = (y - 50) // 80
            return (y, x)
        elif y > 580 and 470 > x > 150:
            x = (x - 150) // 80
            return 'plant'+str(x)
        else:
            return None


    def on_click(self, cell_coords):
        if cell_coords == None:
            self.ChPlant = None
        elif 'plant' in cell_coords:
            self.ChPlant = int(cell_coords[-1])
            print(self.ChPlant)
        else:
            plants = [load_image('CRAZY_CUCUMBER.png'), load_image('KAKTUS.png'), load_image('PEASHOOT.png'), load_image('POWER_PEASHOOT.png')]
            if self.ChPlant != None:
                Pl = Plant(plants[self.ChPlant], self.Pl[self.ChPlant], cell_coords)
                if Pl.price <= self.suns:
                    self.plants[cell_coords[0]][cell_coords[1]] = Pl
                    self.suns -= self.plants[cell_coords[0]][cell_coords[1]].price
                self.ChPlant = None

        print(cell_coords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def render(self):
        screen.blit(self.plant1, (150, 580))
        screen.blit(self.plant2, (230, 580))
        screen.blit(self.plant3, (310, 580))
        screen.blit(self.plant4, (390, 580))

        #image1 = pygame.transform.scale(self.image, (1000, 580))
        #screen.blit(image1, (100, 0))
        '''
        for i in range(6):
            for j in range(10):
                Rect = ((j * 80 + 150, i * 80 + 50), (80, 80))
                pygame.draw.rect(screen, (0, 255, 0), Rect, 1)
        '''


class Zomb(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self, zombys)
        filename = os.path.join('data', 'zomby'+str(name)+'.png')
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.go = True
        self.health = 750
    def update(self):
        if self.go:
            self.rect.x -= 2


class Explosion(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(all_sprites)
        filename = os.path.join('data', image)
        self.image = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y
        for z in zombies:
            if z.tile == self.x and z.line == self.y:
                n = zombies.index(z)
                del zombies[n]


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, damage, x, y):
        super().__init__(all_sprites)
        self.damage = damage
        filename = os.path.join('data', image)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.rect.move(self.x * 80 + 150, 50 + y * 80)


class Plant(pygame.sprite.Sprite):
    def __init__(self, sheet, type, pos):
        super().__init__(all_sprites)
        columns, rows = 8, 2

        self.frames = []
        self.cut_sheet(sheet, columns)
        self.cur_frame = 0
        self.line = pos[0]
        self.number = pos[1]
        self.attack = type[0]
        self.reload = type[1]
        self.at_c = type[2]
        self.pic_change = type[3]
        self.damage = type[4]
        self.health_max = type[5]
        self.price = type[6]
        self.attacking = False
        self.rect.x = self.number

        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(self.number * 80 + 150, 50 + self.line*80)

    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, 80, 80)
        if self.attacking:
            j = 1
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
        else:
            j = 2
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def check_attack(self):
        if self.attack == 0:
            if board.zombies != []:
                self.attacking = True
            else:
                self.attacking = False

    def attacking(self):
        if self.attacking == True:
            if self.attack == 0:
                Bullet()

    def update(self):
        if not(self.attacking):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        else:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return image

def sun():

    font = pygame.font.Font(None, 50)
    text = font.render(str(board.suns), 1, (255, 255, 0))
    text_x = 55
    text_y = 0
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
pygame.init()

zombys = pygame.sprite.Group()
size = width, height = 1050, 660
screen = pygame.display.set_mode(size)

f = open('level.txt', 'r')
zombies = f.read().split(',')
screen.fill((100, 255, 10))
clock = 0
clockT = pygame.time.Clock();
board = Pole(10, 6)
all_sprites = pygame.sprite.Group()
image1 = pygame.transform.scale(board.image, (1000, 580))
screen.blit(image1, (100, 0))
running = True
zombies = []

while pygame.event.wait().type != pygame.QUIT:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        for i in all_sprites:
            i.update()
        image1 = pygame.transform.scale(board.image, (1000, 580))
        screen.blit(image1, (50, 0))
        image1 = pygame.transform.scale(load_image('CARPET.png'), (50, 580))
        screen.blit(image1, (0, 0))
        #screen.fill((100, 255, 10))
        board.render()
        all_sprites.draw(screen)
        zombys.draw(screen)
        sun()

        pygame.display.flip()

        pygame.display.flip()
        board.render()
        if clock % 150 == 0:
           zo1 = True
           zombies.append(Zomb(1100, random.randint(1, 6) * 80 + 10, random.randint(1, 6)))
        for z in zombies:
            z.update()
        pygame.time.delay(50)
        clock += 1


pygame.quit()
