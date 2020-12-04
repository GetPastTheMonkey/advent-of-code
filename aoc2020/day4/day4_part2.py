from utils import get_input_lines

valid_count = 0
field_count = 0
required_fields = 7

# Read input lines
for line in get_input_lines(__file__):
    if len(line) > 0:
        for field, val in map(lambda line_part: line_part.split(":"), line.split(" ")):
            if field == "byr" and 1920 <= int(val) <= 2002:
                field_count += 1
            elif field == "iyr" and 2010 <= int(val) <= 2020:
                field_count += 1
            elif field == "eyr" and 2020 <= int(val) <= 2030:
                field_count += 1
            elif field == "hgt" and ((val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193) or
                                     (val[-2:] == "in" and 59 <= int(val[:-2]) <= 76)):
                field_count += 1
            elif field == "hcl" and val[0] == "#" and all([v in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                 "a", "b", "c", "d", "e", "f"} for v in val[1:]]):
                field_count += 1
            elif field == "ecl" and val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                field_count += 1
            elif field == "pid" and len(val) == 9 and all([v in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
                                                           for v in val]):
                field_count += 1
    else:
        if field_count == required_fields:
            valid_count += 1
        field_count = 0

# Last passport not checked yet
if field_count == required_fields:
    valid_count += 1

print(valid_count)
