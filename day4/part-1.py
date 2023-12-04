# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()


def calculate_points(line):
    need = set(
        map(
            lambda x: int(x) if x != "" else x,
            line.split(" | ")[0].split(": ")[1].strip().split(" "),
        )
    )
    have = set(
        map(
            lambda x: int(x) if x != "" else x,
            set(line.split(" | ")[1].strip().split(" ")),
        )
    )
    need.discard("")
    have.discard("")
    score = 0
    for num in need:
        if num in have:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score


ans = 0
for line in lines:
    ans += calculate_points(line)
print(ans)
