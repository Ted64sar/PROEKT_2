import pygame
import os


class Enimy(pygame.sprite.Sprite):
    def __init__(self, sheet, type, line):
        self.spd_mod = 1
        self.is_attaked = False
        self.attekers = []
        self.line = line
        columns, rows, x, y = 8, 2, 0, 0
        super().__init__(all_sprites)
        self.speed = type[0] * self.spd_mod
        self.healt_max = type[1]
        self.hp = self.healt_max
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.dead = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, 80, 80)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.hp <= 0:
            self.dead = True
            '''
            death_reason = attacer.attaktype
            self.death(death_reason)
            '''


class Plant(pygame.sprite.Sprite):
    def __init__(self, sheet, type, pos):
        super().__init__(all_sprites)
        columns, rows, x, y = 8, 2, 0, 0
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, 80, 80)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
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


all_sprites = pygame.sprite.Group()
