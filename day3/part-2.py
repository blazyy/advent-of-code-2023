# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

# Construct 2D matrix from input
nrows, ncols = len(lines), len(lines[0].strip())
mat = [[0] * ncols for c in range(nrows)]
for r, line in enumerate(lines):
    for c, ch in enumerate(line.strip()):
        mat[r][c] = ch


def get_gear_ratio(r, c):
    gear_ratios = []
    adj = set()
    for dr, dc in [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]:
        nr, nc = r + dr, c + dc
        if (
            nr >= 0
            and nr < nrows
            and nc >= 0
            and nc < ncols
            and mat[nr][nc].isnumeric()
            and (nr, nc) not in adj
        ):
            while nc - 1 >= 0 and mat[nr][nc - 1].isnumeric():
                nc -= 1
            cur_num = ""
            while nc < ncols and mat[nr][nc].isnumeric():
                cur_num += mat[nr][nc]
                adj.add((nr, nc))
                nc += 1
            gear_ratios.append(int(cur_num))
    if len(gear_ratios) != 2:
        return 0
    return gear_ratios[0] * gear_ratios[1]


ans = 0
for r in range(nrows):
    for c in range(ncols):
        if mat[r][c] == "*":
            ans += get_gear_ratio(r, c)


print(ans)
