from utils import get_input_lines


def parse(s: str) -> int:
    # STEP 1: Solve all parenthesis
    while "(" in s:
        open_idx = None
        close_idx = None
        level = 0

        for idx, char in enumerate(s):
            if char == "(":
                level += 1
                if open_idx is None:
                    open_idx = idx
            elif char == ")":
                level -= 1
                if level == 0:
                    close_idx = idx
                    break

        if open_idx is None or close_idx is None:
            raise ValueError("Could not parse parenthesis")

        substr = s[open_idx + 1: close_idx]
        s = s[:open_idx] + str(parse(substr)) + s[close_idx + 1:]

    # STEP 2: Solve all additions
    symbols = s.split(" ")
    while "+" in symbols:
        idx = symbols.index("+")
        res = int(symbols[idx - 1]) + int(symbols[idx + 1])
        symbols = symbols[:idx - 1] + [str(res)] + symbols[idx + 2:]

    # STEP 3: Solve all multiplications
    state = 0  # 0: int or parenthesis next, 1: operator next
    res = None
    for symbol in symbols:
        if state == 0:
            # Parser expects an int as next symbol
            if res is None:
                res = int(symbol)
            else:
                res *= int(symbol)
            state = 1
        elif state == 1:
            # Parses expects a multiplication operator as next symbol
            if symbol != "*":
                raise ValueError(f"Unknown operator: {symbols}")
            state = 0

    return res


result = 0
for line in get_input_lines(__file__):
    result += parse(line)
print(result)
