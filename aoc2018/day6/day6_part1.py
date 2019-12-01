from os.path import join, dirname, realpath
from re import match

# Load file
coordinates = []
max_x = 0
max_y = 0
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        m = match("^(?P<x>\d+), (?P<y>\d+)$", line)
        x = int(m.group("x"))
        y = int(m.group("y"))
        coordinates.append((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

# Loop through grid and find closest coordinate point
print("Going to initialize grid of size {}x{}...".format(max_x, max_y))

grid = []
for i in range(max_x+1):
    grid.append([])
    for j in range(max_y+1):
        grid[i].append((None, max_x + max_y))

        # Looking at coordinate point (i, j), loop through coordinate points to find closest one
        for coord in coordinates:
            coord_i, coord_j = coord
            # Calculate Manhattan distance of coordinate point to (i, j)
            distance = abs(coord_i - i) + abs(coord_j - j)

            if distance < grid[i][j][1]:
                # Found a shorter distance, update coordinate info
                grid[i][j] = (coord, distance)
            elif distance == grid[i][j][1]:
                # Found the same distance again, two coordinate points are nearest
                grid[i][j] = (None, distance)

print("Initialized. Going to count all entries...")

# Loop through grid and count entries per coordinate point
coordinate_bucket = dict()
for i in range(max_x+1):
    for j in range(max_y+1):
        if grid[i][j][0] is not None:
            value = coordinate_bucket.get(grid[i][j][0], 0)
            coordinate_bucket[grid[i][j][0]] = value + 1

print("Finished counting all entries. Currently has {} coordinate points in bucket".format(len(coordinate_bucket)))
print("Removing all coordinate points with contact to grid edge (infinite areas)...")

# Loop through top and bottom wall of grid and remove coordinates from bucket
for j in range(max_y+1):
    coordinate_bucket.pop(grid[0][j][0], None)
    coordinate_bucket.pop(grid[max_x][j][0], None)

# Loop through left and right wall of grid and remove coordinates from bucket
for i in range(max_x+1):
    coordinate_bucket.pop(grid[i][0][0], None)
    coordinate_bucket.pop(grid[i][max_y][0], None)

print("Finished removing infinite areas. {} are left, need to find maximum".format(len(coordinate_bucket)))

max_c = max(coordinate_bucket, key=coordinate_bucket.get)
print("Area around coordinate point {} is the biggest one with an area of {}".format(max_c, coordinate_bucket[max_c]))
