import hashlib
from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    secret = f.read()

number = 1
while True:
    test_str = "{}{}".format(secret, number)
    digest = hashlib.md5(test_str).hexdigest()
    if digest.startswith("000000"):
        print(number)
        exit()
    number += 1
