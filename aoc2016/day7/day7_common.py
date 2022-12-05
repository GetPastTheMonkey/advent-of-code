from typing import Tuple, List


def parse_line_brackets(line: str) -> Tuple[List[str], List[str]]:
    s1 = line.split("[")
    s2 = map(lambda x: x.split("]"), s1)

    outside_brackets = []
    inside_brackets = []

    for group in s2:
        if len(group) == 1:
            outside_brackets.append(group[0])
        elif len(group) == 2:
            outside_brackets.append(group[1])
            inside_brackets.append(group[0])
        else:
            assert False, "Group has incorrect length"

    return outside_brackets, inside_brackets
