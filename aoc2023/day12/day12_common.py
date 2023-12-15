from utils import get_input_lines

CACHE = dict()  # type: dict[tuple[int, int, int], int]


def day12_cached(pattern: str, p_idx: int, groups: list[int], g_idx: int, g_len: int) -> int:
    cache_key = (p_idx, g_idx, g_len)

    if cache_key in CACHE:
        return CACHE[cache_key]

    if p_idx == len(pattern):
        # Base cases
        if g_idx == len(groups) and g_len == 0:
            # Last group has passed and current group length is 0
            return 1
        elif g_idx == len(groups) - 1 and g_len == groups[-1]:
            # Last group is current group and current group has correct length
            return 1
        else:
            # No condition correct -> No correct combination!
            return 0

    # Sum up all possibilities based on current pattern character
    result = 0

    # CASE 1: Current character is "." or "?"
    if pattern[p_idx] in {".", "?"}:
        if g_len == 0:
            # SUB-CASE 1.1: No current group, increase p_idx
            result += day12_cached(pattern, p_idx + 1, groups, g_idx, g_len)
        elif g_idx < len(groups) and g_len == groups[g_idx]:
            # SUB-CASE 1.2: Current group is finished, increase p_idx and g_idx, reset g_len to 0
            result += day12_cached(pattern, p_idx + 1, groups, g_idx + 1, 0)

    # CASE 2: Current character is "#" or "?"
    if pattern[p_idx] in {"#", "?"}:
        # No sub-cases, just increase p_idx and g_len. Case 1 will handle it if it is incorrect
        result += day12_cached(pattern, p_idx + 1, groups, g_idx, g_len + 1)

    CACHE[cache_key] = result
    return result


def day12_solve(*, part_1: bool) -> int:
    s = 0

    for line in get_input_lines(__file__):
        rec, nums = line.split(" ")
        nums = list(map(int, nums.split(",")))

        if not part_1:
            mult = 5
            rec = "?".join(mult * [rec])
            nums = mult * nums

        CACHE.clear()
        s += day12_cached(rec, 0, nums, 0, 0)

    return s
