from os.path import join, dirname, realpath


class Cart:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    STRAIGHT = {UP: UP, DOWN: DOWN, LEFT: LEFT, RIGHT: RIGHT}
    LEFT_TURN = {UP: LEFT, DOWN: RIGHT, LEFT: DOWN, RIGHT: UP}
    RIGHT_TURN = {UP: RIGHT, DOWN: LEFT, LEFT: UP, RIGHT: DOWN}
    SLASH_TURN = {UP: RIGHT, DOWN: LEFT, LEFT: DOWN, RIGHT: UP}
    BACKSLASH_TURN = {UP: LEFT, DOWN: RIGHT, LEFT: UP, RIGHT: DOWN}
    CHAR_TO_DIRECTION = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}

    def __init__(self, direction, position):
        self._direction = self.CHAR_TO_DIRECTION[direction]
        self._position = position
        self._memory = 0
        self._crashed = False

    def direction(self):
        return self._direction

    def crash(self):
        self._crashed = True

    def is_crashed(self):
        return self._crashed

    def position(self):
        return self._position

    def move(self, grid):
        # Move in the direction the cart is facing
        self._position = (self._position[0] + self._direction[0], self._position[1] + self._direction[1])

        # Check if the cart needs to turn
        new_position = grid[self._position]
        if new_position == '/':
            self._direction = self.SLASH_TURN[self._direction]
        elif new_position == '\\':
            self._direction = self.BACKSLASH_TURN[self._direction]
        elif new_position == '+':
            direction_map = [self.LEFT_TURN, self.STRAIGHT, self.RIGHT_TURN]
            self._direction = direction_map[self._memory % 3][self._direction]
            self._memory += 1


class Controller:
    def __init__(self, file_input):
        self._carts = []
        self._map = {}

        cart_translator = {'v': '|', '^': '|', '<': '-', '>': '-'}
        for y_coord, line in enumerate(file_input):
            for x_coord, character in enumerate(line):
                if character in " \n":
                    continue
                if character in cart_translator:
                    self._map[(x_coord, y_coord)] = cart_translator[character]
                    self._carts.append(Cart(character, (x_coord, y_coord)))
                else:
                    self._map[(x_coord, y_coord)] = character

    def run(self):
        while True:
            self._tick()
            if len(self._carts) == 1:
                return self._carts[0]

    def _tick(self):
        # Order carts
        self._carts.sort(key=(lambda c: (c.position()[1], c.position()[0])))

        # Drive carts in order
        for cart in self._carts:
            cart.move(self._map)

            # Detect collision
            for cart2 in self._carts:
                if cart.position() == cart2.position() and cart != cart2:
                    cart.crash()
                    cart2.crash()
                    print "Crash happened at position {}".format(cart.position())

        # Remove crashed carts
        self._carts = [c for c in self._carts if not c.is_crashed()]


with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    controller = Controller(f)
last_cart = controller.run()
print "Last cart is at position {}".format(str(last_cart.position()).replace(" ", ""))
