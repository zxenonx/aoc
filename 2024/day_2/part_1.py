"""
--- Day 2

### PART 1
"""


def check_safety(report: list[int]) -> bool:
    return is_increasing(report) or is_decreasing(report)


def is_decreasing(levels: list[int]) -> bool:
    value = bool(levels[0] > levels[1]) and is_between_1_and_3(abs(levels[0] - levels[1]))
    for i in range(len(levels[1:])):
        value = value and bool(levels[i] > levels[i + 1]) and is_between_1_and_3(abs(levels[i] - levels[i + 1]))
    return value


def is_increasing(levels: list[int]) -> bool:
    value = bool(levels[0] < levels[1]) and is_between_1_and_3(abs(levels[0] - levels[1]))
    for i in range(len(levels[1:])):
        value = value and bool(levels[i] < levels[i + 1]) and is_between_1_and_3(abs(levels[i] - levels[i + 1]))
    return value


def is_between_1_and_3(difference: int) -> bool:
    return 1 <= difference <= 3


with open("input", "r") as f:
    reports = f.read().split("\n")

    count = 0
    for report in reports:
        data = report.split(" ")
        levels = [int(level) for level in data]
        print(levels)

        if check_safety(levels):
            count += 1

    print(count)
