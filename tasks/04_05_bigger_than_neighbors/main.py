import sys


def main():
    try:
        n = int(input())
        arr = [int(n) for n in input().split()]
    except ValueError:
        sys.exit(1)

    if n != len(arr):
        sys.exit(1)

    counter = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
