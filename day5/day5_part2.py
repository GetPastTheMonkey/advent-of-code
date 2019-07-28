from os.path import join, dirname, realpath
from re import sub

# Load file
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    original_polymer = f.readline()


def react_polymer(polymer):
    changed = False
    return_polymer = []
    skip_next = False

    for k in range(len(polymer) - 1):
        diff = abs(ord(polymer[k]) - ord(polymer[k + 1]))
        if diff != 32 and not skip_next:
            return_polymer.append(polymer[k])
        elif skip_next:
            skip_next = False
        else:
            changed = True
            skip_next = True

    if not skip_next:
        return_polymer.append(polymer[len(polymer) - 1])

    return changed, ''.join(return_polymer)


def fully_react_polymer(polymer):
    changed = True
    while changed:
        changed, polymer = react_polymer(polymer)
    return polymer


char_dict = dict()
for i in range(ord('A'), ord('Z') + 1):
    polymer_to_test = sub('[' + chr(i) + chr(i + 32) + ']', '', original_polymer)
    current_char_polymer = fully_react_polymer(polymer_to_test)
    char_dict[chr(i)] = len(current_char_polymer)
    print("Finished with character {}".format(chr(i)))

min_char = min(char_dict, key=(lambda x: char_dict[x]))
print("The shortest polymer can be achieved by removing type '{}' and it is {} characters long".format(min_char,
                                                                                                       char_dict[
                                                                                                           min_char]))
