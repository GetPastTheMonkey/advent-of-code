from os.path import join, dirname, realpath


def is_nice(word):
    word_length = len(word)
    cond1 = False
    cond2 = False
    for i in range(word_length - 2):
        # Condition 1
        if word[i:i+2] in word[i+2:]:
            cond1 = True

        # Condition 2
        if word[i] == word[i + 2]:
            cond2 = True
    return cond1 and cond2


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    print(sum([1 for w in f if is_nice(w)]))
