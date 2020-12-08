from utils import get_input_lines

instr_ptr = 0
accumulator = 0
program = []

for instr, num in map(lambda x: x.split(" "), get_input_lines(__file__)):
    num = int(num)
    program.append((instr, num))

visited = set()
while True:
    if instr_ptr in visited:
        break

    visited.add(instr_ptr)

    instr, num = program[instr_ptr]
    if instr == "nop":
        instr_ptr += 1
    elif instr == "acc":
        instr_ptr += 1
        accumulator += num
    elif instr == "jmp":
        instr_ptr += num
    else:
        raise ValueError(f"Unknown instruction {instr}")

print(accumulator)
