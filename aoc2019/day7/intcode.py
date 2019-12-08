class IntcodeComputer(object):
    def __init__(self, phase=0, clear_input=True):
        self._instr_ptr = 0
        self._instr = []
        self._mode = []
        self._input = None
        self._phase = phase
        self._first_input = True
        self._output = None
        self._is_finished = False
        self._clear_input = clear_input
        super(IntcodeComputer, self).__init__()

    def set_input(self, inp):
        self._input = inp

    def _get_input(self):
        if self._first_input:
            self._first_input = False
            return self._phase, False
        else:
            inp = self._input
            imp_is_none = self._input is None
            if self._clear_input:
                self._input = None
            return inp, imp_is_none

    def run(self, instr):
        self._instr = instr
        self._instr_ptr = 0
        self._mode = []
        self._is_finished = False
        return self.resume()

    def resume(self):
        should_stop = False
        while not should_stop:
            should_stop = self._run_step()
        return self._is_finished

    @property
    def instructions(self):
        return self._instr.copy()

    @property
    def finished(self):
        return self._is_finished

    def _put_output(self, output):
        self._output = output

    def get_output(self):
        return self._output

    def _get_value(self, offset):
        address = self._instr[self._instr_ptr + offset]
        try:
            if self._mode[-offset] == 1:
                return address
        except IndexError:
            pass
        return self._instr[address]

    def _run_step(self):
        opcode_mode = self._instr[self._instr_ptr]
        opcode = opcode_mode % 100
        self._mode = list(map(int, str(opcode_mode // 100)))

        should_stop = False

        if opcode == 1:
            op1 = self._get_value(1)
            op2 = self._get_value(2)
            self._instr[self._instr[self._instr_ptr + 3]] = op1 + op2
            self._instr_ptr += 4
        elif opcode == 2:
            op1 = self._get_value(1)
            op2 = self._get_value(2)
            self._instr[self._instr[self._instr_ptr + 3]] = op1 * op2
            self._instr_ptr += 4
        elif opcode == 3:
            inp, inp_is_none = self._get_input()
            if inp_is_none:
                should_stop = True
            else:
                self._instr[self._instr[self._instr_ptr + 1]] = inp
                self._instr_ptr += 2
        elif opcode == 4:
            self._put_output(self._get_value(1))
            self._instr_ptr += 2
        elif opcode == 5:
            check = self._get_value(1)
            if check == 0:
                self._instr_ptr += 3
            else:
                self._instr_ptr = self._get_value(2)
        elif opcode == 6:
            check = self._get_value(1)
            if check == 0:
                self._instr_ptr = self._get_value(2)
            else:
                self._instr_ptr += 3
        elif opcode == 7:
            left = self._get_value(1)
            right = self._get_value(2)
            self._instr[self._instr[self._instr_ptr + 3]] = 1 if left < right else 0
            self._instr_ptr += 4
        elif opcode == 8:
            left = self._get_value(1)
            right = self._get_value(2)
            self._instr[self._instr[self._instr_ptr + 3]] = 1 if left == right else 0
            self._instr_ptr += 4
        elif opcode == 99:
            should_stop = True
            self._is_finished = True
        else:
            raise ValueError("Encountered unknown opcode {}. Terminating immediately!".format(opcode))

        # print("\tOpcode was {}, new instruction pointer is {}".format(opcode, self._instr_ptr))
        return should_stop
