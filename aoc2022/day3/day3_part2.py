from typing import Set

from utils import get_input_lines


def rucksack_to_priority_set(rucksack: str) -> Set[int]:
    return set((ord(x) - ord("a") + 1 if x.islower() else ord(x) - ord("A") + 27 for x in rucksack))


def main():
    lines = list(get_input_lines(__file__))
    group_size = 3
    groups = (lines[i:i + group_size] for i in range(0, len(lines), group_size))
    intersection_sum = 0

    for sack_1, sack_2, sack_3 in groups:
        sack_1_priorities = rucksack_to_priority_set(sack_1)
        sack_2_priorities = rucksack_to_priority_set(sack_2)
        sack_3_priorities = rucksack_to_priority_set(sack_3)

        intersection = sack_1_priorities.intersection(sack_2_priorities).intersection(sack_3_priorities)
        assert len(intersection) == 1, "More than one element in all sacks"
        intersection_sum += intersection.pop()

    print(intersection_sum)


if __name__ == '__main__':
    main()
