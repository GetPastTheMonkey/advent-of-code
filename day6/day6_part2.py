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

final_sum = 0
threshold = 10000

for i in range(max_x+1):
    for j in range(max_y+1):
        # Looking at coordinate point (i, j), loop through coordinate points and sum up all distances
        distance_sum = 0
        for coord in coordinates:
            coord_i, coord_j = coord
            # Calculate Manhattan distance of coordinate point to (i, j)
            distance = abs(coord_i - i) + abs(coord_j - j)
            distance_sum += distance

        if distance_sum < threshold:
            final_sum += 1

print("There are {} points that have a summed up distance less than {}".format(final_sum, threshold))
