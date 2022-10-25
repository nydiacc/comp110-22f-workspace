"""EX07 - Dictionary Utils."""

__author__ = "730563759"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the dictionary values."""
    invert_dict: dict[str, str] = {}
    for i in input_dict:
        if input_dict[i] in invert_dict:
            raise KeyError("KeyError")
        else:
            invert_dict[input_dict[i]] = i
    return invert_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """This function returns the most popular color."""
    color_votes: dict[str, int] = {}
    color: str = ""
    vote_count: int = 0
    for i in color_dict:
        if color_dict[i] in color_votes:
            color_votes[color_dict[i]] += 1 
        else: 
            color_votes[color_dict[i]] = 1
    for i in color_votes:
        if color_votes[i] > vote_count:
            vote_count = color_votes[i]
            color = i
    return color


def count(count_list: list[str]) -> dict[str, int]:
    """This function returns a dictionary how many times it occurs."""
    count_dict: dict[str, int] = {}
    for i in count_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict