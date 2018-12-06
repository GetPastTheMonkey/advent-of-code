from os.path import join, dirname, realpath

known_frequencies = []
current_sum = 0
solution = None
round = 0

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    frequency_changes = [int(x) for x in f]

while solution is None:
    round += 1
    print "Starting round {}, solution is {}, current sum is {}, known frequencies has {} entries".format(round, solution, current_sum, len(known_frequencies))
    for next_change in frequency_changes:
        current_sum += next_change

        if current_sum in known_frequencies:
            solution = current_sum
            break
        else:
            known_frequencies.append(current_sum)

print "The solution is: {}".format(solution)
