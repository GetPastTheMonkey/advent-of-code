from utils import get_input

integers = set()
with get_input(__file__) as f:
    for line in f:
        integers.add(int(line))

total = 2020
found = False
for i in integers:
    for j in integers:
        if i + j < total and total - i - j in integers:
            print(i * j * (total - i - j))
            found = True
            break
    if found:
        break
