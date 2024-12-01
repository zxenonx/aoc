"""
--- Day 1: Historian Hysteria ---

### PART  1
To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list,
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4;
if you pair up a 9 with a 3, the distance apart is 6.

To find the total distance between the left list and the right list, add up the distances between all of the pairs you found.
"""

with open("input", "r") as f:
    data = f.read().split("\n")

    left = sorted([int(x.split("  ")[0]) for x in data if x != ""])
    right = sorted([int(x.split("  ")[1]) for x in data if x != ""])

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(total)