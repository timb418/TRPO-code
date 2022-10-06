# Author: Timur Bagirov
# Date: 01 October 2022
# Расписание звонков
import sys


def main():
    try:
        lesson = int(input())
    except ValueError:
        sys.exit(1)
    lesson = lesson * 45 + (lesson // 2) * 5 + ((lesson + 1) // 2 - 1) * 15
    print(lesson // 60 + 9, lesson % 60)


if __name__ == "__main__":
    main()
