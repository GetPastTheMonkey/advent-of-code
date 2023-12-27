from aoc2023.day22.day22_common import get_dependencies


def num_fallen(dependencies: list[set[int]], floor_bricks: set[int], removed: set[int]) -> int:
    unsupported = set()  # type: set[int]

    for idx in range(len(dependencies)):
        if idx in removed:
            # This brick has already been removed
            continue

        if idx in floor_bricks:
            # This brick is supported by the floor and can never fall
            continue

        remaining_deps = dependencies[idx] - removed

        if len(remaining_deps) > 0:
            # The brick is still supported by another non-removed brick
            continue

        # At this point, the brick with this index is not supported by any other brick or the ground
        unsupported.add(idx)

    if len(unsupported) == 0:
        # Base condition --> There are no unsupported bricks
        return 0

    # Recursive --> See how removing the unsupported bricks propagates through the system
    # As unsupported is not empty, the removed bricks are strictly increasing. This guarantees termination.
    return len(unsupported) + num_fallen(dependencies, floor_bricks, removed | unsupported)


def main():
    dependencies = get_dependencies()
    floor_bricks = {idx for idx, deps in enumerate(dependencies) if len(deps) == 0}
    print(sum(num_fallen(dependencies, floor_bricks, {idx}) for idx in range(len(dependencies))))


if __name__ == '__main__':
    main()
