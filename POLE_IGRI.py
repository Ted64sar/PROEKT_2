import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size
        if x < self.width and y < self.height:
            return y, x
        else:
            return 0, 0

    def render(self):
        for i in range(self.height):
            for j in range(self.width):

    def on_click(self, cell_coords):
        z = self.board[cell_coords[0]][cell_coords[1]]
        z = z % 2
        self.board[cell_coords[0]][cell_coords[1]] = z

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

class Garden:
    def __init__(self, zombiez, plants):
        self.width = 12
        self.rows = 6



