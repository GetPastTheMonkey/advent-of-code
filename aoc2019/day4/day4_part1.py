from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    minimum, maximum = map(int, f.readline().split("-"))


def test_not_decreasing(l):
    return l[0] <= l[1] <= l[2] <= l[3] <= l[4] <= l[5]


def test_adjacent(l):
    return l[0] == l[1] or l[1] == l[2] or l[2] == l[3] or l[3] == l[4] or l[4] == l[5]


possible_passwords = 0
for num in range(minimum, maximum + 1):
    number_as_list = map(int, str(num))
    if test_adjacent(number_as_list) and test_not_decreasing(number_as_list):
        possible_passwords += 1

print("Number of possible passwords: {}".format(possible_passwords))
