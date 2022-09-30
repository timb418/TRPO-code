# Author: Timur Bagirov
# Date: 28 September 2022
# Алгоритм Евклида
import sys


def main():
    a: int = 0
    b: int = 0

    try:
        a = int(input())
        b = int(input())
    except ValueError:
        sys.exit(1)

    print(gcd(a, b))


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


if __name__ == "__main__":
    main()
