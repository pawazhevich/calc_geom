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

    point_amount = 50
    points = creators.get_parr(point_amount)
    for i in range(point_amount):
        points[i].draw(screen)

    run = True
    while run:
        screen.fill(clr.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(50)
        for i in range(point_amount):
            points[i].move()
            points[i].draw(screen)
        CH = relative.alg_darvisa(points)
        pair_index = relative.diameter(CH)
        pair = [CH[pair_index[0]], CH[pair_index[1]]]

        dr.draw_pset(screen, CH)
        dr.draw_pset(screen, [pair[0], pair[1]], clr.YELLOW)

        if relative.length(pair[0].get_coords(), pair[1].get_coords()) > 200:
            pair[0].set_speed(-pair[0].get_speed()[0], -pair[0].get_speed()[1])
            pair[1].set_speed(-pair[0].get_speed()[0], -pair[0].get_speed()[1])

        pygame.display.flip()


def main6():
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
        clock.tick(100)
        for i in points:
            i.move()
            i.draw(screen, clr.YELLOW, 10)

        CH = relative.quick_hall(points)
        dr.draw_pset(screen, CH)
        perimetr = clc.calc_perimetr(CH)
        print(perimetr)
        if perimetr > 1000:
            for i in CH:
                i.set_speed(-i.get_speed()[1], i.get_speed()[0])

        pygame.display.flip()


def main7():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()
    points = []
    CH = []

    run = True
    while run:
        screen.fill(clr.WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                p = point.Point(pos[0], pos[1])
                points.append(p)
                relative.dynamic_hull(CH, p)
        for p in points:
            p.draw(screen)

        if CH:
            dr.draw_pset(screen, CH)
            CH[0].draw(screen, clr.GREEN)

        pygame.display.flip()


def main8():
    screen = pygame.display.set_mode([800, 800])
    polygon = [[200, 200], [400, 200], [350, 300], [290, 350], [200, 350]]
    line1 = [[90, 400], [300, 110]] #segment
    line2 = [[305, 100], [305, 345]]
    line3 = [[100, 150], [300, 150]] #no intersection
    line4 = [[300, 200], [250, 200]] #paraller & intersect
    line5 = [[350, 300], [370, 340]]
    line6 = [[250, 210], [400, 300]]
    line7 = [[200, 100], [200, 400]]
    line8 = [[360, 200], [367, 150]] #one point
    line9 = [[500, 150], [100, 350]]
    line10 = [[250, 300], [295, 307]]
    segments = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()
    cut_segm = []

    dr.draw_pset(screen, polygon, clr.BLACK)
    for i in range(len(segments)):
        segm = relative.cut_segment(polygon, segments[i])
        cut_segm.append(segm)
        dr.draw_line(screen, segments[i][0], segments[i][1], clr.GREEN)
        dr.draw_line(screen, segm[0], segm[1], clr.RED)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(30)
        pygame.display.flip()

    pygame.quit()


def main10():
    screen = pygame.display.set_mode([800, 800])
    screen.fill(clr.WHITE)
    pygame.display.set_caption('Geometry')
    clock = pygame.time.Clock()

    p = []
    points = []
    i = 0
    point_amount = 25
    while i < point_amount:
        p.append([random.randint(100, 700), random.randint(100, 700)])
        i = i + 1
    i = 0
    while i < point_amount:
        points.append(point.Point(p[i][0], p[i][1], 0, 0))
        i = i + 1
    pair = []
    distance, pair = relative.get_near_pair(p, pair)
    print(distance)
    print(relative.length(pair[0], pair[1]))
    a = point.Point(pair[0][0], pair[0][1], 0, 0)
    b = point.Point(pair[1][0], pair[1][1], 0, 0)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(clr.WHITE)
        clock.tick(30)

        for i in range(len(points)):
            points[i].draw(screen, clr.GREEN, 5)
        a.draw(screen, clr.RED)
        b.draw(screen, clr.RED)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main10()
