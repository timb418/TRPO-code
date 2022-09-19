# Author: Timur Bagirov
# Date: 19 September 2022
# Перестановка слов


def main():
    try:
        input_str = input()
    except ValueError:
        exit(1)

    first_half, second_half = str(input_str).split(" ")

    print(second_half, first_half)


if __name__ == "__main__":
    main()
