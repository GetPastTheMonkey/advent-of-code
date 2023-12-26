import math
from collections import defaultdict
from enum import Enum
from queue import Queue

from utils import get_input_lines


class NodeType(Enum):
    BROADCAST = 0
    FLIPFLOP = 1
    CONJUNCTION = 2
    UNTYPED = 3


class PulsePropagation:
    def __init__(self):
        self._node_types = defaultdict(lambda: NodeType.UNTYPED)
        self._prev_nodes = defaultdict(list)
        self._next_nodes = defaultdict(list)

        for line in get_input_lines(__file__):
            src, dst = line.split(" -> ")
            dst = dst.split(", ")

            if src.startswith("%"):
                src = src[1:]
                self._node_types[src] = NodeType.FLIPFLOP
            elif src.startswith("&"):
                src = src[1:]
                self._node_types[src] = NodeType.CONJUNCTION
            else:
                self._node_types[src] = NodeType.BROADCAST

            # Handle previous nodes
            for d in dst:
                self._prev_nodes[d].append(src)

            # Handle next nodes
            self._next_nodes[src] = dst

        self._flipflop = {node: False for node in self._node_types.keys()}
        self._conjunction = {node: {prev: False for prev in self._prev_nodes[node]} for node in self._node_types.keys()}

        # Statistics for part 1
        self._low_pulses = 0
        self._high_pulses = 0
        self._button_presses = 0

        # Statistics for part 2
        rx_previous_list = self._prev_nodes["rx"]
        assert len(rx_previous_list) == 1
        self._rx_previous = rx_previous_list[0]
        assert self._node_types[self._rx_previous] == NodeType.CONJUNCTION
        self._cycles = {prev: 0 for prev in self._prev_nodes[self._rx_previous]}

    @property
    def score(self) -> int:
        return self._low_pulses * self._high_pulses

    @property
    def button_presses(self) -> int:
        return self._button_presses

    @property
    def cycles_found(self) -> bool:
        return all(cycle > 0 for cycle in self._cycles.values())

    @property
    def cycles_lcm(self) -> int:
        return math.lcm(*self._cycles.values())

    def push_button(self):
        # Queue state: sender, receiver, signal
        queue = Queue()  # type: Queue[tuple[str, str, bool]]
        queue.put(("button", "broadcaster", False))
        self._button_presses += 1

        while not queue.empty():
            # Get next signal
            sender, receiver, signal = queue.get()

            # PART 1: Increase pulse counter
            if signal:
                self._high_pulses += 1
            else:
                self._low_pulses += 1

            # PART 2: Detect cycle
            if receiver == self._rx_previous and signal and self._cycles[sender] == 0:
                self._cycles[sender] = self._button_presses

            # Determine if a new signal should be sent to the next nodes
            next_signal = False
            send_signal = False

            match self._node_types[receiver]:
                case NodeType.BROADCAST:
                    next_signal = signal
                    send_signal = True
                case NodeType.FLIPFLOP:
                    if not signal:
                        self._flipflop[receiver] = not self._flipflop[receiver]
                        next_signal = self._flipflop[receiver]
                        send_signal = True
                case NodeType.CONJUNCTION:
                    self._conjunction[receiver][sender] = signal
                    next_signal = not all(self._conjunction[receiver].values())
                    send_signal = True

            # Send signal to the next nodes if needed
            if send_signal:
                for n in self._next_nodes[receiver]:
                    queue.put((receiver, n, next_signal))
