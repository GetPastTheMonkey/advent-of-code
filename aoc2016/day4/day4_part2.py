import re

from utils import get_input_lines


def main():
    for line in get_input_lines(__file__):
        r = re.match(r"(?P<enc_name>[a-z-]+)-(?P<sector>[0-9]+)\[[a-z]+]", line)
        enc_name = r.group("enc_name")
        sector = int(r.group("sector"))

        dec_name = "".join([chr(((ord(x) - ord("a") + sector) % 26) + ord("a")) if x != "-" else " " for x in enc_name])

        if dec_name == "northpole object storage":
            print(sector)
            break


if __name__ == '__main__':
    main()
