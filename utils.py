from functools import reduce
from os.path import realpath, dirname, join
from typing import IO, Generator, List, Any, TypeVar

T = TypeVar("T")


def chunk(arr: List[T], size: int) -> Generator[T, Any, None]:
    for i in range(0, len(arr), size):
        yield arr[i:i + size]


def get_input(file) -> IO:
    return open(join(dirname(realpath(file)), "input.txt"))


def get_input_lines(file) -> Generator[str, Any, None]:
    with get_input(file) as f:
        for line in f:
            yield line.strip()


def chinese_remainder(modulos: List[int], rests: List[int]) -> int:
    sum_ = 0
    prod = reduce(lambda acc, b: acc * b, modulos)

    for m_i, a_i in zip(modulos, rests):
        p = prod // m_i
        sum_ += a_i * mul_inv(p, m_i) * p

    return sum_ % prod


def mul_inv(a: int, b: int) -> int:
    if b == 1:
        return 1

    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
