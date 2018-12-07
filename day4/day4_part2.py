from os.path import join, dirname, realpath
from re import match

# Load file
guard_schedule = []
with open(join(dirname(realpath(__file__)), "input.txt")) as f:
    for line in f:
        m = match("^\[(?P<y>\d{4})-(?P<mo>\d{2})-(?P<d>\d{2}) (?P<h>\d{2}):(?P<mi>\d{2})\] (?P<a>.+)$", line)
        year = int(m.group("y"))
        month = int(m.group("mo"))
        day = int(m.group("d"))
        hour = int(m.group("h"))
        minute = int(m.group("mi"))
        action = m.group("a")
        guard_schedule.append((year, month, day, hour, minute, action))


# Sort guard schedule
def sorting(tuple1, tuple2):
    year1, month1, day1, hour1, minute1, _ = tuple1
    year2, month2, day2, hour2, minute2, _ = tuple2
    if year1 != year2:
        return year1 - year2
    if month1 != month2:
        return month1 - month2
    if day1 != day2:
        return day1 - day2
    if hour1 != hour2:
        return hour1 - hour2
    return minute1 - minute2


guard_schedule.sort(cmp=sorting)

current_guard = None
sleep_start = None
guard_bucket = dict()
guard_minute_bucket = dict()
for _, _, _, _, mi, action in guard_schedule:
    # Check for new guard
    m = match("^Guard #(?P<guard_id>\d+) begins shift$", action)
    if m is not None:
        assert sleep_start is None
        current_guard = int(m.group("guard_id"))
        sleep_start = None

    # Check for falling asleep
    if action == "falls asleep":
        assert current_guard is not None and sleep_start is None
        sleep_start = mi

    if action == "wakes up":
        assert current_guard is not None and sleep_start is not None
        sleep_duration = mi - sleep_start

        # Update guard minute bucket
        tmp_dict = guard_minute_bucket.get(current_guard, dict())
        for i in range(sleep_start, mi):
            j = tmp_dict.get(i, 0)
            tmp_dict[i] = j + 1
        guard_minute_bucket[current_guard] = tmp_dict

        # Reset sleep start
        sleep_start = None

# Find max minute for every guard
max_per_guard = dict()
for guard, minute_bucket in guard_minute_bucket.iteritems():
    max_minute = max(minute_bucket, key=minute_bucket.get)
    max_per_guard[guard] = (max_minute, minute_bucket[max_minute])

# Find max minute of all guards
max_guard = max(max_per_guard, key=(lambda k: max_per_guard[k][1]))
print "Guard {} slept most frequently of all guards! He slept {} times during minute {}".format(max_guard,
                                                                                                max_per_guard[
                                                                                                    max_guard][1],
                                                                                                max_per_guard[
                                                                                                    max_guard][0])
print "Solution: {}".format(max_guard * max_per_guard[max_guard][0])
