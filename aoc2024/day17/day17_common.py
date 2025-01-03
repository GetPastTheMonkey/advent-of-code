from utils import get_input_lines


def day17_input() -> tuple[list[int], dict[str, int]]:
    instructions = []
    registers = {"A": 0, "B": 0, "C": 0}

    for line in get_input_lines(__file__):
        if line.startswith("Register"):
            _, reg, val = line.split(" ")
            registers[reg[0]] = int(val)
        elif line.startswith("Program"):
            instructions = [int(i) for i in line.split(": ")[-1].split(",")]

    return instructions, registers


def read_combo(operand: int, registers: dict[str, int]) -> int:
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return registers[chr(ord("A") + operand - 4)]
    else:
        raise ValueError(f"Invalid combo operand: {operand}")


def day17_run(instructions: list[int], registers: dict[str, int]) -> list[int]:
    instr_ptr = 0
    output = []  # type: list[int]

    while 0 <= instr_ptr < len(instructions) - 1:
        opcode, operand = instructions[instr_ptr:instr_ptr + 2]
        is_jump = False

        match opcode:
            case 0:
                registers["A"] = registers["A"] // (2 ** read_combo(operand, registers))
            case 1:
                registers["B"] = registers["B"] ^ operand
            case 2:
                registers["B"] = read_combo(operand, registers) % 8
            case 3:
                if registers["A"] != 0:
                    instr_ptr = operand
                    is_jump = True
            case 4:
                registers["B"] = registers["B"] ^ registers["C"]
            case 5:
                value = read_combo(operand, registers)
                output.append(value % 8)
            case 6:
                registers["B"] = registers["A"] // (2 ** read_combo(operand, registers))
            case 7:
                registers["C"] = registers["A"] // (2 ** read_combo(operand, registers))

        # Advance instruction pointer by 2
        if not is_jump:
            instr_ptr += 2

    return output
