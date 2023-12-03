def get_number_from_string(line):
    left_num = right_num = None
    l, r = 0, len(line) - 1
    while not left_num or not right_num:
        if not left_num and line[l].isnumeric():
            left_num = line[l]
        if not right_num and line[r].isnumeric():
            right_num = line[r]
        l += 1
        r -= 1
    return int(f"{left_num}{right_num}")


# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

# Calculate and print answer
sum_ = 0
for line in lines:
    sum_ += get_number_from_string(line)
print(sum_)
