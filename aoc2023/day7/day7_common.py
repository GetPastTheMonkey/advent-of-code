from functools import cmp_to_key

from utils import get_input_lines


def get_cards(*, part_1: bool):
    if part_1:
        return ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", ]
    else:
        return ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def hand_to_score(hand: str, *, part_1: bool) -> int:
    assert len(hand) == 5

    counter = dict()

    for c in get_cards(part_1=part_1):
        counter[c] = 0

    for c in hand:
        counter[c] += 1

    if not part_1:
        counter_copy = counter.copy()
        del counter_copy["J"]
        m = max(counter_copy, key=counter_copy.get)

        counter[m] += counter["J"]
        counter["J"] = 0

    def count(c_: int) -> int:
        return len([x for x in counter.values() if x == c_])

    num_5 = count(5)
    num_4 = count(4)
    num_3 = count(3)
    num_2 = count(2)

    if num_5 == 1:
        # Five of a kind
        return 6
    elif num_4 == 1:
        # Four of a kind
        return 5
    elif num_3 == 1 and num_2 == 1:
        # Full house
        return 4
    elif num_3 == 1:
        # Three of a kind
        return 3
    elif num_2 == 2:
        # Two pairs
        return 2
    elif num_2 == 1:
        # One pair
        return 1
    else:
        # High card
        return 0


def cmp(hand_1, hand_2, *, part_1: bool) -> int:
    h_1, s_1, _ = hand_1
    h_2, s_2, _ = hand_2

    cards = get_cards(part_1=part_1)

    if s_1 != s_2:
        return s_1 - s_2

    for c_1, c_2 in zip(h_1, h_2):
        if c_1 != c_2:
            return cards.index(c_2) - cards.index(c_1)

    return 0


def day7_solve(*, part_1: bool) -> int:
    s = 0
    hands = []

    for line in get_input_lines(__file__):
        hand, bet = line.split(" ")
        bet = int(bet)

        hands.append((hand, hand_to_score(hand, part_1=part_1), bet))

    def my_cmp(h1, h2):
        return cmp(h1, h2, part_1=part_1)

    hands.sort(key=cmp_to_key(my_cmp))

    for idx, hand in enumerate(hands):
        s += (idx + 1) * hand[2]

    return s
