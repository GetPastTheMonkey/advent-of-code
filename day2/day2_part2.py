from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    box_ids = f.readlines()

solution_1 = None
solution_2 = None

for key_1, box_id_1 in enumerate(box_ids):
    for key_2, box_id_2 in enumerate(box_ids):
        if key_1 < key_2:
            distance = sum([1 for c1, c2 in zip(box_id_1, box_id_2) if c1 != c2])
            if distance < 2:
                solution_1 = box_id_1
                solution_2 = box_id_2
                break
        if solution_1 is not None and solution_2 is not None:
            break

print "Found the following words:\n\t{}\t{}".format(solution_1, solution_2)
print "Solution: {}".format(''.join([c1 for c1, c2 in zip(solution_1, solution_2) if c1 == c2]))
