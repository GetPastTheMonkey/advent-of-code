from hashlib import md5


def main():
    puzzle_input = "ugkcyxxp"
    missing_char = "_"
    iteration = 0
    password_length = 8
    password = [missing_char] * password_length

    while True:
        iteration_try = f"{puzzle_input}{iteration}".encode()
        hashed_hex = md5(iteration_try).hexdigest()
        iteration += 1

        if hashed_hex.startswith("0"*5):
            position = hashed_hex[5]
            to_put = hashed_hex[6]

            if not (ord("0") <= ord(position) <= ord("7")):
                # Skipping because position is invalid
                continue

            position = int(position)

            if password[position] != missing_char:
                # Skipping because position is already set
                continue

            password[position] = to_put
            print("".join(password))

            if all(map(lambda x: x != missing_char, password)):
                # Stopping because all positions are full
                break


if __name__ == '__main__':
    main()
