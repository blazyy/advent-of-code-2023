# from collections import deque

# # Read input
# lines = []
# with open("input.txt", "r") as f:
#     lines = f.readlines()

# processed = []
# processing = deque([i for i in range(1, len(lines) + 1)])
# matches_memo = {}

# while len(processing):
#     for i in range(len(processing)):
#         card_number = processing.popleft()
#         processed.append(card_number)
#         matches = None
#         if card_number in matches_memo:
#             matches = matches_memo[card_number]

#         else:
#             line = lines[card_number - 1]
#             need = set(
#                 map(
#                     lambda x: int(x) if x != "" else x,
#                     line.split(" | ")[0].split(": ")[1].strip().split(" "),
#                 )
#             )
#             have = set(
#                 map(
#                     lambda x: int(x) if x != "" else x,
#                     set(line.split(" | ")[1].strip().split(" ")),
#                 )
#             )
#             need.discard("")
#             have.discard("")
#             matches = 0
#             for num in need:
#                 if num in have:
#                     matches += 1
#             matches_memo[card_number] = matches

#         for new_card_number in range(card_number + 1, card_number + matches + 1):
#             if new_card_number <= len(lines):
#                 processing.append(new_card_number)

# print(len(processed))

# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()


def get_matches(line):
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
    return matches


# Calculate matches
matches = [0] * len(lines)
for i in range(len(lines)):
    matches[i] = get_matches(lines[i])

# Add all instances using matches
instances = [1] * len(lines)
for i in range(len(lines)):
    for j in range(i + 1, i + 1 + matches[i]):
        instances[j] += instances[i]

print(sum(instances))
