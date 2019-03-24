import pygame
from other import color as clr


class Polygon:
    def __init__(self, points):
        self.points = points

    def draw(self, window):
        points = self.points.copy()
        points.append(points[0])
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 15)
        for i in range(len(points)-1):
            pygame.draw.line(window, clr.BLACK, points[i], points[i+1])
            txt = my_font.render("%d" % (i+1), False, clr.BLACK)
            window.blit(txt, (points[i][0], points[i][1]))

    def get_coords(self):
        return self.points.copy()
