# Author: Timur Bagirov
# Date: 19 September 2022
# Идеальный исполнитель


def main():
    a, b = 0, 0
    try:
        a, b = int(input()), int(input())
    except ValueError:
        exit(1)

    while a != b:
        if (a // 2 >= b) and (a % 2 == 0):
            print(":2")
            a //= 2
        else:
            print("-1")
            a -= 1


if __name__ == "__main__":
    main()
