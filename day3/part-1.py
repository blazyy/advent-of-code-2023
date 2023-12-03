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


def is_valid_part_number(indices):
    for r, c in indices:
        for dr, dc in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]:
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < nrows and nc >= 0 and nc < ncols:
                ch = mat[nr][nc]
                if not ch.isalnum() and ch != ".":
                    return True
    return False


ans = 0
for r in range(nrows):
    cur_num, cur_indices, building = "", [], False
    for c in range(ncols):
        if mat[r][c].isnumeric():
            building = True
            cur_num += mat[r][c]
            cur_indices.append((r, c))
            if c == ncols - 1:
                if is_valid_part_number(cur_indices):
                    ans += int(cur_num)
        elif building:
            if is_valid_part_number(cur_indices):
                ans += int(cur_num)
            cur_num, cur_indices, building = "", [], False


print(ans)
