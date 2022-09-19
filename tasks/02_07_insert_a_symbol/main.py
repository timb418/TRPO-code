# Author: Timur Bagirov
# Date: 19 September 2022
# Вставка символа


def main():
    input_str: str = ""
    try:
        input_str = input()
    except ValueError:
        exit(1)

    print("*".join(input_str))


if __name__ == "__main__":
    main()
