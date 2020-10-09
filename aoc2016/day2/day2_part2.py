from os.path import join, dirname, realpath

instructions = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        instructions.append(list(line.strip()))

moves = {
    "1": {"U": "1", "L": "1", "D": "3", "R": "1"},
    "2": {"U": "2", "L": "2", "D": "6", "R": "3"},
    "3": {"U": "1", "L": "2", "D": "7", "R": "4"},
    "4": {"U": "4", "L": "3", "D": "8", "R": "4"},
    "5": {"U": "5", "L": "5", "D": "5", "R": "6"},
    "6": {"U": "2", "L": "5", "D": "A", "R": "7"},
    "7": {"U": "3", "L": "6", "D": "B", "R": "8"},
    "8": {"U": "4", "L": "7", "D": "C", "R": "9"},
    "9": {"U": "9", "L": "8", "D": "9", "R": "9"},
    "A": {"U": "6", "L": "A", "D": "A", "R": "B"},
    "B": {"U": "7", "L": "A", "D": "D", "R": "C"},
    "C": {"U": "8", "L": "B", "D": "C", "R": "C"},
    "D": {"U": "B", "L": "D", "D": "D", "R": "D"}
}

button = "5"
code = ""
for line in instructions:
    for instr in line:
        button = moves[button][instr]
    code += button

print(code)
