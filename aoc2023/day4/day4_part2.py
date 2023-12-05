from collections import defaultdict

from utils import get_input_lines


def main():
    card_counter = defaultdict(lambda: 0)

    for line in get_input_lines(__file__):
        card_id, numbers = line.split(": ")
        card_id = int(card_id[5:])
        winners, my_nums = numbers.split(" | ")

        # Add current card ID
        card_counter[card_id] += 1

        winners = set([int(num) for num in winners.split(" ") if num])
        my_nums = set([int(num) for num in my_nums.split(" ") if num])
        correct = len(winners.intersection(my_nums))

        # Add next cards
        for i in range(correct):
            card_counter[card_id + i + 1] += card_counter[card_id]

    print(sum(card_counter.values()))


if __name__ == '__main__':
    main()
