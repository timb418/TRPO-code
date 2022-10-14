import sys


def main():
    try:
        arr = [int(s) for s in input().split()]
        a = arr[0]
        b = arr[1]
        c = arr[2]
        d = arr[3]
        e = arr[4]

    except (ValueError, IndexError):
        sys.exit(1)

    counter = 0
    for i in range(1001):
        if i != e:
            if (a * i ** 3 + b * i ** 2 + c * i + d) / (i - e) == 0:
                counter = counter + 1
    print(counter)


if __name__ == "__main__":
    main()
