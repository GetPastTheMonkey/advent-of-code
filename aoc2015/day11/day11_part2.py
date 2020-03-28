from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    password = f.read()


def password_increase(pw):
    pw_list = [ord(d) for d in pw]
    for i in range(1, len(pw_list) + 1):
        overflow_happened = False

        pw_list[-i] += 1

        if pw_list[-i] > ord('z'):
            pw_list[-i] = ord('a')
            overflow_happened = True

        if not overflow_happened:
            break
    return "".join([chr(d) for d in pw_list])


def password_check(pw):
    # Condition 1: Three consecutive letters
    cond1 = any([ord(pw[i]) + 1 == ord(pw[i + 1]) and ord(pw[i]) + 2 == ord(pw[i + 2]) for i in range(len(pw) - 2)])

    # Condition 2: i, o and l are not in the password
    cond2 = all([i not in pw for i in ['i', 'o', 'l']])

    # Condition 3: At least two different pairs of letters
    pairs = []
    for i in range(ord('a'), ord('z') + 1):
        pairs.append("{}{}".format(chr(i), chr(i)))
    cond3 = sum([1 if p in pw else 0 for p in pairs]) >= 2

    return cond1 and cond2 and cond3


while not password_check(password):
    password = password_increase(password)

password = password_increase(password)

while not password_check(password):
    password = password_increase(password)

print(password)
