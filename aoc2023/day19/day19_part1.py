from utils import get_input_lines


def parse_input():
    rules = dict()  # type: dict[str, list[tuple[str, ...]]]
    inputs = []  # type: list[tuple[int, int, int, int]]
    parsing_rules = True

    for line in get_input_lines(__file__):
        if len(line) == 0:
            parsing_rules = False
        elif parsing_rules:
            name, rule = line.split("{")
            rule = [r.split(":") for r in rule[:-1].split(",")]
            rules[name] = rule
        else:
            x, m, a, s = [int(xmas[2:]) for xmas in line[1:-1].split(",")]
            inputs.append((x, m, a, s))

    return rules, inputs


def should_accept(x: int, m: int, a: int, s: int, rules: dict[str, list[tuple[str, ...]]]) -> bool:
    func = "in"

    while func not in {"A", "R"}:
        rule_list = rules[func]

        for rule in rule_list:
            if len(rule) == 1:
                func = rule[0]
                break
            elif len(rule) == 2:
                cond, next_func = rule

                source = f"cond_result = {cond}"
                loc = {"x": x, "m": m, "a": a, "s": s}
                exec(source, globals(), loc)

                if loc["cond_result"]:
                    func = next_func
                    break
            else:
                raise ValueError("Wut")

    return func == "A"


def main():
    rules, inputs = parse_input()
    result = 0

    for x, m, a, s in inputs:
        if should_accept(x, m, a, s, rules):
            result += x + m + a + s

    print(result)


if __name__ == '__main__':
    main()
