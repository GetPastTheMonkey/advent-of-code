from os.path import join, dirname, realpath


class OrbitElement(object):
    def __init__(self, id):
        self.id = id
        self.children = set()

    def count(self):
        c = len(self.children)
        for child in self.children:
            c += child.count()
        return c


orbits = dict()
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        # x)y ==> y orbits x, x is center of y
        x = line[0:3]
        y = line[4:7]

        if x not in orbits:
            orbits[x] = OrbitElement(x)
        if y not in orbits:
            orbits[y] = OrbitElement(y)

        orbits[x].children.add(orbits[y])

co = 0
for orb in orbits.values():
    co += orb.count()

print(co)
