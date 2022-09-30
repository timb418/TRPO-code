t = 1


def squares():
    global t
    input_num = int(input())
    if input_num:
        squares()
    for i in range(1, input_num + 1):
        if i ** 2 == input_num:
            print(input_num, end=" ")
            t += 1


squares()
if t == 1:
    print(0)
