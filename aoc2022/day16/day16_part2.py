from datetime import datetime

from aoc2022.day16.day16_common import VALVES, DISTANCES, FLOWS, START

ABSOLUTE_BEST = 0


def recursion(my_minutes, my_room, el_minutes, el_room, open_valves, so_far) -> int:
    global ABSOLUTE_BEST

    # Theoretical maximum: All valves are opened after the next turn
    theoretical_max = max(my_minutes - 1, el_minutes - 1) * sum(map(lambda x: FLOWS[x], set(VALVES) - open_valves))

    if so_far + theoretical_max < ABSOLUTE_BEST:
        # Immediately return if the current best solution is better than the current value plus the theoretical max
        return so_far

    largest = so_far

    for my_v in VALVES:
        if my_v == my_room:
            continue

        if my_v in open_valves:
            continue

        my_dist = DISTANCES[my_room][my_v]
        my_move_valid = my_minutes > my_dist
        my_minutes_left = my_minutes - my_dist - 1 if my_move_valid else my_minutes
        my_next_room = my_v if my_move_valid else my_room
        my_so_far_increment = my_minutes_left * FLOWS[my_next_room] if my_move_valid else 0

        for el_v in VALVES:
            if el_v == el_room:
                continue

            if el_v in open_valves:
                continue

            if my_v == el_v:
                continue

            el_dist = DISTANCES[el_room][el_v]
            el_move_valid = el_minutes > el_dist
            el_minutes_left = el_minutes - el_dist - 1 if el_move_valid else el_minutes
            el_next_room = el_v if el_move_valid else el_room
            el_so_far_increment = el_minutes_left * FLOWS[el_next_room] if el_move_valid else 0

            if not my_move_valid and not el_move_valid:
                continue

            largest = max(largest, recursion(
                my_minutes=my_minutes_left,
                my_room=my_next_room,
                el_minutes=el_minutes_left,
                el_room=el_next_room,
                open_valves=open_valves | {my_v, el_v},
                so_far=so_far + my_so_far_increment + el_so_far_increment
            ))

    if largest > ABSOLUTE_BEST:
        print(f"{datetime.now()} - Found new largest value: {largest} (If unchanged for 15 minutes, try submitting...)")
        ABSOLUTE_BEST = largest
    return largest


if __name__ == '__main__':
    print(recursion(26, START, 26, START, set(), 0))
