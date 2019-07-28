import heapq
from itertools import count
from os.path import join, dirname, realpath


class Unit:
    _INITIAL_HP = 200
    HP_LOSS_ON_HIT = 3

    def __init__(self, position, team):
        self._position = position
        self._team = team
        self._hp = self._INITIAL_HP

    def __str__(self):
        return "{} at {} with {} HP".format(self._team, self._position, self._hp)

    def is_alive(self):
        return self._hp > 0

    def position(self):
        return self._position

    def hp(self):
        return self._hp

    def team(self):
        return self._team

    def register_hit(self):
        self._hp -= self.HP_LOSS_ON_HIT

    def move_to(self, new_position):
        self._position = new_position


class Goblin(Unit):
    HP_LOSS_ON_HIT = None


class ElfDiedException(Exception):
    pass


class Game:
    def __init__(self, grid):
        self._walls = set()
        self._units = []
        self._round_count = 0
        for x, line in enumerate(grid):
            for y, c in enumerate(line):
                if c == '#':
                    self._walls.add((x, y))
                elif c == 'E':
                    self._units.append(Unit((x, y), c))
                elif c == 'G':
                    self._units.append(Goblin((x, y), c))

    def _shortest_path(self, start_position, end_positions, occupied_fields):
        result = []
        best = None
        visited_nodes = occupied_fields
        queue = [(0, [start_position])]
        heapq.heapify(queue)

        while queue:
            distance, path = heapq.heappop(queue)

            if best and len(path) > best:
                return result

            node = path[-1]

            if node in end_positions:
                result.append(path)
                best = len(path)
                continue

            if node in visited_nodes:
                continue

            visited_nodes.add(node)
            x, y = node
            node_neighbours = [(x + dx, y + dy) for (dx, dy) in [(-1, 0), (0, -1), (0, 1), (1, 0)]]
            for node_neighbour in node_neighbours:
                if node_neighbour in visited_nodes:
                    continue
                heapq.heappush(queue, (distance + 1, path + [node_neighbour]))

        return result

    def _get_move_for_unit(self, unit):
        possible_targets = set(u.position() for u in self._units if u.team() != unit.team() and u.is_alive())
        if not possible_targets:
            # No target found, return None
            return None

        # Get adjacent fields of targets
        possible_targets_adjacent = set([(x + dx, y + dy) for (x, y) in possible_targets for (dx, dy) in [(-1, 0), (0, -1), (0, 1), (1, 0)]])

        # Get all occupied fields
        occupied = set(u.position() for u in self._units if u != unit and u.is_alive()) | self._walls

        # Subtract to get all moves in range
        moves_in_range = possible_targets_adjacent - occupied
        if not moves_in_range:
            # There is no free space, stay where the unit is
            return unit.position()
        elif unit.position() in moves_in_range:
            # The unit is already in an optimal position
            return unit.position()

        # Calculate shortest paths to in-range target positions
        paths = self._shortest_path(unit.position(), moves_in_range, occupied)
        reachable_endpoints = [path[-1] for path in paths]
        if not reachable_endpoints:
            # Cannot reach any of the proposed positions, do not move
            return unit.position()
        target_position = min(reachable_endpoints)

        # Calculate next move towards target position
        next_positions = [path[1] for path in paths if path[-1] == target_position]
        return min(next_positions)

    def _distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def run(self):
        while self._round():
            pass
        return self._round_count, sum([unit.hp() for unit in self._units if unit.is_alive()])

    def _round(self):
        # Sort units
        self._units.sort(key=(lambda u: u.position()))

        # Loop through units, move and attack
        for unit in self._units:
            # Check if unit was killed earlier in the round
            if not unit.is_alive():
                continue

            # Get next move for current unit
            move = self._get_move_for_unit(unit)
            if move is None:
                # Cannot reach another unit, abort battle
                return False

            # Move unit
            unit.move_to(move)

            # Make attack if stands next to an enemy
            adjacent_units_tuples = [(unit2.hp(), unit2.position(), unit2) for unit2 in self._units if unit.team() != unit2.team() and unit2.is_alive() and self._distance(unit.position(), unit2.position()) == 1]
            if adjacent_units_tuples:
                attack_target = min(adjacent_units_tuples)[2]
                attack_target.register_hit()

                # Check if target was elf and if the elf died
                if attack_target.team() == "E" and not attack_target.is_alive():
                    raise ElfDiedException

        # Remove dead units from unit list
        new_units = []
        for unit in self._units:
            if unit.is_alive():
                new_units.append(unit)
        self._units = new_units

        self._round_count += 1
        return True


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for power in count(4):
    Goblin.HP_LOSS_ON_HIT = power
    game = Game(lines)
    try:
        rounds, hp_sum = game.run()
        print("The battle lasted {} rounds and the HP sum of all alive units is {}".format(rounds, hp_sum))
        print("Solution: {}".format(rounds * hp_sum))
        print("Elf attack power was {}".format(power))
        break
    except ElfDiedException:
        pass
