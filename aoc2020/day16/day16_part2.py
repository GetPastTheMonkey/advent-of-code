import numpy as np
from utils import get_input_lines

rules = dict()
rule_mapping = dict()
tickets = None
my_ticket = []
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
        rule_name, line_rules_str = line.split(": ")
        for line_rule in line_rules_str.split(" or "):
            lower, upper = map(int, line_rule.split("-"))
            line_rules.append((lower, upper))
        rules[rule_name] = line_rules
        rule_mapping[rule_name] = None
    elif parse_state == 1:
        # Read in own ticket
        my_ticket = list(map(int, line.split(",")))
    elif parse_state == 2:
        # Read in nearby tickets
        all_numbers_valid = True
        numbers = list(map(int, line.split(",")))
        for num in numbers:
            any_rule_valid = False
            for rule_set in rules.values():
                this_rule_valid = False
                for lower, upper in rule_set:
                    if lower <= num <= upper:
                        this_rule_valid = True
                        break

                if this_rule_valid:
                    any_rule_valid = True
                    break

            if not any_rule_valid:
                all_numbers_valid = False
                break

        if all_numbers_valid:
            if tickets is None:
                tickets = np.r_[[numbers]]
            else:
                tickets = np.r_[tickets, [numbers]]
    else:
        raise ValueError(f"Invalid parse state {parse_state}")

while any([x is None for x in rule_mapping.values()]):
    unmapped_rules = set()
    unmapped_cols = set(range(len(rule_mapping.keys())))
    possible_cols_for_rule = dict()

    for rule_name in rule_mapping.keys():
        if rule_mapping[rule_name] is None:
            possible_cols_for_rule[rule_name] = []
            unmapped_rules.add(rule_name)
        else:
            unmapped_cols.remove(rule_mapping[rule_name])

    for u_r in unmapped_rules:
        for u_c in unmapped_cols:
            # Check if the column with index u_c matches the rule u_r
            all_numbers_valid = True
            for num in tickets[:, u_c]:
                rule_set_valid = False
                for lower, upper in rules[u_r]:
                    if lower <= num <= upper:
                        rule_set_valid = True
                        break

                if not rule_set_valid:
                    all_numbers_valid = False
                    break

            if all_numbers_valid:
                possible_cols_for_rule[u_r].append(u_c)

    # Go through rules and find a rule that has only one possible column. Assign it!
    found = False
    for rule_name, possible_cols in possible_cols_for_rule.items():
        if len(possible_cols) == 0:
            print(f"Error! Rule {rule_name} has no possible columns!")
            exit(-1)
        elif len(possible_cols) == 1:
            rule_mapping[rule_name] = possible_cols[0]
            found = True
            break

    if not found:
        print("Error! There is no unique solution!")
        exit(-1)

mult = 1
for rule_name, col_idx in rule_mapping.items():
    if rule_name.startswith("departure"):
        mult *= my_ticket[col_idx]
print(mult)
