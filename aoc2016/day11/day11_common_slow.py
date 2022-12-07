import itertools
from queue import Queue

TUTORIAL = False
IS_PART_1 = None


class Elements:
    # Part 1
    ELEVATOR = 0
    PLUTONIUM = 1
    PROMETHIUM = 2
    RUTHENIUM = 3
    STRONTIUM = 4
    THULIUM = 5

    # Part 2
    ELERIUM = 6
    DILITHIUM = 7

    # Tutorial
    HYDROGEN = 8
    LITHIUM = 9

    _PART_1 = [PLUTONIUM, PROMETHIUM, RUTHENIUM, STRONTIUM, THULIUM]
    _PART_2 = [PLUTONIUM, PROMETHIUM, RUTHENIUM, STRONTIUM, THULIUM, ELERIUM, DILITHIUM]
    _SIMPLE = [HYDROGEN, LITHIUM]

    @classmethod
    def get_elements(cls):
        if TUTORIAL:
            return cls._SIMPLE

        if IS_PART_1 is None:
            raise ValueError("Initialize variable \"IS_PART_1\" first")
        elif IS_PART_1:
            return cls._PART_1
        else:
            return cls._PART_2


class State:
    _MASKS = {
        # Part 1
        Elements.ELEVATOR:      0b110000000000000000000000000000,
        Elements.PLUTONIUM:     0b001111000000000000000000000000,
        Elements.PROMETHIUM:    0b000000111100000000000000000000,
        Elements.RUTHENIUM:     0b000000000011110000000000000000,
        Elements.STRONTIUM:     0b000000000000001111000000000000,
        Elements.THULIUM:       0b000000000000000000111100000000,

        # Part 2
        Elements.ELERIUM:       0b000000000000000000000011110000,
        Elements.DILITHIUM:     0b000000000000000000000000001111,

        # Tutorial
        Elements.HYDROGEN:  0b001111000000000000000000000000,
        Elements.LITHIUM:   0b000000111100000000000000000000,
    }

    _SHIFTS = {
        # Part 1
        Elements.ELEVATOR: 28,
        Elements.PLUTONIUM: 24,
        Elements.PROMETHIUM: 20,
        Elements.RUTHENIUM: 16,
        Elements.STRONTIUM: 12,
        Elements.THULIUM: 8,

        # Part 2
        Elements.ELERIUM: 4,
        Elements.DILITHIUM: 0,

        # Tutorial
        Elements.HYDROGEN: 24,
        Elements.LITHIUM: 20,
    }

    def __init__(self):
        self._state = 0

    def __repr__(self):
        binary = f"{self._state:032b}"
        n = 4
        split = [binary[i:i + n] for i in range(0, len(binary), n)]
        split = [f"G:{int(s[:2], 2)+1} M:{int(s[2:], 2)+1}" for s in split]

        result = ""
        if TUTORIAL:
            result += "ELEVATOR\tHYDROGEN\tLITHIUM\n"
        elif IS_PART_1:
            result += "ELEVATOR\tPLUTONIUM\tPROMETHIUM\tRUTHENIUM\tSTRONTIUM\tTHULIUM\n"
        else:
            result += "ELEVATOR\tPLUTONIUM\tPROMETHIUM\tRUTHENIUM\tSTRONTIUM\tTHULIUM\t\tELERIUM\t\tDILITHIUM\n"
        result += "\t\t".join(split) + "\n"
        return result

    def __eq__(self, other):
        if isinstance(other, State):
            return self._state == other._state
        return False

    def __copy__(self):
        return State.from_int(self.to_int())

    def to_int(self):
        return self._state

    @staticmethod
    def from_int(n: int):
        s = State()
        s._state = n
        return s

    ###############
    #   SETTERS   #
    ###############

    def _set_element(self, element, floor, additional):
        assert 0 <= floor <= 3, "Invalid floor"

        shift = self._SHIFTS[element] + additional
        mask = self._MASKS[element] & (0b11 << shift)
        zeroed_out = self._state & ~mask
        new_part = floor << shift
        self._state = zeroed_out | new_part

    def set_elevator(self, floor):
        self._set_element(Elements.ELEVATOR, floor, 0)

    def set_generator(self, element, floor):
        self._set_element(element, floor, 2)

    def set_microchip(self, element, floor):
        self._set_element(element, floor, 0)

    ###############
    #   GETTERS   #
    ###############

    def _floor_element(self, element: int) -> int:
        return (self._state & self._MASKS[element]) >> self._SHIFTS[element]

    def floor_elevator(self) -> int:
        return self._floor_element(Elements.ELEVATOR)

    def floor_generator(self, element: int) -> int:
        return (self._floor_element(element) & 0b1100) >> 2

    def floor_microchip(self, element: int) -> int:
        return self._floor_element(element) & 0b11

    ###############
    #   BOOLEAN   #
    ###############

    def is_valid(self):
        for element in Elements.get_elements():
            ele_gen = self.floor_generator(element)
            ele_mic = self.floor_microchip(element)

            if ele_gen != ele_mic:
                # The generator is not on the same floor as the microchip
                # Need to check if any other generator is on the same floor
                for other in Elements.get_elements():
                    if element == other:
                        # Not interested in the same element
                        continue

                    other_gen = self.floor_generator(other)
                    other_mic = self.floor_microchip(other)

                    if other_gen == other_mic:
                        # The other element is safe
                        continue

                    if other_gen == ele_mic:
                        # Another generator is on the same floor without its microchip
                        # This state is invalid!!
                        return False
        return True

    ###############
    # NEXT STATES #
    ###############

    def next_states(self):
        my_floor = self.floor_elevator()

        # Get all entities (generators and microchips) on my floor
        entities_on_my_floor = []  # left: true iff entity is generator, right is the element
        for element in Elements.get_elements():
            if self.floor_generator(element) == my_floor:
                entities_on_my_floor.append((True, element))
            if self.floor_microchip(element) == my_floor:
                entities_on_my_floor.append((False, element))

        # Find all combinations who to take 1 or 2 elements with me
        combinations = []
        combinations.extend(itertools.combinations(entities_on_my_floor, 1))
        combinations.extend(itertools.combinations(entities_on_my_floor, 2))

        # Find all possible states based on the found combinations
        states = []

        for take_with_me in combinations:
            if my_floor > 0:
                new = self.__copy__()
                new.set_elevator(my_floor - 1)
                for is_generator, element in take_with_me:
                    if is_generator:
                        new.set_generator(element, my_floor - 1)
                    else:
                        new.set_microchip(element, my_floor - 1)

                if new.is_valid():
                    states.append(new)

            if my_floor < 3:
                new = self.__copy__()
                new.set_elevator(my_floor + 1)
                for is_generator, element in take_with_me:
                    if is_generator:
                        new.set_generator(element, my_floor + 1)
                    else:
                        new.set_microchip(element, my_floor + 1)

                if new.is_valid():
                    states.append(new)

        return states


