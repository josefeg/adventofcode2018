import src.day_five as day_five


polymer = "dabAcCaCBAcCcaDA"


def test_most_sleep_guard_by_most_sleepy_minute():
    reduced_polymer = day_five.reduce_polymer(polymer)
    assert len(reduced_polymer) == 10


def test_remove_problematic_polymer():
    assert day_five.remove_problematic_polymer(polymer) == 4
