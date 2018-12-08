#!/usr/bin/env python3

import re


def init_canvas(width, length):
    canvas = []
    for i in range(length):
        canvas.append(["." for _ in range(width)])
    return canvas


def parse(claim):
    r = re.compile(r"#(\d+)\s@\s+(\d+),(\d+):\s+(\d+)x(\d+)")
    m = r.match(claim)
    return m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))


def paint(canvas, claim):
    unique = True
    new_overlaps = 0
    id, x, y, width, length = parse(claim)
    for i in range(y, y+length):
        for j in range(x, x+width):
            if canvas[i][j] == ".":
                canvas[i][j] = id
            elif canvas[i][j] == "#":
                unique = False
                continue
            elif canvas[i][j] != id:
                unique = False
                canvas[i][j] = "#"
                new_overlaps += 1
    return canvas, new_overlaps, unique


def count_overlaps(x, y, claims):
    overlaps = 0
    canvas = init_canvas(x, y)
    for claim in claims:
        canvas, new_overlaps, _ = paint(canvas, claim)
        overlaps += new_overlaps
    return canvas, overlaps


def find_unique_claim(canvas, claims):
    for claim in claims:
        _, _, unique = paint(canvas, claim)
        if unique:
            return claim.split(" ")[0]


def main():
    with open("resources/day_three.txt") as f:
        claims = f.readlines()

    canvas, overlaps = count_overlaps(1000, 1000, claims)
    print("overlaps =>", overlaps)
    unique_claims = find_unique_claim(canvas, claims)
    print("unique claims =>", unique_claims)


if __name__ == "__main__":
    main()
