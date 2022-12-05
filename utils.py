from os.path import realpath, dirname, join
from typing import IO, Generator


def chunk(arr: list, size: int) -> Generator:
    for i in range(0, len(arr), size):
        yield arr[i:i + size]


def get_input(file) -> IO:
    return open(join(dirname(realpath(file)), "input.txt"))


def get_input_lines(file) -> str:
    with get_input(file) as f:
        for line in f:
            yield line.strip()
