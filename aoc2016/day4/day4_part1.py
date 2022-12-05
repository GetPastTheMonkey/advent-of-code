import re

from utils import get_input_lines


def main():
    sector_sum = 0

    for line in get_input_lines(__file__):
        r = re.match(r"(?P<enc_name>[a-z-]+)-(?P<sector>[0-9]+)\[(?P<checksum>[a-z]+)]", line)
        enc_name = r.group("enc_name").replace("-", "")
        sector = int(r.group("sector"))
        checksum = r.group("checksum")

        counters = dict()
        for i in range(ord("a"), ord("z") + 1):
            counters[chr(i)] = 0

        for c in enc_name:
            counters[c] += 1

        sorted_counters = [k for k, v in sorted(counters.items(), key=lambda item: item[1], reverse=True)]
        sorted_short = sorted_counters[:len(checksum)]

        if "".join(sorted_short) == checksum:
            sector_sum += sector

    print(sector_sum)


if __name__ == '__main__':
    main()
