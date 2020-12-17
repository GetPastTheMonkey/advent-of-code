from utils import get_input_lines

active = set()

for y, line in enumerate(get_input_lines(__file__)):
    for x, char in enumerate(line):
        if char == "#":
            active.add((x, y, 0))

rounds = 6
while rounds > 0:
    rounds -= 1
    new_active = set()

    # Find minimum and maximum coordinates
    min_x, max_x = None, None
    min_y, max_y = None, None
    min_z, max_z = None, None

    for (x, y, z) in active:
        min_x = min(min_x, x) if min_x is not None else x
        max_x = max(max_x, x) if max_x is not None else x
        min_y = min(min_y, y) if min_y is not None else y
        max_y = max(max_y, y) if max_y is not None else y
        min_z = min(min_z, z) if min_z is not None else z
        max_z = max(max_z, z) if max_z is not None else z

    # Go over all cubes in the range of the active cubes
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                # STEP 1: Count active neighbours
                active_neighbours = 0
                for x_d in [-1, 0, 1]:
                    for y_d in [-1, 0, 1]:
                        for z_d in [-1, 0, 1]:
                            if x_d == 0 and y_d == 0 and z_d == 0:
                                # Don't count myself
                                continue
                            if (x + x_d, y + y_d, z + z_d) in active:
                                active_neighbours += 1

                # STEP 2: Decide if the cube should be added
                if (x, y, z) in active and 2 <= active_neighbours <= 3:
                    new_active.add((x, y, z))
                elif (x, y, z) not in active and active_neighbours == 3:
                    new_active.add((x, y, z))

    active = new_active

print(len(active))
