from utils import get_input_lines

jolts = []
for line in get_input_lines(__file__):
    jolts.append(int(line))

jolts.sort()
diff_count = [0, 0, 0]
jolt = 0

for j in jolts:
    diff = j - jolt
    if 0 < diff < len(diff_count) + 1:
        diff_count[diff - 1] += 1
    jolt = j

# Add another difference of 3
diff_count[2] += 1
print(diff_count[0] * diff_count[2])
