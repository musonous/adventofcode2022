import sys


def score(a, b):
    if a == 'A' and b == 'X':  # Rock vs Rock
        return 1 + 3
    if a == 'A' and b == 'Y':  # Rock vs Paper
        return 2 + 6
    if a == 'A' and b == 'Z':  # Rock vs Scissors
        return 3 + 0
    if a == 'B' and b == 'X':  # Paper vs Rock
        return 1 + 0
    if a == 'B' and b == 'Y':  # Paper vs Paper
        return 2 + 3
    if a == 'B' and b == 'Z':  # Paper vs Scissors
        return 3 + 6
    if a == 'C' and b == 'X':  # Scissors vs Rock
        return 1 + 6
    if a == 'C' and b == 'Y':  # Scissors vs Paper
        return 2 + 0
    if a == 'C' and b == 'Z':  # Scissors vs Scissors
        return 3 + 3


def strategy2(a, b):
    if a == 'A' and b == 'X':  # Lose, Rock => Scissors
        return 3 + 0
    if a == 'A' and b == 'Y':  # Draw, Rock => Rock
        return 1 + 3
    if a == 'A' and b == 'Z':  # Win, Rock => Paper
        return 2 + 6
    if a == 'B' and b == 'X':  # Lose, Paper => Rock
        return 1 + 0
    if a == 'B' and b == 'Y':  # Draw, Paper => Paper
        return 2 + 3
    if a == 'B' and b == 'Z':  # Win, Paper => Scissors
        return 3 + 6
    if a == 'C' and b == 'X':  # Lose, Scissors => Paper
        return 2 + 0
    if a == 'C' and b == 'Y':  # Draw, Scissors => Scissors
        return 3 + 3
    if a == 'C' and b == 'Z':  # Win, Scissors => Rock
        return 1 + 6


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

with open(filename) as f:
    line = f.readline()
    total_score = 0
    while line:
        ab = line.strip().split(' ')
        # total_score += score(ab[0], ab[1])
        total_score += strategy2(ab[0], ab[1])
        line = f.readline()

print(total_score)
