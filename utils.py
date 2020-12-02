from os.path import realpath, dirname, join
from typing import IO


def get_input(file) -> IO:
    return open(join(dirname(realpath(file)), "input.txt"))


def get_input_lines(file) -> str:
    with get_input(file) as f:
        for line in f:
            yield line.strip()
