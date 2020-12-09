from utils import get_input_lines

n = 20874512
sums = []
ints = []
solved = False

for line in get_input_lines(__file__):
    i = int(line)
    sums.append(0)
    ints.append(i)
    for idx in range(len(sums)):
        sums[idx] = sums[idx] + i
        if sums[idx] == n:
            subset = ints[idx:]
            print(min(subset) + max(subset))
            solved = True
            break

    if solved:
        break
