from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    nr_scores = int(f.readline())

scores = [3, 7]
elf_1 = 0
elf_2 = 1
while len(scores) < nr_scores + 10:
    # Add new score(s)
    combined = scores[elf_1] + scores[elf_2]
    if combined > 9:
        scores.append(1)
    scores.append(combined % 10)

    # Move elves
    elf_1 = (elf_1 + scores[elf_1] + 1) % len(scores)
    elf_2 = (elf_2 + scores[elf_2] + 1) % len(scores)

print("Last 10 scores are: {}".format(''.join(map(str, scores[-10:]))))
