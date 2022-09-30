# Author: Timur Bagirov
# Date: 30 September 2022
# Принадлежит ли точка квадрату?
import sys


def main():
    try:
        x = float(input())
        y = float(input())
    except ValueError:
        sys.exit(1)

    if IsPointInSquare(x, y):
        print("YES")
    else:
        print("NO")


def IsPointInSquare(x, y):
    b = False
    if -x - 1 <= y <= -x + 1 and x + 1 >= y >= x - 1:
        b = True
    return b


if __name__ == "__main__":
    main()
