from aoc2016.day7.day7_common import parse_line_brackets
from utils import get_input_lines


def contains_abba(s: str) -> bool:
    for i in range(0, len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True

    return False


def main():
    supports_tls = 0

    for line in get_input_lines(__file__):
        must_contain_abba, must_not_contain_abba = parse_line_brackets(line)

        if any(map(contains_abba, must_contain_abba)) and not any(map(contains_abba, must_not_contain_abba)):
            supports_tls += 1

    print(supports_tls)


if __name__ == '__main__':
    main()
