from utils import get_input_lines

input_line = ""
for input_line in get_input_lines(__file__):
    pass

last_time_spoken = dict()
second_last_time_spoken = dict()
last_number = 0
turn_number = 0

for num in map(int, input_line.split(",")):
    turn_number += 1
    if num in last_time_spoken:
        second_last_time_spoken[num] = last_time_spoken[num]
    last_time_spoken[num] = turn_number
    last_number = num

while turn_number < 30_000_000:
    turn_number += 1
    if last_number in second_last_time_spoken:
        last_number = last_time_spoken[last_number] - second_last_time_spoken[last_number]
    else:
        last_number = 0

    if last_number in last_time_spoken:
        second_last_time_spoken[last_number] = last_time_spoken[last_number]
    last_time_spoken[last_number] = turn_number

print(last_number)
