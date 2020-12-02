import re

from utils import get_input_lines

valid_count = 0
for line in get_input_lines(__file__):
    min_count, max_count, test, _, string = re.split("[- :]", line)

    count = 0
    for char in string:
        if test == char:
            count += 1

    if int(min_count) <= count <= int(max_count):
        valid_count += 1

print(valid_count)
