import random
from entity import polygon as plg
from entity import point
from functions import relative
RANGE = 400


def get_point():
    return point.Point(random.randint(200+50, RANGE+150), random.randint(200+50, RANGE+150), random.randrange(-3, 3), random.randrange(-3,3))


def get_parr(num):
    points = []
    for i in range(num):
        points.append(get_point())
    return points


def get_point_in_polygon(polygon):
    point = get_point()
    while relative.octane_test(polygon,point.get_coords()) is False:
        point = get_point()
    return point


def get_parr_in_polygon(polygon, num):
    arr = []
    for i in range(num):
        arr.append(get_point_in_polygon(polygon))
    return arr


def get_polygon(num):
    points = []
    for i in range(num):
        points.append([random.randint(0, RANGE), random.randint(0, RANGE)])
    polygon = plg.Polygon(points)

    return polygon


def get_simple_polygon(num):
    polygon = get_polygon(num)
    while not relative.is_polygon_simple(polygon):
        polygon = get_polygon(num)
    return polygon


def get_convex_polygon(num):
    polygon = get_simple_polygon(num)
    while not relative.is_polygon_convex(polygon):
        polygon = get_simple_polygon(num)
    return polygon
