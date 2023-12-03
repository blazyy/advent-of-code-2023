words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

words_rev = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}

# Read input
lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()


def is_word_digit_left(line, l):
    found, found_word_digit = False, None
    for word in words.keys():
        if found:
            break
        j = l
        for i in range(len(word)):
            if j == len(line) or word[i] != line[j]:
                break
            j += 1
            if i == len(word) - 1:
                found = True
                found_word_digit = word
    if not found:
        return False, found_word_digit
    return True, words[found_word_digit]


def is_word_digit_right(line, r):
    found, found_word_digit = False, None
    for word in words_rev.keys():
        if found:
            break
        j = r
        for i in range(len(word)):
            if j == len(line) or word[i] != line[j]:
                break
            j -= 1
            if i == len(word) - 1:
                found = True
                found_word_digit = word
    if not found:
        return False, found_word_digit
    return True, words_rev[found_word_digit]


def get_number_from_string(line):
    l, r = 0, len(line) - 1
    left_num = right_num = None
    while left_num is None or right_num is None:
        if left_num is None:
            if line[l].isnumeric():
                left_num = line[l]
            else:
                found, found_word_digit = is_word_digit_left(line, l)
                if found:
                    left_num = found_word_digit
        if right_num is None:
            if line[r].isnumeric():
                right_num = line[r]
            else:
                found, found_word_digit = is_word_digit_right(line, r)
                if found:
                    right_num = found_word_digit
        l += 1
        r -= 1
    return int(f"{left_num}{right_num}")


# Calculate and print answer
sum_ = 0
for line in lines:
    sum_ += get_number_from_string(line)
print(sum_)
