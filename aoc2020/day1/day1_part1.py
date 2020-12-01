from utils import get_input

integers = set()
with get_input(__file__) as f:
    for line in f:
        integers.add(int(line))

total = 2020
for i in integers:
    if total - i in integers:
        print(i * (total - i))
        break
