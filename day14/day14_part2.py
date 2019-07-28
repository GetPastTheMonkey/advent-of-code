from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    search_digits = list(map(int, f.readline().strip()))

scores = [3, 7]
elf_1 = 0
elf_2 = 1
while True:
    # Add new score(s)
    combined = scores[elf_1] + scores[elf_2]
    if combined > 9:
        scores.append(1)
    scores.append(combined % 10)

    # Move elves
    elf_1 = (elf_1 + scores[elf_1] + 1) % len(scores)
    elf_2 = (elf_2 + scores[elf_2] + 1) % len(scores)

    # Check if the search_digits is either the last part of the last part - 1
    if scores[-len(search_digits):] == search_digits:
        solution = len(scores) - len(search_digits)
        break
    elif scores[-len(search_digits)-1:-1] == search_digits:
        solution = len(scores) - len(search_digits) - 1
        break

print("The string appeared after {} recipes".format(solution))
