from hashlib import md5


def main():
    puzzle_input = "ugkcyxxp"
    iteration = 0
    password = ""
    password_length = 8

    while True:
        iteration_try = f"{puzzle_input}{iteration}".encode()
        hashed_hex = md5(iteration_try).hexdigest()

        if hashed_hex.startswith("0" * 5):
            password = password + hashed_hex[5]
            print("Found new character in password!")

            if len(password) == password_length:
                break

        iteration += 1

    print(password)


if __name__ == '__main__':
    main()
