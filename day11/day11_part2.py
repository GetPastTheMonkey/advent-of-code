from os.path import join, dirname, realpath

grid_width = 300
grid_height = 300

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    serial_nr = int(f.readline())

# Initialize power level grid
grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
for i in range(grid_width):
    for j in range(grid_height):
        # Coordinate transformation
        x = i + 1
        y = j + 1

        # Power level calculation
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_nr
        power_level *= rack_id
        if power_level >= 100:
            power_level = int(str(power_level)[-3])
        else:
            power_level = 0
        power_level -= 5
        grid[i][j] = power_level

maximum = None
max_x = None
max_y = None
max_size = None

# Find max block
for size in range(min(grid_height, grid_width)):
    # Calculate block
    # Calculate 3x3 block sum
    grid_sum = [[0 for x in range(grid_width - size + 1)] for y in range(grid_height - size + 1)]
    for i in range(grid_width - size + 1):
        for j in range(grid_height - size + 1):
            for k in range(size):
                grid_sum[i][j] += sum(grid[i + k][j:j + size])

    # Find maximum
    for i in range(grid_width - size + 1):
        for j in range(grid_height - size + 1):
            if maximum is None or maximum < grid_sum[i][j]:
                maximum = grid_sum[i][j]
                max_x = i + 1
                max_y = j + 1
                max_size = size

print "({},{},{}) has maximum value of {}".format(max_x, max_y, max_size, maximum)
