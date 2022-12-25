# This solution is written by FogRex#2146 on Discord in the "Day 22 Solutions"
# thread of the "advent-of-code" channel of the "ETH D-INFK" Discord server.
# I really can't be bothered to think about this task any further

import re

# The whole code assumes that the cube has the following layout
# Top: 0, Front: 1, Right: 2, Back: 3, Left: 4, Bottom: 5
# The actual position on the grid is entered into the cube list but in
# contrast to the default layout the very left top row is on side 0 (Top)

# SIZE      contains the size of one side (either 4 or 50)
# cube      denotes the (x, y) start position of each side
# rotation  The top side (0) is always assumed to not be rotated the
#           entries take values from 1 to 3 and (1 denotes 90° clockwise)
#             4 0 2 This (default) grid would have rotation 0 for all cubes       
#               1   -> But note that if the input actually had this shape
#               5      we would label the sides differently and 
#               3      ->  the values in rotation differ too

# Example values for cube and side_rot for the example input
# cube = [(0, 8), (4, 8), (8, 12), (4, 0), (4, 4), (8, 8)]
# side_rot = [0, 0, 0, 3, 2, 0]
SIZE = 0
cube = [(0, 0)] * 6
side_rot = [0] * 6

# The entry in [i][j] = a, b denotes that if we leave side i in direction j
# we enter side "a" in direction "b" (right (0), down (1), left (2), up (3))
# -> here we assume the (default) layout from above (all rotations = 0)
next_side = [[(2, 0), (1, 1), (4, 2), (3, 3)],
             [(2, 3), (5, 1), (4, 3), (0, 3)],
             [(5, 2), (1, 2), (0, 2), (3, 2)],
             [(2, 1), (0, 1), (4, 1), (5, 3)],
             [(0, 0), (1, 0), (5, 0), (3, 0)],
             [(2, 2), (3, 1), (4, 0), (1, 3)]]


def get_input():
    board, dims, instructions = [], {}, []

    idx = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if line == "\n":
                continue
            if "." in line or "#" in line:
                board.append(line.strip("\n"))
                start = len(re.findall(" ", board[idx]))
                dims[idx] = start, len(line.strip("\n")) - start
                idx += 1
            else:
                numbers = list(map(int, re.findall(r"\d+", line)))
                turns = re.findall(r"[LR]", line)
                instructions = list(zip(numbers, turns))
                instructions.append((numbers[-1], "N"))
    return board, dims, instructions


def init_global_params(board, dims):
    global SIZE, cube, side_rot
    SIZE = 4 if len(board[0]) < 50 else 50

    # As mentioned above we already know the position and rotation of side 0
    found = [True] + [False] * 5
    cube[0] = 0, dims[0][0]

    queue = [0]
    while len(queue) > 0:
        cur_side = queue.pop()
        y, x = cube[cur_side]

        # determine if another side exists and add its coords and rotation (right: 0, down: 1, left: 2, up: 3)
        for i in range(4):
            if i == 0 and len(board[y]) > x + SIZE and board[y][x + SIZE] != " " or \
                    i == 1 and len(board) > y + SIZE and len(board[y + SIZE]) > x and board[y + SIZE][x] != " " or \
                    i == 2 and x - SIZE >= 0 and board[y][x - SIZE] != " " or \
                    i == 3 and y - SIZE >= 0 and len(board[y - SIZE]) > x and board[y - SIZE][x] != " ":
                side, rot = next_side[cur_side][(i + side_rot[cur_side]) % 4]
                if not found[side]:
                    found[side] = True
                    queue.append(side)
                    side_rot[side] = (rot - i) % 4
                    if i == 0:
                        cube[side] = y, x + SIZE
                    elif i == 1:
                        cube[side] = y + SIZE, x
                    elif i == 2:
                        cube[side] = y, x - SIZE
                    else:
                        cube[side] = y - SIZE, x


def get_cube_side(row, column):
    for i, c in enumerate(cube):
        if row in range(c[0], c[0] + SIZE) and \
                column in range(c[1], c[1] + SIZE):
            return i
    return -1


def goto_next_side(row, column, facing):
    cur_side = get_cube_side(row, column)

    # determine exit side (correct rotation)
    exit_side = (facing + side_rot[cur_side]) % 4
    # get new cube and adjust the facing
    new_cube, entry_side = next_side[cur_side][exit_side]
    new_facing = (entry_side - side_rot[new_cube]) % 4

    # Determine the offset (entry / exit point)
    offset = row - cube[cur_side][0] if facing % 2 == 0 else column - cube[cur_side][1]
    # Inverts the offset if needed on the new side
    if (facing == 0 and new_facing == 1) or (facing == 1 and new_facing == 0) or \
            (facing == 2 and new_facing == 3) or (facing == 3 and new_facing == 2) or \
            abs(facing - new_facing) == 2:
        offset = SIZE - 1 - offset

    # Calculate new coords
    new_row = cube[new_cube][0]
    new_column = cube[new_cube][1]
    if new_facing % 2 == 0:
        new_row += offset
        if new_facing == 2:
            new_column += SIZE - 1
    else:
        new_column += offset
        if new_facing == 3:
            new_row += SIZE - 1
    return new_row, new_column, new_facing


# executes one move instruction (recursively)
def move(dims, board, row, column, facing, length):
    if length == 0:
        return row, column, facing

    next_row = row
    next_column = column
    next_facing = facing
    if facing % 2 == 0:
        next_column = column - (facing - 1)
        if next_column < dims[row][0] or next_column >= sum(dims[row]):
            next_row, next_column, next_facing = goto_next_side(row, column, facing)
    else:
        next_row = row - (facing - 2)
        if next_row >= len(board) or next_row < 0 or column < dims[next_row][0] or column >= sum(dims[next_row]):
            next_row, next_column, next_facing = goto_next_side(row, column, facing)

    if board[next_row][next_column] == "#":
        return row, column, facing
    # Enter a trail as in the example
    # new = list(board[next_row])
    # new[next_column] = ">" if next_facing == 0 else "v" if next_facing == 1 else "<" if next_facing == 2 else "^"
    # board[next_row] = "".join(new)
    return move(dims, board, next_row, next_column, next_facing, length - 1)


def main():
    board, dims, instructions = get_input()
    init_global_params(board, dims)

    row, column, facing = 0, dims[0][0], 0
    for length, direction in instructions:
        row, column, facing = move(dims, board, row, column, facing, length)
        if direction == "R":
            facing = (facing + 1) % 4
        elif direction == "L":
            facing = (facing - 1) % 4
        # Print the board after every instruction and wait for a keystroke
        # for b in board:
        #     print(b)
        # print(row, column, facing)
        # input()
        # print()
    print((row + 1) * 1000 + (column + 1) * 4 + facing)


if __name__ == '__main__':
    main()
