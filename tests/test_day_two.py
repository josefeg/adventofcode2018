import src.day_two as day_two


def test_count_frequencies():
    assert day_two.count_double_and_triple("abcdef") == (0, 0)
    assert day_two.count_double_and_triple("bababc") == (1, 1)
    assert day_two.count_double_and_triple("abbcde") == (1, 0)
    assert day_two.count_double_and_triple("abcccd") == (0, 1)
    assert day_two.count_double_and_triple("aabcdd") == (2, 0)
    assert day_two.count_double_and_triple("abcdee") == (1, 0)
    assert day_two.count_double_and_triple("ababab") == (0, 2)


def test_calculate_checksum():
    ids = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab"
    ]
    assert day_two.calculate_checksum(ids) == 12


def test_find_similar_letters():
    ids = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz"
    ]
    assert day_two.find_similar_letters(ids) == "fgij"
