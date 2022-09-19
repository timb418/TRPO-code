# Author: Timur Bagirov
# Date: 15 September 2022
# Две шашки

def main():
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

    if y2 <= y1 or (x1 + y1) % 2 != (x2 + y2) % 2:
        print('NO')
    else:
        if x1 - (y2 - y1) <= x2 <= x1 + (y2 - y1):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main()
