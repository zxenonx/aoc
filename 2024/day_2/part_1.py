"""
--- Day 2: Red-Nosed Reports ---

### PART 1
"""

def check_safety(report: list[int]) -> bool:
    """
    Checks if a report is either strictly increasing or strictly decreasing.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the report is either strictly increasing or strictly decreasing
              with each step difference between 1 and 3, otherwise False.
    """
    return is_increasing(report) or is_decreasing(report)

def is_decreasing(report: list[int]) -> bool:
    """
    Checks if a report is strictly decreasing with each step difference
    between 1 and 3.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the list is strictly decreasing with each step difference
              between 1 and 3, otherwise False.
    """
    value = bool(report[0] > report[1]) and is_between_1_and_3(abs(report[0] - report[1]))
    for i in range(len(report[1:])):
        value = value and bool(report[i] > report[i+1]) and is_between_1_and_3(abs(report[i] - report[i + 1]))

    return value

def is_increasing(report: list[int]) -> bool:
    """
    Checks if a report is strictly increasing with each step difference
    between 1 and 3.

    Args:
        report (list[int]): A list of integers representing the report levels.

    Returns:
        bool: True if the list is strictly increasing with each step difference
              between 1 and 3, otherwise False.
    """
    value = bool(report[0] < report[1]) and is_between_1_and_3(abs(report[0] - report[1]))
    for i in range(len(report[1:])):
        value = value and bool(report[i] < report[i + 1]) and is_between_1_and_3(abs(report[i] - report[i + 1]))

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
    reports = f.read().split("\n")
    # print(reports)
    count = 0
    for report in reports:
        data = report.split(" ")
        print(data)
        levels = [int(level) for level in data]

        print(check_safety(levels))

        if check_safety(levels):
            count += 1
    print(count)