# Author: Timur Bagirov
# Date: 30 September 2022
# Принадлежит ли точка области?
import sys


def main():
    try:
        x = float(input())
        y = float(input())
    except ValueError:
        sys.exit(1)

    if isPointInArea(x, y):
        print("YES")
    else:
        print("NO")


def IsPointInsideCircle(x, y):
    xc = -1
    yc = 1
    r = 2

    return (x - xc) * (x - xc) + (y - yc) * (y - yc) < r * r


def IsPointInCircle(x, y):
    xc = -1
    yc = 1
    r = 2

    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r


def isPointInArea(x, y) -> bool:
    left_line_right = (x + y >= 0)
    right_line_left = (2 * x - y + 2 <= 0)
    left_line_left = (x + y <= 0)
    right_line_right = (2 * x - y + 2 >= 0)

    in_circ_area = IsPointInCircle(x, y) and left_line_right and right_line_left
    in_bottom = not IsPointInsideCircle(x, y) and left_line_left and right_line_right

    return in_circ_area or in_bottom


if __name__ == "__main__":
    main()
