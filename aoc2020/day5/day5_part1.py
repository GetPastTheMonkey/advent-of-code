from utils import get_input_lines

max_seat_id = 0

for line in get_input_lines(__file__):
    seat_id = 0

    for i in map(lambda x: 1 if x == "B" or x == "R" else 0, line):
        seat_id *= 2
        seat_id += i

    max_seat_id = max(max_seat_id, seat_id)

print(max_seat_id)
