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

# Calculate 3x3 block sum
grid_3x3 = [[0 for x in range(grid_width-2)] for y in range(grid_height-2)]
for i in range(grid_width-2):
    for j in range(grid_height-2):
        grid_3x3[i][j] = sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3])

maximum = None
max_x = None
max_y = None

# Find max in 3x3 block
for i in range(grid_width-2):
    for j in range(grid_height-2):
        if maximum is None or maximum < grid_3x3[i][j]:
            maximum = grid_3x3[i][j]
            max_x = i + 1
            max_y = j + 1

print "({},{}) has maximum value of {}".format(max_x, max_y, maximum)
