from utils import get_input_lines

original_program = []

for instr, num in map(lambda x: x.split(" "), get_input_lines(__file__)):
    num = int(num)
    original_program.append((instr, num))

for idx_to_change in range(len(original_program)):
    program = original_program.copy()
    instr_to_change, num_to_change = program[idx_to_change]
    if instr_to_change == "nop":
        program[idx_to_change] = ("jmp", num_to_change)
    elif instr_to_change == "jmp":
        program[idx_to_change] = ("nop", num_to_change)
    else:
        continue

    instr_ptr = 0
    accumulator = 0

    visited = set()
    while True:
        if instr_ptr in visited or instr_ptr > len(program) - 1:
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

    if instr_ptr > len(program) - 1:
        print(accumulator)
        break
