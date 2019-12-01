from os.path import join, dirname, realpath
from re import match

# Specify number of workers
worker_count = 5
workers = [{
    "task": None,
    "remaining": 0
} for _ in range(worker_count)]

# Load file
tasks = dict()
for i in range(ord("A"), ord("Z")+1):
    tasks[chr(i)] = dict()
    tasks[chr(i)]["requirements"] = []
    tasks[chr(i)]["duration"] = 60 + (i - 64)  # 60 + position of character in alphabet -> A = 60+1, B = 60+2, ...
    tasks[chr(i)]["has_worker"] = False

with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        m = match("^Step (?P<req>[A-Z]) must be finished before step (?P<step>[A-Z]) can begin\.$", line)
        step = m.group("step")
        reqs = m.group("req")
        tasks[step]["requirements"].append(reqs)


def find_empty_tasks(req):
    empty_list = []
    for key, data in req.items():
        if not data["requirements"] and not data["has_worker"]:
            empty_list.append(key)
    empty_list.sort()
    return empty_list


def distribute_work(req, w):
    empty_tasks = find_empty_tasks(req)
    if empty_tasks:
        print("[ITERATION {}] - Tasks with empty requirements: {}".format(iterations, empty_tasks))
    for worker in w:
        # If the worker is idle and there is still an empty task, then work on it
        if worker["task"] is None and len(empty_tasks) > 0:
            t = empty_tasks.pop(0)
            worker["task"] = t
            worker["remaining"] = req[t]["duration"]
            req[t]["has_worker"] = True
    return req, w


def do_work(w):
    for worker in w:
        if worker["task"] is not None:
            worker["remaining"] -= 1


def remove_finished_tasks(req, w):
    removed_tasks = []

    # Loop through workers and remove finished tasks
    for worker in w:
        if worker["task"] is not None and worker["remaining"] == 0:
            # Remove task from req dict
            print("[ITERATION {}] - Finished task {}".format(iterations, worker["task"]))
            req.pop(worker["task"])
            removed_tasks.append(worker["task"])
            worker["task"] = None

    # Create new task dict
    new_tasks = dict()
    for key, value in req.items():
        new_tasks[key] = {
            "requirements": [],
            "duration": value["duration"],
            "has_worker": value["has_worker"]
        }
        for r in value["requirements"]:
            if r not in removed_tasks:
                new_tasks[key]["requirements"].append(r)
    return new_tasks, w


iterations = 0

while tasks:
    tasks, workers = distribute_work(tasks, workers)
    do_work(workers)
    iterations += 1
    tasks, workers = remove_finished_tasks(tasks, workers)

print("Finished after {} iterations (with {} workers)".format(iterations, worker_count))
