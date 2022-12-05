import re

from utils import get_input


def chunk(arr, size):
    for i in range(0, len(arr), size):
        yield arr[i:i+size]


def day5_solve(reverse: bool):
    nr_of_stacks = 9
    stacks = [[]] * nr_of_stacks

    with get_input(__file__) as f:
        for line in f:
            if line.startswith("move"):
                regex = re.match(r"move (?P<nr>[0-9]*) from (?P<start>[0-9]*) to (?P<end>[0-9]*)", line)
                nr = int(regex.group("nr"))
                start = int(regex.group("start"))
                end = int(regex.group("end"))

                stack_start = stacks[start - 1]
                stack_end = stacks[end - 1]

                stack_transfer = stack_start[:nr]

                if reverse:
                    stack_transfer.reverse()

                stack_end = stack_transfer + stack_end
                stack_start = stack_start[nr:]

                stacks[start - 1] = stack_start
                stacks[end - 1] = stack_end
            elif len(line) > 0:
                for idx, entry in enumerate(map(lambda x: x.strip(), chunk(line, 4))):
                    if not entry:
                        continue
                    elif entry.startswith("["):
                        stacks[idx] = stacks[idx] + [entry[1]]

    print("".join(map(lambda x: x[0], stacks)))
