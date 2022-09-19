# Author: Timur Bagirov
# Date: 19 September 2022
# Заменить пробел и группы пробелов символом "*"


def main():
    input_str: str = ""
    try:
        input_str = input()
    except ValueError:
        exit(1)

    print(" ".join(input_str.split()).replace(" ", "*"))


if __name__ == "__main__":
    main()
