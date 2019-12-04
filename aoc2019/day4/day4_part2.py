from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    minimum, maximum = map(int, f.readline().split("-"))


def test_not_decreasing(l):
    return l[0] <= l[1] <= l[2] <= l[3] <= l[4] <= l[5]


def test_adjacent(l):
    return (l[0] == l[1] and not l[1] == l[2]) or (not l[0] == l[1] and l[1] == l[2] and not l[2] == l[3]) or (
                not l[1] == l[2] and l[2] == l[3] and not l[3] == l[4]) or (
                       not l[2] == l[3] and l[3] == l[4] and not l[4] == l[5]) or (not l[3] == l[4] and l[4] == l[5])


possible_passwords = 0
for num in range(minimum, maximum + 1):
    number_as_list = map(int, str(num))
    if test_adjacent(number_as_list) and test_not_decreasing(number_as_list):
        possible_passwords += 1

print("Number of possible passwords: {}".format(possible_passwords))
