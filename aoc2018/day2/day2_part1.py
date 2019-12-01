from os.path import join, dirname, realpath

boxes_with_2 = 0
boxes_with_3 = 0

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for box_id in f:
        bucket = dict()
        for letter in box_id:
            if not letter.isspace():
                count = bucket.get(letter, 0)
                bucket[letter] = count + 1
        if 2 in bucket.values():
            boxes_with_2 += 1
        if 3 in bucket.values():
            boxes_with_3 += 1

print("There are {} boxes with two of any letter and {} with three of any letter".format(boxes_with_2, boxes_with_3))
print("Checksum: {}".format(boxes_with_2 * boxes_with_3))