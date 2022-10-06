# Author: Timur Bagirov
# Date: 01 October 2022
# Парты
import sys


def main():
    try:
        first_room = int(input())
        second_room = int(input())
        third_room = int(input())
    except ValueError:
        print("ERROR")
        sys.exit(1)

    print(first_room // 2 + second_room // 2 + third_room // 2 +
          first_room % 2 + second_room % 2 + third_room % 2)


if __name__ == "__main__":
    main()
