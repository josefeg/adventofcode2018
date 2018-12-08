import src.day_three as day_three


claims = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2"
    ]


def test_count_overlaps():
    _, overlaps = day_three.count_overlaps(11, 9, claims)
    assert overlaps == 4


def test_find_unique_claim():
    canvas, _ = day_three.count_overlaps(11, 9, claims)
    assert day_three.find_unique_claim(canvas, claims) == "#3"
