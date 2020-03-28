from itertools import permutations
from os.path import join, dirname, realpath

distance_matrix = dict()

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        data = line.split()
        destination_1 = data[0]
        destination_2 = data[2]
        distance = int(data[4])

        if destination_1 not in distance_matrix:
            distance_matrix[destination_1] = dict()
        if destination_2 not in distance_matrix:
            distance_matrix[destination_2] = dict()

        distance_matrix[destination_1][destination_2] = distance
        distance_matrix[destination_2][destination_1] = distance

destinations = list(distance_matrix.keys())
candidates = permutations(destinations)

min_length = None
for candidate in candidates:
    route_length = 0
    for i in range(len(candidate) - 1):
        route_length += distance_matrix[candidate[i]][candidate[i+1]]
    if min_length is None or route_length < min_length:
        min_length = route_length

print(min_length)
