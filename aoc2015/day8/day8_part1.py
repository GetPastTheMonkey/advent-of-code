import re
from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    total_length = 0
    for word in f:
        word = word.strip()
        memory = word[1:-1]
        memory = memory.replace("\\\\", " ")
        memory = memory.replace("\\\"", " ")
        memory = re.sub("\\\\x..", " ", memory)
        total_length += len(word) - len(memory)

print(total_length)
