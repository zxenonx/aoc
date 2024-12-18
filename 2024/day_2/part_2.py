"""
--- Day 2: Red-Nosed Reports ---

### PART 2
"""

def check_safety(report: list[int]) -> bool:
    """
    Determines if a report is either strictly increasing or strictly decreasing.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the report is either strictly increasing or strictly decreasing
              with each step difference between 1 and 3, otherwise False.
    """
    return is_increasing(report) or is_decreasing(report)

def check_safety_unsafe(report: list[int]) -> bool:
    """
    Checks if a report is safe by checking if the report is safe as is or if it is
    safe when removing one level from the report.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the report is safe, otherwise False.
    """
    if check_safety(report):
        return True
    for i in range(len(report)):
        unsafe_report = report[:i] + report[i + 1:]
        if check_safety(unsafe_report):
            return True


def is_decreasing(levels: list[int]) -> bool:
    """
    Checks if a list of integers is strictly decreasing with each step difference
    between 1 and 3.

    Args:
        levels (list[int]): A list of integers representing the levels to check.

    Returns:
        bool: True if the list is strictly decreasing with each step difference
              between 1 and 3, otherwise False.
    """
    value = bool(levels[0] > levels[1]) and is_between_1_and_3(abs(levels[0] - levels[1]))
    for i in range(len(levels[1:])):
        value = value and bool(levels[i] > levels[i + 1]) and is_between_1_and_3(abs(levels[i] - levels[i + 1]))
    return value


def is_increasing(levels: list[int]) -> bool:
    """
    Checks if a list of integers is strictly increasing with each step difference
    between 1 and 3.

    Args:
        levels (list[int]): A list of integers representing the levels to check.

    Returns:
        bool: True if the list is strictly increasing with each step difference
              between 1 and 3, otherwise False.
    """
    value = bool(levels[0] < levels[1]) and is_between_1_and_3(abs(levels[0] - levels[1]))
    for i in range(len(levels[1:])):
        value = value and bool(levels[i] < levels[i + 1]) and is_between_1_and_3(abs(levels[i] - levels[i + 1]))
    return value

def is_between_1_and_3(difference: int) -> bool:
    """
    Checks if an integer is between 1 and 3 inclusive.

    Args:
        difference (int): The integer to check.

    Returns:
        bool: True if the integer is between 1 and 3 inclusive, otherwise False.
    """
    return 1 <= difference <= 3

with open("input", "r") as f:
    reports = [line.split() for line in f.read().splitlines()]
    count = sum(1 for report in reports if check_safety_unsafe([int(level) for level in report]))

print(count)


