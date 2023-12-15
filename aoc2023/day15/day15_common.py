def day15_hash(word: str) -> int:
    curr_val = 0

    for c in word:
        curr_val = (17 * (curr_val + ord(c))) % 256

    return curr_val
