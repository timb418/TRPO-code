# Author: Timur Bagirov
# Date: 30 September 2022
# Рекурсивное сложение
import sys


def main():
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        sys.exit(1)

    if a < 0 or b < 0:
        sys.exit(1)

    print(sumRecursive(a, b))


def sumRecursive(a, b):
    if a == 0:
        return b
    return sumRecursive(a - 1, b + 1)


if __name__ == "__main__":
    main()
