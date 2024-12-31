"""
--- Day 3: Mull It Over ---

### PART 1 & PART 2
"""
import re

def check_instruction(memory: str):
    """
    Extracts all occurrences of 'mul(x,y)' patterns from the given memory string.

    Args:
        memory (str): A string containing various instructions.

    Returns:
        list: A list of strings, each representing an instruction in the form 'mul(x,y)'.
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, memory)

def process_memory(memory: str):
    """
    Processes the given memory string and returns the result of all enabled 'mul(x,y)'
    instructions.

    Args:
        memory (str): A string containing various instructions.

    Returns:
        int: The result of all enabled 'mul(x,y)' instructions.
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    instructions = re.split(r"(don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))", memory)
    enabled = True
    result = 0
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif re.match(pattern, instruction) and enabled:
            result += multiply(instruction)
    return result

def multiply(instruction: str):
    """
    Multiplies the two integers present in a 'mul(x,y)' instruction string.

    Args:
        instruction (str): A string containing the instruction in the form 'mul(x,y)'.

    Returns:
        int: The product of the two integers extracted from the instruction.
    """
    pattern = r"\d{1,3}"
    return int(re.findall(pattern, instruction)[0]) * int(re.findall(pattern, instruction)[1])

with open("input", "r") as f:
    memory = f.read()
    result = sum(
        multiply(instruction) for instruction in check_instruction(memory)
    )

    print("Part 1:", result)
    print("Part 2:", process_memory(memory))






# 171141838 too high
# 3818454 too low
