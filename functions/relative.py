import math


def determinant(p1, p2, p):
    return (p2[0] - p1[0])*(p[1] - p1[1]) - (p2[1] - p1[1])*(p[0] - p1[0])


def get_vector(p1, p2):
    v = []
    for i in range(len(p1)):
        v.append(p2[i]-p1[i])
    return v


def scalar_product(v1, v2):
    product = 0
    for i in range(len(v1)):
        product += v1[i]*v2[i]

    return product


def vector_product(v1, v2):
    return v1[0]*v2[1]-v1[1]*v2[0]


def cos(v1, v2):
    sp = scalar_product
    product = sp(v1, v2)
    len1 = math.sqrt(sp(v1, v1))
    len2 = math.sqrt(sp(v2, v2))
    return product / (len1*len2)


def get_min_point(points):
    min = points[0]
    for i in range(len(points)):
            if min.get_coords()[1] < points[i].get_coords()[1]:
                min = points[i]
            elif min.get_coords()[1] == points[i].get_coords()[1]:
                if min.get_coords()[0] > points[i].get_coords()[0]:
                    min = points[i]
    return min


def check_point_position(p1, p2, p):
    d = determinant(p1, p2, p)
    if d == 0:
        return 0
    else:
        if d > 0:
            return 1
        else:
            return -1


def is_intersect(p1, p2, p3, p4):
    d1 = determinant(p1, p2, p3)
    d2 = determinant(p1, p2, p4)
    d3 = determinant(p3, p4, p1)
    d4 = determinant(p3, p4, p2)
    if d1*d2 < 0 and d3*d4 < 0:
        return True
    elif d1*d2 == 0 or d3*d4 == 0:
        sp = scalar_product
        gv = get_vector
        k1 = sp(gv(p3, p1), gv(p3, p2))
        k2 = sp(gv(p4, p1), gv(p4, p2))
        k3 = sp(gv(p1, p3), gv(p1, p4))
        k4 = sp(gv(p2, p3), gv(p2, p4))
        if k1 <= 0 or k2 <= 0 or k3 <= 0 or k4 <= 0:
            return True
        else:
            return False
    else:
        return False


def is_polygon_simple(plg):
    points = plg.get_coords()
    points.append(points[0])
    """loop for first edge"""
    """1 2 3 4 5 1"""
    for i in range(len(points)-4):
        if is_intersect(points[0], points[1], points[i+2], points[i+3]):
            return False

    for i in range(1, len(points)-3):
        for j in range(i, len(points)-3):
            if is_intersect(points[i], points[i+1], points[j+2], points[j+3]):
                return False

    return True


def is_polygon_convex(plg):
    if is_polygon_simple(plg):
        points = plg.get_coords()
        points.append(points[0])
        points.append(points[1])
        position = check_point_position(points[0], points[1], points[2])
        for i in range(len(points)-2):
            cur_position = check_point_position(points[i], points[i+1], points[i+2])
            if cur_position != position:
                return False
        return True
    else:
        return False


def dimensional_test(polygon, point):
    points = polygon.get_coords()
    xmin = xmax = points[0][0]
    ymin = ymax = points[0][1]
    for pt in points:
        if xmin > pt[0]:
            xmin = pt[0]
        if xmax < pt[0]:
            xmax = pt[0]
        if ymin > pt[1]:
            ymin = pt[1]
        if ymax < pt[1]:
            ymax = pt[1]
    if point[0] > xmax or point[0] < xmin or point[1] < ymin or point[1] > ymax:
        return False
    else:
        return True


def oct(v):
    x = v[0]
    y = v[1]
    if 0 <= y < x:
        return 1
    if 0 < x <= y:
        return 2
    if 0 <= -x < y:
        return 3
    if 0 < y <= -x:
        return 4
    if 0 <= -y < -x:
        return 5
    if 0 < -x <= -y:
        return 6
    if 0 <= x < -y:
        return 7
    if 0 < -y <= x:
        return 8
    return 0


