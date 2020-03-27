from os.path import join, dirname, realpath

NAUGHTY_LIST = [
    "ab",
    "cd",
    "pq",
    "xy"
]


def is_nice(word):
    vowel_count = 0
    last_char = None
    has_double_letter = False
    contains_naughty_string = any([naughty_word in word for naughty_word in NAUGHTY_LIST])
    for char in word:
        if char in {'a', 'e', 'i', 'o', 'u'}:
            vowel_count += 1

        if last_char is not None and last_char == char:
            has_double_letter = True

        last_char = char

    return vowel_count >= 3 and has_double_letter and not contains_naughty_string


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    print(sum([1 for w in f if is_nice(w)]))
