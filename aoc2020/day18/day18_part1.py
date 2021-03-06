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

    # STEP 2: Parse string without parenthesis
    state = 0  # 0: int next, 1: operator next
    res = None
    operator = None  # 0: add, 1: multiply
    for symbol in s.split(" "):
        if state == 0:
            # Parser expects an int as next symbol
            if res is None:
                res = int(symbol)
            elif operator == 0:
                res += int(symbol)
            elif operator == 1:
                res *= int(symbol)
            else:
                raise ValueError(f"Could not parse integer. res={res}, operator={operator}, symbol={symbol}")
            state = 1
        elif state == 1:
            # Parses expects an operator as next symbol
            if symbol == "+":
                operator = 0
            elif symbol == "*":
                operator = 1
            else:
                raise ValueError(f"Unknown operator: {operator}")
            state = 0

    return res


result = 0
for line in get_input_lines(__file__):
    result += parse(line)
print(result)
