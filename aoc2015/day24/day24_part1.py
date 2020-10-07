import math
from os.path import join, dirname, realpath

PACKAGES = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        PACKAGES.append(int(line.strip()))

GROUP_SIZE = sum(PACKAGES) / 3


def get_package_combinations(packages_so_far, packages_left):
    current_sum = sum(packages_so_far)
    left_sum = sum(packages_left)

    if current_sum == GROUP_SIZE:
        # Hit the target spot on
        return [packages_so_far]
    if current_sum > GROUP_SIZE:
        # Overshot target size
        return []
    if current_sum + left_sum == GROUP_SIZE:
        # Only way to hit target size is if all left elements are taken
        return [packages_so_far + packages_left]
    if current_sum + left_sum < GROUP_SIZE:
        # Cannot reach desired size even with all packages
        return []

    result = []

    # Case 1: Take next_item into packages_so_far
    result.extend(get_package_combinations(packages_so_far + [packages_left[0]], packages_left[1:]))

    # Case 2: Do not take next_item into packages_so_far
    result.extend(get_package_combinations(packages_so_far, packages_left[1:]))

    return result


print("Generating all possible combinations to reach group size {}... (might take a few minutes)".format(GROUP_SIZE))
possible_solutions = get_package_combinations([], PACKAGES)
print("Finished generating combinations. Searching for the best one...")
min_length = len(PACKAGES) + 1
min_product = 0

for sol in possible_solutions:
    len_sol = len(sol)
    prod_sol = math.prod(sol)
    if len_sol < min_length:
        min_length = len_sol
        min_product = prod_sol
    elif len_sol == min_length and prod_sol < min_product:
        min_product = prod_sol

print(min_product)
