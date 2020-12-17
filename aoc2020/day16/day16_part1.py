from utils import get_input_lines

rules = []
invalid_sum = 0
parse_state = 0

for line in get_input_lines(__file__):
    if line == "your ticket:":
        parse_state = 1
        continue
    elif line == "nearby tickets:":
        parse_state = 2
        continue
    elif len(line) == 0:
        continue

    if parse_state == 0:
        # Read in rules
        line_rules = []
        line_rules_str = line.split(": ")[1].split(" or ")
        for line_rule in line_rules_str:
            lower, upper = map(int, line_rule.split("-"))
            line_rules.append((lower, upper))
        rules.append(line_rules)
    elif parse_state == 1:
        # Read in own ticket
        continue
    elif parse_state == 2:
        # Read in nearby tickets
        for num in map(int, line.split(",")):
            any_rule_valid = False
            for rule_set in rules:
                this_rule_valid = False
                for lower, upper in rule_set:
                    if lower <= num <= upper:
                        this_rule_valid = True
                        break

                if this_rule_valid:
                    any_rule_valid = True
                    break

            if not any_rule_valid:
                invalid_sum += num
    else:
        raise ValueError(f"Invalid parse state {parse_state}")

print(invalid_sum)
