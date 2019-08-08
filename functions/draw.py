import pygame
from other import color as clr


def draw_line(screen, p1, p2, col=clr.RED):
    print(p1, p2)
    if p1 and p2:
        if p1 != p2:
            pygame.draw.line(screen, col, p1, p2, 4)
        else:
            pygame.draw.circle(screen, col, (int(p1[0]), int(p1[1])), 4)


def draw_pset(screen, set, col=clr.RED):
    arr = set.copy()
    arr.append(set[0])
    for i in range(len(arr)-1):
        draw_line(screen, arr[i], arr[i+1], col)


def draw_ps(screen, points):
    arr = points.copy()
    for i in range(len(arr)):
        arr[i].draw(screen)
