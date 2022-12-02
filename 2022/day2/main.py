# ROCK A, X - 1
# PAPER B, Y - 2
# SCISSORS X, Z - 3
# 0 - lost, 3 - draw, 6 - win

import string

strategy = []

with open("strategy.txt", "r") as file:
    for line in file:
        line = line.translate({ord(c): None for c in string.whitespace})
        strategy.append(line)

p1_combinations = {
    'AX': 4, 'BX': 1, 'CX': 7,
    'AY': 8, 'BY': 5, 'CY': 2,
    'AZ': 3, 'BZ': 9, 'CZ': 6,
}

points = 0
for s in strategy:
    if s in p1_combinations:
        points += p1_combinations[s]

print(f"Part1 Sum: {points}")

# X - playing to lose,
# Y - playing to draw,
# Z - playing to win
# e.g. When A(rock), X(need to lose), im playing Z(paper)

p2_combinations = {
    'AX': 3, 'BX': 1, 'CX': 2,
    'AY': 1, 'BY': 2, 'CY': 3,
    'AZ': 2, 'BZ': 3, 'CZ': 1,
}
points = 0
for s in strategy:
    if s in p2_combinations:
        points += p2_combinations[s]
        if 'X' in s:
            points += 0
        elif 'Y' in s:
            points += 3
        elif 'Z' in s:
            points += 6

print(f"Part2 Sum: {points}")
