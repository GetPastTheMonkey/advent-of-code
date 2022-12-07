import re
from hashlib import md5

SALT = "yjdafjpo"


class LookupTable:
    def __init__(self, key_stretching):
        self._key_stretching = key_stretching
        self._table = dict()

    def __getitem__(self, item: int) -> str:
        if item not in self._table:
            value = SALT + str(item)
            nr_hashes = 2017 if self._key_stretching else 1

            for _ in range(nr_hashes):
                value = md5(value.encode()).hexdigest().lower()

            self._table[item] = value
        return self._table[item]


def day14_solve(key_stretching: bool) -> int:
    lut = LookupTable(key_stretching)
    keys = []
    idx = 0

    while len(keys) < 64:
        has_3 = re.search(r"(\w)\1{2}", lut[idx])

        if has_3:
            char = has_3.group(1)

            for offset in range(1, 1000):
                has_5 = re.search(rf"({char})\1{{4}}", lut[idx + offset])

                if has_5:
                    keys.append(idx)
                    print(f"Add new key #{len(keys):02}: {idx}")
                    break
        idx += 1

    return keys[-1]
