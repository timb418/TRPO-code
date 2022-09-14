# Author: Timur Bagirov
# Date: 14 September 2022
# Спички


def main():
    l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
    print(lists_overlap(range(l1, r1 + 1), range(l2, r2 + 1), range(l3, r3 + 1)))


def lists_overlap(first, second, third):
    if not set(first).isdisjoint(second) and set(third).isdisjoint(first) and set(third).isdisjoint(second):
        return 3
    elif not set(first).isdisjoint(third) and set(second).isdisjoint(first) and set(second).isdisjoint(third):
        return 2
    elif not set(second).isdisjoint(third) and set(third).isdisjoint(first) and set(second).isdisjoint(first):
        return 1
    else:
        return -1


if __name__ == "__main__":
    main()
