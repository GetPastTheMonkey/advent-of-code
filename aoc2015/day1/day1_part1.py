from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    c = 0
    for char in f.read():
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
        else:
            raise ValueError("Invalid character")

print(c)
