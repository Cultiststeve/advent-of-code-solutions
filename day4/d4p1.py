import time
import datetime
from operator import itemgetter

entries = open("inputd4.txt")
# entries = open("sample_input.txt")

# parse string to entries
entry_list = []
for entry in entries:
    month = entry[6:8]
    day = entry[9:11]
    hour = entry[12:14]
    minutes = entry[15:17]
    event = entry[19:]
    print("M: {}, D: {}, H: {}, M: {}, data: {}".format(month, day, hour, minutes, event))
    str_time = entry[6:17]
    # timestamp = datetime.datetime.strptime(str_time, "%m-%d %H:%M").timestamp()
    timestamp = datetime.datetime.strptime(str_time, "%m-%d %H:%M")
    entry_list.append([timestamp, event])

# sort entries
sorted_entry_list = sorted(entry_list, key=itemgetter(0))

# count time for each guard
asleep = False
guard_sleep_times = {}
for entry in sorted_entry_list:
    print(entry)
    if "Guard" in entry[1]:
        # New shift
        end_of_id = entry[1].find("begins")
        current_guard = entry[1][7:end_of_id]
        print(current_guard)
        if current_guard not in guard_sleep_times:
            guard_sleep_times[current_guard] = 0
    elif "falls" in entry[1]:
        if asleep is True:
            raise Exception("Already asleep")
        asleep = True
        start_sleep = entry[0]
    elif "wakes" in entry[1]:
        if asleep is False:
            raise Exception("Already awake")
        asleep = False
        sleep_length = entry[0] - start_sleep
        sleep_length_min = sleep_length / datetime.timedelta(minutes=1)
        print("Slept for : {}".format(sleep_length_min))
        guard_sleep_times[current_guard] += sleep_length_min
    else:
        raise Exception("Could not understand entry")

most_sleep = 0
most_sleep_guard_id = None
for guard in guard_sleep_times:
    if guard_sleep_times[guard] > most_sleep:
        most_sleep = guard_sleep_times[guard]
        most_sleep_guard_id = guard
        print("Guard {} has most sleep at {}".format(guard, most_sleep))
        print(int(most_sleep_guard_id)*int(most_sleep))

# Which min does that guard spend asleep the most
found_sleepy_guard = 0
sleep_times = {}
for entry in sorted_entry_list:
    if found_sleepy_guard == 1:
        start_min = entry[0].minute
        print(start_min)
        found_sleepy_guard = 2

    elif found_sleepy_guard == 2:
        end_min = entry[0].minute
        print(end_min)

        for sleep_min in range(start_min, end_min-1):
            if sleep_min in sleep_times:
                sleep_times[sleep_min] += 1
            else:
                sleep_times[sleep_min] = 1

        found_sleepy_guard = 0
    elif "Guard #" + most_sleep_guard_id in entry[1]:
        print("Found sleepy guard sleep time")
        found_sleepy_guard = 1

max_time_sleep_in_min = 0
max_sleep_min = 0
for min in sleep_times:
    if sleep_times[min] > max_time_sleep_in_min:
        max_time_sleep_in_min = sleep_times[min]
        max_sleep_min = min
        print("Sleep for {} min at  time {}".format(sleep_times[min], min))

ans = (int(max_sleep_min)*int(most_sleep_guard_id))
print("Final ans: {}, for guard: {}".format(ans, most_sleep_guard_id))
