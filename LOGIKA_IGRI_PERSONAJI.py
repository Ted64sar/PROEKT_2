import pygame
import os


class Pole:
    # создание поля
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.plants = [[] * columns for _ in range(rows)]
        self.image = load_image('POLE_IGRY.png')
        # значения по умолчанию
        self.x = 100
        self.y = 50
        self.cell_size = 80

    def render(self):
        image1 = pygame.transform.scale(self.image, (1000, 580))
        screen.blit(image1, (50, 0))

class Zomb(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        filename = os.path.join('data', name)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


class Explosion(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(all_sprites)
        filename = os.path.join('data', image)
        self.image = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, damage, x, y):
        super().__init__(all_sprites)
        self.damage = damage
        filename = os.path.join('data', image)
        self.image = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y


class Plant(pygame.sprite.Sprite):
    def __init__(self, sheet, type, pos):
        super().__init__(all_sprites)
        columns, rows, x, y = 8, 2, 0, 0
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
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

        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
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


pygame.init()
size = width, height = 1050, 660
screen = pygame.display.set_mode(size)
clock = 0
clockT = pygame.time.Clock();
board = Pole(10, 6)
all_sprites = pygame.sprite.Group()
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
