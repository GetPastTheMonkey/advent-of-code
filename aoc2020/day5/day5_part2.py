from utils import get_input_lines

nr_seats = 1024
free_seats = set()
for i in range(nr_seats):
    free_seats.add(i)

for line in get_input_lines(__file__):
    seat_id = 0

    for i in map(lambda x: 1 if x == "B" or x == "R" else 0, line):
        seat_id *= 2
        seat_id += i

    free_seats.remove(seat_id)

free_seats = [sid for sid in free_seats if sid + 1 not in free_seats and sid - 1 not in free_seats]
print(free_seats[0])