def octane_test(polygon, p0):
    if not dimensional_test(polygon, p0):
        return False
    p = polygon.get_coords()
    if dimensional_test(polygon, p0) is False:
        return False
    p_tmp = p.copy()
    p_tmp.append(p[0])
    delta = [0 for _ in range(len(p_tmp))]
    big_delta = [0 for _ in range(len(p_tmp))]
    for i in range(len(p)):
        v1 = [x1 - x2 for x1, x2 in zip(p_tmp[i], p0)]
        v2 = [x1 - x2 for x1, x2 in zip(p_tmp[i + 1], p0)]

        delta[i] = oct(v1)
        delta[i + 1] = oct(v2)
        big_delta[i] = delta[i + 1] - delta[i]
        if big_delta[i] > 4:
            big_delta[i] = big_delta[i] - 8
        elif big_delta[i] < -4:
            big_delta[i] = big_delta[i] + 8
        elif big_delta[i] == 4 or big_delta[i] == -4:
            d = determinant(p_tmp[i], p_tmp[i + 1], p0)
            if d < 0:
                big_delta[i] = -4
            elif d > 0:
                big_delta[i] = 4
            else:
                return "On the line"
    s = 0
    for i in range(len(p)):
        s = s + big_delta[i]
    if s == 8 or s == -8:
        return True
    elif s == 0:
        return False
    else:
        print("Mistake")


def length(p1, p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))


def angle2(p1, p0, p2):
    ca = (p1[0] - p0[0]) * (p2[0] - p0[0]) + (p1[1] - p0[1]) * (p2[1] - p0[1])
    ca = ca / (length(p1, p0) * length(p2, p0))
    if ca > 1 or ca < -1:
        ca = round(ca)
    ca = math.acos(ca)
    if check_point_position(p0, p1, p2) > 0:
        ca = 2 * math.pi - ca
    return ca


def convex_point_relative(polygon, p0):
    p = polygon.get_coords()
    start = 0
    end = len(p)
    p.append(p[-1])
    while end - start > 1:
        sep = (start + end) // 2
        if check_point_position(p[0], p[1], p0) != check_point_position(p[-1], p[0], p0):
            return False
        if check_point_position(p[0], p[sep], p0) == check_point_position(p[0], p[sep], p[1]):
            end = sep
        else:
            start = sep
    return not is_intersect(p0, p[0], p[start], p[end])


def sort_points_cos(points, min_point):
    pv = [1, 0]
    gv = get_vector
    arr = points.copy()

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            v1 = gv(min_point.get_coords(), arr[j].get_coords())
            v2 = gv(min_point.get_coords(), arr[j+1].get_coords())
            if cos(pv, v1) < cos(pv, v2):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def max_remote_point(p1, p2, points):
    v1 = get_vector(p1.get_coords(), p2.get_coords())
    mrp = points[0]
    v2 = get_vector(p1.get_coords(), mrp.get_coords())
    mvp = vector_product(v1, v2)
    for i in points:
        v2 = get_vector(p1.get_coords(), i.get_coords())
        cvp = vector_product(v1, v2)
        if cvp > mvp:
            mvp = cvp
            mrp = i

    return mrp



def alg_darvisa(points):
    min_point = get_min_point(points)
    CH = [min_point]
    arr = points.copy()
    p_mc = 1

    while p_mc != []:
        max_cos = -1
        p_mc = []
        p0 = CH[-1].get_coords()
        for i in range(len(arr)):
            v1 = get_vector(p0, [p0[0]+5, p0[1]])
            v2 = get_vector(p0, arr[i].get_coords())
            if check_point_position(p0, [p0[0]+5, p0[1]], arr[i].get_coords()) == -1:
                cs = cos(v1, v2)
                if cs >= max_cos:
                    max_cos = cs
                    p_mc = arr[i]
        if p_mc:
            CH.append(p_mc)

    p_mc = 1
    while p_mc != []:
        max_cos = -1
        p_mc = []
        p0 = CH[-1].get_coords()
        for i in range(len(arr)):
            v1 = get_vector(p0, [p0[0]-5, p0[1]])
            v2 = get_vector(p0, arr[i].get_coords())
            if check_point_position(p0, [p0[0] - 5, p0[1]], arr[i].get_coords()) == -1:
                cs = cos(v1, v2)
                if cs >= max_cos:
                    max_cos = cs
                    p_mc = arr[i]
        if p_mc:
            CH.append(p_mc)

    return CH


