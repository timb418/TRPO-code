# Author: Timur Bagirov
# Date: 19 September 2022
# Количество палиндромов

def main():
    try:
        k = int(input())
    except ValueError:
        exit(1)

    counter = 0
    for i in range(k - 1):
        if is_palindrome(str(i)):
            counter += 1

    print(counter)


def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    main()
