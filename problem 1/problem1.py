"""
Christmas Package Wrapping Shortage Disaster Prevention Code 1.0
Authors: Elf 1, Elf 2, Elf 3, Elf 4
Date: December 2024
"""


def read_input() -> list[str]:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    return lines


def split_line(line: str) -> tuple[int, int, int]:
    x, y, z = # Elf 2: How can I split a string into 3 integers?

    return x, y, z


def calculate_surface_area(x: int, y: int, z: int) -> int:
    surface_area = # Elf 4: I should have paid more attention in math class...

    return surface_area


def calculate_total_surface_area(lines: list[str]) -> int:
    total_surface_area = 0
    # Elf 3: Oh my god oh my god oh my god!!!!! Please help me
    # figure this out soon or this christmas is going to be a disaster!

    return total_surface_area


"""
Elf 1: Hello fellow programmer!
    This is the entry point of the program.
    It should always be at the bottom of the file, so that all the functions
    it calls are already defined when it runs. This is because the Python interpreter
    reads the file from top to bottom. From here, we call the functions we defined above.
    Let's see if we can get this program to work! Run this file with the command:
        "python problem1.py" or "python3 problem1.py"
    depending on your python version.
"""
if __name__ == '__main__':
    lines: list[str] = read_input() # Elf 1: As you can see, we can define variables with type hints in Python!
    total_surface_area = calculate_total_surface_area(lines) # Elf 4: Who needs type hints anyway? I know all the types!
    print(total_surface_area)
