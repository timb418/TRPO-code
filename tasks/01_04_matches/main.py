# Author: Timur Bagirov
# Date: 14 September 2022
# Спички


class Match:

    @classmethod
    def from_coords(cls, coords):
        yield cls(coords[0:2])
        yield cls(coords[2:4])
        yield cls(coords[4:6])

    def __init__(self, endpoints):
        self.x1, self.x2 = sorted(endpoints)

    def __invert__(self):
        return self.x2 - self.x1

    def __xor__(m1, m2):
        return max(m1.x2, m2.x2) - min(m1.x1, m2.x1) - ~m1 - ~m2

    def __and__(m1, m2):
        return m1 ^ m2 <= 0


def solve(*coords):
    m1, m2, m3 = Match.from_coords(coords)
    if (m1 & m2) + (m1 & m3) + (m2 & m3) >= 2:
        return 0
    if ~m1 >= m2 ^ m3:
        return 1
    if ~m2 >= m1 ^ m3:
        return 2
    if ~m3 >= m1 ^ m2:
        return 3
    return -1


def main():
    l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), \
                             int(input()), int(input()), int(input())
    print(solve(l1, r1, l2, r2, l3, r3))


if __name__ == "__main__":
    main()
