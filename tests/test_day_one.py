import src.day_one as day_one


def test_count_frequencies():
    assert day_one.count_frequencies(["+1", "+1", "+1"]) == 3
    assert day_one.count_frequencies(["+1", "+1", "-2"]) == 0
    assert day_one.count_frequencies(["-1", "-2", "-3"]) == -6


def test_frequency_reached_twice():
    assert day_one.frequency_reached_twice(["+1", "-1"]) == 0
    assert day_one.frequency_reached_twice(["+3", "+3", "+4", "-2", "-4"]) == 10
    assert day_one.frequency_reached_twice(["-6", "+3", "+8", "+5", "-6"]) == 5
    assert day_one.frequency_reached_twice(["+7", "+7", "-2", "-7", "-4"]) == 14
