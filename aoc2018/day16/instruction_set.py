from copy import deepcopy


def addr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] + registers_in[b]
    return out


def addi(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] + b
    return out


def mulr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] * registers_in[b]
    return out


def muli(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] * b
    return out


def banr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] & registers_in[b]
    return out


def bani(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] & b
    return out


def borr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] | registers_in[b]
    return out


def bori(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a] | b
    return out


def setr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = registers_in[a]
    return out


def seti(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = a
    return out


def gtir(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if a > registers_in[b] else 0
    return out


def gtri(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if registers_in[a] > b else 0
    return out


def gtrr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if registers_in[a] > registers_in[b] else 0
    return out


def eqir(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if a == registers_in[b] else 0
    return out


def eqri(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if registers_in[a] == b else 0
    return out


def eqrr(registers_in, a, b, c):
    out = deepcopy(registers_in)
    out[c] = 1 if registers_in[a] == registers_in[b] else 0
    return out


instruction_list = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]
