# Author: Timur Bagirov
# Date: 13 September 2022
# Простое уравнение


def main():
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    if a == c and b == d:
        print("NO")
    elif a == 0 and b == 0:
        print("INF")
    elif b % a == 0:
        x = -b / a
        print(x)
    else:
        print('NO')


if __name__ == "__main__":
    main()
