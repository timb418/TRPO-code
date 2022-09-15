# Author: Timur Bagirov
# Date: 14 September 2022
# Кольцевая автомобильная дорога

def main():
    mkad_length = 109
    v = int(input())
    t = int(input())
    if v >= 0:
        print(v * t % mkad_length)
    else:
        print("-{0}".format(v * t % mkad_length))


if __name__ == "__main__":
    main()