def load_state():
    s = State()

    if TUTORIAL:
        # Floor 0
        s.set_elevator(0)
        s.set_microchip(Elements.HYDROGEN, 0)
        s.set_microchip(Elements.LITHIUM, 0)

        # Floor 1
        s.set_generator(Elements.HYDROGEN, 1)

        # Floor 2
        s.set_generator(Elements.LITHIUM, 2)
    else:
        # Floor 0
        s.set_elevator(0)
        s.set_generator(Elements.THULIUM, 0)
        s.set_microchip(Elements.THULIUM, 0)
        s.set_generator(Elements.PLUTONIUM, 0)
        s.set_generator(Elements.STRONTIUM, 0)

        # Floor 1
        s.set_microchip(Elements.PLUTONIUM, 1)
        s.set_microchip(Elements.STRONTIUM, 1)

        # Floor 2
        s.set_generator(Elements.PROMETHIUM, 2)
        s.set_microchip(Elements.PROMETHIUM, 2)
        s.set_generator(Elements.RUTHENIUM, 2)
        s.set_microchip(Elements.RUTHENIUM, 2)

        # Floor 3: Empty

        if not IS_PART_1:
            # Additionally, add elerium and dilithium to first floor
            s.set_generator(Elements.ELERIUM, 0)
            s.set_microchip(Elements.ELERIUM, 0)
            s.set_generator(Elements.DILITHIUM, 0)
            s.set_microchip(Elements.DILITHIUM, 0)

    return s


def final_state():
    s = State()

    # Everything on floor 3
    floor = 3
    s.set_elevator(floor)

    for element in Elements.get_elements():
        s.set_microchip(element, floor)
        s.set_generator(element, floor)

    return s


#####


def day11_solve(is_part_1):
    # Initialize global boolean flag
    global IS_PART_1
    IS_PART_1 = is_part_1

    # Initialize queue with initial state
    to_do = Queue()
    to_do.put_nowait((load_state().to_int(), []))
    visited = dict()

    # Wanted state
    final = final_state().to_int()

    largest_so_far = 0

    # While not empty, process next element
    while not to_do.empty():
        state, history = to_do.get_nowait()
        so_far = len(history)

        if so_far > largest_so_far:
            print(f"Reached new length: {so_far}")
            largest_so_far = so_far

        if state in visited:
            continue

        if state == final:
            for idx, h in enumerate(history):
                print(f"\nState {idx}:")
                print(State.from_int(h))
            print(State.from_int(state))
            print(so_far)
            break

        # I am visiting this for the first time - with the lowest distance because FIFO queue!!
        visited[state] = so_far

        s = State.from_int(state)
        for next_state in s.next_states():
            next_state_int = next_state.to_int()

            if next_state_int not in visited:
                to_do.put_nowait((next_state_int, history + [state]))
