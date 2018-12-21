from collections import Counter

input_file = open("input.txt")

unsorted_lines = input_file.readlines()

lines = sorted(unsorted_lines)

def parse_line(line):
    date = line[1:11]
    time = line[12:17]
    action = line[19:]
    return date, time, action.strip()

def grab_minute(time):
    hour, minute = time.split(":")
    return int(minute)


guards_schedules = {}

start_minute = None
guard_id = None

for line in lines:
    date, time, action = parse_line(line)
    if action.startswith("Guard #"):
        guard_id = action.split(" ")[1][1:]

    if action == "falls asleep":
        start_minute = grab_minute(time)

    if action == "wakes up":
        end_minute = grab_minute(time)
        sleeping_times = []
        for i in range(start_minute, end_minute):
            sleeping_times.append(i)
        if guard_id in guards_schedules:
            guards_schedules[guard_id] = guards_schedules[guard_id] + sleeping_times
        else:
            guards_schedules[guard_id] = sleeping_times

max_sleep = 0
guard_id = 0
for guard, schedule in guards_schedules.items():
    if len(schedule) > max_sleep:
        max_sleep = len(schedule)
        guard_id = guard

[(time, count)] = Counter(guards_schedules[guard_id]).most_common(1)

print(int(guard_id) * time)
