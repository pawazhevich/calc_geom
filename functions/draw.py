import pygame
from other import color as clr


def draw_line(screen, p1, p2):
    pygame.draw.line(screen, clr.RED, p1.get_coords(), p2.get_coords(), 4)


def draw_pset(screen, set):
    arr = set.copy()
    arr.append(set[0])
    for i in range(len(arr)-2):
        draw_line(screen, arr[i], arr[i+1])


def draw_ps(screen, points):
    arr = points.copy()
    for i in range(len(arr)):
        arr[i].draw(screen)
