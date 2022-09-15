# Author: Timur Bagirov
# Date: 14 September 2022
# Шахматный король


def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
