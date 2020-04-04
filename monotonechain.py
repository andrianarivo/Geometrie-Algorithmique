from typing import List
from point import Point
from functools import reduce


def cmp(a, b):
    return (a > b) - (a < b)


def sign(p: Point, q: Point, r: Point):
    return cmp((p.x - r.x) * (q.y - r.y), (p.y - r.y) * (q.x - r.x))


def drive(hull: List[Point], r: Point):
    hull.append(r)
    while len(hull) >= 3 and sign(*hull[-3:]) < 0:
        hull.pop(-2)
    return hull


class Solution:
    def monotone_chain(self, points: List[List[int]]) -> List[List[int]]:
        trees = [Point.fromlist(point) for point in points]
        trees.sort(key=lambda p: (p.x, p.y))
        lower = reduce(drive, trees, [])
        upper = reduce(drive, trees[::-1], [])
        l = list(set(lower + upper))
        return [point.tolist() for point in l]


s = Solution()
points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
print(s.monotone_chain(points))
