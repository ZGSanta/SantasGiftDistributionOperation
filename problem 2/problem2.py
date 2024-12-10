"""
FFF Fast Floor Finder
Authors: Elf 1, Elf 2
Date: December 2024
"""


def read_input() -> str:
    with open('input.txt', 'r') as file:
        # Elf 1: We can use the read() method to read the entire file at once
        # instead of reading it line by line with readlines()
        line = file.read()
    return line


def retrieve_floor(line: str) -> int:
    floor = 0
    for char in line: # Elf 2: Is there a way to do this without a for loop?

    return floor


if __name__ == '__main__':
    line: str = read_input()
    floor: int = retrieve_floor(line)
    print(floor)
