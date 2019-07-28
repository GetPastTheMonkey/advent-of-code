import numpy as np

from os import makedirs
from os.path import join, dirname, realpath, exists
from re import match

from PIL import Image, ImageDraw


class Simulation:
    EMPTY, RUNNING_WATER, STILL_WATER, CLAY, SOURCE = 0, 1, 2, 3, 4

    def __init__(self):
        with open(join(dirname(realpath(__file__)), "input.txt")) as f:
            self._x_min = None
            self._x_max = None
            self._y_min = 0
            self._y_min_clay = None
            self._y_max = None
            x_groups = []
            y_groups = []

            for line in f:
                m = match("(?P<coord_name>[xy])=(?P<coord>\d+), [xy]=(?P<start>\d+)..(?P<end>\d+)", line)
                if not m:
                    raise RuntimeError("Could not parse input file")
                coord_name = m.group("coord_name")
                coord = int(m.group("coord"))
                start = int(m.group("start"))
                end = int(m.group("end"))

                if coord_name == "x":
                    x_groups.append((coord, start, end))
                    if self._x_min is None or coord < self._x_min:
                        self._x_min = coord
                    if self._x_max is None or coord > self._x_max:
                        self._x_max = coord
                    if self._y_min_clay is None or start < self._y_min_clay:
                        self._y_min_clay = start
                    if self._y_max is None or end > self._y_max:
                        self._y_max = end
                else:
                    y_groups.append((coord, start, end))
                    if self._y_min_clay is None or coord < self._y_min_clay:
                        self._y_min_clay = coord
                    if self._y_max is None or coord > self._y_max:
                        self._y_max = coord
                    if self._x_min is None or start < self._x_min:
                        self._x_min = start
                    if self._x_max is None or end > self._x_max:
                        self._x_max = end

        self._x_min -= 1
        self._x_max += 1

        self._simulation = np.zeros(shape=(self._y_max - self._y_min + 1, self._x_max - self._x_min + 1), dtype="u1")

        for x, y_start, y_end in x_groups:
            for y in range(y_start, y_end + 1):
                self._simulation[y - self._y_min][x - self._x_min] = self.CLAY

        for y, x_start, x_end in y_groups:
            for x in range(x_start, x_end + 1):
                self._simulation[y - self._y_min][x - self._x_min] = self.CLAY

        self._simulation[0 - self._y_min][500 - self._x_min] = self.SOURCE

        self._workset = set()
        self._workset.add((500 - self._x_min, 0 - self._y_min))

        self._image_counter = 0

        # Create images directory if it does not exist yet
        directory = join(dirname(realpath(__file__)), "images")
        if not exists(directory):
            makedirs(directory)

        # self.draw()

    def draw(self, save_to_file=True):
        if save_to_file or self._image_counter % 100 == 0:
            print("[DEBUG] Saving image {}, workset: {}".format(self._image_counter, list(self._workset)))
            clay_list = []
            water_list = []
            still_list = []
            source_list = []
            for y, x in np.ndindex(self._simulation.shape):
                if self._simulation[y][x] == self.CLAY:
                    clay_list.append((x, y))
                elif self._simulation[y][x] == self.STILL_WATER:
                    still_list.append((x, y))
                elif self._simulation[y][x] == self.RUNNING_WATER:
                    water_list.append((x, y))
                elif self._simulation[y][x] == self.SOURCE:
                    source_list.append((x, y))

            for (x, y) in self._workset:
                source_list.append((x, y))

            im = Image.new("RGB", (self._x_max - self._x_min+1, self._y_max - self._y_min+1), (255, 255, 255))
            d = ImageDraw.Draw(im)
            d.point(clay_list, (255, 0, 0))
            d.point(water_list, (0, 255, 255))
            d.point(still_list, (0, 0, 255))
            d.point(source_list, (0, 0, 0))
            im.save(join(dirname(realpath(__file__)), "images", "image_{}.png".format(self._image_counter)))
        self._image_counter += 1

    def _get_coord(self, x, y):
        try:
            return self._simulation[y][x]
        except IndexError:
            if y > self._y_max + 1:
                return self.CLAY
            else:
                return self.EMPTY

    def _set_coord(self, x, y, elem):
        if y > self._y_max:
            return
        self._simulation[y][x] = elem

    def _workset_empty(self):
        return len(self._workset) == 0

    def _get_workset_element(self):
        if self._workset_empty():
            return None
        return self._workset.pop()

    def _add_to_workset(self, x, y):
        if y <= self._y_max:
            self._workset.add((x, y))

    def count_water(self):
        count = 0
        for y, x in np.ndindex(self._simulation.shape):
            if (self._y_min_clay <= y <= self._y_max) and (self._simulation[y][x] == self.RUNNING_WATER or self._simulation[y][x] == self.STILL_WATER):
                count += 1
        return count

    def count_still_water(self):
        count = 0
        for y, x in np.ndindex(self._simulation.shape):
            if (self._y_min_clay <= y <= self._y_max) and self._simulation[y][x] == self.STILL_WATER:
                count += 1
        return count

    def run(self):
        while not self._workset_empty():
            self._step()

    def _step(self):
        x, y = self._get_workset_element()
        if self._get_coord(x, y + 1) == self.EMPTY:
            next_y = y + 1

            while self._get_coord(x, next_y) == self.EMPTY:
                self._set_coord(x, next_y, self.RUNNING_WATER)
                next_y += 1

            self._add_to_workset(x, next_y - 1)
        elif self._get_coord(x, y + 1) == self.CLAY or self._get_coord(x, y + 1) == self.STILL_WATER:
            is_top_row = False

            # Scan to the left
            next_x = x
            while True:
                if self._get_coord(next_x - 1, y) == self.CLAY or self._get_coord(next_x - 1, y) == self.STILL_WATER:
                    # If left is clay or still water -> Left side does not overflow
                    break
                elif self._get_coord(next_x, y + 1) != self.CLAY and self._get_coord(next_x, y + 1) != self.STILL_WATER:
                    # If lower is not clay and not still water -> overflow on left side! Add point to workset
                    is_top_row = True
                    self._add_to_workset(next_x, y)
                    break
                next_x -= 1
            left_x = next_x

            # Scan to the right
            next_x = x
            while True:
                if self._get_coord(next_x + 1, y) == self.CLAY or self._get_coord(next_x + 1, y) == self.STILL_WATER:
                    # If right is clay or still water -> right side does not overflow
                    break
                elif self._get_coord(next_x, y + 1) != self.CLAY and self._get_coord(next_x, y + 1) != self.STILL_WATER:
                    # If lower is not clay and not still water -> overflow on right side! Add point to workset
                    is_top_row = True
                    self._add_to_workset(next_x, y)
                    break
                next_x += 1
            right_x = next_x

            # Set water type
            water_type = self.RUNNING_WATER if is_top_row else self.STILL_WATER

            # Fill row from left_x to right_x with water_type
            for ix in range(left_x, right_x + 1):
                self._set_coord(ix, y, water_type)

            # If not top row -> Add upper to workset
            if not is_top_row:
                self._add_to_workset(x, y - 1)

        self.draw(False)
