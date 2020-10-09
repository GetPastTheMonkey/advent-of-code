from os.path import join, dirname, realpath

instructions = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        instructions.append(list(line.strip()))

moves = {
    1: {"U": 1, "L": 1, "D": 4, "R": 2},
    2: {"U": 2, "L": 1, "D": 5, "R": 3},
    3: {"U": 3, "L": 2, "D": 6, "R": 3},
    4: {"U": 1, "L": 4, "D": 7, "R": 5},
    5: {"U": 2, "L": 4, "D": 8, "R": 6},
    6: {"U": 3, "L": 5, "D": 9, "R": 6},
    7: {"U": 4, "L": 7, "D": 7, "R": 8},
    8: {"U": 5, "L": 7, "D": 8, "R": 9},
    9: {"U": 6, "L": 8, "D": 9, "R": 9}
}

button = 5
code = 0
for line in instructions:
    for instr in line:
        button = moves[button][instr]
    code = 10*code + button

print(code)
