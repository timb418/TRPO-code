import sys


def main():
    try:
        n = int(input())
        numbers = input().split()
        if len(numbers) != n:
            sys.exit(1)

    except ValueError:
        sys.exit(1)

    print(' '.join(numbers[::2]))


if __name__ == "__main__":
    main()
