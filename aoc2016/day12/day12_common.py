from utils import get_input_lines


def day12_solve(init_c: int) -> int:
    registers = {
        "a": 0,
        "b": 0,
        "c": init_c,
        "d": 0,
    }

    curr_idx = 0
    lines = list(map(lambda x: x.split(" "), get_input_lines(__file__)))

    while True:
        commands = lines[curr_idx]

        if commands[0] == "cpy":
            registers[commands[2]] = registers[commands[1]] if commands[1] in registers else int(commands[1])
        elif commands[0] == "inc":
            registers[commands[1]] += 1
        elif commands[0] == "dec":
            registers[commands[1]] -= 1
        elif commands[0] == "jnz":
            jnz = registers[commands[1]] if commands[1] in registers else int(commands[1])

            if jnz != 0:
                offset = registers[commands[2]] if commands[2] in registers else int(commands[2])

                if offset == 0:
                    raise ValueError("Infinite loop detected!")

                curr_idx = curr_idx + offset - 1  # Minus 1 because end of loop will add 1 again

        curr_idx += 1

        if not (0 <= curr_idx < len(lines)):
            return registers["a"]
