from os.path import join, dirname, realpath

# Load file
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    polymer_file = f.readline()


def react_polymer(polymer):
    changed = False
    return_polymer = []
    skip_next = False

    for i in range(len(polymer)-1):
        diff = abs(ord(polymer[i]) - ord(polymer[i+1]))
        if diff != 32 and not skip_next:
            return_polymer.append(polymer[i])
        elif skip_next:
            skip_next = False
        else:
            changed = True
            skip_next = True

    if not skip_next:
        return_polymer.append(polymer[len(polymer)-1])

    return changed, ''.join(return_polymer)


polymer_changed = True
while polymer_changed:
    polymer_changed, polymer_file = react_polymer(polymer_file)

print("The resulting polymer is {} characters long".format(len(polymer_file)))
