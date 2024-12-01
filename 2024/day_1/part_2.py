"""
--- Day 1: Historian Hysteria ---

### PART 2
"""

def count_occurrences(target_value: int, numbers: list[int]) -> int:
    """
    Returns the number of occurrences of the target value in the given list of numbers.

    :param target_value: The value to search for.
    :param numbers: The list of numbers to search in.
    :return: The count of occurrences of the target value.
    """
    count = 0
    for num in numbers:
        if num == target_value:
            count += 1
    return count

with open("input", "r") as f:
    data = f.read().split("\n")

    left = sorted([int(x.split("  ")[0]) for x in data if x != ""])
    right = sorted([int(x.split("  ")[1]) for x in data if x != ""])

    similarity_score = 0
    for i in range(len(left)):
        similarity_score += (left[i] * count_occurrences(left[i], right))

    print(similarity_score)