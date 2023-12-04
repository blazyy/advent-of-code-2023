from collections import deque

# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

processed = []
processing = deque([i for i in range(1, len(lines) + 1)])
matches_memo = {}

while len(processing):
    for i in range(len(processing)):
        card_number = processing.popleft()
        processed.append(card_number)
        matches = None
        if card_number in matches_memo:
            matches = matches_memo[card_number]

        else:
            line = lines[card_number - 1]
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
            matches = 0
            for num in need:
                if num in have:
                    matches += 1
            matches_memo[card_number] = matches

        for new_card_number in range(card_number + 1, card_number + matches + 1):
            if new_card_number <= len(lines):
                processing.append(new_card_number)

print(len(processed))
