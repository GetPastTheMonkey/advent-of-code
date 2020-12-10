from utils import get_input_lines

jolts = []
max_n = 0
for line in get_input_lines(__file__):
    n = int(line)
    max_n = max(n, max_n)
    jolts.append(n)

jolts.sort()
reachability = {0: 1}
for j in jolts:
    reachability[j] = reachability.get(j - 1, 0) + reachability.get(j - 2, 0) + reachability.get(j - 3, 0)

print(reachability[max_n])
