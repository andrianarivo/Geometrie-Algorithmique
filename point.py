from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def fromlist(point: List[int]):
        return Point(point[0], point[1])

    def tolist(self) -> List[int]:
        return [self.x, self.y]

    def __eq__(self, value) -> bool:
        return (self.x == value.x) and (self.y == value.y)

    def __hash__(self) -> int:
        return self.x + self.y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)