def max_remote_points(points):
    max_len = 0
    pair = []
    l = len(points)
    for i in range(l - 1):
        for j in range(i+1, l):
            cur_len = length(points[i].get_coords(),points[j].get_coords())
            if cur_len >= max_len:
                max_len = cur_len
                pair = [points[i], points[j]]
    return pair


def left_point(points):
    l = len(points)
    lp = points[0]
    for i in range(l):
        if points[i].get_coords()[0] < lp.get_coords()[0]:
            lp = points[i]
    return lp


def right_point(points):
    l = len(points)
    rp = points[0]
    for i in range(l):
        if points[i].get_coords()[0] > rp.get_coords()[0]:
            rp = points[i]
    return rp


def quick_hall(points):
    sp = []
    sl = []
    CH = []
    left = left_point(points)
    right = right_point(points)
    for i in points:
        if check_point_position(left.get_coords(), right.get_coords(), i.get_coords()) == -1:
            sl.append(i)
        else:
            if check_point_position(left.get_coords(), right.get_coords(), i.get_coords()) == 1:
                sp.append(i)
    CH.append(left)
    CH.append(right)
    iter_hall(sl, left, right, CH)
    iter_hall(sp, right, left, CH)
    CH.append(left)
    return CH


def iter_hall(points, left, right, CH):
    sl = []
    for i in points:
        if check_point_position(left.get_coords(), right.get_coords(), i.get_coords()) == -1:
            sl.append(i)
    if sl:
        lrp = max_remote_point(right, left, sl)

        CH.insert(CH.index(left)+1, lrp)
        iter_hall(sl, left, lrp, CH)
        iter_hall(sl, lrp, right, CH)


def dynamic_hull(CH, point):

    if len(CH) == 0:
        CH.append(point)
        return

    elif len(CH) == 1:
        if not CH[0].__eq__(point):
            CH.append(point)
        return

    elif len(CH) == 2:
        if not CH[0].__eq__(point) and not CH[1].__eq__(point):
            p1 = CH[0].get_coords()
            p2 = CH[1].get_coords()
            p = point.get_coords()
            if check_point_position(p1, p2, p) != 0:
                if check_point_position(p1, p2, p) == 1:
                    CH.insert(1, point)
                else:
                    CH.append(point)
                return
            else:
                if scalar_product(get_vector(p, p1), get_vector(p, p2)) < 0:
                    return
                if scalar_product(get_vector(p1, p), get_vector(p1, p2)) < 0:
                    CH[0] = point
                    return
                if scalar_product(get_vector(p2, p), get_vector(p2, p1)) < 0:
                    CH[1] = point
                    return
    else:
        new = []
        CH.append(CH[0])
        flag = -1
        for i in range(len(CH)-1):
            p1 = CH[i].get_coords()
            p2 = CH[i+1].get_coords()
            p = point.get_coords()
            if check_point_position(p1, p2, p) == 1:
                if point not in new:
                    new.append(CH[i])
                    new.append(point)
                else:
                    if flag == 1:
                        if new[-1] != point:
                            del new[-1]
                            new.append(CH[i])
                    else:
                        new.append(CH[i])
                flag = 1
            else:
                flag = -1
                new.append(CH[i])

        if flag == 1 and check_point_position(CH[0].get_coords(), CH[1].get_coords(), point.get_coords()) == 1:
            del new[0]

        CH.clear()
        CH.extend(new)

