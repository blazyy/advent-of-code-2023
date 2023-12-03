import re

RED_LIM = 12
GRN_LIM = 13
BLU_LIM = 14


def is_game_possible(line):
    sets = line.split(": ")[1].split(";")
    for set_ in sets:
        tokens = set_.split(",")
        for token in tokens:
            freq = int(re.findall(r"\d+", token)[0])
            if "red" in token and freq > RED_LIM:
                return False
            if "blue" in token and freq > BLU_LIM:
                return False
            if "green" in token and freq > GRN_LIM:
                return False
    return True


# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

# Calculate and print answer
sum_ = 0
for i, line in enumerate(lines):
    if is_game_possible(line):
        sum_ += i + 1
print(sum_)
