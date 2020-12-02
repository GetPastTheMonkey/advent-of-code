import re

from utils import get_input_lines

valid_count = 0
for line in get_input_lines(__file__):
    idx_1, idx_2, test, _, string = re.split("[- :]", line)

    # != is xor for booleans
    if (string[int(idx_1) - 1] == test) != (string[int(idx_2) - 1] == test):
        valid_count += 1

print(valid_count)
