from os.path import join, dirname, realpath


class Reindeer:
    def __init__(self, line):
        line_split = line.strip().split()
        self._name = line_split[0]
        self._velocity = int(line_split[3])
        self._sprint_duration = int(line_split[6])
        self._rest_duration = int(line_split[-2])

        self._distance = 0
        self._duration = 0
        self._is_running = True

    def run(self):
        self._duration += 1
        if self._is_running:
            self._distance += self._velocity
            if self._duration >= self._sprint_duration:
                self._is_running = False
                self._duration = 0
        elif self._duration >= self._rest_duration:
            self._is_running = True
            self._duration = 0

    def get_distance(self):
        return self._distance


reindeer_list = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for l in f:
        reindeer_list.append(Reindeer(l))

race_duration = 2503
for i in range(race_duration):
    for r in reindeer_list:
        r.run()

print(max(map(lambda x: x.get_distance(), reindeer_list)))
