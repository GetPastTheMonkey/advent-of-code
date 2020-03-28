import re
from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    total_length = 0
    for word in f:
        word = word.strip()
        escaped = word.replace("\\", "\\\\")
        escaped = escaped.replace("\"", "\\\"")
        escaped = "\"" + escaped + "\""
        total_length += len(escaped) - len(word)

print(total_length)
