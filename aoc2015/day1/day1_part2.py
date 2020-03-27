from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    c = 0
    pos = 0
    for char in f.read():
        pos += 1
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
        else:
            raise ValueError("Invalid character")

        if c < 0:
            print(pos)
            exit()

print("Santa never went to the basement!")
