from os.path import join, dirname, realpath
from re import match

# Load file
requirements = dict()
for i in range(ord("A"), ord("Z")+1):
    requirements[chr(i)] = []

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        m = match("^Step (?P<req>[A-Z]) must be finished before step (?P<step>[A-Z]) can begin\.$", line)
        step = m.group("step")
        req = m.group("req")
        requirements[step].append(req)


def find_empty_requirements(reqs):
    return_list = []
    for key, value in reqs.iteritems():
        if not value:
            return_list.append(key)
    return return_list


def find_next_step(reqs):
    possible_steps = find_empty_requirements(reqs)
    possible_steps.sort()
    return possible_steps[0]


def update_requirements(req, step):
    resulting_requirements = dict()
    for key, values in req.iteritems():
        if key != step:
            new_values = []
            for value in values:
                if value != step:
                    new_values.append(value)
            resulting_requirements[key] = new_values
    return resulting_requirements


def do_a_step(req):
    next_step = find_next_step(req)
    return next_step, update_requirements(req, next_step)

solution = []
while requirements:
    step, requirements = do_a_step(requirements)
    solution.append(step)
print "The requirements should be completed in the following order: {}".format(''.join(solution))
