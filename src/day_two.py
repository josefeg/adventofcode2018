#!/usr/bin/env python3


def count_occurences(id):
    occurences = {}
    for c in id:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    return occurences


def count_double_and_triple(id):
    occurences = count_occurences(id)
    double = 0
    triple = 0
    for key, value in occurences.items():
        if value == 2:
            double += 1
        elif value == 3:
            triple += 1
    return (double, triple)


def calculate_checksum(ids):
    doubles = 0
    triples = 0

    for id in ids:
        d, t = count_double_and_triple(id)
        if d > 0:
            doubles += 1
        if t > 0:
            triples += 1
    return doubles * triples


def find_similar_letters(ids):
    for i in ids:
        for j in ids:
            chars = list(zip(i, j))
            diffs = 0
            similar_letters = []
            for c1, c2 in chars:
                if c1 == c2:
                    similar_letters.append(c1)
                else:
                    diffs += 1

                if diffs > 1:
                    break

            if diffs == 1:
                return "".join(similar_letters)


def main():
    with open("resources/day_two.txt") as f:
        ids = f.readlines()

    print(calculate_checksum(ids))
    print(find_similar_letters(ids))


if __name__ == "__main__":
    main()
