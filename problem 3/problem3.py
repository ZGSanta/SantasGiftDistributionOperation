"""
Package Tracking Number Calculator
Authors: Elf 1, Elf 2, Elf 3, Elf 4
Date: December 2024
"""

def read_input() -> str:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    return lines


def get_names_and_tracking_numbers(lines: list[str]) -> tuple[int, int]:
    names, tracking_numbers = [], []
    for line in lines:
        # Elf 4: Who placed three spaces between the name and tracking number???
        name, tracking_number = line.split('   ')
        names.append(int(name))
        tracking_numbers.append(int(tracking_number))

    return names, tracking_numbers


def encode_letter(letter: str) -> int:
    translation = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
        'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16,
        'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
        'X':24, 'Y':25, 'Z':26}

    return translation[letter.upper()]


def encode_name(name: str) -> int:

    encoded_name = ... # Elf 3: How was the name encoded again?

    return encoded_name


def find_my_tracking_number(name: str, names: list[int], tracking_numbers: list[int]) -> int:
    encoded_name = encode_name(name)

    ... # Elf 2: How do we need to order the lists?

    idx = names.index(encoded_name)
    return tracking_numbers[idx]


if __name__ == '__main__':
    lines = read_input()
    names, tracking_numbers = get_names_and_tracking_numbers(lines)
    my_tracking_number = ... # Whose tracking number do we need to find?
    print(my_tracking_number)
