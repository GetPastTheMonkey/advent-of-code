from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    line = f.readline().split(" ")
    row_final = int(line[-3][:-1])
    col_final = int(line[-1][:-2])

row, col = 1, 1

x = 20151125
multi = 252533
div = 33554393

while True:
    # Update coordinates
    if row == 1:
        row = col + 1
        col = 1
        print("Starting row {}. {} rows to go".format(row, row_final + col_final - row))
    else:
        row -= 1
        col += 1

    # Generate next value
    x = (x * multi) % div

    # Check if last coordinates
    if row == row_final and col == col_final:
        print(x)
        break
