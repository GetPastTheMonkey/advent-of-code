from os.path import join, dirname, realpath
from re import match

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    m = match("(?P<p>\d+) players; last marble is worth (?P<m>\d+) points", f.readline())
    player_count = int(m.group("p"))
    marble_max = int(m.group("m"))

circle = [0]
current_marble = 1
current_marble_index = 1
current_player = 0
point_counter = [0 for x in range(player_count)]

while current_marble <= marble_max:
    # Check if current marble has multiple of 23 as value
    if current_marble % 23:
        # Marble is not a multiple of 23 -> Normal case
        current_circle_length = len(circle)
        if current_circle_length > 1:
            insert_index = (current_marble_index+2) % current_circle_length
            if insert_index == 0:
                # Append marble
                circle.append(current_marble)
                current_marble_index = current_circle_length
            else:
                # Insert marble at calculated index
                circle.insert(insert_index, current_marble)
                current_marble_index = insert_index
        else:
            # Circle has only 1 marble, special case
            circle.append(current_marble)
            current_marble_index = 1
    else:
        # Marble is a multiple of 23 -> Special case!
        current_marble_index = (current_marble_index-7) % len(circle)
        point_counter[current_player] += circle.pop(current_marble_index) + current_marble

    # Prepare for next round
    current_marble += 1
    current_player = (current_player+1) % player_count

print "Game finished"
print "The maximum score was: {}".format(max(point_counter))
