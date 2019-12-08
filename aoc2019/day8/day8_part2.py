from os.path import join, dirname, realpath

from PIL import Image, ImageDraw

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    numbers = f.readline()

width = 25
height = 6

image_size = height * width
images = []

BLACK = 0
WHITE = 1
TRANSPARENT = 2

i = 0
while i < len(numbers):
    images.append(map(int, numbers[i:i+image_size]))
    i += image_size

final_image = images[0]
for img in images[1:]:
    for indx, color in enumerate(img):
        if final_image[indx] == TRANSPARENT and not color == TRANSPARENT:
            # Final image is transparent at this position
            # but current layer is not transparent
            final_image[indx] = color

white_points = []
for indx, color in enumerate(final_image):
    if color == WHITE:
        pos_x = indx % width
        pos_y = indx // width
        white_points.append((pos_x, pos_y))

im = Image.new("RGB", (width, height))
d = ImageDraw.Draw(im)
d.point(white_points, (255, 255, 255))

filepath = join(dirname(realpath(__file__)), "solution.png")
im.save(filepath)

print("Solution saved at {}".format(filepath))
