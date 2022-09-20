# Author: Timur Bagirov
# Date: 19 September 2022
# Простая проверка слов


def main():
    desired_list_length: int = 10
    words: list = []
    try:
        for i in range(desired_list_length):
            words.append(input())
    except ValueError:
        exit(1)

    counter: int = 0
    for i in range(len(words)):
        word = str(words[i])
        if word.startswith("S") and word.__contains__("i") and len(word) == 6:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
