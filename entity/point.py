import math, pygame, random
from other import color as clr


class Point:
    def __init__(self, x=0, y=0, xv=1 , yv=1):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.clr = clr.BLACK

    def move(self):
        self.x = self.x+self.xv
        self.y = self.y + self.yv

    def draw(self, window, color=clr.BLACK, width = 4):
        pygame.draw.circle(window, color, (int(self.x), int(self.y)), width)

    def get_coords(self):
        return [self.x, self.y]

    def set_speed(self, xv, yv):
        self.xv = xv
        self.yv = yv

    def set_rand_speed(self):
        self.xv = random.randrange(-3, 3)
        self.yv = random.randrange(-3, 3)

    def get_speed(self):
        return [self.xv, self.yv]

    def set_color(self, color):
        self.clr = color

    def get_next_coords(self):
        return [self.x+self.xv, self.y+self.yv]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
