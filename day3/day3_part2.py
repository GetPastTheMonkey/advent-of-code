from os.path import join, dirname, realpath
from re import match

# Load file
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    claims_file = f.readlines()

# Parse claims from file lines into list of tuples
claims = []
for claim_file in claims_file:
    m = match("^#(?P<row>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)$", claim_file)
    row = int(m.group("row"))
    x = int(m.group("x"))
    y = int(m.group("y"))
    width = int(m.group("width"))
    height = int(m.group("height"))
    claims.append((row, x, y, width, height))

# Generate grid of dimension row_count x col_count
row_count = max([x+width for (_, x, _, width, _) in claims])
col_count = max([y+height for (_, _, y, _, height) in claims])
grid = [[0 for _ in range(col_count)] for _ in range(row_count)]

# Loop through claims and increment grid
for (_, x, y, width, height) in claims:
    for i in range(x, x+width):
        for j in range(y, y+height):
            grid[i][j] += 1

# Loop through claims again and find the one that has only 1s in the grid
for (row, x, y, width, height) in claims:
    candidate = True
    for i in range(x, x+width):
        for j in range(y, y+height):
            if grid[i][j] != 1:
                candidate = False
                break
        if not candidate:
            break

    if candidate:
        print "Found a candidate: Claim with ID {}".format(row)
        break
