import re


def get_power_of_cubes(line):
    sets = line.split(": ")[1].split(";")
    min_red = min_blue = min_green = None
    for set_ in sets:
        tokens = set_.split(",")
        for token in tokens:
            freq = int(re.findall(r"\d+", token)[0])
            if "red" in token:
                if min_red is None:
                    min_red = freq
                else:
                    min_red = max(min_red, freq)
            if "blue" in token:
                if min_blue is None:
                    min_blue = freq
                else:
                    min_blue = max(min_blue, freq)
            if "green" in token:
                if min_green is None:
                    min_green = freq
                else:
                    min_green = max(min_green, freq)
    return min_red * min_blue * min_green


# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

# Calculate and print answer
sum_ = 0
for i, line in enumerate(lines):
    sum_ += get_power_of_cubes(line)
print(sum_)
