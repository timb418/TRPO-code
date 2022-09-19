# Author: Timur Bagirov
# Date: 19 September 2022
# Замена фрагмента


def main():
    input_str: str = ""
    try:
        input_str = input()
    except ValueError:
        exit(1)

    first_occurrence_index = int(input_str.find("h"))
    last_occurrence_index = int(input_str.rfind("h"))

    print(input_str[0:first_occurrence_index + 1] +
          input_str[first_occurrence_index + 1:last_occurrence_index - 1].replace("h", "H") +
          input_str[last_occurrence_index - 1:])


if __name__ == "__main__":
    main()
