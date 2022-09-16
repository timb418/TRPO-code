# Author: Timur Bagirov
# Date: 13 September 2022
# Простое уравнение


def main():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())

    if a == 0 and b == 0:
        print('INF')
    elif a == 0 or b * c == a * d:
        print('NO')
    elif b % a == 0:
        x = -b // a
        print(x)
    else:
        print('NO')


if __name__ == "__main__":
    main()
