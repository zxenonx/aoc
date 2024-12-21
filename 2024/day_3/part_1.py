"""
--- Day 3: Mull It Over ---

### PART 1
"""
import re
def check_instruction(memory: str):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, memory)

def multiply(instruction: str):
    pattern = r"\d{1,3}"
    return int(re.findall(pattern, instruction)[0]) * int(re.findall(pattern, instruction)[1])

with open("input", "r") as f:
    memory = f.read()
    result = sum([multiply(instruction) for instruction in check_instruction(memory)])

    print(result)


