from utils import chunk

INITIAL = "00111101111101000"


def dragon_curve(a: str) -> str:
    b = a[::-1]
    b_flipped = "".join("1" if b_i == "0" else "0" for b_i in b)
    return a + "0" + b_flipped


def day16_solve(part_1: bool) -> str:
    random_data = INITIAL
    disk_size = 272 if part_1 else 35651584

    while len(random_data) < disk_size:
        random_data = dragon_curve(random_data)

    checksum = random_data[:disk_size]

    while len(checksum) % 2 == 0:
        pairs = chunk(checksum, 2)
        checksum = "".join(["1" if p[0] == p[1] else "0" for p in pairs])

    return checksum
