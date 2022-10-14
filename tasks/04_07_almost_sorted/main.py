import sys


def main():
    try:
        arr = [int(n) for n in input().split()]
    except ValueError:
        sys.exit(1)

    possible_to_be_sorted = False
    if sorted(arr) == arr:
        possible_to_be_sorted = True

    if not possible_to_be_sorted:
        pass

    for i in range(len(arr)):
        arr_copy = arr.copy()
        del arr_copy[i]
        if arr_copy == sorted(arr_copy):
            possible_to_be_sorted = True
            break

    if possible_to_be_sorted:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
