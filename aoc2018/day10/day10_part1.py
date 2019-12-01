from os import makedirs
from os.path import join, dirname, realpath, exists
from re import match

from PIL import Image, ImageDraw

points = []
min_x = None
min_y = None
max_x = None
max_y = None

# Canvas for drawing
i = 300
canvas_min_x = -i
canvas_min_y = -i
canvas_max_x = i
canvas_max_y = i

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for l in f:
        m = match("position=<\s*(?P<x>[0-9-]+),\s*(?P<y>[0-9-]+)> velocity=<\s*(?P<dx>[0-9-]+),\s*(?P<dy>[0-9-]+)>", l)
        x = int(m.group("x"))
        y = int(m.group("y"))
        dx = int(m.group("dx"))
        dy = int(m.group("dy"))
        points.append((x, y, dx, dy))
        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_x is None or max_x < x:
            max_x = x
        if max_y is None or max_y < y:
            max_y = y


def move(pts):
    new_pts = []
    for x, y, dx, dy in pts:
        new_pts.append((x+dx, y+dy, dx, dy))
    return new_pts


def draw(pts, it):
    pt_list = []
    for x, y, _, _ in pts:
        # Check if point is on canvas
        if canvas_min_x <= x <= canvas_max_x and canvas_min_y <= y <= canvas_max_y:
            pt_list.append((x-canvas_min_x, y-canvas_min_y))
    if not pt_list:
        print("[DEBUG] Not drawing iteration {}, no point is visible".format(it))
        return

    # There is at least one point on the canvas

    if len(pt_list) < len(pts):
        print("[DEBUG] Not drawing iteration {}, not all points are visible".format(it))
        return

    im = Image.new("RGB", (canvas_max_x-canvas_min_x, canvas_max_y-canvas_min_y))
    d = ImageDraw.Draw(im)
    d.point(pt_list, (255, 255, 255))
    im.save(join(dirname(realpath(__file__)), "images", "image_{}.png".format(it)))
    print("[DEBUG] Drawn iteration {}, {} pixels were on canvas".format(it, len(pt_list)))


def should_finish(pts):
    # Finish when the first point leaves the draw area
    for x, y, _, _ in pts:
        if x < min_x or x > max_x or y < min_y or y > max_y:
            print("[DEBUG] A point left the area, safe to finish")
            return True
    return False


# Create images directory if it does not exist yet
directory = join(dirname(realpath(__file__)), "images")
if not exists(directory):
    makedirs(directory)

iteration = 0
while True:
    iteration += 1
    points = move(points)
    if should_finish(points):
        break
    draw(points, iteration)
