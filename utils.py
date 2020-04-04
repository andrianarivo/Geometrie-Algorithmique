from point import Point


def cmp(a, b):
    return (a > b) - (a < b)


#
# if p3  is on segment p1 and p2
#
def seg(p1: Point, p2: Point, p3: Point) -> bool:
    return max(p1.x, p2.x) >= p3.x >= min(p1.x, p2.x) and max(p1.y, p2.y) >= p3.y >= min(p1.y, p2.y)