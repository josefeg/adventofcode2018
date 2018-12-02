#!/usr/bin/env python3


def accumulator(starting_value, change):
    operator = change[0]
    if operator == "+":
        return starting_value + int(change[1:])
    elif operator == "-":
        return starting_value - int(change[1:])


def count_frequencies(changes):
    frequency = 0
    for change in changes:
        frequency = accumulator(frequency, change)
    return frequency


def frequency_reached_twice(changes):
    def internal(initial_value, previously_seen):
        frequency = initial_value
        for change in changes:
            frequency = accumulator(frequency, change)
            if frequency in previously_seen:
                return frequency
            previously_seen.add(frequency)
        return internal(frequency, previously_seen)

    return internal(0, set([0]))


def main():
    with open("resources/day_one.txt") as f:
        frequencies = f.readlines()

    print(count_frequencies(frequencies))
    print(frequency_reached_twice(frequencies))


if __name__ == "__main__":
    main()
