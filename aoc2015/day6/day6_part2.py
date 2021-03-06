from os.path import join, dirname, realpath

coordinates = dict()
for i in range(1000):
    if i not in coordinates:
        coordinates[i] = dict()
    for j in range(1000):
        coordinates[i][j] = 0

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        arr = line.strip().split(" ")

        x_min, y_min = map(int, arr[-3].split(","))
        x_max, y_max = map(int, arr[-1].split(","))

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if len(arr) == 4:
                    # Toggle
                    coordinates[x][y] += 2
                elif arr[1] == "on":
                    coordinates[x][y] += 1
                else:
                    coordinates[x][y] -= 1
                    if coordinates[x][y] < 0:
                        coordinates[x][y] = 0

total = 0
for x in coordinates:
    for y in coordinates[x]:
        total += coordinates[x][y]
print(total)
