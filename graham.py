from typing import List
from point import Point


#
# return
# 0 --> p1, p2 and p3 are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
#
def orient(p1: Point, p2: Point, p3: Point) -> float:
    to = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)
    if to == 0:
        return 0
    elif to > 0:
        return 1
    else:
        return 2


#
#
def ccw(a: Point, b: Point, c: Point) -> bool:
    return ((b.x - a.x) * (c.y - a.y)) > ((b.y - a.y) * (c.x - a.x))


#
#   TODO: finish the graham scan algorithm.
#   PS: reference in C++ lang: https://ttzztt.gitbooks.io/lc/content/jingchiai/erect-the-fence.html
#
def graham(points: List[Point]) -> List[Point]:
    n = len(points)
    if n < 4:
        return points

    # find the bottom most point
    ymin = points[0].y
    min = 0
    for point in points:
        y = point.y
        if y < ymin or (ymin == y and point.x < points[min].x):
            ymin = point.y
            min = points.index(point)

    # place the bottom most point at the first position
    temp = points[0]
    points[0] = points[min]
    points[min] = temp

    # Sort n-1 points with respect to the first point.
    # A point p1 comes before p2 in sorted output
    # if p2 has larger polar angle (in counterclockwise direction) than p1
    # In the tied case, the one has smaller distance from p0 comes first
    p0 = points[0]

    stack = []

    p = 0
    s = len(stack)
    copy = stack.copy()
    while True:
        q = (p + 1) % s
        for point in points:
            if (q != 0) and (orient(stack[p], point, stack[q]) == 0) and (seg(stack[p], stack[q], point)) and (
                    point not in copy):
                copy.append(point)
        p = q
        if p == 0:
            break

    return copy
