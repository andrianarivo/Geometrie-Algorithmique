from point import Point
from typing import List


#
# return
# 0 --> p1, p2 and p3 are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
#
def ccw(p1: Point, p2: Point, p3: Point) -> float:
    to = (p2.y - p1.y) * (p3.x - p2.x) - (p3.y - p2.y) * (p2.x - p1.x)
    if to == 0:
        return 0
    elif to > 0:
        return 1
    else:
        return 2


#
# if p3  is on segment p1 and p2
#
def seg(p1: Point, p2: Point, p3: Point) -> bool:
    return max(p1.x, p2.x) >= p3.x >= min(p1.x, p2.x) and max(p1.y, p2.y) >= p3.y >= min(p1.y, p2.y)


def jarvis(points: List[Point]) -> List[Point]:
    n = len(points)
    stack = []

    if n < 4:
        return points

    l = 0
    p = 0
    q = 0

    for i in range(0, n):
        if points[i].x < points[l].x:
            l = i

    p = l

    while True:
        stack.append(points[p])
        q = (p + 1) % n

        for i in range(0, n):
            if ccw(points[p], points[i], points[q]) == 2:
                q = i

        for i in range(0, n):
            if i != p and i != q and ccw(points[p], points[i], points[q]) == 0 and seg(points[p], points[q], points[i]):
                stack.append(points[i])

        p = q

        if p == l:
            break

    return stack


points = [[1, 2], [2, 2], [4, 2]]
trees = [Point.fromlist(point) for point in points]
fence = jarvis(trees)
l = [point.tolist() for point in fence]
print(l)
