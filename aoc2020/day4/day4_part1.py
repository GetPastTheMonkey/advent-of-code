from utils import get_input_lines

valid_count = 0
field_count = 0
required_fields = 7

# Read input lines
for line in get_input_lines(__file__):
    if len(line) > 0:
        for field_part in line.split(" "):
            field, val = field_part.split(":")
            if field != "cid":
                field_count += 1
    else:
        if field_count == required_fields:
            valid_count += 1
        field_count = 0

# Last passport not checked yet
if field_count == required_fields:
    valid_count += 1

print(valid_count)
