from os.path import join, dirname, realpath

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    numbers = f.readline()

height = 6
width = 25

image_size = height * width
images = []

i = 0
while i < len(numbers):
    images.append(map(int, numbers[i:i+image_size]))
    i += image_size

fewest_nr_zeros = image_size + 1
fewest_nr_zeros_indx = None
for indx, img in enumerate(images):
    nr_zeros = len([i for i in img if i == 0])
    if nr_zeros < fewest_nr_zeros:
        fewest_nr_zeros = nr_zeros
        fewest_nr_zeros_indx = indx

nr_ones = len([i for i in images[fewest_nr_zeros_indx] if i == 1])
nr_twos = len([i for i in images[fewest_nr_zeros_indx] if i == 2])

print("Solution: {}".format(nr_ones * nr_twos))
