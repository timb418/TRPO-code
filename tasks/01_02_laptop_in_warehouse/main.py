# Author: Timur Bagirov
# Date: 13 September 2022
# Ноутбуки на складе

def main():
    print("Введите 6 чисел: первые три задают длину, высоту и ширину склада. "
          "Следующие три задают соответственно длину, высоту и ширину коробки:")

    wh_length = int(input())
    wh_height = int(input())
    wh_width = int(input())

    box_length = int(input())
    box_height = int(input())
    box_width = int(input())

    print((wh_length // box_length) * (wh_height // box_height) * (wh_width // box_width))
    # такое округление здесь потому, что половину коробки
    # не имеет смысл хранить, если она не помещается
    # по какому-то измерению + они все в одной плоскости


if __name__ == "__main__":
    main()
