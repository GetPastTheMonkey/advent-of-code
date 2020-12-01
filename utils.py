from os.path import realpath, dirname, join
from typing import IO


def get_input(file) -> IO:
    return open(join(dirname(realpath(file)), "input.txt"))
