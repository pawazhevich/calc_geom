import pygame
import random
from other import color as clr
from entity import point
from calc import calculations as clc
from functions import draw as dr
from functions import relative
from functions import creators
from entity import polygon as plg

SIZE = 800


def main():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()

    out_polygon = plg.Polygon([[15, 300], [150, 150], [400, 45], [650, 150], [770, 400], [650, 650], [400, 770], [150, 650], [40, 500]])
    inn_polygon = plg.Polygon([[80, 350], [150, 450], [200, 480], [230, 450], [400, 500], [450, 500], [400, 400], [350,350]])
    points = creators.get_parr_in_polygon(out_polygon, 100)
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    run = True
    while run:

        screen.fill(clr.WHITE)
        clock.tick(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        act_len = len(points)
        for i in range(len(points)):
            points[i].move()
            points[i].draw(screen)
            if not relative.convex_point_relative(out_polygon, points[i].get_next_coords()):
                points[i].set_speed(-points[i].get_speed()[1], points[i].get_speed()[0])

            if relative.octane_test(inn_polygon, points[i].get_coords()) is True:
                points[i].set_speed(0, 0)
                points[i].draw(screen, clr.RED)

        out_polygon.draw(screen)
        inn_polygon.draw(screen)
        pygame.display.flip()


def main1():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()

    point_amount = 500
    points = creators.get_parr(point_amount)
    for i in range(point_amount):
        points[i].draw(screen)

    min_point = relative.get_min_point(points)
    min_point.draw(screen, clr.RED)

    del points[points.index(min_point)]
    sorted_arr = relative.sort_points_cos(points, min_point)
    CH = [min_point, sorted_arr[0]]
    run = True
    counter = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(clr.WHITE)
        clock.tick(20)

        dr.draw_ps(screen, points)
        min_point.draw(screen)
        dr.draw_pset(screen, CH)
        if counter < len(sorted_arr):
            while relative.check_point_position(CH[-1].get_coords(),
                                               CH[-2].get_coords(),
                                               sorted_arr[counter].get_coords()) <= 0:
               del CH[len(CH)-1]
            CH.append(sorted_arr[counter])
            counter += 1
        elif counter == len(sorted_arr):
            CH.append(min_point)
        pygame.display.flip()


def main5():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()

    point_amount = 10
    points = creators.get_parr(point_amount)
    for i in range(point_amount):
        points[i].draw(screen)

    run = True
    while run:
        screen.fill(clr.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(150)
        for i in range(point_amount):
            points[i].move()
            points[i].draw(screen)
        pair = relative.max_remote_points(points)[0], relative.max_remote_points(points)[1]
        CH = relative.alg_darvisa(points)

        dr.draw_pset(screen, CH)
        pair[0].draw(screen, clr.GREEN)
        pair[1].draw(screen, clr.GREEN)

        if relative.length(pair[0].get_coords(), pair[1].get_coords()) > 200:
            pair[0].set_speed(-pair[0].get_speed()[0], -pair[0].get_speed()[1])
            pair[1].set_speed(-pair[0].get_speed()[0], -pair[0].get_speed()[1])

        pygame.display.flip()


def main6():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()

    point_amount = 5
    points = creators.get_parr(point_amount)
    for i in range(point_amount):
        points[i].draw(screen)

    run = True
    while run:
        screen.fill(clr.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(200)
        for i in points:
            i.move()
            i.draw(screen)

        CH = relative.quick_hall(points)
        dr.draw_pset(screen, CH)

        if clc.calc_perimetr(CH) > 900:
            for i in CH:
                i.set_speed(-i.get_speed()[1], i.get_speed()[0])

        pygame.display.flip()


if __name__ == "__main__":
    main6()
