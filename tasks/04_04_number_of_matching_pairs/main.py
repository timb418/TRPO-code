import sys


def main():
    try:
        n = int(input())
        arr = [int(s) for s in input().split()]

    except ValueError:
        sys.exit(1)

    if n != len(arr):
        sys.exit(1)

    counter = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                counter += 1
    print(counter)


if __name__ == "__main__":
    main()
