from os.path import join, dirname, realpath


class OrbitElement(object):
    def __init__(self, id):
        self.id = id
        self.children = set()
        self.parent = None

    def __str__(self):
        return self.id

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
        orbits[y].parent = orbits[x]

my_upchain = list()
parent = orbits["YOU"]
while parent is not None:
    my_upchain.append(parent)
    parent = parent.parent

santa_upchain = list()
parent = orbits["SAN"]
while parent is not None:
    santa_upchain.append(parent)
    parent = parent.parent

co = 0
el = None
for mu in my_upchain:
    if mu in santa_upchain:
        el = mu
        break
    else:
        co += 1

for su in santa_upchain:
    if su == el:
        break
    else:
        co += 1

co -= 2  # Subtract first and last link (from YOU to its orbit and from SAN to its orbit)

print(co)
