from utils import get_input_lines

pos_x = 0
pos_y = 0

waypoint_x = 10
waypoint_y = 1

for line in get_input_lines(__file__):
    action = line[0]
    n = int(line[1:])

    # Handle actions
    if action == "N":
        waypoint_y += n
    elif action == "S":
        waypoint_y -= n
    elif action == "E":
        waypoint_x += n
    elif action == "W":
        waypoint_x -= n
    elif action == "L":
        # Rotate (n//90) times CCW: (new_x, new_y) = (-old_y, old_x)
        for i in range(n // 90):
            tmp_x = waypoint_x
            waypoint_x = -waypoint_y
            waypoint_y = tmp_x
    elif action == "R":
        # Rotate (n//90) times CW: (new_x, new_y) = (old_y, -old_x)
        for i in range(n // 90):
            tmp_x = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -tmp_x
    elif action == "F":
        pos_x += n * waypoint_x
        pos_y += n * waypoint_y
    else:
        raise NotImplementedError(f"Unknown action '{action}'")

print(abs(pos_x) + abs(pos_y))
