from collections import deque

from aoc2016.day19.day19_common import ELVES


def main() -> int:
    view_left = deque()
    view_right = deque()

    # Setup initial views
    for i in range(ELVES):
        if i <= (ELVES // 2):
            view_left.append(i)
        else:
            view_right.append(i)

    # NOTE: view_left[0] is always the current elf
    # NOTE: If ELVES is even -> len(view_left) == len(view_right)
    #       Else                len(view_left) > len(view_right)

    while len(view_right) > 0:
        if len(view_left) > len(view_right):
            # The number of elves is odd -> Remove the last one that is to my left
            view_left.pop()
        else:
            # The number of elves is even -> Remove the first one in the right list (because I am in the left array)
            view_right.popleft()

        # Rotate the table to the right
        view_right.append(view_left.popleft())
        view_left.append(view_right.popleft())

    return view_left[0] + 1  # +1 because the puzzle is 1-indexed


if __name__ == '__main__':
    print(main())
