from os.path import join, dirname, realpath


class Wire:
    def __init__(self, line):
        line_split = line.split()

        self.output = line_split[-1]
        line_before_arrow = line_split[:-2]

        self._operator = "ASSIGN"
        self._inputs = []

        for entry in line_before_arrow:
            if entry in ["NOT", "AND", "OR", "LSHIFT", "RSHIFT"]:
                self._operator = entry
            else:
                self._inputs.append(int(entry) if entry.isdigit() else entry)

    def is_ready(self):
        return all([isinstance(i, int) for i in self._inputs])

    def update_inputs(self, wire_outputs):
        ins = self._inputs
        self._inputs = []
        for i in ins:
            if i in wire_outputs:
                self._inputs.append(wire_outputs[i])
            else:
                self._inputs.append(i)

    def get_output(self):
        if not self.is_ready():
            raise ValueError("Wire is not yet ready!")

        if self._operator == "ASSIGN":
            return self._inputs[0]
        elif self._operator == "NOT":
            return 65535 - self._inputs[0]
            # return ~self._inputs[0]  # Gives negative values
        elif self._operator == "AND":
            return self._inputs[0] & self._inputs[1]
        elif self._operator == "OR":
            return self._inputs[0] | self._inputs[1]
        elif self._operator == "LSHIFT":
            return self._inputs[0] << self._inputs[1]
        elif self._operator == "RSHIFT":
            return self._inputs[0] >> self._inputs[1]
        else:
            raise ValueError("Unknown operator \"{}\"".format(self._operator))


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    wires = [Wire(l) for l in f]
    signals = dict()

while len(signals) != len(wires):
    for wire in wires:
        if wire.is_ready():
            signals[wire.output] = wire.get_output()
        else:
            wire.update_inputs(signals)

print(signals["a"])
