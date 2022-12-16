from aoc2022.day16.day16_common import VALVES, DISTANCES, FLOWS, START


def recursion(minutes, room, open_valves, so_far) -> int:
    largest = so_far

    for v in VALVES:
        if v == room:
            # Already in this room
            continue

        if v in open_valves:
            # Valve already open, no need to return
            continue

        if minutes <= DISTANCES[room][v]:
            # Cannot reach room in the available time (equality because we need 1 more to open the valve)
            continue

        largest = max(largest, recursion(
            minutes=minutes - DISTANCES[room][v] - 1,
            room=v,
            open_valves=open_valves | {v},
            so_far=so_far + ((minutes - DISTANCES[room][v] - 1) * FLOWS[v])
        ))

    return largest


if __name__ == '__main__':
    print(recursion(30, START, set(), 0))
