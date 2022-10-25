"""EX07 - Dictionary Utils Test."""

__author__ = "730563759"


from dictionary import invert, favorite_color, count


# invert_edge_case
def test_invert_empty_dict() -> None:
    """Test an empty dictionary, return empty dictionary."""
    dict_one: dict[str, str] = {}
    assert invert(dict_one) == {}
    return None


# invert_use_case
def test_invert_same_number() -> None:
    """Test a dictionary with equivalent keys and values."""
    dict_one: dict[str, str] = {'1': '1', '2': '2', '3': '3'}
    assert invert(dict_one) == {'1': '1', '2': '2', '3': '3'}
    return None


# invert_use_case_symbols
def test_invert() -> None:
    """Test a dictionary with symbols and their name."""
    dict_one: dict[str, str] = {'exclamtion mark': '!', 'question mark': '?', 'asterisk': '*'}
    invert(dict_one) == {'!': 'exclamtion mark', '?': 'question mark', '*': 'asterisk'}
    return None


# favorite_color_edge_case
def test_favorite_color_all_different() -> None:
    """Test the favorite color when everyone has different favorite colors."""
    dict_one: dict[str, str] = {'Nydia': 'blue', 'Kris': 'gray', 'Dillon': 'red'}
    favorite_color(dict_one) == 'blue'
    return None


# favorite_color_use_case
def test_favorite_color_tie() -> None:
    """Test the favorite color when there is a tie."""
    dict_one: dict[str, str] = {'Nydia': 'blue', 'Nancy': 'green', 'Victoria': 'blue', 'Michelle': 'green'}
    favorite_color(dict_one) == 'blue'
    return None


# favorite_color_use_case
def test_favorite_color() -> None:
    """Test favorite color when there is only one outlier."""
    dict_one: dict[str, str] = {'Nydia': 'blue', 'Nancy': 'pink', 'Victoria': 'pink', 'Michelle': 'pink', 'James': 'pink'}
    favorite_color(dict_one) == 'pink'
    return None


# count_edge_case
def test_count_empty_strings() -> None:
    """Test a list of empty strings."""
    list_one: list[str] = ["", "", "", "", ""]
    count(list_one) == {"": 5}
    return None


# count_use_case
def test_count() -> None:
    """Test random list of numbers."""
    list_one: list[str] = ["100", "95", "90", "85", "100", "90", "70", "95", "100", "90"]
    count(list_one) == {"100": 3, "95": 2, "90": 3, "85": 1, "70": 1}
    return None


# count_use_case
def test_count_number_repeated_its_value() -> None:
    """Test a list of numbers that repeat the number of times as their value."""
    list_one: list[str] = ["5", "3", "5", "2", "4", "3", "1", "5", "4", "4", "2", "5", "3", "4", "5"]
    count(list_one) == {"5": 5, "3": 3, "2": 2, "4": 4, "1": 1}
    return None