from utils import get_input_lines

memory = dict()
mask = ["X"] * 36

for line in get_input_lines(__file__):
    x, y = line.split(" = ")
    if x == "mask":
        mask = list(y)
    else:
        addr = int(x[4:-1])
        val = "{0:036b}".format(int(y))
        final_val = []
        for idx, v in enumerate(val):
            final_val.append(v if mask[idx] == "X" else mask[idx])
        memory[addr] = int("".join(final_val), 2)

print(sum(memory.values()))
