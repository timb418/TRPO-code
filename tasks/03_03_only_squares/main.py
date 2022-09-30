# Author: Timur Bagirov
# Date: 30 September 2022
# Только квадраты


def main():
    counter = 1
    counter = squares(counter)
    if counter == 1:
        print(0)


def squares(counter: int) -> int:
    input_num = int(input())
    if input_num:
        counter = squares(counter)
    for i in range(1, input_num + 1):
        if i ** 2 == input_num:
            print(input_num, end=" ")
            counter += 1
    return counter


if __name__ == "__main__":
    main()
