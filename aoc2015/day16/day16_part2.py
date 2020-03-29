from os.path import join, dirname, realpath

correct_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        line_split = line.strip()[4:].split()
        aunt_nr = int(line_split[0][:-1])

        candidate = True

        for i in range(1, len(line_split), 2):
            category = line_split[i][:-1]
            amount = line_split[i + 1]
            amount = int(amount[:-1]) if ',' in amount else int(amount)

            if category in ["cats", "trees"]:
                if correct_aunt[category] >= amount:
                    candidate = False
                    break
            elif category in ["pomeranians", "goldfish"]:
                if correct_aunt[category] <= amount:
                    candidate = False
                    break
            elif correct_aunt[category] != amount:
                candidate = False
                break

        if candidate:
            print(aunt_nr)
