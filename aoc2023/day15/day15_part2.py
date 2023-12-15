from collections import defaultdict

from aoc2023.day15.day15_common import day15_hash
from utils import get_input_lines

TupleList = list[tuple[str, int]]


def list_remove(list_: TupleList, label: str) -> TupleList:
    new_list = []

    for elem in list_:
        if elem[0] != label:
            new_list.append(elem)

    return new_list


def list_add(list_: TupleList, label: str, value: int):
    new_list = []
    found = False

    for elem in list_:
        if elem[0] == label:
            new_list.append((label, value))
            found = True
        else:
            new_list.append(elem)

    if not found:
        new_list.append((label, value))

    return new_list


def main():
    s = 0
    boxes = defaultdict(list)  # type: defaultdict[int, TupleList]

    for line in get_input_lines(__file__):
        for word in line.split(","):
            if word.endswith("-"):
                label = word[:-1]
                box_id = day15_hash(label)
                boxes[box_id] = list_remove(boxes[box_id], label)
            else:
                label, value = word.split("=")
                box_id = day15_hash(label)
                boxes[box_id] = list_add(boxes[box_id], label, int(value))

    for box_id, box in boxes.items():
        for idx, (_, value) in enumerate(box):
            mult = (box_id + 1) * (idx + 1) * value
            s += mult

    print(s)


if __name__ == '__main__':
    main()
