"""Quiz02 Sample."""

def key_values(a_list: list[str], a_dict: dict[str, int]) -> dict[str, int]:
    """Key Values."""
    return_dict: dict[str, int] = {}
    for i in a_list:
        for key in a_dict:
            if a_list[i] == key:
                return_dict[key] = a_dict[key]
    return return_dict


def main() -> None:
    """Entrypoint of code."""
    dict_one: dict[str, int] = {"a": 23, "b": 15, "c": 30}
    print(key_values(["a", "b"], dict_one))


if __name__ == "__main__":
    main()