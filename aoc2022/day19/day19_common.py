from queue import Queue

from utils import get_input_lines


def load_data():
    for line in get_input_lines(__file__):
        if len(line) == 0:
            continue

        items = line.split()

        yield (
            int(items[1][:-1]),
            int(items[6]),
            int(items[12]),
            int(items[18]),
            int(items[21]),
            int(items[27]),
            int(items[30]),
        )


def max_obsidian(costs, time):
    queue = Queue()
    queue.put((
        (0, 0, 0, 0),  # Materials (ore, clay, obsidian, geode)
        (1, 0, 0, 0),  # Robots (ore, clay, obsidian, geode)
        time           # Time left
    ))

    best = 0
    cache = set()

    while not queue.empty():
        materials, robots, time = queue.get()

        best = max(best, materials[-1])

        if time == 0:
            continue

        num_costs = len(costs[0])
        max_costs = tuple(max(cost[i] for cost in costs) for i in range(num_costs))

        # For each cost: Only have as many robots as can be spent per turn
        # Then add last robot unchanged, as this is not related to costs
        robots = tuple([min(robots[i], max_costs[i]) for i in range(num_costs)] + [robots[-1]])

        # For each cost: Only have as many materials as can be spent
        # Then add last material unchanged, as this is not related to spending
        materials = tuple([min(materials[i], time * max_costs[i] - robots[i] * (time - 1)) for i in range(num_costs)] +
                          [materials[-1]])

        state = materials, robots, time

        if state in cache:
            continue

        cache.add(state)

        if len(cache) % 1_000_000 == 0:
            print(time, best, len(cache))

        # Always add the option to not purchase anything
        queue.put((
            tuple(m + r for m, r in zip(materials, robots)),
            robots,
            time - 1
        ))

        # Loop through robots
        for idx in range(len(robots)):
            # Check if enough materials are available
            if all(materials[i] >= costs[idx][i] for i in range(num_costs)):
                # enough materials are available -> Set materials and robots accordingly and add to queue

                # New materials: First increment by the number of available robots, then remove costs
                new_materials = list(m + r for m, r in zip(materials, robots))
                new_materials = list(new_materials[i] - costs[idx][i] for i in range(num_costs)) + [new_materials[-1]]

                # New robots: Copy from initial robots, except with the additional purchased robot
                new_robots = list(robots)
                new_robots[idx] += 1

                queue.put((
                    tuple(new_materials),
                    tuple(new_robots),
                    time - 1
                ))

    return best


def day19_solve(part_1: bool) -> int:
    accumulator = 0 if part_1 else 1
    time = 24 if part_1 else 32

    for i, data in enumerate(load_data()):
        costs = [
            (data[1], 0, 0),
            (data[2], 0, 0),
            (data[3], data[4], 0),
            (data[5], 0, data[6]),
        ]

        if not part_1 and i >= 3:
            break

        obs = max_obsidian(costs, time)

        if part_1:
            accumulator += data[0] * obs
        else:
            accumulator *= obs

    return accumulator
