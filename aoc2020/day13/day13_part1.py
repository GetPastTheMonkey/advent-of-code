from utils import get_input_lines

arrival, bus_ids = get_input_lines(__file__)
arrival = int(arrival)

smallest_bus_id = None
smallest_wait = None

for bus_id in bus_ids.split(","):
    if bus_id == "x":
        continue

    bus_id = int(bus_id)
    bus_wait = bus_id - (arrival % bus_id)

    if smallest_wait is None or bus_wait < smallest_wait:
        smallest_wait = bus_wait
        smallest_bus_id = bus_id

print(smallest_wait * smallest_bus_id)
