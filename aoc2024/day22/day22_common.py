def next_secret(secret: int) -> int:
    secret ^= secret * 64
    secret %= 16777216

    secret ^= secret // 32
    secret %= 16777216

    secret ^= secret * 2048
    secret %= 16777216

    return secret


def get_secrets(initial: int) -> list[int]:
    secret = initial
    secrets = []

    for _ in range(2000):
        secret = next_secret(secret)
        secrets.append(secret)

    return secrets
