from itertools import chain, combinations, ifilter
from os.path import join, dirname, realpath

liters = 150

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    containers = map(int, f)

print(len(list(ifilter(lambda x: sum(x) == liters, chain.from_iterable(combinations(containers, i+1) for i in xrange(len(containers)))))))
