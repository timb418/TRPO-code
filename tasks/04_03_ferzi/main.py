import sys


def main():
    n = 8
    x_axis = []
    y_axis = []
    try:
        for i in range(n):
            new_x, new_y = [int(s) for s in input().split()]
            x_axis.append(new_x)
            y_axis.append(new_y)
    except ValueError:
        sys.exit(1)

    possible = True
    for i in range(n):
        for j in range(i + 1, n):
            if x_axis[i] == x_axis[j] or y_axis[i] == y_axis[j] \
                    or abs(x_axis[i] - x_axis[j]) == abs(
                    y_axis[i] - y_axis[j]):
                possible = False

    if possible:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
