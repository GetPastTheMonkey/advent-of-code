import json
from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    obj = json.load(f)


def sum_rec(o):
    if isinstance(o, int):
        return o
    if isinstance(o, list):
        return sum(map(sum_rec, o))
    if isinstance(o, dict):
        return sum(map(sum_rec, o.values()))
    return 0


print(sum_rec(obj))
