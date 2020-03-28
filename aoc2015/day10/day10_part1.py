from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    number = f.read()

iterations = 40
for i in range(iterations):
    new_number = ""
    current_digit = None
    current_digit_count = 0
    for digit in number:
        if current_digit is None:
            current_digit = digit
            current_digit_count = 1
        elif digit == current_digit:
            current_digit_count += 1
        else:
            new_number += "{}{}".format(current_digit_count, current_digit)
            current_digit = digit
            current_digit_count = 1

    if current_digit_count > 0:
        new_number += "{}{}".format(current_digit_count, current_digit)

    number = new_number

print(len(number))
