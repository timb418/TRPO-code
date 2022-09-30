# Author: Timur Bagirov
# Date: 28 September 2022
# Сумма факториалов
import sys


def main():
    n: int = 0

    try:
        n = int(input())
    except ValueError:
        sys.exit(1)

    sum_of_factors: int = 0
    for i in range(1, n + 1):
        sum_of_factors += get_factorial(i)

    print(sum_of_factors)


def get_factorial(num) -> int:
    factorial = 1
    if num <= 0:
        sys.exit(0)
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial


if __name__ == "__main__":
    main()
