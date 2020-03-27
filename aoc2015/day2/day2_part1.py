from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    total = 0
    for line in f:
        x, y, z = map(int, line.split("x"))
        s1, s2, s3 = x*y, x*z, y*z
        total += 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)

print(total)
