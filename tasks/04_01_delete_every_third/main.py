import sys


def main():
    try:
        input_str = input()
    except ValueError:
        sys.exit(1)

    edited_str = ""

    for i in range(len(input_str)):
        if i % 3 != 0:
            edited_str += input_str[i]

    print(edited_str)


if __name__ == "__main__":
    main()
