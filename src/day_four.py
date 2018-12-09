#!/usr/bin/env python3

import re


def parse(record):
    r = re.compile(r"\[(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})\]\s+(.*)")
    m = r.match(record)
    return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), m.group(6)


def get_guard_id(text):
    r = re.compile(r"[^#]*#(\d+).*")
    m = r.match(text)
    return int(m.group(1))


def process(records):
    records = sorted(records)
    guard_minutes = {}
    guard_id = 0
    last_sleep_time = 0
    for record in records:
        y, m, d, h, minute, t = parse(record)
        if t.find("#") != -1:
            guard_id = get_guard_id(record)
            if guard_id not in guard_minutes:
                guard_minutes[guard_id] = [0 for _ in range(60)]
        elif t == "falls asleep":
            last_sleep_time = minute
        elif t == "wakes up":
            for i in range(last_sleep_time, minute):
                guard_minutes[guard_id][i] += 1
    return guard_minutes


def find_guards_asleep_most(guard_minutes):
    max_mins_asleep = 0
    most_sleepy_guard = 0
    for guard_id, minutes in guard_minutes.items():
        mins_asleep = sum(minutes)
        if mins_asleep > max_mins_asleep:
            max_mins_asleep = mins_asleep
            most_sleepy_guard = guard_id
    return most_sleepy_guard


def find_minute_asleep_most(minutes):
    current_max = 0
    current_max_min = 0
    for i in range(len(minutes)):
        if minutes[i] > current_max:
            current_max = minutes[i]
            current_max_min = i
    return current_max_min


def most_sleep_guard_by_most_sleepy_minute(records):
    guard_minutes = process(records)
    guard_asleep_most = find_guards_asleep_most(guard_minutes)
    minute_most_asleep = find_minute_asleep_most(guard_minutes[guard_asleep_most])
    return guard_asleep_most * minute_most_asleep


def guard_by_most_sleepy_minute(records):
    guard_minutes = process(records)

    most_sleepy_minute = 0
    most_sleepy_minute_amount = 0
    guard_with_most_sleepy_minute = 0
    for guard_id, minutes in guard_minutes.items():
        for i in range(len(minutes)):
            if minutes[i] > most_sleepy_minute_amount:
                most_sleepy_minute = i
                most_sleepy_minute_amount = minutes[i]
                guard_with_most_sleepy_minute = guard_id

    return guard_with_most_sleepy_minute * most_sleepy_minute


def main():
    with open("resources/day_four.txt") as f:
        records = f.readlines()

    print(most_sleep_guard_by_most_sleepy_minute(records))
    print(guard_by_most_sleepy_minute(records))


if __name__ == "__main__":
    main()
