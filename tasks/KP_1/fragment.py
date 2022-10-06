# Author: Timur Bagirov
# Date: 01 October 2022
# Обращение фрагмента
import sys


def main():
    try:
        s = input()
    except ValueError:
        sys.exit(1)

    first_occurrence = s[:s.find('h')]
    substr = s[s.find('h'):s.rfind('h') + 1]
    last_occurrence = s[s.rfind('h') + 1:]
    s = first_occurrence + substr[::-1] + last_occurrence

    print(s)


if __name__ == "__main__":
    main()
