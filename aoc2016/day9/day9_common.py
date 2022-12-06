from utils import get_input_lines


def decompressed_length(text: str, recursive: bool) -> int:
    looking_for_open_parens = True
    result = 0
    buffer = ""
    idx = 0

    while idx < len(text):
        if looking_for_open_parens:
            if text[idx] == "(":
                looking_for_open_parens = False
                buffer = ""
            else:
                result += 1
        else:
            if text[idx] == ")":
                looking_for_open_parens = True
                nr_chars, repetitions = map(int, buffer.split("x"))

                if recursive:
                    to_repeat = text[idx + 1:idx + 1 + nr_chars]
                    result += repetitions * decompressed_length(to_repeat, recursive)
                else:
                    result += nr_chars * repetitions

                idx += nr_chars
            else:
                buffer += text[idx]

        idx += 1

    return result


def day9_solve(recursive: bool):
    for line in get_input_lines(__file__):
        print(decompressed_length(line, recursive))
