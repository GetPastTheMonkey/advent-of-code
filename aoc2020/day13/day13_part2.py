from functools import reduce
from typing import List

from utils import get_input_lines

mods = []
rems = []

for offset, bus_id in enumerate(list(get_input_lines(__file__))[1].split(",")):
    if bus_id == "x":
        continue

    bus_id = int(bus_id)

    # Use Chinese Remainder Theorem
    # (X mod bus_id) = k * bus_id - offset, with k such that the right hand side is not negative
    rhs = bus_id - offset if offset > 0 else 0

    # Correct right hand side if it is too small
    while rhs < 0:
        rhs += bus_id

    mods.append(bus_id)
    rems.append(rhs)


def modular_inverse(a: int, b: int) -> int:
    # Source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    t, new_t = 0, 1
    r, new_r = b, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"Integer {a} is not invertible modulo {b}")

    if t < 0:
        t += b

    return t


def chinese_remainder(remainders: List[int], modulos: List[int]) -> int:
    solution = 0
    big_m = reduce(lambda x1, x2: x1 * x2, modulos)
    for a_i, m_i in zip(remainders, modulos):
        big_m_i = big_m // m_i
        solution += a_i * big_m_i * modular_inverse(big_m_i, m_i)
    return solution % big_m


print(chinese_remainder(rems, mods))
